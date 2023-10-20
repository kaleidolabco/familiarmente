import React from "react";
import { useNavigate } from 'react-router-dom';

import { Typography, Container, Alert, Button } from '@mui/material';

function CompletedAssessment() {
    const navigate = useNavigate();

    const handleExit = () => {
        navigate("/cargos");
    };

    return (
        <Container maxWidth="xl" sx={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'flex-end',
        }}>
            <Alert severity="success">La prueba ha sido completada. Te agradecemos mucho el tiempo invertido en ejercicio, si continuas en nuestro proceso uno de nuestros analistas te contactara prontamente y te informara las siguientes etapas del proceso. De igual manera si no cumplieses con el perfil solicitado tu Hoja de Vida estará en nuestra base de datos para futuros procesos.</Alert>
            <Button sx={{ mt: 3, mr: 1 }} onClick={handleExit} variant="contained">
                Salir
            </Button>
        </Container>);
}

export default CompletedAssessment;
