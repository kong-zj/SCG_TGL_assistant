import React, {Component} from 'react';
import './index.css'
import { Link } from 'react-router-dom';

import ProductTable from 'src/components/product/ProductTable';


class ProductList extends Component {
    
    render () {
        return (
            <div>
              生产单列表
              <br />
                <ProductTable></ProductTable>
            
            </div>
        );
    }
}

export default ProductList;