import {get, post} from '../utils/axios';

// 登录
export const apiSignInRequest = (data: any) => post('/api/sta_auth/signin/', data);

// 注册
export const apiSignUpRequest = (data: any) => post('/api/sta_auth/signup/', data);

// 退出登录
export const apiSignOutRequest = () => post('/api/sta_auth/signout/');

