import 'antd/dist/antd.css';
import { Layout } from 'antd';
import React from "react";
import { BrowserRouter, Redirect, Route } from 'react-router-dom';

import { BreedsList } from 'breeds-list/BreedList';
import { BreedDetails } from 'breeds-list/breed-details/BreedDetails';
import { BreedSearch } from 'breed-search/BreedSearch';
import { Home } from 'home/Home';
import { AppRoutes } from 'utils';

import './App.css';
import { SideBar } from 'sidebar/SideBar';


const App = () => {
  const { Content, Header } = Layout;

  return (
    <Layout className="App" hasSider>
      <BrowserRouter>
        <SideBar />
        
        <Content id='appContent'>
          <Header id='headerContainer'>
            <h1 id='appTitle'>AKC Breed Data</h1>
          </Header>

          {/* app content */}
          <div id='pageContent'>
            <Route path={AppRoutes.Home} component={Home} />
            <Route exact path={AppRoutes.BreedSearch} component={BreedSearch} />
            <Route exact path={`${AppRoutes.Breeds}/:id`} component={BreedDetails} />
            <Route exact path={AppRoutes.Breeds} component={BreedsList} />
            <Redirect from='*' to={AppRoutes.Home} />
          </div>
        </Content>
      </BrowserRouter>
    </Layout>
  );
}

export default App;
