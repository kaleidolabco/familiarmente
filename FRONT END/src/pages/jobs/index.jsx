import { useEffect, useContext, useState } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

// Custom hooks
import { useFetch } from '../../hooks';

// material-ui
import { Alert, Grid, Typography } from '@mui/material';

// project import
import MainCard from '../../components/MainCard';
import JobsList from './JobsList';
import Search from '../../layout/MainLayout/Header/HeaderContent/Search';
import Loader from '../../components/Loader';
import JobsFilters from './JobsFilters';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';

// ==============================|| JOBS PAGE ||============================== //

const SampleJobs = [
    {
        "nombre_cargo": "Desarrollador de software",
        "empresa": "Tecnosoft S.A.",
        "descripcion": "¡Únete a nuestro equipo como Desarrollador de Software en Tecnosoft S.A.! Estamos buscando a un profesional apasionado por la programación y el desarrollo de soluciones tecnológicas innovadoras. Si te encanta enfrentar desafíos técnicos y trabajar en un entorno dinámico, esta es tu oportunidad de marcar la diferencia en el mundo digital. Como Desarrollador de Software, serás parte de un equipo talentoso encargado de diseñar, desarrollar e implementar aplicaciones web de alta calidad para satisfacer las necesidades de nuestros clientes. Tendrás la oportunidad de trabajar en proyectos emocionantes y de gran impacto, utilizando tecnologías de vanguardia para construir soluciones escalables y eficientes.",
        "fecha_publicacion": "2023-07-26",
        "vacantes": 3,
        "ubicacion": "Cali - Valle del Cauca"
    },
    {
        "nombre_cargo": "Ejecutivo de ventas",
        "empresa": "Comercializadora ABC",
        "descripcion": "Buscamos un ejecutivo de ventas dinámico y proactivo para promocionar nuestros productos a clientes potenciales. Deberás establecer relaciones comerciales, realizar seguimiento de clientes y alcanzar metas de ventas.",
        "fecha_publicacion": "2023-07-26",
        "vacantes": 2,
        "ubicacion": "Cali - Valle del Cauca"
    },
    {
        "nombre_cargo": "Diseñador gráfico",
        "empresa": "Creatividad Total S.A.S.",
        "descripcion": "Estamos en la búsqueda de un talentoso diseñador gráfico para crear piezas visuales impactantes. Deberás trabajar en estrecha colaboración con el equipo de marketing para desarrollar material gráfico para campañas publicitarias y redes sociales.",
        "fecha_publicacion": "2023-07-26",
        "vacantes": 1,
        "ubicacion": "Cali - Valle del Cauca"
    },
    {
        "nombre_cargo": "Asistente administrativo",
        "empresa": "Grupo Empresarial XYZ",
        "descripcion": "Se requiere un asistente administrativo con habilidades organizativas para apoyar en tareas administrativas y de gestión. Serás responsable de la atención a clientes, archivo de documentos y coordinación de agendas.",
        "fecha_publicacion": "2023-07-26",
        "vacantes": 2,
        "ubicacion": "Cali - Valle del Cauca"
    },
    {
        "nombre_cargo": "Ingeniero de sistemas",
        "empresa": "Tecnología Avanzada S.A.",
        "descripcion": "Estamos en busca de un ingeniero de sistemas para diseñar, implementar y mantener infraestructuras de tecnología. Deberás resolver problemas técnicos y asegurar la eficiencia de los sistemas informáticos de la empresa.",
        "fecha_publicacion": "2023-07-26",
        "vacantes": 3,
        "ubicacion": "Cali - Valle del Cauca"
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

            <Grid item xs={12} md={4}>
                <JobsFilters />
            </Grid>

            <Grid item xs={12} md={8} container>
                <MainCard sx={{width:'100%'}}>
                    {isLoading ?
                        <>
                            <Loader />
                            <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
                        </>
                        :

                        jobsList.length > 0 ?
                            <JobsList
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

        </Grid>

    )
}

export default JobsPage;