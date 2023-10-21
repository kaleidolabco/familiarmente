import React, { useState } from 'react'
// material-ui
import {
    Alert,
    Button,
    FormControlLabel,
    FormHelperText,
    Grid,
    InputLabel,
    InputAdornment,
    MenuItem,
    OutlinedInput,
    Select,
    Stack,
    Switch,
    Typography
} from '@mui/material';
import { LoadingButton } from '@mui/lab';

// third party
import * as Yup from 'yup';
import { Formik } from 'formik';

// project import
import MainCard from '../../components/MainCard';
import Search from '../../layout/MainLayout/Header/HeaderContent/Search';
import AnimateButton from '../../components/@extended/AnimateButton';

// assets
import { SearchOutlined } from '@ant-design/icons';

const CuntriesOptions = [
    {
        label: 'Colombia',
        value: 'CO'
    },
    {
        label: 'Ecuador',
        value: 'EC'
    }
]

const JobsFilters = () => {

    const [country, setCountry] = useState(1);
    const [isLoadingSearch, setIsLoadingSearch] = useState(false);

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

        setIsLoadingSearch(true);
        setTimeout(() => {
            setIsLoadingSearch(false);
            console.log(values)
        }, 1000);
        
    }

    return (
        <MainCard title='Filtros de búsqueda' >

            <Formik
                initialValues={{
                    searchstring: '',
                    country: 'all',
                    remotejob: false,
                    submit: null
                }}
                validationSchema={Yup.object().shape({
                    searchstring: Yup.string().max(255, 'La búsqueda no debe exceder los 255 caracteres'),
                })}
                onSubmit={onSubmit}
            >
                {({ errors, handleBlur, handleChange, handleSubmit, isSubmitting, touched, values }) => (
                    <form noValidate onSubmit={handleSubmit}>
                        <Grid container spacing={3}>

                            <Grid item xs={12} md={12}>
                                <Stack spacing={1}>
                                    {/* <Search placeHolder='Buscar por palabra clave...' setSearchString={null} /> */}
                                    <OutlinedInput
                                        size="small"
                                        id="searchstring-input"
                                        autoComplete='off'
                                        // type="firstname"
                                        value={values.searchstring}
                                        name="searchstring"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        startAdornment={
                                            <InputAdornment position="start" sx={{ mr: -0.5 }}>
                                                <SearchOutlined />
                                            </InputAdornment>
                                        }
                                        aria-describedby="searchstring-text"
                                        inputProps={{
                                            'aria-label': 'weight'
                                        }}
                                        placeholder='Buscar por palabra clave...'
                                    />
                                    {touched.searchstring && errors.searchstring && (
                                        <FormHelperText error id="helper-text-searchstring">
                                            {errors.searchstring}
                                        </FormHelperText>
                                    )}
                                </Stack>
                            </Grid>

                            <Grid item xs={12} md={12}>
                                <Stack spacing={1}>
                                    <InputLabel htmlFor="firstname-signup">Filtrar por ubicación</InputLabel>
                                    <Select
                                        fullWidth
                                        id="country-input"
                                        name="country"
                                        value={values.country}
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        // error={Boolean(touched.country && errors.country)}
                                    >
                                        <MenuItem selected={true} key={1} value={'all'}>
                                            Todos los países
                                        </MenuItem>
                                        {CuntriesOptions.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                                {option.label}
                                            </MenuItem>
                                        ))}

                                    </Select>
                                </Stack>
                            </Grid>

                            <Grid item xs={12} md={12} sx={{ display: 'flex', alignItems: 'flex-end' }}>
                                <Stack spacing={2} direction="row" justifyContent='flex-start' alignItems='center'>
                                    <FormControlLabel
                                        sx={{ m: 0 }}
                                        labelPlacement='start'
                                        control={
                                            <Switch
                                                id='remote-job'
                                                name='remotejob'
                                                checked={values.remotejob}
                                                onChange={handleChange} />
                                        }
                                        label="Trabajo remoto"
                                    />
                                </Stack>
                            </Grid>

                            <Grid item xs={12}>
                                <AnimateButton>
                                    <LoadingButton
                                        disableElevation
                                        loadingPosition="start"
                                        startIcon={<></>}
                                        loading={isLoadingSearch}
                                        disabled={isLoadingSearch}
                                        fullWidth
                                        size="large"
                                        type="submit"
                                        variant="contained"
                                        color="primary"
                                    >
                                        {isLoadingSearch ? "Buscando" : "Buscar"}
                                    </LoadingButton>
                                </AnimateButton>
                            </Grid>

                        </Grid>
                    </form>
                )}

            </Formik>

        </MainCard>
    )
}

export default JobsFilters;