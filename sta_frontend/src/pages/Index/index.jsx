import React, {Component} from 'react';
import './index.css'
import { Link } from 'react-router-dom';


class Index extends Component {
    
    render () {
        return (
            <div>
              用户登录前首页
              <br />
              <Link to="/home" className="link">跳转Home页面</Link>
              <Link to="/signin" className="link">登录</Link>
              <Link to="/signup" className="link">注册</Link>
            
            </div>
        );
    }
}

export default Index;