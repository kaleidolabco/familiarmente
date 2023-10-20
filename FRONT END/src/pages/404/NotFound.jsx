
import { Box, Button, Container, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

// assets
import { ArrowLeftOutlined } from '@ant-design/icons';

const NotFound = () => (
    <Box
        component="main"
        sx={{
            alignItems: 'center',
            display: 'flex',
            flexGrow: 1,
            height: '100vh'
        }}
    >
        <Container maxWidth="md">
            <Box
                sx={{
                    alignItems: 'center',
                    display: 'flex',
                    flexDirection: 'column'
                }}
            >
                <Typography
                    align="center"
                    color="textPrimary"
                    variant="h1"
                >
                    Página no encontrada
                </Typography>
                <Typography
                    align="center"
                    color="textSecondary"
                    variant="h5"
                >
                    <br></br>
                    Hubo un error en la página que estaba buscando.
                    <br></br>
                    Es posible que la URL sea incorrecta o que la página haya sido eliminada.
                </Typography>
                <Box sx={{ textAlign: 'center' }}>
                    <img
                        alt="Under development"
                        src={`/images/undraw_page_not_found_su7k.svg`}
                        style={{
                            marginTop: 50,
                            display: 'inline-block',
                            maxWidth: '100%',
                            width: 560
                        }}
                    />
                </Box>

                <Button
                    startIcon={(<ArrowLeftOutlined fontSize="small" />)}
                    sx={{ mt: 3 }}
                    variant="contained"
                    component={Link} to={'/perfil'}
                >
                    IR AL INICIO
                </Button>
            </Box>
        </Container>
    </Box>
);

export default NotFound;
