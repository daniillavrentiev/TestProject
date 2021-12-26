import React, {useState, useEffect} from "react";
import axios from "axios";
import MyNavbar from "./components/NavBar/NavBar";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './App.css';

function App() {

  return (

    <div className='App'>
            <Router>
                <MyNavbar />
            </Router>
      </div>
  );
}

export default App;
