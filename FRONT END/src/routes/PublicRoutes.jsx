import { lazy } from 'react';

// project import
import Loadable from '../components/Loadable';
import MinimalLayout from '../layout/MinimalLayout';

// render - principal
const NotFoundPage = Loadable(lazy(() => import('../pages/404/NotFound')));

// ==============================|| MAIN ROUTING ||============================== //

const PublicRoutes = {
    path: '/',
    element: <MinimalLayout />,
    children: [
        {
            path: '*',
            element: <NotFoundPage />
        }
    ]
};

export default PublicRoutes;
