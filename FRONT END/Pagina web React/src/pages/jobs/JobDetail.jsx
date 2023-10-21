import { useEffect, useContext, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../hooks';

// material-ui
import { Alert, Button, Divider, Grid, Stack, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';

// assets
import { FormOutlined } from '@ant-design/icons';

//Project Imports
import MainCard from '../../components/MainCard';
import Loader from '../../components/Loader';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';

const loremIpsum = '¡Únete a nuestro equipo como Desarrollador de Software en Tecnosoft S.A.! Estamos buscando a un profesional apasionado por la programación y el desarrollo de soluciones tecnológicas innovadoras. Si te encanta enfrentar desafíos técnicos y trabajar en un entorno dinámico, esta es tu oportunidad de marcar la diferencia en el mundo digital. Como Desarrollador de Software, serás parte de un equipo talentoso encargado de diseñar, desarrollar e implementar aplicaciones web de alta calidad para satisfacer las necesidades de nuestros clientes.'

const JobDetail = () => {

    let { job_id } = useParams();
    const { token, userData } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);
    const navigate = useNavigate();

    const { data: getData, isLoading: getIsLoading, hasError: getHasError, postAWS: getJobAWS } = useFetch();
    const { data: applyData, isLoading: applyIsLoading, hasError: applyHasError, postAWS: applyJobAWS } = useFetch();

    const [jobData, setJobData] = useState(null);
    const [applicationStatus, setApplicationStatus] = useState(null);

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

    // Función para obtener los datos del cargo seleccionado
    const getJob = async (id) => {

        const data = await getJobAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_job",
            {
                "id": job_id
            },
            token
        );

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al intentar obtener los datos de este cargo",
                'error'
            );
            return;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            setJobData({ error: 'Lo sentimos, no se ha podido acceder a la información de este cargo' })
            return;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        const dataJob = data.data;

        setJobData(dataJob);
    }

    // Función para obtener los datos de postulación a este cargo
    const getJobApplication = async () => {

        const data = await applyJobAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_job_application",
            {
                "id_usuario_candidato": userData.id,
                "id_cargo": job_id
            },
            token
        );

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al obtener los datos de postulación a este cargo",
                'error'
            );
            return;
        }

        if (data.success) {
            // Existe una postulación creada para este cargo
            setApplicationStatus(data.data.estado_postulacion);
        }
        else {
            // openAlert(`${data.message}: ${data.error?.error}`, 'error')
            // return;
        }
    }

    // Función para crear una postulacion al cargo seleccionado
    const applyToJob = async () => {

        const data = await applyJobAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "apply_to_job",
            {
                "id_usuario_candidato": userData.id,
                "id_cargo": job_id
            },
            token
        );

        console.log(data)

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al postular a este cargo",
                'error'
            );
            return;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            return;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        const dataApplication = data.data;
        navigate('postular')
    }

    useEffect(() => {
        getJob();
        getJobApplication();
    }, []);

    if (getIsLoading || !jobData) {
        return (
            <MainCard title='Cargando datos del cargo...' returnButton={true}>
                <Loader />
                <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
            </MainCard>
        )
    }

    return (
        <MainCard
            title={jobData.error ? 'Sin información del cargo' : `Detalles del cargo: ${jobData?.nombre}`}
            returnButton={true}>

            {jobData.error ?

                <Alert severity="info">{jobData.error}</Alert>
                :
                <>
                    <Grid container spacing={1}>

                        <Grid item xs={12} md={6} >
                            <Stack spacing={1} direction='row'>
                                <Typography color="text.secondary">Salario:</Typography>
                                <Typography variant="subtitle1" sx={{ mb: 1.5 }} color="text.primary">
                                    {`${parseFloat(jobData.minimo_salario_mensual).toLocaleString()} - 
                                        ${parseFloat(jobData.maximo_salario_mensual).toLocaleString()}  ${jobData.moneda}`}
                                </Typography>
                            </Stack>

                            <Typography color="text.secondary">
                                Ubicación: {jobData.ubicacion} {jobData.trabajo_remoto ? '(REMOTO)' : ''}
                            </Typography>
                        </Grid>

                        <Grid item xs={12} md={6} sx={{ textAlign: { xs: 'left', md: 'right' } }}>
                            <Typography sx={{ fontSize: '1.1rem' }} variant="button" display="block" color="primary">
                                {jobData.empresa_oferente || 'SIN EMPRESA'}
                            </Typography>
                            <Typography color="text.secondary">
                                {formatDate(jobData.fecha_de_registro)}
                            </Typography>
                        </Grid>

                    </Grid>

                    <Divider sx={{ my: 2 }} />

                    <Grid container spacing={3}>

                        <Grid item md={12} >
                            <Typography variant="body1" dangerouslySetInnerHTML={{ __html: jobData.descripcion }} />
                        </Grid>

                        <Grid item md={12} >
                            <Typography variant="h4" component="div" color="primary">
                                Requisitos:
                            </Typography>
                            <Typography variant="body1" dangerouslySetInnerHTML={{ __html: jobData.requisitos }} />
                        </Grid>

                        <Grid item md={12} >
                            <Typography variant="h4" component="div" color="primary">
                                Proceso de contratación:
                            </Typography>
                            <Typography variant="body1" dangerouslySetInnerHTML={{ __html: jobData.proceso_de_contratacion }} />
                        </Grid>

                        <Grid item md={12} >
                            <Typography sx={{ mb: 1.5, fontSize: '1.1rem', textAlign: 'right' }} color="text.secondary">
                                {`${jobData.vacantes} vacantes`}
                            </Typography>
                        </Grid>

                    </Grid>

                    <Divider sx={{ my: 2 }} />


                    <Stack spacing={1} direction='row' justifyContent='right' >
                        {/* <Button variant="contained" size='large' startIcon={<FormOutlined />} component={Link} to="postular">
                            POSTULAR AL CARGO
                        </Button> */}
                        {
                            applicationStatus ?
                                applicationStatus == "Postulado" ?
                                    <Button variant="contained" size='large' startIcon={<FormOutlined />} component={Link} to="postular">
                                        COMPLETAR ASSESSMENT
                                    </Button>
                                    :
                                    <Button variant="contained" size='large' startIcon={<FormOutlined />}
                                        component={Link}
                                        to={"/aplicaciones/" + job_id}
                                    >
                                        VER ESTADO DE POSTULACIÓN
                                    </Button>
                                :
                                <LoadingButton
                                    disableElevation
                                    loadingPosition="start"
                                    startIcon={<FormOutlined />}
                                    loading={applyIsLoading}
                                    disabled={applyIsLoading || getIsLoading}
                                    onClick={applyToJob}
                                    // fullWidth
                                    size="large"
                                    variant="contained"
                                    color="primary"
                                >
                                    {applyIsLoading ? "POSTULANDO..." : "POSTULAR AL CARGO"}
                                </LoadingButton>
                        }

                    </Stack>

                </>
            }


        </MainCard>

    )
}

export default JobDetail;