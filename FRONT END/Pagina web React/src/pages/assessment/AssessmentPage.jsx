import { useEffect, useContext, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../hooks';

// Project imports
import MainCard from '../../components/MainCard';
import QuestionView from './QuestionView';
import CompletedAssessment from './CompletedAssessment';
import Loader from '../../components/Loader';

// material-ui
import { Alert, Button, Container, Divider, Grid, Stack, Typography } from '@mui/material';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';

const AssessmentPage = () => {

    let { job_id } = useParams();
    const { token, userData } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);
    const navigate = useNavigate();

    const { data: getData, isLoading: getIsLoading, hasError: getHasError, postAWS: getAssessmentDataAWS } = useFetch();
    const { data: getApplicationData,
        isLoading: getApplicationIsLoading,
        hasError: getApplicationHasError,
        postAWS: getApplicationDataAWS
    } = useFetch();

    const { data: updateApplicationData,
        isLoading: updateApplicationIsLoading,
        hasError: updateApplicationHasError,
        postAWS: updateApplicationAWS
    } = useFetch();

    const [assessmentFinished, setAssessmentFinished] = useState(false);

    const [assessmentData, setAssessmentData] = useState(null);
    const [questionsList, setQuestionsList] = useState(null);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [currentQuestion, setCurrentQuestion] = useState(null);

    
    // Función para cambiar de pregunta
    const handleNextQuestion = () => {

        if( !questionsList ) return;
        
        if (currentQuestionIndex < questionsList.length - 1) {
            setCurrentQuestionIndex(currentQuestionIndex + 1);
            setCurrentQuestion( questionsList[currentQuestionIndex + 1]);
        } else {
            // Assessment Finalizado
            onCompletedAssessment();
        }

    };


    // Función para obtener el estado del candidato en el assessment
    const getApplicationStatus = async () => {

        const data = await getApplicationDataAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_job_application",
            {
                "id_usuario_candidato": userData.id,
                "id_cargo": job_id
            },
            token
        );

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al intentar obtener los datos de la postulación del candidato",
                'error'
            );
            return null;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            return null;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        const dataPostulacion = data.data;
        return dataPostulacion
    }

    // Función para obtener los datos del assessment del cargo seleccionado
    const getAssessmentJob = async () => {

        const data_postulacion = await getApplicationStatus();
        const estado_postulacion = data_postulacion?.estado_postulacion?.toLowerCase()

        if (estado_postulacion != 'postulado') {
            setAssessmentFinished(true);
            return;
        }

        const data = await getAssessmentDataAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_job_assessment_data",
            {
                "id_cargo": job_id
            },
            token
        );

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al intentar obtener los datos del assessment",
                'error'
            );
            setAssessmentData({ error: 'Lo sentimos, no se ha podido acceder a la información del assessment' })
            return;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            setAssessmentData({ error: 'Lo sentimos, no se ha podido acceder a la información del assessment' })
            return;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        const dataAssessment = data.data;

        setAssessmentData(dataAssessment);
    
    }

    // Función para extraer la lista de preguntas de la lista disponible
    function extractQuestions(assessment_data) {
        const questions = [];

        function extractFromCompetencia(competencia) {
            if (competencia.datos_momentos && competencia.datos_momentos.momentos) {
                competencia.datos_momentos.momentos.forEach(momento => {
                    if (momento.datos_preguntas && momento.datos_preguntas.preguntas) {
                        momento.datos_preguntas.preguntas.forEach(pregunta => {
                            questions.push({
                                id: pregunta.id,
                                pregunta: pregunta.pregunta,
                                competencia: competencia.nombre,
                                momento: momento.nombre
                            });
                        });
                    }
                });
            }
        }

        if (assessment_data && assessment_data.datos_competencias && assessment_data.datos_competencias.competencias) {
            assessment_data.datos_competencias.competencias.forEach(competencia => {
                extractFromCompetencia(competencia);
            });
        }

        return questions;
    }

    // Función para actualizar aplicación a assessment completado
    const onCompletedAssessment = async () => {

        const data = await updateApplicationAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "update_job_application_completed_assessment",
            {
                "id_usuario_candidato": userData.id,
                "id_cargo": job_id,
                "id_assessment": assessmentData.id
            },
            token
        );


        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al finalizar el envío de datos de la entrevista",
                'error'
            );
            setAssessmentFinished(true);
            return;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            setAssessmentFinished(true);
            return;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        openAlert(`¡Datos enviados de forma exitosa!`, 'success');
        setAssessmentFinished(true);
    }

    useEffect(() => {
        getAssessmentJob();
    }, []);

    useEffect ( () => {
        if(!assessmentData) return;

        // De los datos del assessment extraigo las preguntas
        const questionsArray = extractQuestions(assessmentData);
        
        if(questionsArray.length > 0){
            setQuestionsList(questionsArray);
            setCurrentQuestion(questionsArray[currentQuestionIndex])
        }else{
            onCompletedAssessment();
        }
    }, [assessmentData])


    if (assessmentFinished) {
        return (
            <MainCard
                title={"¡Has completado la aplicación al cargo!"}
                returnButton={true}
            >
                <CompletedAssessment />
            </MainCard>
        );
    }

    if (getIsLoading || !assessmentData || !currentQuestion) {
        return (
            <MainCard title='Cargando datos del cargo...' returnButton={true}>
                <Loader />
                <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
            </MainCard>
        )
    }

    return (
        <MainCard
            title={assessmentData.error ? 'Sin información del assessment' : `Entrevista`}
            returnButton={true}
        >
            {assessmentData.error ?

                <Alert severity="info">{assessmentData.error}</Alert>
                :
                <QuestionView
                    question={currentQuestion}
                    onContinue={handleNextQuestion}
                    assessmentId={assessmentData?.id ?? 'indeterminado'}
                />

            }
        </MainCard>
    )
}

export default AssessmentPage;