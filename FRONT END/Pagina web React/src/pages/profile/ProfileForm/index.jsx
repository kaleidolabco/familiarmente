import { useContext, useEffect, useState } from 'react';
import { Link as RouterLink, useNavigate } from 'react-router-dom';

// material-ui
import {
    Avatar,
    Box,
    Breadcrumbs,
    Button,
    Divider,
    FormControl,
    FormHelperText,
    Grid,
    Link,
    IconButton,
    InputAdornment,
    InputLabel,
    MenuItem,
    OutlinedInput,
    Select,
    Stack,
    TextField,
    Typography
} from '@mui/material';
import { LoadingButton } from '@mui/lab';

import moment from 'moment';
import { AdapterMoment } from '@mui/x-date-pickers/AdapterMoment'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

// custom hooks
import { useFetch, useUploadFetch } from '../../../hooks/';

// third party
import * as Yup from 'yup';
import { Formik } from 'formik';

// project import
import AnimateButton from '../../../components/@extended/AnimateButton';
import FileInput from '../../../components/FileInput';
import { strengthColor, strengthIndicator } from '../../../utils/password-strength';

// assets
import {
    EyeOutlined,
    EyeInvisibleOutlined,
    CameraOutlined,
    FilePdfOutlined,
    PaperClipOutlined
} from '@ant-design/icons';

// Contexts
import { ContextUI } from '../../../context/ContextUI';
import { AuthContext } from '../../../context/Authentication/Auth';

import axios from 'axios';

import { generateNocacheURL } from '../../../utils/generate-no-cache-url';

// ============================|| REGISTER ||============================ //

