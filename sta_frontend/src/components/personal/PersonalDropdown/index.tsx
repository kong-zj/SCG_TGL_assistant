import React from 'react';
import './index.css';
import { SettingOutlined } from '@ant-design/icons';
import type { MenuProps } from 'antd';
import { Dropdown, Space } from 'antd';

import PersonalAvatar from '../PersonalAvatar';
import { apiSignOutRequest } from 'src/api/auth';

const items: MenuProps['items'] = [
    {
        key: '1',
        label: '个人中心',
        disabled: true,
    },
    {
        type: 'divider',
    },
    {
        key: '2',
        label: 'Profile',
        // extra: '⌘P',
    },
    {
        key: '3',
        label: 'Settings',
        icon: <SettingOutlined />,
        // extra: '⌘B',
    },
    {
        type: 'divider',
    },
    {
        key: '4',
        label: '退出登录',
        // extra: '⌘S',
    },
];

const PersonalDropdown: React.FC = () => {

    const onClick: MenuProps['onClick'] = ({ key }) => {
        console.log(`Click on item ${key}`);
        if (key === '4') {
            onSubmitSignOut();
        }
    };

    const onSubmitSignOut = () => {
        apiSignOutRequest('testapi').then(res => {
            // 这里是成功回调
            console.log(res)
          }).catch(err => {
            // 这里是错误回调
            console.log(err)
          })
    };


    return (
        <Dropdown menu={{ items, onClick }}>
            <a onClick={(e) => e.preventDefault()}>
                <Space>
                    <PersonalAvatar></PersonalAvatar>
                </Space>
            </a>
        </Dropdown>
    );
}



export default PersonalDropdown;