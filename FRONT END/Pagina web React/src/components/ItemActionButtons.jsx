import {  useContext } from 'react';
import { Link } from 'react-router-dom';

// material-ui
import { IconButton, Tooltip } from '@mui/material';

// Custom hooks
import { useFetch } from '../hooks';

//Context
import { AuthContext } from '../context/Authentication/Auth';
import { ContextUI } from '../context/ContextUI';

// assets
import { DeleteOutlined, EyeOutlined } from '@ant-design/icons';

// components 
import ActionDelete from './ActionDelete';

const ItemActionButtons = ({ idCargo, nombreCargo, onFinish, urlDelete, actionDelete, dataDelete }) => {

    const { openAlert } = useContext(ContextUI);
    const { token } = useContext(AuthContext);

    const { data, isLoading, hasError, postAWS } = useFetch();

    const onDelete = () => {
        openAlert('Por favor confirma que deseas eliminar el cargo: ' + nombreCargo,
            'warning', <ActionDelete callback={onConfirmDelete} />);
    }

    const onConfirmDelete = async () => {
        // console.log('eliminando')
        const delete_request = await postAWS(
            urlDelete,
            actionDelete,
            dataDelete,
            token
        );


        if (delete_request.success) {
            openAlert(delete_request.message, 'success');
        }
        else {
            openAlert(`${delete_request.message}: ${delete_request.error?.error}`, 'error')
        }

        onFinish();
    }

    return (
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <Tooltip title="Ver más detalles">
                <IconButton aria-label="delete" color='primary' component={Link} to={idCargo}>
                    <EyeOutlined />
                </IconButton>
            </Tooltip>
            <Tooltip title="Eliminar cargo">
                <IconButton aria-label="delete" color='error' onClick={onDelete}>
                    <DeleteOutlined />
                </IconButton>
            </Tooltip>
        </div>
    )
}


export default ItemActionButtons;