import React, { useState, useEffect, useContext } from 'react';

// MUI components
import { CircularProgress } from '@mui/material';

// custom hooks
import { useFetch } from '../../../../hooks';

// Context
import { AuthContext } from '../../../../context/Authentication/Auth';
import { ContextUI } from '../../../../context/ContextUI';

// Componentes
import AvatarQuestion from './AvatarQuestion';
import VideoQuestion from './VideoQuestion';


const Avatar = ({ questionData, setIsAvatarQuestion }) => {

    const { openAlert } = useContext(ContextUI);

    const { data, isLoading, hasError, postAWS } = useFetch();

    const [avatarTypeData, setAvatarTypeData] = useState(null);
    const [avatarType, setavatarType] = useState(null);

    const getTipoAvata = async () => {

        if ( !(questionData.id_parametro_tipo_avatar) ){
            setAvatarTypeData({});
            setavatarType('sin avatar');
            return;
        }

        const aws_request = await postAWS(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_parameter",
            {
                "id": questionData.id_parametro_tipo_avatar
            },
            null
        );

        if (!aws_request) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al obtener los datos del entrevistador",
                'error'
            );
            return;
        }

        if (aws_request.success) {
            const data_avatar_type = aws_request.data;
            setAvatarTypeData(data_avatar_type);
            setavatarType(data_avatar_type.nombre);
            // console.log(data_avatar_type);
        }
        else {
            if (aws_request.message) {
                openAlert(`${aws_request.message}: ${aws_request.error?.error}`, 'error');
            }
        }
    }

    useEffect ( () => {
        getTipoAvata();
    }, []);

    // Si no existe avatar, lo notifico al padre para cargar la pregunta de manera diferente
    useEffect ( () => {
        const with_avatar = avatarType?.toLowerCase() != 'sin avatar';
        setIsAvatarQuestion(with_avatar);
    }, [avatarType]);


    if (isLoading || !avatarTypeData || !avatarType) {
        return (
            <CircularProgress />
        )
    }

    if ( avatarType?.toLowerCase() == 'video propio'){
        return <VideoQuestion urlVideo={ questionData.video_avatar_pregunta }/>
    }

    if ( avatarType?.toLowerCase() == 'avatar virtual'){
        return <AvatarQuestion idAvatar={ questionData.id_avatar_virtual } textAvatar = {questionData.texto_avatar}/>
    }

    if ( avatarType?.toLowerCase() == 'sin avatar'){
        return null
    }
}

export default Avatar;
