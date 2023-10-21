import React from 'react';
import { Link } from 'react-router-dom';

// material-ui
import { Box, Button, CardContent, Divider, Grid, Typography } from '@mui/material';

import MainCard from '../../components/MainCard';

const ConversationCard = ({ title, link }) => {
    return (
        <Grid item xs={6} md={4}>
            <MainCard sx={{ justifyContent: 'center', alignItems: 'space-between' }}>
                {/* <Box sx={{ height:'100%', justifyContent: 'space-between', flexDirection:'column' }}> */}
                    <CardContent>
                        <Typography variant="h6" color="textPrimary" textAlign='center' gutterBottom>
                            {title}
                        </Typography>
                        {/* <Typography variant="body1">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</Typography> */}
                    </CardContent>
                    <Divider />
                    {/* <Button variant="text" fullWidth >Comenzar</Button> */}
                    <Button variant="text" fullWidth component={Link} to={link}>COMENZAR</Button>
                {/* </Box> */}

            </MainCard>
        </Grid>

    )
}

export default ConversationCard