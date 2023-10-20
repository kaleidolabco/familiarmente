// assets
import {
    AppstoreAddOutlined,
    AntDesignOutlined,
    TeamOutlined,
    FileSearchOutlined,
    DesktopOutlined,
    LoadingOutlined,
    ScheduleOutlined,
    UserOutlined,
    SolutionOutlined
} from '@ant-design/icons';

// icons
const icons = {
    DesktopOutlined,
    FileSearchOutlined,
    TeamOutlined,
    AntDesignOutlined,
    LoadingOutlined,
    AppstoreAddOutlined,
    ScheduleOutlined,
    UserOutlined,
    SolutionOutlined
};

// ==============================|| MENU ITEMS - UTILITIES ||============================== //

const pages = {
    id: 'dashboard-pages',
    title: 'Principal',
    type: 'group',
    children: [
        {
            id: 'perfil',
            title: 'Perfil',
            type: 'item',
            url: '/perfil',
            icon: icons.UserOutlined
        },
        {
            id: 'cargos',
            title: 'Iniciar conversación',
            type: 'item',
            url: '/conversacion',
            icon: icons.DesktopOutlined,
        },
        {
            id: 'aplicaciones',
            title: 'Terapias de mis hijos',
            type: 'item',
            url: '/terapias',
            icon: icons.SolutionOutlined
        }
    ]
};

export default pages;
