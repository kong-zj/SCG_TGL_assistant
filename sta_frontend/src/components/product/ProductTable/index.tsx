import React, { useEffect, useState } from 'react';
import './index.css';
import type { GetProp, TableProps } from 'antd';
import { Table } from 'antd';
import type { SorterResult } from 'antd/es/table/interface';
import qs from 'qs';

import { apiFilterProductRequest } from 'src/api/product';

type ColumnsType<T extends object = object> = TableProps<T>['columns'];
type TablePaginationConfig = Exclude<GetProp<TableProps, 'pagination'>, boolean>;

// 一行数据的结构
interface DataType {
  productId: number;
  orderId: number;
  productDate: string;
  startProductTime: string;
}

interface TableParams {
  pagination?: TablePaginationConfig;
  sortField?: SorterResult<any>['field'];
  sortOrder?: SorterResult<any>['order'];
  filters?: Parameters<GetProp<TableProps, 'onChange'>>[1];
}

// 表列
const columns: ColumnsType<DataType> = [
  {
    title: '小票号',
    dataIndex: 'productId',
    sorter: true,
    // render: (name) => `${name.first} ${name.last}`,
    width: '8%',
  },
  {
    title: '生产日期',
    dataIndex: 'productDate',
    width: '10%',
  },
  {
    title: '时间',
    dataIndex: 'startProductTime',
  },
  {
    title: '任务单号',
    dataIndex: 'orderId',
  },
  {
    title: '单位名称',
    dataIndex: 'companyName',
  },
  {
    title: '工程名称',
    dataIndex: 'projectName',
  },
  {
    title: '施工部位',
    dataIndex: 'littleProjectName',
  },
];

const getRandomuserParams = (params: TableParams) => ({
  results: params.pagination?.pageSize,
  page: params.pagination?.current,
  ...params,
});

const ProductTable: React.FC = () => {
  const [data, setData] = useState<DataType[]>();
  const [loading, setLoading] = useState(false);
  const [tableParams, setTableParams] = useState<TableParams>({
    pagination: {
      current: 1,
      pageSize: 40,
    },
  });

  const fetchData = () => {
    setLoading(true);

    apiFilterProductRequest().then(res => {
      // 这里是成功回调
      const results = (res as any).results;
      console.log(results);
      setData(results);
      setLoading(false);
    }).catch(err => {
      // 这里是错误回调
      console.log(err);
      setLoading(false);
    })
    

  };

  useEffect(fetchData, [
    tableParams.pagination?.current,
    tableParams.pagination?.pageSize,
    tableParams?.sortOrder,
    tableParams?.sortField,
    JSON.stringify(tableParams.filters),
  ]);

  const handleTableChange: TableProps<DataType>['onChange'] = (pagination, filters, sorter) => {
    setTableParams({
      pagination,
      filters,
      sortOrder: Array.isArray(sorter) ? undefined : sorter.order,
      sortField: Array.isArray(sorter) ? undefined : sorter.field,
    });

    // `dataSource` is useless since `pageSize` changed
    if (pagination.pageSize !== tableParams.pagination?.pageSize) {
      setData([]);
    }
  };

  return (
    <Table<DataType>
      columns={columns}
      // rowKey={(record) => record.login.uuid}
      dataSource={data}
      pagination={tableParams.pagination}
      loading={loading}
      onChange={handleTableChange}
    />
  );
};

export default ProductTable;
