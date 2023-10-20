import { useState } from 'react';

import LoadingButton from '@mui/lab/LoadingButton';

const ActionDelete = ({ isLoading, callback }) => {

    const [deletePressed, setDeletePressed] = useState(false);

    const onConfirmDelete = async () => {
        setDeletePressed(true)
        callback();
    }

    return (

        <LoadingButton
            loading={deletePressed}
            // loadingPosition="start"
            // startIcon={<></>}
            // disableElevation
            color="error"
            variant='contained'
            size="small"
            onClick={onConfirmDelete}>
            ELIMINAR
        </LoadingButton>
    )
};

export default ActionDelete;