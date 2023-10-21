import React, { useEffect, useState } from 'react';

// material-ui
import { Box, FormControl, InputAdornment, OutlinedInput } from '@mui/material';

// assets
import { SearchOutlined } from '@ant-design/icons';

// ==============================|| HEADER CONTENT - SEARCH ||============================== //

const Search = ({ setSearchString, placeHolder='Buscador...' }) => {

    const [searchTerm, setSearchTerm] = useState('');

    // Manejar el cambio en el contenido de la barra de búsqueda
    const handleChange = (event) => {
        const { value } = event.target;
        setSearchTerm(value);
    };

    useEffect(() => {
        // Definir una función de temporizador
        const timer = setTimeout(() => {
            if (setSearchString) {
                setSearchString(searchTerm)
            }
        }, 800); // Tiempo de retardo en milisegundos

        // Limpiar el temporizador cuando searchTerm cambia o el componente se desmonta
        return () => {
            clearTimeout(timer);
        };
    }, [searchTerm]);

    // const handleChange = (e) => {
    //     if (setSearchString) {
    //         setSearchString(e.target.value)
    //     }
    // }

    return (
        <Box sx={{ ml: { xs: 0, md: 1, width:'100%' } }}>
            <FormControl sx={{ width: { xs: '100%' } }}>
                <OutlinedInput
                    size="small"
                    id="header-search"
                    value={searchTerm}
                    onChange={handleChange}
                    startAdornment={
                        <InputAdornment position="start" sx={{ mr: -0.5 }}>
                            <SearchOutlined />
                        </InputAdornment>
                    }
                    aria-describedby="header-search-text"
                    inputProps={{
                        'aria-label': 'weight'
                    }}
                    placeholder={placeHolder}
                />
            </FormControl>
        </Box>
    )
};

export default Search;
