import React from 'react'
import { Link } from 'react-router-dom'

const NavBar = () => {
  return (
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
                Nested Tech
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/">Home</a>
              </li>
              {/* {token === null &&  */}
              <>
                <li class="nav-item">
                  <Link class="nav-link" to="/login">Login</Link>
                </li>
                <li class="nav-item">
                  <Link class="nav-link" to="/register">Register</Link>
                </li>
              </>
              {/* } */}

            {/* {token !== null &&  */}
              <>
                <li class="nav-item">
                  <a class="nav-link" href="#">Dashboard</a>
                </li>
                <li class="nav-item">
                  {/* <a class="nav-link" onClick={logoutUser} style={{cursor:"pointer"}}>Logout</a> */}
                </li>
              </>
              {/* }    */}
              
            </ul>
          </div>
        </div>
      </nav>
  )
}

export default NavBar