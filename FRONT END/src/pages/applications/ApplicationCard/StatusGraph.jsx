import React from 'react';

// MUI imports
import {
    CircularProgress,
    Stack,
    Box,
    Typography
} from '@mui/material';



export const getProgress = (status) => {

    let color = 'secondary';
    let label = 'Postulado';
    let progress = 0;

    switch (status.toLowerCase()) {
        case 'postulado':
            color = 'secondary'
            label = 'Postulado'
            progress = 25
            break;
        case 'assessment completado':
            color = 'primary'
            label = 'Assessment completado'
            progress = 50
            break;
        case 'evaluado':
            color = 'warning'
            label = 'Evaluado'
            progress = 75
            break;
        case 'proceso finalizado':
            color = 'success'
            label = 'Proceso finalizado'
            progress = 100
            break;

        default:
            break;
    }

    return { color, label, progress };
}

const StatusGraph = ({ status = 'Postulado', size = '3rem' }) => {

    const progress = getProgress(status)

    return (
        <Stack 
            spacing={{md: 0, xs: 2}} 
            direction={{ md: "column", xs: "row" }} 
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
                    value={progress.progress}
                    color={progress.color}
                    sx={{
                        animationDuration: '550ms',
                        position: 'absolute',
                        left: 0
                    }}
                    thickness={9}
                    size={size}
                />
            </Box>

            <Typography variant="body1" component="div" color="primary" sx={{m:0}}>
                {progress.label}
            </Typography>

        </Stack>
    )
}

export default StatusGraph;