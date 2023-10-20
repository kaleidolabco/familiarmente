import { useEffect, useState, useContext } from "react"
import axios from 'axios';


export const useUploadFetch = () => {

    // const { token } = useContext(AuthContext);

    const [state, setState] = useState({
        data: null,
        isLoading: false,
        hasError: null,
    })

    const postUpload = async (url, content_type, body) => {
        setState({
            ...state,
            isLoading: true
        })

        const headers = {
            "Content-Type": content_type
        }

        let response_data = null;
        let error = null

        // const result = await fetch(url_subida, {
        //     method: "PUT",
        //     body: profilePhoto,
        // });

        // console.log(body)
        try {
            const response = await axios.put(url, body, {headers});
            response_data = response;
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
        postUpload
    }
}
