import { useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';

// material-ui
import { Grid, Stack, Typography } from '@mui/material';

// project import
import AuthLogin from './auth-forms/AuthLogin';
import AuthWrapper from './AuthWrapper';

// ================================|| LOGIN ||================================ //

const Login = () => {
    
    return(
        <AuthWrapper>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                    <Stack direction="row" justifyContent="space-between" alignItems="baseline" sx={{ mb: { xs: -0.5, sm: 0.5 } }}>
                        <Typography variant="h3">Inicio de sesión</Typography>
                        <Typography component={Link} to="/registro" variant="body1" sx={{ textDecoration: 'none' }} color="primary">
                            No tienes una cuenta?
                        </Typography>
                    </Stack>
                    <Typography variant="h5" color='secondary'>Padres y madres</Typography>
                </Grid>
                <Grid item xs={12}>
                    <AuthLogin />
                </Grid>
            </Grid>
        </AuthWrapper>
    )
}

export default Login;
