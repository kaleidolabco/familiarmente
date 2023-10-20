import { useEffect, useState, useContext } from "react"
import axios from 'axios';

// context
import { AuthContext } from "../context/Authentication/Auth";

export const useFetch = () => {

    // const { token } = useContext(AuthContext);

    const [state, setState] = useState({
        data: null,
        isLoading: false,
        hasError: null,
    })

    const postAWS = async (url, type_action , data, token_auth = null) => {
        setState({
            ...state,
            isLoading: true
        })

        const headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        const authorization = token_auth ?  {
            "headers": {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": token_auth
            }
        }   : null

        const body = {
            "request_data": {
                "type_action": type_action,
                "data": data
            },
            ...authorization
        }

        let response_data = null;
        let error = null

        // console.log(body)
        try {
            const request = await axios.post(url, body, headers)
            const response = await request;
            response_data = response?.data;

            // console.log(response)
        }
        catch (e) {
            console.error(e);
            error = "Error al procesar la solicitud: " + e; 
        }

        setState({
            data: response_data,
            isLoading: false,
            hasError: error
        })

        return response_data
    }

    return {
        data: state.data,
        isLoading: state.isLoading,
        hasError: state.hasError,
        postAWS
    }
}
