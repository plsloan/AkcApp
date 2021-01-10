import { Layout, Menu } from "antd";
import React, { useState } from "react";
import { withRouter } from "react-router-dom";

import { AppRoutes } from "../utils";

function SideBarC(props) {
  const { history } = props
  const { Header, Sider } = Layout;

  const appRoutesKeys = Object.keys(AppRoutes)

  const [isSideBarCollapsed, setIsSideBarCollapsed] = useState(false);
  const [selectedMenuKey, setSelectedMenuKey] = useState(appRoutesKeys.length ? appRoutesKeys[0] : '');

  const onClickMenuItem = (route) => () => {
    const selectedKey = appRoutesKeys.find(val => AppRoutes[val] === route) || ''
    setSelectedMenuKey(selectedKey)
    
    history.push(route)
  }
  const onCollapseSideBar = (collapsed, _type) => setIsSideBarCollapsed(collapsed);

  return (
    <Sider collapsible collapsed={isSideBarCollapsed} onCollapse={onCollapseSideBar} width='150px' >
      <Header />
      <Menu defaultSelectedKeys={['home']} theme="dark" selectedKeys={[selectedMenuKey]}>
          {appRoutesKeys.map((key) => 
              <Menu.Item 
                key={key}
                onClick={onClickMenuItem(AppRoutes[key])}
              >
                {key}
              </Menu.Item>
          )}
      </Menu>
    </Sider>
  );
}

export const SideBar = withRouter(SideBarC);