import { useEffect, useContext, useState } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../hooks';

// material-ui
import { Alert, Grid, Typography } from '@mui/material';

// project import
import MainCard from '../../components/MainCard';
import Loader from '../../components/Loader';
import ApplicationsList from './ApplicationsList';
import ApplicationsHelp from './ApplicationsHelp';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';

const ApplicationsPage = () => {

    const { token, userData } = useContext(AuthContext);
    const { data, isLoading, hasError, postAWS } = useFetch();
    const { openAlert } = useContext(ContextUI);

    const [jobsList, setJobsList] = useState([]);
    // const [searchString, setSearchString] = useState('');
    const [message, setMessage] = useState('No se han encontrado registros');
    const [page, setPage] = useState(1);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [totalElements, setTotalElements] = useState(0)

    const changePage = (event, newPage) => {
        // console.log(newPage, event)
        setPage(newPage + 1);
        getApplications(newPage + 1);
    };

    const changeRowsPerPage = (event) => {
        const new_row_per_page = parseInt(event.target.value, 10)
        setRowsPerPage(new_row_per_page);
        setPage(1);
        getApplications(1, new_row_per_page);
    };


    // Función para obtener la lista de postulaciones del usuario
    const getApplications = async (page_numer = page, rows_per_page_numer=rowsPerPage) => {

        const data = await postAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_all_job_applications_candidate",
            {
                "id_usuario_candidato": userData.id,
                "cantidad_por_pagina": rows_per_page_numer,
                "pagina": page_numer
            },
            token
        );

        if (!data) {
            openAlert(
                "Lo sentimos, ha ocurrido un error al intentar obtener la lista de apliaciones",
                'error'
            );
            return;
        }

        if (!data.success) {
            openAlert(`${data.message}: ${data.error?.error}`, 'error')
            return;
        }

        // después de validar la data seteo los datos para mostrar en el formulario
        const data_applications = data.data.postulaciones;
        if(data_applications) setJobsList(data_applications);
        
        // console.log(data_applications)

    }


    useEffect(() => {
        getApplications();
    }, [])

    return (
        <Grid container spacing={3}>

            <Grid item xs={12} md={8} container>
                <MainCard sx={{ width: '100%' }}>
                    {isLoading ?
                        <>
                            <Loader />
                            <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
                        </>
                        
                        :

                        jobsList.length > 0 ?
                            <ApplicationsList
                                rows={jobsList}
                                controllerPage={page}
                                controllerRowsPerPage={rowsPerPage}
                                changePage={changePage}
                                changeRowsPerPage={changeRowsPerPage}
                                totalElements={totalElements}
                            />
                            :
                            <Alert severity="info">{message}</Alert>
                    }
                </MainCard>
            </Grid>

            <Grid item xs={12} md={4}>
                <ApplicationsHelp />
            </Grid>

        </Grid>

    )
}

export default ApplicationsPage;