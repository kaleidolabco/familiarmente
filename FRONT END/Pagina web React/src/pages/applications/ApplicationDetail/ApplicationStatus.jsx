import React, { useState } from 'react';

// Utils
import { formatDate } from '../../../utils/format-date';

//MUI imports
import {
    Box,
    Button,
    Container,
    Grid,
    Stepper,
    Step,
    StepLabel,
    StepContent,
    Typography
} from '@mui/material';

// Project imports
import MainCard from '../../../components/MainCard';
import { getProgress } from '../ApplicationCard/StatusGraph';

const steps = [
    {
        label: 'Postulado',
        description: `¡Felicidades por haber dado el primer paso! Al haber completado la postulación, 
            tu currículum ha sido enviado a nuestra empresa. Nuestro equipo de recursos humanos revisará 
            cuidadosamente tu solicitud y perfil en relación con los requisitos del cargo. 
            Mantente atento a tu correo electrónico, ya que podríamos contactarte para obtener información 
            adicional o para avanzar en el proceso de selección.`,
    },
    {
        label: 'Assessment completado',
        description: `¡Excelente trabajo! Has completado el assessment y tus respuestas han sido 
            registradas en nuestro sistema. Ahora, un evaluador revisará minuciosamente tus resultados 
            para determinar tu calificación y cómo encajan tus habilidades con el perfil del cargo. 
            Te pedimos paciencia mientras completamos este análisis y evaluación.`,
    },
    {
        label: 'Evaluado',
        description: `Gracias por tu paciencia. Hemos evaluado tus resultados del assessment y revisado 
            tu perfil en profundidad. Tu desempeño y competencias han sido considerados cuidadosamente por 
            nuestro equipo de selección. Si cumples con los criterios requeridos, pronto recibirás noticias 
            nuestras para la siguiente fase del proceso.`,
    },
    {
        label: 'Proceso finalizado',
        description: `Agradecemos sinceramente tu participación en nuestro proceso de selección. 
            Hemos concluido las evaluaciones y la revisión exhaustiva de los candidatos. 
            En esta etapa, estaremos en contacto contigo para comunicarte los resultados finales. 
            Si has sido seleccionado para el puesto, recibirás una oferta por escrito con detalles sobre 
            las condiciones laborales. En caso contrario, consideraremos tu perfil para futuras oportunidades 
            y te notificaremos sobre otras posiciones que puedan ser de tu interés.`,
    },
];

const ApplicationStatus = ({ applicationData = {} }) => {

    const getStep = (status) => {
        const progress_label = status.toLowerCase();
        let index = 1;

        if (!progress_label) return index;

        switch (progress_label) {
            case 'postulado':
                index = 0;
                break;
            case 'assessment completado':
                index = 1;
                break;
            case 'evaluado':
                index = 2;
                break;
            case 'proceso finalizado':
                index = 3;
                break;
    
            default:
                break;
        }

        return index;
    }

    return (
        <MainCard title='Estado de la aplicación al cargo' sx={{ width: '100%' }} returnButton>
            <Container>

                <Typography variant="h4" component="div" color='primary'>
                    {applicationData.nombre_cargo}
                </Typography>

                <Typography variant="overline" color="text.secondary">
                    {applicationData.empresa_cargo}
                </Typography>

                <Typography variant="body2" color="text.secondary">
                    {applicationData.ubicacion_cargo}
                </Typography>

                <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
                    {`Aplicado el ${formatDate(applicationData.fecha_de_registro)}:`}
                </Typography>

                <Typography variant='body1' sx={{ mb: 3 }}>
                    {`Tu postulación se encunetra en estado de ${applicationData.estado_postulacion}:`}
                </Typography>

                <Stepper activeStep={getStep(applicationData.estado_postulacion)} orientation="vertical">

                    {steps.map((step, index) => (
                        <Step key={step.label} sx={{ color: 'primary' }}>
                            <StepLabel
                                optional={
                                    index === 3 ? (
                                        <Typography variant="caption">Última etapa</Typography>
                                    ) : null
                                }
                            >
                                {step.label}
                            </StepLabel>
                            <StepContent>
                                <Typography>{step.description}</Typography>
                                {index === 2 &&
                                    <Box sx={{ my: 2 }}>
                                        <Typography variant='subtitle2' color='secondary'>TU CALIFICACIÓN:</Typography>
                                        <Typography variant='h3' color='primary'>{`${applicationData.calificacion_final} / 5.00`}</Typography>
                                        <br/>
                                        <Typography variant='subtitle2' color='secondary' >COMENTARIOS DEL EVALUADOR:</Typography>
                                        <Typography variant='body1' color='text.primary'>{applicationData.observaciones_finales}</Typography>
                                    </Box>
                                }
                            </StepContent>
                        </Step>
                    ))}
                </Stepper>
            </Container>
        </MainCard>

    )
}

export default ApplicationStatus;