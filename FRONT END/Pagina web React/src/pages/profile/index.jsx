import { useContext, useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

// custom hooks
import { useFetch } from '../../hooks';

// Contexts
import { AuthContext } from '../../context/Authentication/Auth';
import { ContextUI } from '../../context/ContextUI';

// material-ui
import { Alert, Grid, Stack, Typography } from '@mui/material';

// project import
import ProfileForm from './ProfileForm';
import ProfileStatistics from './ProfileStatistics';
import MainCard from '../../components/MainCard';
import Loader from '../../components/Loader';

// ================================|| REGISTER ||================================ //

const Profile = () => {

    const { token, userData } = useContext(AuthContext);
    const { openAlert } = useContext(ContextUI);

    const [countries, setCountries] = useState([]);
    const [genders, setGenders] = useState([]);
    const [studyLevels, setStudyLevels] = useState([]);
    const [yearsExperience, setYearsExperience] = useState([]);
    const [userFormData, setUserFormData] = useState(null)

    const { postAWS: postAWSParameters } = useFetch();
    const { data: dataGetUser, isLoading: isLoadingGetUser, hasError: hasErrorGetUser, postAWS: postGetUser } = useFetch();

    useEffect(() => {
        getCountries();
        getGenders();
        getStudyLevels();
        getYearsExperience();
        getUserData();
    }, []);

    useEffect(() => {
        if (!dataGetUser) return;

        if (!dataGetUser.success) {
            openAlert(`${dataGetUser.message}: ${dataGetUser.error?.error}`, 'error')
            setUserFormData({ error: 'Lo sentimos, no se ha podido acceder a la información' })
            return;
        }

        setUserFormData(dataGetUser.data)
        console.log(dataGetUser.data);

    }, [dataGetUser]);

    const getUserData = async () => {
        const user_id = userData.id;

        const r = await postGetUser(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_user_candidate",
            {
                "id": user_id
            },
            token
        );
    }

    const getCountries = async () => {
        const aws_request = await postAWSParameters(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "pais"
            },
            null
        );

        // console.log(aws_request)
        if (aws_request.success) {
            setCountries(aws_request.data?.parametros);
        }
    }

    const getGenders = async () => {
        const aws_request = await postAWSParameters(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "genero"
            },
            null
        );

        // console.log(aws_request)
        if (aws_request.success) {
            setGenders(aws_request.data?.parametros);
        }
    }

    const getStudyLevels = async () => {
        const aws_request = await postAWSParameters(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "nivel_de_estudios"
            },
            null
        );

        // console.log(aws_request)
        if (aws_request.success) {
            setStudyLevels(aws_request.data?.parametros);
        }
    }

    const getYearsExperience = async () => {
        const aws_request = await postAWSParameters(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_by_name_parameters",
            {
                "nombre_tipo_parametro": "anos_de_experiencia"
            },
            null
        );

        // console.log(aws_request)
        if (aws_request.success) {
            setYearsExperience(aws_request.data?.parametros);
        }
    }

    if (isLoadingGetUser || !userFormData) {
        return (
            <Grid container spacing={3}>
                <Loader />
                <Grid item xs={12} md={12}>
                    <MainCard title='Datos del perfil' >
                        <Typography sx={{ width: '100%', textAlign: 'left', fontWeight: 'medium' }}>Cargando...</Typography>
                    </MainCard>
                </Grid>
            </Grid>
        )
    }

    return (
        <Grid container spacing={3}>
            {   userFormData && !userFormData.error && 
                <Grid item xs={12} md={4}>
                    <MainCard title="Estadísticas">
                        <ProfileStatistics userFormData = {userFormData}/>
                    </MainCard>
                </Grid>
            }
            <Grid item xs={12} md={userFormData.error ? 12 : 8}>
                <MainCard title="Datos del perfil">
                    {
                        userFormData.error ?
                            <Alert severity="info">{userFormData.error}</Alert>
                            :
                            <ProfileForm
                                countries={countries}
                                genders={genders}
                                educationalLevelList={studyLevels}
                                experienceList={yearsExperience}
                                userFormData = {userFormData}
                            />
                    }
                </MainCard>
            </Grid>
        </Grid>
    )
};

export default Profile;
