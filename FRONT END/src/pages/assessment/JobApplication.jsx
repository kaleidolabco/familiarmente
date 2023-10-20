import { useEffect, useContext, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../hooks';

// Project imports
import MainCard from '../../components/MainCard';
import Loader from '../../components/Loader';

// material-ui
import { Alert, Box, Button, Container, Divider, Grid, Stack, Typography } from '@mui/material';

// assets
import { FormOutlined } from '@ant-design/icons';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';


const JobApplication = () => {

    let { job_id } = useParams();
    const { token, userData } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);
    const navigate = useNavigate();

    const { data: getData, isLoading: getIsLoading, hasError: getHasError, postAWS: getJobAWS } = useFetch();
    const { data: applyData, isLoading: applyIsLoading, hasError: applyHasError, postAWS: applyJobAWS } = useFetch();

    const [jobData, setJobData] = useState(null);
    const [applicationStatus, setApplicationStatus] = useState(null);

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


    useEffect(() => {
        getJob();
        getJobApplication();
    }, []);


    if (getIsLoading || !jobData) {
        return (
            <MainCard title='Cargando datos de postulación...' returnButton={true}>
                <Loader />
                <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
            </MainCard>
        )
    }

    return (
        <MainCard title={jobData.error ? 'Sin información de la postulación' : `Postular a: ${jobData?.nombre}`} 
            returnButton={true}>

            {jobData.error ?

                <Alert severity="info">{jobData.error}</Alert>
                :
                <Container>
                    <Grid container spacing={3} sx={{ textAlign: 'center' }}>
                        <Grid item md={12} >
                            <Typography variant="body1">
                                Bienvenido al proceso de evaluación para el cargo:
                                <span style={{ textTransform: 'uppercase', fontWeight: 'bold' }}>{ ` ${jobData.nombre}.` }</span>
                                <br/>
                                En la siguiente entrevista debes responder a las preguntas que el evaluador
                                te proponga para validar que tu perfil es el adecuado para el cargo.
                                Sigue las instrucciones que se muestran a continuación y presiona sobre
                                "Comenzar Evaluación".
                            </Typography>
                        </Grid>

                        <Grid item md={12} sx={{ mb: 2 }}>
                            <Typography variant="h4" component="div" color="primary">
                                Instrucciones:
                            </Typography>
                            <Typography variant="body1">
                                Para asegurarnos de obtener una evaluación precisa de tus habilidades y aptitudes, te recomendamos seguir las siguientes indicaciones:
                            </Typography>
                            <Typography variant="body">

                            </Typography>
                            <ul className="list" style={{ textAlign: 'left' }}>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Antes de comenzar, asegúrate de que tu dispositivo cuente con una cámara y un micrófono funcionales.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Brinda los permisos necesarios para acceder a la cámara y micrófono de tu dispositivo en el navegador web.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Busca un lugar tranquilo y libre de ruidos donde puedas completar el assessment sin interrupciones.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Asegúrate de que la iluminación del ambiente sea adecuada para que tu rostro esté bien visible durante todo el proceso.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Durante el assessment, mantén siempre tu rostro visible en la cámara para que podamos hacer una evaluación adecuada.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Verifica que tienes una conexión a internet estable y confiable durante todo el proceso del assessment. Una conexión inestable podría afectar la realización adecuada de las tareas.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Realiza el assessment en un momento en el que puedas dedicar toda tu atención a las preguntas y desafíos planteados.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Algunas secciones del assessment pueden tener límite de tiempo. Lee las instrucciones con detenimiento y administra tu tiempo adecuadamente para completar cada tarea.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        Responde a cada pregunta con honestidad y basándote en tus habilidades y experiencia reales.
                                    </Typography>
                                </li>
                                <li>
                                    <Typography variant="body" sx={{ color: 'text.secondary' }}>
                                        No hay respuestas correctas o incorrectas, queremos conocerte tal como eres.
                                    </Typography>
                                </li>
                            </ul>
                        </Grid>
                    </Grid>

                    {/* <Divider sx={{ my: 2 }} /> */}

                    <Stack spacing={1} direction='row' justifyContent='center' sx={{ my: 3 }}>
                        <Button 
                            variant="outlined" 
                            size='large' 
                            startIcon={<FormOutlined />} 
                            component={Link} 
                            to={"assessment/"}
                        >
                            Comenzar Evaluación
                        </Button>
                    </Stack>
                </Container>
            }

        </MainCard>
    )
}

export default JobApplication;