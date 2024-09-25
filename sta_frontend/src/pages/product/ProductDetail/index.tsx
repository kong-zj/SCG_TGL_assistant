import React, {Component} from 'react';
import './index.css'
import { Link } from 'react-router-dom';

import ProductInfo from 'src/components/product/ProductInfo';


class ProductDetail extends Component {
    
    render () {
        return (
            <div>
              生产单列表
              <br />
                <ProductInfo></ProductInfo>
            
            </div>
        );
    }
}

export default ProductDetail;