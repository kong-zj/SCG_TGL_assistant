import React, { Component, Suspense } from 'react';
import cookie from 'react-cookies';
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'
import { } from 'react-router-dom';
import { message } from 'antd';

import SignIn from "./pages/auth/SignIn";
import SignUp from "./pages/auth/SignUp";
import Index from "./pages/Index";
import Home from "./pages/Home"
import ProductList from './pages/product/ProductList';
import ProductDetail from './pages/product/ProductDetail';

import logo from './logo.svg';
import './App.css';

function App() {
  return (

    <div>
      {/* 注册路由 */}
      <Suspense>
        <Routes>
          <Route path="/index" element={<Index />} />
          <Route path="/" element={<Index />} />

          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />

          <Route path="/home" element={<Home />} />
          <Route path="/productlist" element={<ProductList />} />
          <Route path="/product/:pk" element={<ProductDetail />} />


        </Routes>
      </Suspense>
    </div>

  )
}

export default App;
