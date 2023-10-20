import { lazy } from 'react';

import { Navigate } from 'react-router-dom';

// project import
import Loadable from '../components/Loadable';
import MainLayout from '../layout/MainLayout';
import PrivateRoute from '../context/Authentication/PrivateRoute';

// render - sample page
const SamplePage = Loadable(lazy(() => import('../pages/extra-pages/SamplePage')));

// render - principal
const DashboardPage = Loadable(lazy(() => import('../pages/dashboard')));
const ProfilePage = Loadable(lazy(() => import('../pages/profile')));
const JobsPage = Loadable(lazy(() => import('../pages/jobs')));
const ConversationsPage = Loadable(lazy(() => import('../pages/conversations')));
const JobsDetail = Loadable(lazy(() => import('../pages/jobs/JobDetail')));
const JobsAplication = Loadable(lazy(() => import('../pages/assessment/JobApplication')));
const AssessmentPage = Loadable(lazy(() => import('../pages/assessment/AssessmentPage'))); 
const ApplicationsPage = Loadable(lazy(() => import('../pages/applications')));
const ApplicationsDetail = Loadable(lazy(() => import('../pages/applications/ApplicationDetail')));
// const NotFoundPage = Loadable(lazy(() => import('../pages/404/NotFound')));

// render - utilities
// const Typography = Loadable(lazy(() => import('pages/components-overview/Typography')));
// const Color = Loadable(lazy(() => import('pages/components-overview/Color')));
// const Shadow = Loadable(lazy(() => import('pages/components-overview/Shadow')));
// const AntIcons = Loadable(lazy(() => import('pages/components-overview/AntIcons')));

// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
    path: '/',
    element: <PrivateRoute> <MainLayout /> </PrivateRoute> ,
    children: [
        {
            path: '/',
            element: <Navigate to="/perfil" replace />
        },
        {
            path: 'perfil',
            element: <ProfilePage />
        },
        {
            path: 'conversacion',
            element: <ConversationsPage />
        },
        {
            path: 'conversacion',
            children: [
                {
                    path: ':job_id',
                    element: <JobsDetail />
                },
                {
                    path: ':job_id/postular',
                    element: <JobsAplication />
                },
                {
                    path: ':job_id/postular/assessment',
                    element: <AssessmentPage />
                }
            ]
        },
        {
            path: 'terapias',
            element: <ApplicationsPage />
        },
        {
            path: 'terapias',
            children: [
                {
                    path: ':job_application_id',
                    element: <ApplicationsDetail />
                }
            ]
        }
    ]
};

export default MainRoutes;
