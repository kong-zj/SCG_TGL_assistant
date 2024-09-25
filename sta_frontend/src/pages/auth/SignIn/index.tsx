import React, {Component} from 'react';
import axios from "axios";
import { Form, Input, Button, Checkbox, message} from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import cookie from 'react-cookies'
import './index.css'
import {Link} from "react-router-dom";
import SignInForm from '../../../components/auth/SignInForm'


class SignIn extends Component {
    //防止修改url访问
    componentWillMount () {
        const username = cookie.load('username');
        const change = cookie.load('changeSuccess');
        if (username !== undefined) window.location.href = '/index';
        if(change !== undefined){
            message.success("密码修改成功，请重新登录", 2);
            cookie.remove('changeSuccess', {path:'/'});
        }
    }

    componentDidMount () {
        if (cookie.load('registerSuccess') !== undefined) {
            message.success('注册成功，请登陆', 2);
            cookie.remove('registerSuccess', {path:'/'});
        }
    }

    state = {
        username: '',
        password: ''
    }

    //保存用户输入的用户名
    handleUsername = e => {
        this.setState({username: e.target.value});
    }

    //保存用户输入的密码
    handlePassword = e => {
        this.setState({password: e.target.value});
    }

    //处理表单的登录请求
    handleSubmit = () => {
        //将当前的this对象复制一份到that变量，记录状态
        let that = this;
        if (that.state.username === '' && that.state.password === '') return;
        //向后端发送请求
        axios.post('/api/login', {
            username: this.state.username,
            password: this.state.password
        })
            .then(function (response) {
                const data = response.data;
                const result = data.status;
                if (result === 'success'){
                    //成功登录
                    //在 Index 用 cookie 判断是否登录
                    cookie.save('username', that.state.username, { path: '/' });
                    cookie.save('loginSuccess', 'true', { path: '/' });
                    cookie.save('email', data.email, {path:'/'});
                    //页面跳转
                    window.location.href = '/index';
                }
                else{
                    message.warning('账号或密码错误', 2)
                }
            })
            .catch( err => {
                console.log("用户登录请求失败, ERR : " + err);
            });
    }

    //跳转注册界面
    goRegister = () => {
        window.location.href = '/register'
    }

    render () {
        return (
            <div className='myForm'>
              <SignInForm></SignInForm>
                
            </div>
        );
    }
}

export default SignIn;