import React, {Component} from 'react';
import './index.css'

import PersonalDropdown from 'src/components/personal/PersonalDropdown';


class Home extends Component {
    
    render () {
        return (
            <div>
              用户登录后首页
              <PersonalDropdown></PersonalDropdown>
            </div>
        );
    }
}

export default Home;