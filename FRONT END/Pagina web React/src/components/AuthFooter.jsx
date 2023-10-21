// material-ui
import { useMediaQuery, Container, Link, Typography, Stack } from '@mui/material';

// ==============================|| FOOTER - AUTHENTICATION ||============================== //

const AuthFooter = () => {
    const matchDownSM = useMediaQuery((theme) => theme.breakpoints.down('sm'));

    return (
        <Container maxWidth="xl">
            <Stack
                direction={matchDownSM ? 'column' : 'row'}
                justifyContent={matchDownSM ? 'center' : 'space-between'}
                spacing={2}
                textAlign={matchDownSM ? 'center' : 'inherit'}
            >
                <Typography variant="subtitle2" color="secondary" component="span">
                    {'© '}
                    <Typography component={Link} variant="subtitle2" href="https://www.kaleidolab.scenariovr.co/" target="_blank" underline="hover">
                        Kaleido Lab
                    </Typography>
                    {'. Todos los derechos reservados. Registro de derecho de autor otorgado DNDA. '}
                    
                </Typography>

                <Stack
                    direction={matchDownSM ? 'column' : 'row'}
                    spacing={matchDownSM ? 1 : 3}
                    textAlign={matchDownSM ? 'center' : 'inherit'}
                >
                    <Typography
                        variant="subtitle2"
                        color="secondary"
                        component={Link}
                        href="https://www.kaleidolab.scenariovr.co/nosotros/"
                        target="_blank"
                        underline="hover"
                    >
                        Nosotros
                    </Typography>
                    <Typography
                        variant="subtitle2"
                        color="secondary"
                        component={Link}
                        href="https://www.kaleidolab.scenariovr.co/politica-de-privacidad/"
                        target="_blank"
                        underline="hover"
                    >
                        Política de privacidad
                    </Typography>
                    <Typography
                        variant="subtitle2"
                        color="secondary"
                        component={Link}
                        href="https://www.kaleidolab.scenariovr.co/contacto/"
                        target="_blank"
                        underline="hover"
                    >
                        Contáctanos
                    </Typography>
                </Stack>
            </Stack>
        </Container>
    );
};

export default AuthFooter;
