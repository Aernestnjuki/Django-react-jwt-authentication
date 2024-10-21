import React, {useContext} from 'react'
import axios from 'axis'
import jwt_decode from 'jwt-decode'
import dayjs from 'dayjs'
import AuthContext from '../context/AuthContext'

const baseURL = "http://127.0.0.1:8000/"

const UseAxios = () => {

  const [authToken, setUser, setAuthTokens] = useContext(AuthContext)  
  return (
    <div>UseAxios</div>
  )
}

export default UseAxios