import {get, post} from '../utils/axios';

// product列表
export const apiFilterProductRequest = () => get('/product/product/?orderId=56666');

// 单个product详细信息
export const apiGetProductInfoRequest = (pk: number) => get(`/product/product/${pk}`);