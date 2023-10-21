import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

// material-ui
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';

// project import
import EnhancedTableHead from './EnhancedTableHead';

// assets
import { DeleteOutlined, FilterOutlined } from '@ant-design/icons';

// functions
function descendingComparator(a, b, orderBy) {
    if (b[orderBy] < a[orderBy]) {
        return -1;
    }
    if (b[orderBy] > a[orderBy]) {
        return 1;
    }
    return 0;
}

function getComparator(order, orderBy) {
    return order === 'desc'
        ? (a, b) => descendingComparator(a, b, orderBy)
        : (a, b) => -descendingComparator(a, b, orderBy);
}

// Since 2020 all major browsers ensure sort stability with Array.prototype.sort().
// stableSort() brings sort stability to non-modern browsers (notably IE11). If you
// only support modern browsers you can replace stableSort(exampleArray, exampleComparator)
// with exampleArray.slice().sort(exampleComparator)
function stableSort(array, comparator) {
    const stabilizedThis = array.map((el, index) => [el, index]);
    stabilizedThis.sort((a, b) => {
        const order = comparator(a[0], b[0]);
        if (order !== 0) {
            return order;
        }
        return a[1] - b[1];
    });
    return stabilizedThis.map((el) => el[0]);
}

export default function ListTable({ rows = [], headCells = [], controllerPage, controllerRowsPerPage, changePage, changeRowsPerPage, totalElements }) {
    const [order, setOrder] = useState('asc');
    const [orderBy, setOrderBy] = useState('');
    const [page, setPage] = useState(0);
    const [dense, setDense] = useState(false);
    const [rowsPerPage, setRowsPerPage] = useState(5);

    const handleRequestSort = (event, property) => {
        const isAsc = orderBy === property && order === 'asc';
        setOrder(isAsc ? 'desc' : 'asc');
        setOrderBy(property);
    };

    const handleClick = (event, name) => {

    };

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };

    const handleChangeDense = (event) => {
        setDense(event.target.checked);
    };

    // Avoid a layout jump when reaching the last page with empty rows.
    const emptyRows =
        page > 0 ? Math.max(0, (1 + page) * rowsPerPage - rows.length) : 0;

    const sortList = controllerPage && controllerRowsPerPage ? 
    stableSort(rows, getComparator(order, orderBy))
    :
    stableSort(rows, getComparator(order, orderBy))
        .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)

    return (
        <Box sx={{ width: '100%', px: 1 }}>

            <TableContainer>
                <Table
                    sx={{ minWidth: 750 }}
                    aria-labelledby="tableTitle"
                    size={dense ? 'small' : 'medium'}
                >
                    <EnhancedTableHead
                        headCells={headCells}
                        order={order}
                        orderBy={orderBy}
                        onRequestSort={handleRequestSort}
                        rowCount={rows.length}
                    />

                    <TableBody>
                        {sortList.map((row, index) => {

                                const labelId = `enhanced-table-checkbox-${index}`;

                                return (
                                    <TableRow
                                        hover
                                        onClick={(event) => handleClick(event, row.name)}
                                        role="checkbox"
                                        tabIndex={-1}
                                        key={index}
                                    >
                                        {
                                            Object.entries(row).map((item, index) => {
                                                const [key, value] = item;
                                                const elementKey = `table-cell-${key}-${value}`;

                                                return (
                                                    <TableCell
                                                        key={elementKey}
                                                        align={index != 0 ? "right" : "left"}
                                                        component="th"
                                                        scope="row"
                                                        padding="none"
                                                    >
                                                        {value}
                                                    </TableCell>
                                                )
                                            })
                                        }
                                        {/* <TableCell
                                            component="th"
                                            id={labelId}
                                            scope="row"
                                            padding="none"
                                        >
                                            {row.name}
                                        </TableCell>
                                        <TableCell align="right">{row.calories}</TableCell>
                                        <TableCell align="right">{row.fat}</TableCell>
                                        <TableCell align="right">{row.carbs}</TableCell>
                                        <TableCell align="right">{row.protein}</TableCell> */}
                                    </TableRow>
                                );
                            })}
                        {emptyRows > 0 && (
                            <TableRow
                                style={{
                                    height: (dense ? 33 : 53) * emptyRows,
                                }}
                            >
                                <TableCell colSpan={6} />
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </TableContainer>
            <TablePagination
                rowsPerPageOptions={[5, 10, 20]}
                component="div"
                count={ totalElements || rows.length }
                labelDisplayedRows={({ from, to, count }) => { return `${from} – ${to} de ${count !== -1 ? count : `más de ${to}`}`; }}
                labelRowsPerPage="Ítems por página"
                rowsPerPage={ controllerRowsPerPage || rowsPerPage }
                page={ controllerPage? controllerPage - 1  : page }
                onPageChange={ changePage || handleChangePage}
                onRowsPerPageChange={ changeRowsPerPage ? changeRowsPerPage : handleChangeRowsPerPage}
            />

            {/* <FormControlLabel
                control={<Switch checked={dense} onChange={handleChangeDense} />}
                label="Dense padding"
            /> */}
        </Box>
    );
}

ListTable.propTypes = {
    rows: PropTypes.array.isRequired
};