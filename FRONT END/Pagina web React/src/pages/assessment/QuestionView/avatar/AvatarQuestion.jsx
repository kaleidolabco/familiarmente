import React, { useState, useEffect, useContext } from 'react';
import  {SitePal} from 'sitepal-react-v2'; 

// MUI components
import { CircularProgress } from '@mui/material';

// custom hooks
import { useFetch } from '../../../../hooks';

// Context
import { AuthContext } from '../../../../context/Authentication/Auth';
import { ContextUI } from '../../../../context/ContextUI';

const AvatarQuestion = ({ idAvatar, textAvatar }) => {

    const { postAWS, isLoading, hasError, data } = useFetch();
    const { token } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);

    const [sayText, setSayText] = useState(null);
    const [avatarData, setAvatarData] = useState(null);

    const getAvatarData = async () => {
        
        const aws_request = await postAWS(import.meta.env.VITE_AWS_ASSESSMENTS_ENDPOINT,
            "get_avatar", {
                "id": idAvatar
            }, 
            token
        );

        if (!aws_request) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al intentar cargando al entrevistador",
                'error'
            );
            return;
        }

        // console.log(aws_request)
        if (aws_request.success) {
            const data_avatar = aws_request.data;
            // console.log(idAvatar, data_avatar)
            setAvatarData(data_avatar);

            // Escucho la carga del avatar para reproducir el audio de la pregunta
            window.vh_sceneLoaded = () => {
                console.log("Avatar Cargado");
                // if( !avatarData || !textAvatar ) return;
                setSayText([textAvatar, data_avatar.voz, data_avatar.lenguaje, data_avatar.motor]);
            }
        }
        else {
            if (data.message) {
                openAlert(`${data.message}: ${data.error?.error}`, 'error');
            }
        }
    }

    useEffect ( () => {
        getAvatarData();
    }, []);


    if (isLoading || !avatarData) {
        return (
            <CircularProgress />
        )
    }

    return (

        // https://www.sitepal.com/docs/vhost_API_Reference.pdf - pag 7
        <SitePal
            embed={`${avatarData.id_cuenta_sitepal}, 600, 800,"", 1, 2, ${avatarData.id_escena_sitepal}, 0, 1, 1, "${avatarData.id_embed_sitepal}", 0, 1`}
            sayText={sayText}
        />
    )
}

export default AvatarQuestion;