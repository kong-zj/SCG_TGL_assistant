import React, {Component} from 'react';
import './index.css'

import SignUpForm from '../../../components/auth/SignUpForm';

class SignUp extends Component {
    
    render () {
        return (
            <div>
              <SignUpForm />
              
            </div>
        );
    }
}

export default SignUp;