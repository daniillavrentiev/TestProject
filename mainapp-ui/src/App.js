import React, {useState, useEffect} from "react";
import axios from "axios";
import MyNavbar from "./components/NavBar/NavBar";
import ProductList from "./components/Products/ProductList";
import ProductDetail from "./components/Products/ProductDetail";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {

  return (

    <div className='App'>
            <Router>
                <MyNavbar />
                <Switch>
                    <Route path="/product/" exact component={ProductList} />
                    <Route path="/product_detail/:id/" exact component={ProductDetail} />
                </Switch>
            </Router>
      </div>
  );
}

export default App;
