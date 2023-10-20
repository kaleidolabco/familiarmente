import React, { useEffect } from 'react'

import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

// Material UI
import { Button } from '@mui/material';
import { activeItem } from '../../../../../store/reducers/menu';

const HeaderOption = ({ id, title, path }) => {

    const menu = useSelector((state) => state.menu);
    const dispatch = useDispatch();
    const { openItem } = menu;

    const onClick = (id) => {
        dispatch(activeItem({ openItem: [id] }));
    };

    // active menu item on page load
    useEffect(() => {
        const currentIndex = document.location.pathname
            .toString()
            .split('/')
            .findIndex((_id) => _id === id);
        if (currentIndex > -1) {
            dispatch(activeItem({ openItem: [id] }));
        }
        // eslint-disable-next-line
    }, []);

    const isSelected = openItem.findIndex((_id) => _id === id) > -1;

    return (
        <Link to={path}>
        <Button
            color={isSelected ? "primary" : "secondary"}
            sx={{ mr: 1, whiteSpace: 'nowrap', minWidth: 'auto' }}
            onClick={() => onClick(id)}
        >
            {title}
        </Button>
        </Link>
        
    )
}

export default HeaderOption;
