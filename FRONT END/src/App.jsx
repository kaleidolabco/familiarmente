// project import
import Routes from './routes';
import ScrollTop from './components/ScrollTop';

// Contextos
import { ContextUIProvider } from './context/ContextUI';
import { AuthProvider } from './context/Authentication/Auth';

// ==============================|| APP - THEME, ROUTER, LOCAL  ||============================== //

const App = () => (
        <ContextUIProvider>
            <ScrollTop>
                <AuthProvider>
                    <Routes />
                </AuthProvider>
            </ScrollTop>
        </ContextUIProvider>
);

export default App;
