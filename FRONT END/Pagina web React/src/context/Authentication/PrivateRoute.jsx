import React, { useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "./Auth";

const PrivateRoute = ({ children }) => {
  const { activeSession } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if ( ! activeSession ){
      navigate("/autenticacion")
    }
  }, [])

  return !!activeSession && children;
};


export default PrivateRoute