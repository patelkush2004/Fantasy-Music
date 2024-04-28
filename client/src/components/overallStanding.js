import React from "react";
import './Standings.css';
import { useState, useEffect } from 'react';

import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';

import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';

const OVERALL = "http://localhost:3001/overall";

const columns = [
  { id: 'rank', label: 'Rank', minWidth: 50, align: 'left' },
  { id: 'artist_picture', label: 'Artist', minWidth: 50, align: 'center'},
  { id: 'artist', label: 'Name', minWidth: 320 },
  {
    id: 'daily_streams',
    label: 'Daily Streams',
    minWidth: 150,
    align: 'left',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'total_streams',
    label: 'Total Streams',
    minWidth: 150,
    align: 'left',
    format: (value) => value.toLocaleString('en-US'),
  },
];

function addMillion(data, str) {
    return data.map(item => {
      item.daily_streams = item.daily_streams + str;
      item.total_streams = item.total_streams + str;
      return item;
    });
  }

export default function OverallStanding() {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [rows, setRows] = useState([]);

  const getRows = async () => {
    const response = await fetch(OVERALL);
    const data = await response.json();
    addMillion(data, ' million');
    setRows(data);
  }

  useEffect(() => {
    getRows();
  }, []);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  const [value, setValue] = useState('1');

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className="Standings">
        <p className="Standings-title">
            overall standings
        </p>
        <Box sx={{ width: '90%', typography: 'body1', margin: 'auto' }}>
        <TabContext value={value}>
            <Box sx={{borderBottom: 1, borderColor: 'divider' }}>
            <TabList onChange={handleChange} aria-label="lab API tabs example">
                <Tab label="Standings" value="1" />
                <Tab label="My Team" value="2" />
            </TabList>
            </Box>
            <TabPanel value="1">
                <Paper sx={{ width: '100%', overflow: 'hidden', margin: 'auto' }}>
                    <TableContainer sx={{ maxHeight: 680 }}>
                        <Table stickyHeader aria-label="sticky table">
                        <TableHead>
                            <TableRow>
                            {columns.map((column) => (
                                <TableCell
                                key={column.id}
                                align={column.align}
                                style={{ minWidth: column.minWidth }}
                                sx={{ fontWeight: 'bold', backgroundColor: '#48A2EE', color: 'white'}}
                                >
                                {column.label}
                                </TableCell>
                            ))}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows
                            .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                            .map((row) => {
                                return (
                                <TableRow hover role="checkbox" tabIndex={-1} key={row.code} sx={{ height: '20px' }}>
                                    {columns.map((column) => {
                                        const value = row[column.id];
                                        return (
                                            <TableCell key={column.id} align={column.align}>
                                            {column.id === 'artist_picture' ? 
                                                <img src={value} alt="artist_picture" style={{width: '66px', height: '66px', borderRadius: '50%'}}/> :
                                                (column.format && typeof value === 'number' ? column.format(value) : value)
                                            } 
                                            </TableCell>
                                        );
                                    })}
                                </TableRow>
                                );
                            })}
                        </TableBody>
                        </Table>
                    </TableContainer>
                    <TablePagination
                        rowsPerPageOptions={[10, 25, 100]}
                        component="div"
                        count={rows.length}
                        rowsPerPage={rowsPerPage}
                        page={page}
                        onPageChange={handleChangePage}
                        onRowsPerPageChange={handleChangeRowsPerPage}
                        sx={{ fontWeight: 'bold', backgroundColor: '#48A2EE', color: 'white'}}
                    />
                </Paper>
            </TabPanel>
            <TabPanel value="2">Item Two</TabPanel>
        </TabContext>
        </Box>
    </div>
  );
}
