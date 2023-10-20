import React, { createContext, useEffect, useMemo, useState } from 'react';
import PropTypes from 'prop-types';

// material-ui
import { CssBaseline, StyledEngineProvider } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';

// project import
import Palette from '../themes/palette';
import Typography from '../themes/typography';
import CustomShadows from '../themes/shadows';
import componentsOverride from '../themes/overrides';
import AlertSystem from '../components/AlertSystem/AlertSystem';

export const ContextUI = createContext({});

// ==============================|| DEFAULT THEME - MAIN  ||============================== //

export function ContextUIProvider({ children }) {

    //  Estados 
    const [openNotifications, setOpenNotifications] = useState(false);
    const [messageNotifications, setMessageNotifications] = useState('');
    const [notificationActions, setNotificationActions] = useState(null);
    const [notificationSeverity, setNotificationSeverity] = useState(null);

    //  Función para abrir la notificación con un mensaje específico
    const openAlert = (message = '', severity = 'error', actions = null,) => {
        setOpenNotifications(true);
        setMessageNotifications(message);
        setNotificationSeverity(severity);
        setNotificationActions(actions);
    }

    const theme = Palette('light', 'default');

    // eslint-disable-next-line react-hooks/exhaustive-deps
    const themeTypography = Typography(`'Public Sans', sans-serif`);
    const themeCustomShadows = useMemo(() => CustomShadows(theme), [theme]);

    const themeOptions = useMemo(
        () => ({
            breakpoints: {
                values: {
                    xs: 0,
                    sm: 768,
                    md: 1024,
                    lg: 1266,
                    xl: 1536
                }
            },
            direction: 'ltr',
            mixins: {
                toolbar: {
                    minHeight: 60,
                    paddingTop: 8,
                    paddingBottom: 8
                }
            },
            palette: theme.palette,
            customShadows: themeCustomShadows,
            typography: themeTypography
        }),
        [theme, themeTypography, themeCustomShadows]
    );

    const themes = createTheme(themeOptions);
    themes.components = componentsOverride(themes);

    return (
        <ContextUI.Provider value={{ openAlert }}>
            <StyledEngineProvider injectFirst>
                <ThemeProvider theme={themes}>
                    <CssBaseline />
                    {children}

                    <AlertSystem
                        open={openNotifications}
                        actions={notificationActions}
                        message={messageNotifications}
                        severity={notificationSeverity}
                        autoHideDuration={6000}
                        setOpen={setOpenNotifications} />
                        
                </ThemeProvider>
            </StyledEngineProvider>
        </ContextUI.Provider>
    );
}

ContextUIProvider.propTypes = {
    children: PropTypes.node
};
