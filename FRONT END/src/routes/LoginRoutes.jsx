import { lazy } from 'react';

// project import
import Loadable from '../components/Loadable';
import MinimalLayout from '../layout/MinimalLayout';

// render - sample page
const SamplePage = Loadable(lazy(() => import('../pages/extra-pages/SamplePage')));

// render - login
const AuthLogin = Loadable(lazy(() => import('../pages/authentication/Login')));
const AuthRegister = Loadable(lazy(() => import('../pages/authentication/Register')));
const NotFoundPage = Loadable(lazy(() => import('../pages/404/NotFound')));

// ==============================|| AUTH ROUTING ||============================== //

const LoginRoutes = {
    path: '/',
    element: <MinimalLayout />,
    children: [
        {
            path: 'autenticacion',
            element: <AuthLogin />
        },
        {
            path: 'registro',
            element: <AuthRegister />
        },
        {
            path: '*',
            element: <NotFoundPage />
        }
    ]
};

export default LoginRoutes;
