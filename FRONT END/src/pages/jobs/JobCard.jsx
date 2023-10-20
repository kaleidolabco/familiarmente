import React from 'react'
import { Link } from 'react-router-dom';

import { styled } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

const Img = styled('img')({
    margin: 'auto',
    display: 'block',
    maxWidth: '100%',
    maxHeight: '100%',
});

export const JobCard = ({ jobData = {} }) => {

    const onClickJob = () => {

    }

    function extractTextFromHTML(htmlString) {
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlString, 'text/html');
        const text = doc.body.textContent;
        return text;
    }

    function formatDate(inputDate) {
        const months = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ];

        const dateParts = inputDate.split(" ")[0].split("-");
        const year = dateParts[0];
        const month = parseInt(dateParts[1], 10) - 1;
        const day = parseInt(dateParts[2], 10);

        return `${day} de ${months[month]} de ${year}`;
    }

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
                    <Grid item xs container direction="column" spacing={2}>
                        <Grid item xs>
                            <Typography gutterBottom variant="h5" component="div" color="primary">
                                {jobData.nombre || 'Nombre del cargo'}
                            </Typography>

                            <Grid container>
                                <Grid item xs={12} md={8} sm container>
                                    <Typography variant="overline" color="text.secondary">
                                        {jobData.empresa_oferente || 'Sin empresa'}
                                    </Typography>
                                </Grid>

                                <Grid item xs={12} md={4} sm container sx={{ justifyContent: 'flex-end' }}>
                                    <Typography variant="overline" color="text.secondary" textAlign='right'>
                                        {formatDate(jobData.fecha_de_registro)}
                                    </Typography>
                                </Grid>
                            </Grid>


                            <Typography
                                variant="body2"
                                gutterBottom
                                sx={{
                                    overflow: "hidden",
                                    textOverflow: "ellipsis",
                                    display: "-webkit-box",
                                    WebkitLineClamp: "3",
                                    WebkitBoxOrient: "vertical",
                                }}>
                                {extractTextFromHTML(jobData.descripcion || 'Sin descripción')}
                            </Typography>

                            <Grid container>
                                <Grid item xs={12} md={8} sm container>
                                    <Typography variant="body2" color="text.secondary">
                                        UBICACIÓN: {jobData.ubicacion} {jobData.trabajo_remoto? '(REMOTO)': ''}
                                    </Typography>
                                </Grid>

                                <Grid item xs={12} md={4} sm container sx={{ justifyContent: { xs: 'flex-start', md: 'flex-end' } }}>
                                    <Typography variant="body2" color="text.secondary">
                                        {jobData.vacantes + ' vacantes' || ''} 
                                    </Typography>
                                </Grid>
                            </Grid>

                        </Grid>

                        <Grid item>
                            <Button size='small' variant="outlined" component={Link} to={jobData.id}>MÁS DETALLES</Button>
                        </Grid>
                    </Grid>

                    {/* <Grid item>
                        <Typography variant="subtitle1" component="div">
                            18 - agosto - 2023
                        </Typography>
                    </Grid> */}
                    {/* <Grid item>
                        <Img
                            style={{ width: 50, height: 50, objectFit: 'contain' }}
                            alt="complex"
                            src="https://www.innpulsacolombia.com/milab/sites/default/files/styles/large/public/2021-07/LOGO_POSITIVO%20%282%29%20%281%29.png?itok=r98JhCuK" />
                    </Grid> */}

                </Grid>
            </Grid>
        </Paper>
    )
}
