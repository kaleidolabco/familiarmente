import React, { useEffect, useState, useContext } from "react";
import { useNavigate } from 'react-router-dom';

// Custom hooks
import { useFetch } from "../../hooks";

// Custom components
import Loader from "../../components/Loader";

// Contexts
import { ContextUI } from "../ContextUI";
export const AuthContext = React.createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);
  const [userData, setUserData] = useState(null);
  const [activeSession, setActiveSession] = useState(false)
  const [pending, setPending] = useState(true);

  const { postAWS } = useFetch();
  const navigate = useNavigate();
  const { openAlert } = useContext(ContextUI)

  useEffect(() => {

    const ls_token = localStorage.getItem('token');
    // const ls_user_data = localStorage.getItem('user_data');

    if (ls_token && ls_token != "null") {
      validateToken(ls_token);
    }
    else {
      setPending(false);
    }
  }, []);

  useEffect( ()=>{
    localStorage.setItem('token', token)
    localStorage.setItem('user_data', userData)
  }, [token, userData])

  const validateToken = async (token_to_validate) => {

    const aws_request = await postAWS(import.meta.env.VITE_AWS_AUTH_ENDPOINT,
      "validate_token",
      { "token": token_to_validate },
      false
    );

    // console.log(aws_request)

    if (aws_request.success) {

      setToken(token_to_validate);
      setUserData(aws_request.data);
      setActiveSession(true);
      // if(location.pathname == '/autenticacion' || location.pathname == '/registro'){
      //   navigate('/');
      // }
    } else {
      openAlert('Sesión expirada', 'warning')
    }
    setPending(false);
  }


  const login = (token, user_data) => {
    setToken(token);
    setUserData( JSON.parse(user_data) );
    setActiveSession(true)
    navigate("/perfil");
  }

  const logout = () => {
    localStorage.clear();
    navigate("/autenticacion");
  }

  if (pending) {
    return (<Loader />)
  }

  return (
    <AuthContext.Provider
      value={{
        activeSession, token, userData, login, logout
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};