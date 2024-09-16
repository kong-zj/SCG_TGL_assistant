import React, { useState } from 'react';
import './index.css';
// import type { CascaderProps } from 'antd';
import {
  AutoComplete,
  Button,
  Cascader,
  Checkbox,
  Col,
  Form,
  Input,
  InputNumber,
  Row,
  Select,
} from 'antd';
import { apiSignUpRequest } from '../../../api/auth';

const { Option } = Select;


const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 8 },
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 16 },
  },
};

const tailFormItemLayout = {
  wrapperCol: {
    xs: {
      span: 24,
      offset: 0,
    },
    sm: {
      span: 16,
      offset: 8,
    },
  },
};


class SignUpForm extends React.Component {
  //   const [form] = Form.useForm();

  onFinish = values => {
    console.log('Received values of form: ', values);
    apiSignUpRequest(values).then(res => {
      // 这里是成功回调
      console.log(res)
    }).catch(err => {
      // 这里是错误回调
      console.log(err)
    })
  };

  prefixSelector = (
    <Form.Item name="prefix" noStyle>
      <Select style={{ width: 70 }}>
        <Option value="86">+86</Option>
        <Option value="87">+87</Option>
      </Select>
    </Form.Item>
  );

  suffixSelector = (
    <Form.Item name="suffix" noStyle>
      <Select style={{ width: 70 }}>
        <Option value="USD">$</Option>
        <Option value="CNY">¥</Option>
      </Select>
    </Form.Item>
  );

  //   const [autoCompleteResult, setAutoCompleteResult] = useState<string[]>([]);

  //   onWebsiteChange = value => {
  //     if (!value) {
  //       setAutoCompleteResult([]);
  //     } else {
  //       setAutoCompleteResult(['.com', '.org', '.net'].map((domain) => `${value}${domain}`));
  //     }
  //   };

  //   const websiteOptions = autoCompleteResult.map((website) => ({
  //     label: website,
  //     value: website,
  //   }));

  render() {
    return (
      <Form
        {...formItemLayout}
        // form={form}
        name="register"
        onFinish={this.onFinish}
        initialValues={{
          residence: ['zhejiang', 'hangzhou', 'xihu'], prefix: '86'
        }}
        style={{ maxWidth: 600 }}
        scrollToFirstError
      >

        <Form.Item
          name="username"
          label="username"
          rules={[
            {
              required: true,
              message: 'Please input your username',
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          name="email"
          label="E-mail"
          rules={[
            {
              type: 'email',
              message: 'The input is not valid E-mail!',
            },
            {
              required: true,
              message: 'Please input your E-mail!',
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          name="password"
          label="Password"
          rules={[
            {
              required: true,
              message: 'Please input your password!',
            },
          ]}
          hasFeedback
        >
          <Input.Password />
        </Form.Item>

        <Form.Item
          name="confirm"
          label="Confirm Password"
          dependencies={['password']}
          hasFeedback
          rules={[
            {
              required: true,
              message: 'Please confirm your password!',
            },
            ({ getFieldValue }) => ({
              validator(_, value) {
                if (!value || getFieldValue('password') === value) {
                  return Promise.resolve();
                }
                return Promise.reject(new Error('The new password that you entered do not match!'));
              },
            }),
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item label="Captcha" extra="We must make sure that your are a human.">
          <Row gutter={8}>
            <Col span={12}>
              <Form.Item
                name="captcha"
                noStyle
                rules={[{ required: true, message: 'Please input the captcha you got!' }]}
              >
                <Input />
              </Form.Item>
            </Col>
            <Col span={12}>
              <Button>Get captcha</Button>
            </Col>
          </Row>
        </Form.Item>

        <Form.Item
          name="agreement"
          valuePropName="checked"
          rules={[
            {
              validator: (_, value) =>
                value ? Promise.resolve() : Promise.reject(new Error('Should accept agreement')),
            },
          ]}
          {...tailFormItemLayout}
        >
          <Checkbox>
            I have read the <a href="">agreement</a>
          </Checkbox>
        </Form.Item>
        <Form.Item {...tailFormItemLayout}>
          <Button type="primary" htmlType="submit">
            Register
          </Button>
        </Form.Item>
      </Form >
    );
  }


};

export default SignUpForm;  