// material-ui
import { useTheme } from '@mui/material/styles';

/**
 * if you want to use image instead of <svg> uncomment following.
 *
 * import logoDark from 'assets/images/logo-dark.svg';
 * import logo from 'assets/images/logo.svg';
 *
 */
import logo from '../../assets/images/Logotipo_Familiarmente.jpeg';
// ==============================|| LOGO SVG ||============================== //

const Logo = () => {

    return (
        <img src={logo} alt="logo - kaleido" width="100" />
    );
};

export default Logo;
