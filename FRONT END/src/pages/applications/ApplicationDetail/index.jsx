import { useEffect, useContext, useState } from 'react';
import PropTypes from 'prop-types';
import { Link, useParams } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../../hooks';

// material-ui
import { Alert, Grid, Typography } from '@mui/material';

// project import
import MainCard from '../../../components/MainCard';
import Loader from '../../../components/Loader';
import ApplicationStatus from './ApplicationStatus';
import StatusGraph from '../ApplicationCard/StatusGraph';

// Contexts
import { AuthContext } from '../../../context/Authentication/Auth';
import { ContextUI } from '../../../context/ContextUI';

// ==============================|| JOBS PAGE ||============================== //

const ApplicationsDetail = () => {

    let { job_application_id } = useParams();
    const { token, userData } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);
    const { data, isLoading, hasError, postAWS } = useFetch();

    const [applicationData, setApplicationData] = useState(null);
    const [message, setMessage] = useState('No se ha podido acceder a la información');

    // Función para obtener los datos de postulación a este cargo
    const getJobApplication = async () => {

        const data = await postAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_job_application",
            {
                "id_usuario_candidato": userData.id,
                "id_cargo": job_application_id
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
            // console.log(data.data)
            setApplicationData(data.data);
        }
        else {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            setApplicationData({ error: "Lo sentimos, no se ha podido acceder a los datos de la aplicación al cargo" })
        }
    }


    useEffect(() => {
        getJobApplication();
    }, []);


    if (isLoading || !applicationData) return (
        <MainCard sx={{ width: '100%' }}>
            <Loader />
            <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando datos de la aplicación...</Typography>
        </MainCard>
    );

    return (
        <Grid container spacing={3}>

            <Grid item xs={12} md={8} container>

                { !applicationData.error ?
                    <ApplicationStatus applicationData={applicationData}/>
                    :
                    <Alert severity="info">{applicationData.error || 'No se ha podido acceder a la información'}</Alert>
                }

            </Grid>

            <Grid item xs={12} md={4}>
                <MainCard title='Porcentaje de avance' sx={{ width: '100%' }}>
                    <br />
                    <StatusGraph status={applicationData.estado_postulacion} size='8rem' />
                </MainCard>
            </Grid>

        </Grid>

    )
}

export default ApplicationsDetail;