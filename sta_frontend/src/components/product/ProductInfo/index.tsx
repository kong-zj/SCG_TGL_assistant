import React, { useEffect, useState } from 'react';
import './index.css';
import { Typography } from 'antd';

import { apiGetProductInfoRequest } from 'src/api/product';
import { useParams } from 'react-router-dom';

const { Title } = Typography;

// interface ProductInfoType {
//   value: string;
//   label: string;
// }

const ProductInfo: React.FC = () => {

  const [info, setInfo] = useState({});
  // 接收路由传递的参数
  const params = useParams();
  
  useEffect(() => {
    let pk_number = (params.pk as any) as number;
    apiGetProductInfoRequest(pk_number).then(res => {
      // 这里是成功回调
      setInfo(res as any);
      console.log(res)
    }).catch(err => {
      // 这里是错误回调
      console.log(err)
    })
  }, []);



  return (
    <>
      <Title>h1. Ant Design</Title>
      {info.productId}
      <br></br>
      {info.orderId}
      <br></br>
      {info.companyName}
      <br></br>
      {info.projectName}
      <br></br>
      {info.littleProjectName}
      <br></br>
      {info.pump}
    </>
  );
}



export default ProductInfo;