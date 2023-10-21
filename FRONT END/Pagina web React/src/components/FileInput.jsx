import { useRef, useState } from "react";
import { Box, Breadcrumbs, Button, IconButton, Stack, TextField, Typography } from "@mui/material";

// assets
import { PaperClipOutlined, CameraOutlined, DeleteOutlined } from '@ant-design/icons';

const FileInput = ({ label = "Subir archivo", accept = "", value, onChange, error, icon }) => {
    const fileInputRef = useRef();
    const [attachment, setAttachment] = useState(value);

    const handleFileChange = (event) => {
        const files = Array.from(event.target.files);
        const [file] = files;
        setAttachment(file);
        // console.log(file);
        if (!!onChange) onChange({ target: { value: file } });
    };

    const handleUploadButtonClick = () => {
        fileInputRef.current.click();
    };

    const handleDeleteButtonClick = () => {
        setAttachment(null);
        if (!!onChange) onChange({ target: { value: null } });
    };

    return (
        <Stack direction="column" spacing={0}>
            <Stack direction="row" spacing={1}>
                <input
                    type="file"
                    accept={accept}
                    ref={fileInputRef}
                    style={{ display: "none" }}
                    onChange={handleFileChange}
                />
                <Button
                    variant="outlined"
                    startIcon={ icon || <PaperClipOutlined /> }
                    onClick={handleUploadButtonClick}
                    error={error}
                >
                    { label }
                </Button>
                {attachment && (
                    <IconButton color="error" aria-label="delete" size="medium" onClick={handleDeleteButtonClick}>
                        <DeleteOutlined fontSize="inherit" />
                    </IconButton>
                )}
            </Stack>


            {/* <Stack sx={{mx: 1.5}}>
                {
                    attachment &&
                    <Breadcrumbs aria-label="breadcrumb">
                        <Typography variant="caption"
                            sx={{ overflow: "hidden", textOverflow: "ellipsis", width: '100%' }}>

                            {attachment.name}

                        </Typography>
                    </Breadcrumbs>
                }
            </Stack> */}
        </Stack>
    );
};

export default FileInput;
