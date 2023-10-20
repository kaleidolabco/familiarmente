import React from 'react'
import { Link } from 'react-router-dom';

// material ui imports
import { styled } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

// Project imports
import StatusGraph from './StatusGraph';

// Utils
import { formatDate } from '../../../utils/format-date';

const Img = styled('img')({
    margin: 'auto',
    display: 'block',
    maxWidth: '100%',
    maxHeight: '100%',
});

const ApplicationCard = ( { applicationData={} } ) => {

    return (
        <Paper
            sx={{
                p: 2,
                margin: '.5rem 0',
                width: '100%',
                flexGrow: 1,
                border: 'none',
                boxShadow: 'none',
                backgroundColor: (theme) =>
                    theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
            }}
        >
            <Grid container spacing={2}>

                <Grid item xs={12} md={12} sm container>
                    <Grid item xs container direction="row" spacing={1}>

                        <Grid xs={12} md={12} item>
                            <Typography gutterBottom variant="h5" component="div" color="primary" sx={{m:0}}>
                                { applicationData.nombre }
                            </Typography>
                        </Grid>

                        <Grid xs={12} md={8} item container>
                            <Grid item xs={12} md={12} sm>
                                <Typography variant="overline" color="text.secondary">
                                    { applicationData.empresa_oferente }
                                </Typography>
                            </Grid>

                            <Grid item xs={12} md={12}>
                                <Typography variant="body2" color="text.secondary">
                                    UBICACIÓN: { applicationData.ubicacion }
                                </Typography>
                            </Grid>

                            <Grid item xs={12} md={12}>
                                <Typography variant="overline" color="text.secondary">
                                    { formatDate(applicationData.fecha_de_postulacion) }
                                </Typography>
                            </Grid>
                        </Grid>

                        <Grid xs={12} md={4} item container sx={{justifyContent:{md: 'center', xs:'flex-start'}}}>
                            <StatusGraph status={ applicationData.estado_postulacion }/>
                        </Grid>


                        <Grid item md={12}>
                            <Button 
                                size='small' 
                                variant="outlined" 
                                component={Link} 
                                to={applicationData.id_cargo}
                            >
                                VER MÁS DETALLES
                            </Button>
                        </Grid>
                    </Grid>

                </Grid>
            </Grid>
        </Paper>
    )
}


export default ApplicationCard;