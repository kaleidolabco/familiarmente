import { useContext, useEffect, useState } from 'react';
import { Link as RouterLink, useNavigate } from 'react-router-dom';

// material-ui
import {
    Box,
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
import { useFetch } from '../../../hooks/';

// third party
import * as Yup from 'yup';
import { Formik } from 'formik';

// project import
import FirebaseSocial from './FirebaseSocial';
import AnimateButton from '../../../components/@extended/AnimateButton';
import { strengthColor, strengthIndicator } from '../../../utils/password-strength';

// assets
import { EyeOutlined, EyeInvisibleOutlined } from '@ant-design/icons';

// Contexts
import { ContextUI } from '../../../context/ContextUI';

// ============================|| REGISTER ||============================ //

const AuthRegister = ({ countries, genders, educationalLevelList, experienceList }) => {
    const navigate = useNavigate();
    const { openAlert } = useContext(ContextUI);

    const { data, isLoading, hasError, postAWS } = useFetch();

    const [level, setLevel] = useState();
    const [showPassword, setShowPassword] = useState(false);

    const today = moment(); // Obtener la fecha actual como un objeto Moment
    const formattedDate = today.format('YYYY-MM-DD'); // Formatear la fecha como una cadena en formato YYYY-MM-DD

    const [birthday, setBirthday] = useState(moment(formattedDate))

    const handleChangeBirthday = (value) => {
        // console.log(value.format("YYYY-MM-DD"));
        setBirthday(value);
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

        console.log(values)

        const aws_request = await postAWS(import.meta.env.VITE_AWS_USERS_ENDPOINT,
            "add_candidate",
            {
                "nombres_candidato": values.firstname,
                "apellidos_candidato": values.lastname,
                "correo_candidato": values.email,
                "clave_candidato": values.password,
                "telefono_candidato": values.telephone,
                "id_parametro_pais_candidato": values.country,
                "fecha_nacimiento_candidato": birthday.format("YYYY-MM-DD"),
                "id_parametro_genero_candidato": values.gender,
                "id_parametro_nivel_de_estudios_candidato": values.study,
                "id_parametro_anos_de_experiencia_candidato": values.experience,
                "titulo_profesional_candidato": values.title,
            },
            null
        );

        // console.log(aws_request)
        if (aws_request.success) {
            openAlert(aws_request.message, 'success');
            navigate('/autenticacion');
        }
        else {
            openAlert(aws_request.error?.error, 'error')
        }
    }

    return (
        <>
            <Formik
                initialValues={{
                    firstname: '',
                    lastname: '',
                    email: '',
                    telephone: '',
                    country: '',
                    gender: '',
                    study:'42cdb121-0488-4e64-a857-1253566f075b',
                    experience:'b1160229-a65c-4b1b-9b97-9fa067483f32',
                    title: 'Padre/Madre',
                    password: '',
                    submit: null
                }}
                validationSchema={Yup.object().shape({
                    firstname: Yup.string().max(255).required('El nombre es requerido'),
                    lastname: Yup.string().max(255).required('El apellido es requerido'),
                    email: Yup.string().email('Debes ingresar un correo electrónico válido').max(255).required('El correo elecrónico es requerido'),
                    telephone: Yup.string().max(20, 'No debe contener más de 20 caracteres').required('El teléfono es requerido'),
                    country: Yup.string().required('Debes seleccionar un país'),
                    gender: Yup.string().required('Debes seleccionar un género'),
                    // study: Yup.string().required('Debes seleccionar un nivel de estudios'),
                    // experience: Yup.string().required('Debes seleccionar tu experiencia'),
                    // title: Yup.string('Debes ingresar un texto válido'),
                    password: Yup.string().max(255).required('La contraseña es requerida')
                })}
                onSubmit={onSubmit}
            >
                {({ errors, handleBlur, handleChange, handleSubmit, isSubmitting, touched, values }) => (
                    <form noValidate onSubmit={handleSubmit}>
                        <Grid container spacing={3}>
                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="firstname-signup">Nombres*</InputLabel>
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
                                    <InputLabel htmlFor="lastname-signup">Apellidos*</InputLabel>
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

                            <Grid item xs={12}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="email-signup">Correo Electrónico*</InputLabel>
                                    <OutlinedInput
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
                            </Grid>

                            {/* <Grid item xs={12} md={6}>
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
                                    <InputLabel htmlFor="country-signup">País</InputLabel>
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

                            <Grid item xs={12}>
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
                            <Grid item xs={12}>
                                <Typography variant="body2">
                                    Al registrarte aceptas nuestros &nbsp;
                                    <Link variant="subtitle2" target="_blank" underline="hover" href="https://www.kaleidolab.scenariovr.co/politica-de-privacidad/">
                                        Términos de servicio
                                    </Link>
                                    &nbsp; y nuestra &nbsp;
                                    <Link variant="subtitle2" target="_blank" underline="hover" href="https://www.kaleidolab.scenariovr.co/politica-de-privacidad/">
                                        Política de privacidad
                                    </Link>
                                </Typography>
                            </Grid>
                            {errors.submit && (
                                <Grid item xs={12}>
                                    <FormHelperText error>{errors.submit}</FormHelperText>
                                </Grid>
                            )}
                            <Grid item xs={12}>
                                <AnimateButton>
                                    {/* <Button
                                        disableElevation
                                        disabled={isSubmitting}
                                        fullWidth
                                        size="large"
                                        type="submit"
                                        variant="contained"
                                        color="primary"
                                    >
                                        Crear cuenta
                                    </Button> */}

                                    <LoadingButton
                                        disableElevation
                                        loadingPosition="start"
                                        startIcon={<></>}
                                        loading={isLoading}
                                        fullWidth
                                        size="large"
                                        type="submit"
                                        variant="contained"
                                        color="primary"
                                    >
                                        {isLoading ? "Creando usuario" : "Crear Cuenta"}
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

export default AuthRegister;
