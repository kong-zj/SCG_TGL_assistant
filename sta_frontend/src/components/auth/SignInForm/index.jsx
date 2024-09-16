import React from 'react';
import './index.css';
import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Checkbox, Form, Input, Flex } from 'antd';
import { apiSignInRequest } from '../../../api/auth';
import axios from 'axios';


class SignInForm extends React.Component {

  onFinish = values => {
    console.log('Received values of form: ', values);
        //向后端发送登录请求
        // signInRequest(values).then(res => {
        //   console.log(res);
        // })
        apiSignInRequest(values).then(res=>{
          // 这里是成功回调
          console.log(res)
        }).catch(err=>{
          // 这里是错误回调
          console.log(err)
        })
        // const data = {
        //   username: values.username,
        //   password: values.password
        // }
        // axios.post('/api/sta_auth/signin/', data, {
        //   headers: {
        //     'Content-Type': 'application/json'
        //   }
        // })
        //   .then(function (response) {
        //     const data = response.data;
        //     const result = data.status;
        //     if (result === 'success') {
        //       //成功登录
        //       //在 Index 用 cookie 判断是否登录
        //       // cookie.save('username', that.state.username, { path: '/' });
        //       // cookie.save('loginSuccess', true, { path: '/' });
        //       // cookie.save('email', data.email, { path: '/' });
        //       //页面跳转
        //       window.location.href = '/index';
        //     }
        //     else {
        //       // message.warning('账号或密码错误', 2)
        //     }
        //   })
        //   .catch(err => {
        //     console.log("用户登录请求失败, ERR : " + err);
        //   });

  };


  render() {
    return (
      <Form
        name="login"
        initialValues={{ remember: true }}
        style={{ maxWidth: 360 }}
        onFinish={this.onFinish}
      >
        <Form.Item
          name="username"
          rules={[{ required: true, message: '请输入您的用户名' }]}
        >
          <Input prefix={<UserOutlined />} placeholder="用户名" />
        </Form.Item>
        <Form.Item
          name="password"
          rules={[{ required: true, message: '请输入您的密码' }]}
        >
          <Input prefix={<LockOutlined />} type="password" placeholder="密码" />
        </Form.Item>
        <Form.Item>
          <Flex justify="space-between" align="center">
            <Form.Item name="remember" valuePropName="checked" noStyle>
              <Checkbox>记住我</Checkbox>
            </Form.Item>
            <a href="">忘记密码?</a>
          </Flex>
        </Form.Item>

        <Form.Item>
          <Button block type="primary" htmlType="submit">
            登录
          </Button>
          新来的? <a href="">现在注册!</a>
        </Form.Item>
      </Form>
    );
  }

};

export default SignInForm;  