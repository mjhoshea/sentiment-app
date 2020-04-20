import React from "react";
import {NavLink} from "react-router-dom";

function Nav(){
    return(
   <nav>
      <div className="navbar-header">
        <h1><a href="/">SENTIMENT</a></h1>
      </div>
      
        <ul className="navbar">
          <li ><NavLink to="/">Home</NavLink></li>
          <li ><NavLink to="/features">Features</NavLink></li>
          <li ><NavLink to="/contact">Contact</NavLink></li>
        </ul>
  </nav>
    )
}

export default Nav;