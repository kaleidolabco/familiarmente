import { useEffect, useContext, useState, useRef } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';

// Custom hooks
import { useFetch, useUploadFetch } from '../../../hooks';

// Project imports
import Avatar from './avatar/Avatar';
import Camera from './camera';
import Timer from './timer';
import Loader from '../../../components/Loader';

// material-ui
import { Alert, Button, Container, Divider, Grid, Stack, Typography } from '@mui/material';
import LoadingButton from '@mui/lab/LoadingButton';

// assets
import { VideoCameraOutlined, ArrowRightOutlined } from '@ant-design/icons';

// Contexts
import { AuthContext } from '../../../context/Authentication/Auth';
import { ContextUI } from '../../../context/ContextUI';

const QuestionView = ({ question, assessmentId, onContinue }) => {

    const { token, userData } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);
    const navigate = useNavigate();

    const { data: getData, isLoading: getIsLoading, hasError: getHasError, postAWS: getQuestionAWS } = useFetch();
    const { data: updateData, isLoading: updateIsLoading, hasError: updateHasError, postAWS: updateAnswerAWS } = useFetch();
    const { isLoading: isLoadingGetUrlUpload, postAWS: getUrlUpload } = useFetch();
    const { isLoading: isLoadingUpload, hasError: hasErrorUpload, postUpload: putUpload } = useUploadFetch();

    // Variable para gestionar el estado de carga y deshabilitar el botón de submit
    const isLoading = getIsLoading || isLoadingUpload || isLoadingGetUrlUpload || updateIsLoading;

    const cameraRef = useRef(null);
    const [recording, setRecording] = useState(false);
    const [recordedChunks, setRecordedChunks] = useState(false);
    const [isPreparing, setIsPreparing] = useState(true);
    const [questionData, setQuestionData] = useState(null);
    const [questionFinished, setQuestionFinished] = useState(false);
    const [isAvatarQuestion, setIsAvatarQuestion] = useState(true);

    const startRecording = () => {
        setRecording(true);
        cameraRef?.current?.handleStartCapture(); 
    }

    const stopRecording = () => {
        setRecording(false);
        setRecordedChunks(true);
        cameraRef?.current?.handleStopCapture();
    }

    // Obtener datos de la pregunta
    const getQuestionData = async (pregunta_id) => {

        const candidate_answer = await getAnswer(pregunta_id);
        
        if (candidate_answer) {
            openAlert(
                "Ya enviaste una respuesta a esta pregunta. Presiona sobre 'Continuar' para pasar a la siguiente pregunta",
                'warning'
            );
            setRecordedChunks(true);
            setQuestionFinished(true);
        }

        const data = await getQuestionAWS(import.meta.env.VITE_AWS_ASSESSMENTS_ENDPOINT,
            "get_question_candidate",
            {
                "id": pregunta_id
            },
            token
        );

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al intentar obtener los datos de la pregunta",
                'error'
            );
            return;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            setQuestionData({ error: 'Lo sentimos, no se ha podido acceder a la información de esta pregunta' })
            return;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        const dataQuestion = data.data;
        // console.log(dataQuestion)

        setQuestionData(dataQuestion);
    }

    // Obtener datos de una respuesta si existen
    const getAnswer = async (pregunta_id) => {
        const data = await getQuestionAWS(import.meta.env.VITE_AWS_ASSESSMENTS_ENDPOINT,
            "get_answer_candidate",
            {
                "id_usuario_candidato": userData.id,
                "id_pregunta": pregunta_id
            },
            token
        );

        if (!data) {
            return null;
        }

        if (!data.success) {
            return null;
        }

        

        // después de validar la data seteo los datos para mostrar en el formulario
        const respuesta_usuario = data.data?.video_respuesta_usuario;
        return respuesta_usuario;
    }

    // Función para empezar con el preocesamiento de la respuesta y enviarla
    const processAnswer = async () => {

        const video_data = await cameraRef?.current?.handleGetVideoAnswer();
        const video_file = video_data?.video_file;
        const emotions_data = video_data?.emotions;
        // console.log(video_file);

        const url_video_respuesta = await uploadVideoAnswer(video_file);
        if (!url_video_respuesta) {
            setQuestionFinished(true);
            return
        }

        const data = {
            "id_usuario_candidato": userData.id,
            "id_pregunta": question.id,
            "video_respuesta_usuario": url_video_respuesta,
            "data_emociones": emotions_data
        }

        console.log(data)

        sendAnswer(data);
    }

    // función para subir video de la respuesta del usuario
    const uploadVideoAnswer = async (video_file) => {

        //Valido que exista un archivo para subir si no devuelvo la misma url
        if (!video_file && !(video_file instanceof File)) {
            openAlert('Ha ocurrido un error al enviar tu respuesta. Vuelve a intentarlo por favor', 'error');
            return null;
        }

        const aws_get_upload_url_request = await getUrlUpload(import.meta.env.VITE_AWS_ASSESSMENTS_ENDPOINT,
            "get_url_upload_answer_video_candidate",
            {
                "id_pregunta": question.id,
                "id_assessment": assessmentId,
                "id_usuario_candidato": userData.id,
                "tamano_archivo": video_file.size
            },
            token
        );

        if (!aws_get_upload_url_request) {
            openAlert('Lo sentimos, ha ocurrido un error al enviar tu respuesta.', 'error');
            return;
        }

        if (aws_get_upload_url_request.success) {
            const { url_subida, url_lectura } = aws_get_upload_url_request.data

            // console.log(url_lectura);
            if (!(url_subida && url_lectura)) return null;

            const upload_video = await putUpload(url_subida, 'video/webm', video_file);
            if (upload_video) {
                return url_lectura
            }
            else {
                openAlert('Ha ocurrido un error al enviar tu respuesta. Vuelve a intentarlo por favor', 'error');
                return null;
            }
        }

        else {
            openAlert(aws_get_upload_url_request.error?.error, 'error');
            return null;
        }
    }

    // función para crear la respuesta en la base de datos
    const sendAnswer = async (data) => {

        const send_answer_request = await updateAnswerAWS(import.meta.env.VITE_AWS_ASSESSMENTS_ENDPOINT,
            "add_answer_candidate",
            data,
            token
        );

        if (!send_answer_request) {
            openAlert(
                "Lo sentimos, ha ocurrido un error durante el envío de la respuesta",
                'error'
            );
            return;
        }


        if (send_answer_request.success) {
            openAlert(send_answer_request.message, 'success');
            setQuestionFinished(true);
        }
        else {
            openAlert(`${send_answer_request.message}: ${send_answer_request.error?.error}`, 'error')
        }
    }

    // Función para cambiar de pregunta
    const continueQuestion = () => {
        setRecordedChunks(false);
        setQuestionFinished(false);
        onContinue();
    }

    const onCameraReady = () => {
        setIsPreparing(false);
    }

    useEffect(() => {
        if (!question) return;

        getQuestionData(question.id);
        // console.log(question)

    }, [question]);

    if (getIsLoading || !questionData || !question) {
        return (
            <Grid container spacing={3} sx={{ textAlign: 'center', p: 3 }}>
                <Loader />
                <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
            </Grid>
        )
    }

    return (

        <Grid container spacing={3} sx={{ textAlign: 'center', p: 1 }}>

            <Grid item container spacing={1} md={4} xs={12} justifyContent={'center'}>
                <Grid item md={12} sx={{ height: isAvatarQuestion? '55vh' : 0  }}>
                    <Avatar questionData={questionData} setIsAvatarQuestion={setIsAvatarQuestion}/>
                </Grid>

                <Grid item md={12} >
                    <Typography variant="body1" color='text.secondary'>
                        {questionData.pregunta}
                    </Typography>
                </Grid>

            </Grid>

            <Grid item container spacing={1} md={8} xs={12}>

                <Grid item md={12} sx={{ height: '55vh' }}>
                    <Camera ref={cameraRef} onCameraReady={onCameraReady} />
                </Grid>

                <Grid item md={12} >
                    <Stack spacing={1} direction='row' justifyContent='center' >
                        {!questionFinished &&
                            <LoadingButton
                                disabled={isPreparing}
                                loading={isPreparing}
                                variant="contained"
                                size='medium'
                                startIcon={<VideoCameraOutlined />}
                                onClick={recording ? stopRecording : startRecording}
                            >
                                {   isPreparing ?
                                        'Preparando cámara'
                                        :
                                        recording ?
                                            <Timer
                                                seconds={questionData?.duracion_maxima_de_respuesta || 30}
                                                onTimeFinalized={stopRecording}
                                            />
                                            :
                                            recordedChunks ? 'Repetir respuesta' : 'Grabar respuesta'
                                }
                            </LoadingButton>
                        }

                        {recordedChunks && !recording &&
                            <LoadingButton
                                variant="outlined"
                                size='medium'
                                endIcon={<ArrowRightOutlined />} //<CaretRightOutlined />
                                onClick={questionFinished ? continueQuestion : processAnswer}
                                disabled={isLoading}
                                loading={isLoading}
                                loadingPosition="end"
                            >
                                {questionFinished ? 'Continuar' : 'Enviar respuesta'}
                            </LoadingButton>
                        }
                    </Stack>
                </Grid>

            </Grid>

        </Grid>

    )
}

export default QuestionView;