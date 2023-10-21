import { useEffect } from 'react';

// material-ui
import { Box, Button, IconButton, Link, useMediaQuery } from '@mui/material';
import { QuestionCircleOutlined } from '@ant-design/icons';

import Profile from './Profile';
import Notification from './Notification';
import MobileSection from './MobileSection';
import Logo from '../../../../components/Logo';
import HeaderOption from './HeaderOption';
import menuItems from '../../../../menu-items';

const pages = ['Products', 'Pricing', 'Blog'];

// ==============================|| HEADER - CONTENT ||============================== //

const HeaderContent = () => {
    const matchesXs = useMediaQuery((theme) => theme.breakpoints.down('md'));
    // useEffect(()=> {
    //     console.log(menuItems?.items[0]?.children)
    // }, []);
    
    return (
        <>
            {!matchesXs &&
                <>
                    <Logo />
                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' }, ml: 3, justifySelf: 'start' }}>
                        {menuItems?.items[0]?.children.map((menuItem, i) => (
                            <HeaderOption
                                key={menuItem.id}
                                id={menuItem.id}
                                title={menuItem.title}
                                path={menuItem.url}
                            />
                                
                        ))}
                    </Box>
                </>
            }

            {!matchesXs && <div style={{ width: '100%' }} />}
            {matchesXs && <Box sx={{ width: '100%', ml: 1 }} />}


            <IconButton
                component={Link}
                href="https://www.kaleidolab.scenariovr.co/"
                target="_blank"
                disableRipple
                color="secondary"
                title="Download Free Version"
                sx={{ color: 'text.primary', bgcolor: 'grey.100' }}
            >
                <QuestionCircleOutlined />
            </IconButton>

            <Notification />
            {!matchesXs && <Profile />}
            {matchesXs && <MobileSection />}
        </>
    );
};

export default HeaderContent;
