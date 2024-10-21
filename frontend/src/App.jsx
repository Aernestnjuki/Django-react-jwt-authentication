import React from 'react'
import { createBrowserRouter, createRoutesFromElements, RouterProvider, Route } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'

import Homepage from './pages/Homepage'
import Loginpage from './pages/Loginpage'
import RegisterPage from './pages/RegisterPage'

const App = () => {

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path='/' element={ <AuthProvider />} >
        <Route index element={ <Homepage />} />
        <Route path='/register' element={ <RegisterPage />} />
        <Route path='/login' element={ <Loginpage />} />
      </Route>
    )
  )

  return <RouterProvider router={router} />
}

export default App