const ProfileForm = ({ countries = [], genders = [], educationalLevelList = [], experienceList = [], userFormData = {} }) => {

    const {
        apellidos,
        clave,
        correo,
        descripcion_perfil_usuario,
        fecha_de_nacimiento,
        fecha_de_registro,
        foto_de_perfil,
        hoja_de_vida,
        id,
        id_parametro_anos_de_experiencia,
        id_parametro_genero,
        id_parametro_nivel_de_estudios,
        id_parametro_pais,
        nombres,
        telefono,
        titulo_profesional,
    } = userFormData;

    const navigate = useNavigate();
    const { openAlert } = useContext(ContextUI);
    const { token, userData } = useContext(AuthContext);

    const { data: dataUpdate, isLoading: isLoadingUpdate, hasError: hasErrorUpdate, postAWS: postUpdate } = useFetch();
    const { isLoading: isLoadingGetUrlUpload, postAWS: getUrlUpload } = useFetch();
    const { isLoading: isLoadingUpload, hasError: hasErrorUpload, postUpload: putUpload } = useUploadFetch();

    // Variable para gestionar el estado de carga y deshabilitar el botón de submit
    const isLoading = isLoadingUpload || isLoadingGetUrlUpload || isLoadingUpdate;

    const [level, setLevel] = useState();
    const [showPassword, setShowPassword] = useState(false);

    const BirthDay = moment(fecha_de_nacimiento); // Obtener la fecha actual como un objeto Moment
    const formattedDate = BirthDay.format('YYYY-MM-DD'); // Formatear la fecha como una cadena en formato YYYY-MM-DD

    const [birthday, setBirthday] = useState(moment(formattedDate));
    const [profilePhoto, setProfilePhoto] = useState(foto_de_perfil);
    const [profilePhotoUrl, setProfilePhotoUrl] = useState(generateNocacheURL(foto_de_perfil));

    const [curriculum, setCurriculum] = useState(hoja_de_vida);
    const [curriculumURL, setCurriculumURL] = useState(generateNocacheURL(hoja_de_vida));

    const handleChangeBirthday = (value) => {
        // console.log(value.format("YYYY-MM-DD"));
        setBirthday(value);
    }

    const handleChangeProfilePhoto = (event) => {
        const file = event.target.value;
        setProfilePhoto(file);
        setProfilePhotoUrl(file ? URL.createObjectURL(file) : null);
        // profilePhoto ? URL.createObjectURL(profilePhoto) : null
    }

    const handleChangeCurriculum = (event) => {
        const file = event.target.value;
        setCurriculum(file);
        setCurriculumURL(file ? URL.createObjectURL(file) : null);
    }

    const handleClickShowPassword = () => {
        setShowPassword(!showPassword);
    };

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    const changePassword = (value) => {
        const temp = strengthIndicator(value);
        setLevel(strengthColor(temp));
    };

    useEffect(() => {
        changePassword('');
    }, []);

    const onChange = (values) => {
        console.log(values)
    }

    const onSubmit = async (values, { setErrors, setStatus, setSubmitting }) => {
        try {
            setStatus({ success: false });
            setSubmitting(false);
        } catch (err) {
            console.error(err);
            setStatus({ success: false });
            setErrors({ submit: err.message });
            setSubmitting(false);
        }

        // Carga de la foto de perfil
        let urlProfileImage = null;
        if (profilePhotoUrl) {
            urlProfileImage = await uploadProfilePhoto();
            if (!urlProfileImage) return;
        }

        // Carga de la hoja de vida
        let urlCurriculum = null;
        if (curriculumURL) {
            urlCurriculum = await uploadCurriculum();
            if (!urlCurriculum) return;
        }


        const aws_request = await postUpdate(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "update_user_candidate",
            {
                "id_candidato": userData.id,
                "nombres_candidato": values.firstname,
                "apellidos_candidato": values.lastname,
                "clave_candidato": values.password,
                "telefono_candidato": values.telephone,
                "id_parametro_pais_candidato": values.country,
                "fecha_nacimiento_candidato": birthday.format("YYYY-MM-DD"),
                "id_parametro_genero_candidato": values.gender,
                "id_parametro_nivel_de_estudios_candidato": values.study,
                "id_parametro_anos_de_experiencia_candidato": values.experience,
                "titulo_profesional_candidato": values.title,
                "foto_de_perfil_candidato": urlProfileImage,
                "descripcion_perfil_usuario_candidato": values.description,
                "hoja_de_vida_candidato": urlCurriculum
            },
            token
        );

        // console.log(aws_request)
        if (aws_request.success) {
            openAlert(aws_request.message, 'success');
        }
        else {
            openAlert(aws_request.error?.error, 'error')
        }
    }

    // función para subir la foto de perfil
    const uploadProfilePhoto = async () => {

        //Valido que exista un archivo para subir si no devuelvo la misma url
        if (!(profilePhoto instanceof File)) {
            return profilePhotoUrl;
        }

        const aws_get_upload_url_request = await getUrlUpload(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_url_upload_profile_photo_candidate",
            {
                "id_candidato": userData.id
            },
            token
        );

        if (aws_get_upload_url_request.success) {
            const { url_subida, url_lectura } = aws_get_upload_url_request.data

            // console.log(url_lectura);
            if (!(url_subida && url_lectura)) return null;

            const upload_photo = await putUpload(url_subida, 'image/jpeg', profilePhoto);
            if (upload_photo) {
                setProfilePhotoUrl(generateNocacheURL(url_lectura));
                return url_lectura
            }
            else {
                openAlert('Error en la subida de la imágen de perfil. recuerda que sólo se admiten imágenes en formato jpeg.', 'error');
                return null;
            }
        }

        else {
            openAlert(aws_get_upload_url_request.error?.error, 'error');
            return null;
        }
    }

    // función para subir el archivo pdf de la hoja de vida
    const uploadCurriculum = async () => {

        //Valido que exista un archivo para subir si no devuelvo la misma url
        if (!(curriculum instanceof File)) {
            return curriculumURL;
        }

        const aws_get_upload_url_request = await getUrlUpload(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "get_url_upload_curriculum_candidate",
            {
                "id_candidato": userData.id
            },
            token
        );

        if (aws_get_upload_url_request.success) {
            const { url_subida, url_lectura } = aws_get_upload_url_request.data

            // console.log(url_lectura);
            if (!(url_subida && url_lectura)) return null;

            const upload_curriculum = await putUpload(url_subida, 'application/pdf', curriculum);
            if (upload_curriculum) {
                setCurriculumURL(generateNocacheURL(url_lectura));
                return url_lectura
            }
            else {
                openAlert('Error en la subida de la hoja de vida. recuerda que sólo se admiten archivos en formato PDF.', 'error');
                return null;
            }
        }

        else {
            openAlert(aws_get_upload_url_request.error?.error, 'error');
            return null;
        }
    }

    return (
        <>
            <Formik
                initialValues={{
                    firstname: nombres || '',
                    lastname: apellidos || '',
                    email: correo || '',
                    telephone: telefono || '',
                    country: id_parametro_pais || '',
                    gender: id_parametro_genero || '',
                    study: id_parametro_nivel_de_estudios || '',
                    experience: id_parametro_anos_de_experiencia || '',
                    title: titulo_profesional || '',
                    password: clave || '',
                    description: descripcion_perfil_usuario || '',
                    submit: null
                }}
                validationSchema={Yup.object().shape({
                    firstname: Yup.string().max(255).required('El nombre es requerido'),
                    lastname: Yup.string().max(255).required('El apellido es requerido'),
                    email: Yup.string().email('Debes ingresar un correo electrónico válido').max(255).required('El correo elecrónico es requerido'),
                    telephone: Yup.string().max(20, 'No debe contener más de 20 caracteres').required('El teléfono es requerido'),
                    country: Yup.string().required('Debes seleccionar un país'),
                    gender: Yup.string().required('Debes seleccionar un género'),
                    study: Yup.string().required('Debes seleccionar un nivel de estudios'),
                    experience: Yup.string().required('Debes seleccionar tu experiencia'),
                    title: Yup.string('Debes ingresar un texto válido'),
                    password: Yup.string().max(255).required('La contraseña es requerida'),
                    description: Yup.string().max(3000, 'No debe contener más de 3000 caracteres')
                })}
                onSubmit={onSubmit}
            >
                {({ errors, handleBlur, handleChange, handleSubmit, isSubmitting, touched, values }) => (
                    <form noValidate onSubmit={handleSubmit}>
                        <Grid container spacing={3}>

                            <Grid item xs={12}>

                                <Stack direction={'column'} spacing={2} alignItems="center">
                                    <Avatar
                                        cache="false"
                                        alt="Usuario"
                                        src={profilePhotoUrl}
                                        sx={{ width: 150, height: 150 }}
                                    />
                                    <FileInput
                                        label="Cambiar foto"
                                        accept="image/jpeg" //"image/png, image/jpeg"  //image/*
                                        value={profilePhoto}
                                        onChange={handleChangeProfilePhoto}
                                        icon={<CameraOutlined />} />

                                    <Breadcrumbs aria-label="breadcrumb">
                                        <Typography variant="h5" textAlign={'center'}
                                            sx={{ overflow: "hidden", textOverflow: "ellipsis", width: '100%', my: 2 }}>
                                            {values.email}
                                        </Typography>
                                    </Breadcrumbs>

                                </Stack>

                            </Grid>


                            {/* <Grid item xs={12}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="email-signup">Correo Electrónico</InputLabel>
                                    <OutlinedInput
                                        disabled
                                        fullWidth
                                        autoComplete='off'
                                        error={Boolean(touched.email && errors.email)}
                                        id="email-signup"
                                        type="email"
                                        value={values.email}
                                        name="email"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        placeholder="demo@company.com"
                                        inputProps={{}}
                                    />
                                    {touched.email && errors.email && (
                                        <FormHelperText error id="helper-text-email-signup">
                                            {errors.email}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid> */}

                            <Grid item xs={12}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="password-signup">Contraseña</InputLabel>
                                    <OutlinedInput
                                        fullWidth
                                        autoComplete="new-password"
                                        error={Boolean(touched.password && errors.password)}
                                        id="password-signup"
                                        type={showPassword ? 'text' : 'password'}
                                        value={values.password}
                                        name="password"
                                        onBlur={handleBlur}
                                        onChange={(e) => {
                                            handleChange(e);
                                            changePassword(e.target.value);
                                        }}
                                        endAdornment={
                                            <InputAdornment position="end">
                                                <IconButton
                                                    aria-label="toggle password visibility"
                                                    onClick={handleClickShowPassword}
                                                    onMouseDown={handleMouseDownPassword}
                                                    edge="end"
                                                    size="large"
                                                >
                                                    {showPassword ? <EyeOutlined /> : <EyeInvisibleOutlined />}
                                                </IconButton>
                                            </InputAdornment>
                                        }
                                        placeholder="******"
                                        inputProps={{}}
                                    />
                                    {touched.password && errors.password && (
                                        <FormHelperText error id="helper-text-password-signup">
                                            {errors.password}
                                        </FormHelperText>
                                    )}
                                </Stack>
                                <FormControl fullWidth sx={{ mt: 2 }}>
                                    <Grid container spacing={2} alignItems="center">
                                        <Grid item>
                                            <Box sx={{ bgcolor: level?.color, width: 85, height: 8, borderRadius: '7px' }} />
                                        </Grid>
                                        <Grid item>
                                            <Typography variant="subtitle1" fontSize="0.75rem">
                                                {level?.label}
                                            </Typography>
                                        </Grid>
                                    </Grid>
                                </FormControl>
                            </Grid>


                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="firstname-signup">Nombres</InputLabel>
                                    <OutlinedInput
                                        id="firstname-login"
                                        autoComplete='off'
                                        type="firstname"
                                        value={values.firstname}
                                        name="firstname"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        placeholder="John"
                                        fullWidth
                                        error={Boolean(touched.firstname && errors.firstname)}
                                    />
                                    {touched.firstname && errors.firstname && (
                                        <FormHelperText error id="helper-text-firstname-signup">
                                            {errors.firstname}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="lastname-signup">Apellidos</InputLabel>
                                    <OutlinedInput
                                        fullWidth
                                        autoComplete='off'
                                        error={Boolean(touched.lastname && errors.lastname)}
                                        id="lastname-signup"
                                        type="lastname"
                                        value={values.lastname}
                                        name="lastname"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        placeholder="Doe"
                                        inputProps={{}}
                                    />
                                    {touched.lastname && errors.lastname && (
                                        <FormHelperText error id="helper-text-lastname-signup">
                                            {errors.lastname}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            {/* <Grid item xs={12} md={12}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="title-signup">Título profesional</InputLabel>
                                    <OutlinedInput
                                        fullWidth
                                        error={Boolean(touched.title && errors.title)}
                                        id="title-signup"
                                        value={values.title}
                                        name="title"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        placeholder="Ingeniero"
                                        inputProps={{}}
                                    />
                                    {touched.title && errors.title && (
                                        <FormHelperText error id="helper-text-title-signup">
                                            {errors.title}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid> */}

                            <Grid item xs={12} md={12}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="description-form">Acerca de mí</InputLabel>

                                    <TextField
                                        fullWidth
                                        multiline
                                        maxRows={3}
                                        minRows={3}
                                        error={Boolean(touched.description && errors.description)}
                                        id="description-form"
                                        value={values.description}
                                        name="description"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        placeholder="..."
                                        inputProps={{}}
                                    // helperText='Realiza una descripción de tu perfil'
                                    />
                                    <Stack spacing={.75} sx={{ my: 1 }}>
                                        {/* <Typography variant="h5">Crea un cargo y publícalo</Typography>  */}
                                        <Breadcrumbs aria-label="breadcrumb">
                                            <Typography variant="h6">
                                                Escribe una descripción de tu perfil
                                            </Typography>
                                        </Breadcrumbs>
                                    </Stack>
                                    {touched.description && errors.description && (
                                        <FormHelperText error id="helper-text-company-signup">
                                            {errors.description}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            <Grid item xs={12} md={12} sx={{ mt: 3 }}>
                                <Divider variant="middle"> Otros datos </Divider>
                            </Grid>


                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="telephone-signup">Teléfono</InputLabel>
                                    <OutlinedInput
                                        fullWidth
                                        autoComplete='off'
                                        error={Boolean(touched.telephone && errors.telephone)}
                                        id="telephone-signup"
                                        value={values.telephone}
                                        name="telephone"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        placeholder="+57 310 000 0000"
                                        inputProps={{}}
                                    />
                                    {touched.telephone && errors.telephone && (
                                        <FormHelperText error id="helper-text-telephone-signup">
                                            {errors.telephone}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            {/* <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="study-signup">Nivel de estudios</InputLabel>
                                    <Select
                                        fullWidth
                                        id="study-signup"
                                        name="study"
                                        value={values.study}
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        error={Boolean(touched.study && errors.study)}
                                    >
                                        {educationalLevelList.map((option) => (
                                            <MenuItem key={option.id} value={option.id}>
                                                {option.nombre}
                                            </MenuItem>
                                        ))}
                                    </Select>

                                    {touched.study && errors.study && (
                                        <FormHelperText error id="helper-text-study-signup">
                                            {errors.study}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid> */}

                            {/* <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="experience-signup">Experiencia laboral</InputLabel>
                                    <Select
                                        fullWidth
                                        id="experience-signup"
                                        name="experience"
                                        value={values.experience}
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        error={Boolean(touched.experience && errors.experience)}
                                    >
                                        {experienceList.map((option) => (
                                            <MenuItem key={option.id} value={option.id}>
                                                {option.nombre}
                                            </MenuItem>
                                        ))}
                                    </Select>

                                    {touched.experience && errors.experience && (
                                        <FormHelperText error id="helper-text-experience-signup">
                                            {errors.experience}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid> */}

                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="country-signup">País*</InputLabel>
                                    <Select
                                        fullWidth
                                        id="country-signup"
                                        name="country"
                                        value={values.country}
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        error={Boolean(touched.country && errors.country)}
                                    >
                                        {countries.map((option) => (
                                            <MenuItem key={option.id} value={option.id}>
                                                {option.nombre}
                                            </MenuItem>
                                        ))}
                                    </Select>

                                    {touched.country && errors.country && (
                                        <FormHelperText error id="helper-text-country-signup">
                                            {errors.country}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="gender-signup">Género</InputLabel>
                                    <Select
                                        fullWidth
                                        id="gender-signup"
                                        name="gender"
                                        value={values.gender}
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        error={Boolean(touched.gender && errors.gender)}
                                    // helperText="Selecciona el género que mejor te represente"
                                    >
                                        {genders.map((option) => (
                                            <MenuItem key={option.id} value={option.id}>
                                                {option.nombre}
                                            </MenuItem>
                                        ))}
                                    </Select>

                                    {touched.gender && errors.gender && (
                                        <FormHelperText error id="helper-text-gender-signup">
                                            {errors.gender}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="birthday-signup">Fecha de nacimiento</InputLabel>

                                    <LocalizationProvider dateAdapter={AdapterMoment}
                                        adapterLocale='es'
                                    >
                                        <DatePicker
                                            fullWidth
                                            id="birthday-signup"
                                            type="birthday"
                                            value={birthday}
                                            name="birthday"
                                            onChange={handleChangeBirthday}
                                        />
                                    </LocalizationProvider>

                                </Stack>
                            </Grid>

                            {/* Hoja de vida */}
                            <Grid item xs={12} sx={{ my: 2 }}>

                                <Stack direction={'column'} spacing={1} alignItems="center">
                                    {curriculum && <FilePdfOutlined style={{ fontSize: '5rem' }} />}

                                    {curriculum ?
                                        <Link
                                            variant="body1"
                                            textAlign={'center'}
                                            onClick={() => window.open(curriculumURL, "_blank")}
                                            sx={{ overflow: "hidden", textOverflow: "ellipsis", width: '100%', cursor: 'pointer' }}
                                        >
                                            {
                                                curriculum instanceof File ?
                                                    curriculum.name : 'Hoja de vida'
                                            }
                                        </Link>
                                        :
                                        <Typography
                                            variant="body1"
                                            color='text.secondary'
                                            textAlign={'center'}
                                            sx={{ overflow: "hidden", textOverflow: "ellipsis", width: '100%' }}
                                        >
                                            Aún no has cargado una hoja de vida
                                        </Typography>
                                    }


                                    <FileInput
                                        label="Subir hoja de vida"
                                        accept="application/pdf"
                                        value={curriculum}
                                        onChange={handleChangeCurriculum}
                                        icon={<PaperClipOutlined />} />

                                </Stack>

                            </Grid>

                            {errors.submit && (
                                <Grid item xs={12}>
                                    <FormHelperText error>{errors.submit}</FormHelperText>
                                </Grid>
                            )}
                            <Grid item xs={12}>
                                <AnimateButton>
                                    <LoadingButton
                                        disableElevation
                                        loadingPosition="start"
                                        startIcon={<></>}
                                        loading={isLoading}
                                        disabled={isLoading}
                                        fullWidth
                                        size="large"
                                        type="submit"
                                        variant="contained"
                                        color="primary"
                                    >
                                        {isLoading ? "Actualizando datos" : "Guardar datos"}
                                    </LoadingButton>
                                </AnimateButton>
                            </Grid>
                            {/* <Grid item xs={12}>
                                <Divider>
                                    <Typography variant="caption">Regístrate con</Typography>
                                </Divider>
                            </Grid>
                            <Grid item xs={12}>
                                <FirebaseSocial />
                            </Grid> */}
                        </Grid>
                    </form>
                )}
            </Formik>
        </>
    );
};

export default ProfileForm;
