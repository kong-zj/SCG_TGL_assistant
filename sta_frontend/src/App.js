import React, { Component, Suspense } from 'react';
// import Header from "./components/Header";
import Login from "./pages/Auth/Login";
import cookie from 'react-cookies';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { } from 'react-router-dom';
import { message } from 'antd';


import logo from './logo.svg';
import './App.css';

function App() {
  return (

    <div>
      {/* 注册路由 */}
      <Suspense>
        <Routes>
          <Route path="/login" element={<Login />} />
        </Routes>
      </Suspense>
    </div>

  )
}

export default App;
