import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

// custom hooks
import { useFetch } from '../../hooks';

// material-ui
import { Grid, Stack, Typography } from '@mui/material';

// project import
import AuthRegister from './auth-forms/AuthRegister';
import AuthWrapper from './AuthWrapper';

// ================================|| REGISTER ||================================ //

const Register = () => {

    const [countries, setCountries] = useState([]);
    const [genders, setGenders] = useState([]);
    const [studyLevels, setStudyLevels] = useState([]);
    const [yearsExperience, setYearsExperience] = useState([]);

    const { postAWS } = useFetch();

    useEffect(() => {
        getCountries();
        getGenders();
        getStudyLevels();
        getYearsExperience();
    }, []);

    const getCountries = async() => {
        const aws_request = await postAWS(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "pais"
            },
            null
        );

        // console.log(aws_request)
        if ( aws_request.success ){
            setCountries(aws_request.data?.parametros);
        }
    }

    const getGenders = async() => {
        const aws_request = await postAWS(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "genero"
            },
            null
        );

        // console.log(aws_request)
        if ( aws_request.success ){
            setGenders(aws_request.data?.parametros);
        }
    }

    const getStudyLevels = async() => {
        const aws_request = await postAWS(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "nivel_de_estudios"
            },
            null
        );

        // console.log(aws_request)
        if ( aws_request.success ){
            setStudyLevels(aws_request.data?.parametros);
        }
    }

    const getYearsExperience = async() => {
        const aws_request = await postAWS(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "anos_de_experiencia"
            },
            null
        );

        // console.log(aws_request)
        if ( aws_request.success ){
            setYearsExperience(aws_request.data?.parametros);
        }
    }

    return (
        <AuthWrapper>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                    <Stack direction="row" justifyContent="space-between" alignItems="baseline" sx={{ mb: { xs: -0.5, sm: 0.5 } }}>
                        <Typography variant="h3">Registro</Typography>
                        <Typography component={Link} to="/autenticacion" variant="body1" sx={{ textDecoration: 'none' }} color="primary">
                            Ya tienes una cuenta?
                        </Typography>
                    </Stack>
                    <Typography variant="h5" color='secondary'>Padres y madres</Typography>
                </Grid>

                <Grid item xs={12}>
                    <AuthRegister countries={ countries } genders={ genders } educationalLevelList={ studyLevels } experienceList={ yearsExperience }/>
                </Grid>
            </Grid>
        </AuthWrapper>
    )
};

export default Register;
