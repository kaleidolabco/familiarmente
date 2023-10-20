import { Link } from 'react-router-dom';

// material-ui
import { Button, Divider, Grid, Stack, Typography } from '@mui/material';

// project import
import MainCard from '../../components/MainCard';
import AnalyticCard from '../../components/cards/statistics/AnalyticCard';

// assets
import { DeleteOutlined, EyeOutlined, SettingOutlined, UsergroupAddOutlined, ScheduleOutlined } from '@ant-design/icons';

// ==============================|| SAMPLE PAGE ||============================== //

const DashboardPage = () => (



        <Grid container rowSpacing={4.5} columnSpacing={2.75} justifyContent='center'>

            {/* Datos de interés */}
            <Grid container rowSpacing={4.5} columnSpacing={2.75} item xs={12} md={12}>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <AnalyticCard title="Cargos creados" count="25" percentage={59.3} extra="20 publicados" />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <AnalyticCard title="Assessments" count="80" percentage={33.4} extra="El 33.4% completados" />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <AnalyticCard title="Competencias" count="4"  extra="Usadas en los assessments" />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <AnalyticCard title="Total evaluados" count="40 candidatos" percentage={50} isLoss color="warning" extra="Aún falta calificar usuarios" />
                </Grid>
            </Grid>
            
        </Grid>
        

);

export default DashboardPage;
