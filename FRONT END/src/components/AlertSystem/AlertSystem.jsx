import React from 'react';
// import CloseIcon from '@mui/icons-material/Close';
import { CloseOutlined } from '@ant-design/icons';
import IconButton from '@mui/material/IconButton';
// import MuiAlert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import Slide from '@mui/material/Slide';
import Alert from '@mui/material/Alert';

function TransitionLeft(props) {
    return <Slide {...props} direction="left" />;
}

function TransitionUp(props) {
    return <Slide {...props} direction="up" />;
}

function TransitionRight(props) {
    return <Slide {...props} direction="right" />;
}

function TransitionDown(props) {
    return <Slide {...props} direction="down" />;
}

// const actionDelete =(
//     <Button color="secondary" size="small" onClick={()=>onRemoveProductCart()}>
//       ELIMINAR
//     </Button>
//   );

//   const onRemoveProductClick = () => {
//     openNotification('¿Desea eliminar del carrito el producto ' + name + '?', 
//       'warning', actionDelete);
//   }
// const Alert = React.forwardRef(function Alert(props, ref) {
//     return <MuiAlert elevation={6} ref={ref} variant="outlined" {...props} />;
// });

export default function AlertSystem({ open, message, severity = 'info', setOpen = null, actions = null }) {

    const handleClose = () => {
        if (setOpen) {
            setOpen(false);
        }
    };

    const action = (
        <React.Fragment>
            {
                actions ? actions : <></>
            }
            <IconButton
                size="small"
                aria-label="close"
                color="inherit"
                onClick={handleClose}
            >
                <CloseOutlined style={{ fontSize: '0.75rem', color: 'inherit' }}/>
                {/* <CloseIcon fontSize="small" /> */}
            </IconButton>
        </React.Fragment>
    );

    return (
        <Snackbar
            disableWindowBlurListener={false}
            anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
            open={open}
            autoHideDuration={5000}
            onClose={handleClose}
            sx={{ maxWidth: '85vw' }}
            TransitionComponent={TransitionDown}
        >

            <Alert
                variant='filled'
                className='interactable-ui'
                action={action}
                // onClose={handleClose} 
                severity={severity}
                sx={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center' }}
            >
                {message}
            </Alert>

        </Snackbar>
    );
}