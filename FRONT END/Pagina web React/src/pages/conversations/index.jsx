import { useEffect, useContext, useState } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../hooks';

// material-ui
import { Alert, Grid, Typography } from '@mui/material';

// project import
import MainCard from '../../components/MainCard';
import ConversationCard from './ConversationCard';
import Loader from '../../components/Loader';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';

// ==============================|| JOBS PAGE ||============================== //

const SampleJobs = [
    {
        "nombre": "Mi hij@ tiene rabietas frecuentes o están sumamente irritables la mayor parte del tiempo",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ se queja de dolores frecuentes de estómago o de cabeza, sin ninguna causa médica conocida",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ está moviendose constantemente y no puede sentarse tranquilamente (excepto cuando está viendo videos o jugando videojuegos)",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ duerme demasiado o muy poco, tiene pesadillas frecuentes o parece que tiene sueño durante el día",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ no está interesado en jugar con otros niños o tiene dificultades para hacer amigos",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ repite acciones o revisa las cosas muchas veces por temor a que algo malo pueda suceder",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ ha perdido interés en las cosas que solía disfrutar",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ pasa cada vez más tiempo a solas y evita las actividades sociales con amigos o familiares",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    },
    {
        "nombre": "Mi hij@ hace dieta de manera excesiva o tiene miedo a aumentar de peso",
        "link": "f486f696-4569-4ed7-b439-6e8745550fd2",
    }

]

const JobsPage = () => {

    const { token, userData } = useContext(AuthContext);
    const { data, isLoading, hasError, postAWS } = useFetch();

    const [jobsList, setJobsList] = useState([]);
    const [searchString, setSearchString] = useState('');
    const [message, setMessage] = useState('No se han encontrado registros');
    const [page, setPage] = useState(1);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [totalElements, setTotalElements] = useState(0)

    const changePage = (event, newPage) => {
        // console.log(newPage, event)
        setPage(newPage + 1);
        getJobs(newPage + 1);
    };

    const changeRowsPerPage = (event) => {
        const new_row_per_page = parseInt(event.target.value, 10)
        setRowsPerPage(new_row_per_page);
        setPage(1);
        getJobs(1, new_row_per_page);
    };

    const getJobs = async (page_numer = null, rows_per_page_numer) => {

        // if (searchString.trim().length !== '') {
        //     await searchJobs(searchString, page_numer || page, rows_per_page_numer || rowsPerPage);
        //     return;
        // }

        const r = await postAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "get_all_published_jobs",
            {
                "cantidad_por_pagina": rows_per_page_numer || rowsPerPage,
                "pagina": page_numer || page
            },
            token
        );
    }

    const searchJobs = async (string_to_search, page_numer = null, rows_per_page_numer) => {
        const r = await postAWS(import.meta.env.VITE_AWS_JOBS_ENDPOINT,
            "search_by_name_published_jobs",
            {
                "nombre_buscado": string_to_search,
                "cantidad_por_pagina": rows_per_page_numer || rowsPerPage,
                "pagina": page_numer || page
            },
            token
        );
    }

    // Consulto los datos cada vez que cambia el input de búsuqeda
    // useEffect(() => {
    //     // console.log(searchString)
    //     if (searchString.trim().length !== '') {
    //         const restarted_page = 1;
    //         setPage(restarted_page);
    //         getJobs(restarted_page, rowsPerPage);
    //     }
    // }, [searchString])


    useEffect(() => {
        if (!data) return;

        if (data.success) {

            if (data.data && data.data.cargos) {

                const cargos = data.data.cargos

                if (cargos.length > 0) {
                    setJobsList(cargos);
                    setTotalElements(data.data.elementos_totales);
                }

                else {
                    setMessage(data.message);
                }

            }
        }

        else {
            if (data.message) {
                setMessage(data.message);
            }
        }
    }, [data])


    // Realizo la consulta cuando el componente se monta
    useEffect(() => {
        getJobs();
    }, [])

    return (
        <Grid container spacing={3}>

            <Grid item xs={12} md={12} container>
                {/* <MainCard sx={{ width: '100%' }}> */}
                    {isLoading ?
                        <>
                            <Loader />
                            <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
                        </>
                        :

                        SampleJobs.length > 0 ?
                            <Grid container spacing={2}>
                                {
                                    SampleJobs.map((job) =>
                                        <ConversationCard title={job.nombre} link={job.link}/>
                                    )
                                }
                            </Grid>

                            :
                            <Alert severity="info">No hay datos para mostrar</Alert>
                    }
                {/* </MainCard> */}
            </Grid>

        </Grid>

    )
}

export default JobsPage;