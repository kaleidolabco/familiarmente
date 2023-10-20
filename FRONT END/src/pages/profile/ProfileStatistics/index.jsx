import React, { useEffect, useState } from 'react';

// MUI imports
import {
    CircularProgress,
    Stack,
    Box,
    Typography
} from '@mui/material';



export const getProgress = (status) => {

    let color = 'secondary';
    let label = 'Postulado'

    switch (status) {
        case 1:
            color = 'secondary'
            label = 'Postulado'
            break;
        case 2:
            color = 'primary'
            label = 'Assessment completado'
            break;
        case 3:
            color = 'warning'
            label = 'Evaluado'
            break;
        case 4:
            color = 'success'
            label = 'Proceso finalizado'
            break;

        default:
            break;
    }

    return { color, label };
}

const ProfileStatistics = ({ PercentProfileCompleted = 50, size = '10rem', userFormData }) => {

    const [percentCompletedProfile, setPercentCompletedProfile] = useState(0);

    function validarNuloOVacio(valor) {
        // Primero, verifica si el valor es nulo o indefinido
        if (valor === null || valor === undefined) {
            return true; // Es nulo o indefinido
        }

        // Luego, verifica si es una cadena de texto y si está vacía
        if (typeof valor === 'string' && valor.trim() === '') {
            return true; // Es una cadena de texto vacía
        }

        // Si no cumple ninguna de las condiciones anteriores, no es nulo ni vacío
        return false;
    }

    useEffect(() => {
        console.log(userFormData)
        const values_to_validate = [
            "nombres",
            "apellidos",
            "correo",
            "descripcion_perfil_usuario",
            "fecha_de_nacimiento",
            "foto_de_perfil",
            "hoja_de_vida",
            "telefono",
            "titulo_profesional"
        ]

        const percent_per_item = 100 / values_to_validate.length;
        let percent = 0;

        for (const element of values_to_validate) {
            if ( !validarNuloOVacio(userFormData[element]) ) percent += percent_per_item;
        }
    
        setPercentCompletedProfile(parseInt(percent));
    }, [])

    return (
        <Stack
            spacing={3}
            direction="column"
            alignItems='center'
            justifyContent='center'
        >
            <Box sx={{ position: 'relative' }} >
                <CircularProgress
                    variant="determinate"
                    value={100}
                    sx={{
                        color: (theme) => theme.palette.secondary.light,
                    }}
                    thickness={9}
                    size={size}
                />
                <CircularProgress
                    variant="determinate"
                    value={percentCompletedProfile}
                    color='primary'
                    sx={{
                        animationDuration: '550ms',
                        position: 'absolute',
                        left: 0
                    }}
                    thickness={9}
                    size={size}
                />
            </Box>

            <Typography variant="body1" component="div" color="primary" sx={{ m: 0 }}>
                {`Tu perfil está completado en un ${percentCompletedProfile}%`}
            </Typography>

            <Typography variant="body2" component="div" color="secondary" sx={{ m: 0 }}>
                Completa tu perfil para tener una mejor oportunidad al postularte a un cargo
            </Typography>

        </Stack>
    )
}

export default ProfileStatistics;