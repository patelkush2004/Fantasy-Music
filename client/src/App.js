import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import logo from './logo.png';
import './App.css';
import Button from '@mui/material/Button';
import OverallStanding from './components/overallStanding';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={
            <>
            <header className="App-header">
              <img src={logo} className="App-logo" alt="logo" />
                <p className="App-title">
                  fantasy music
                </p>
              <div className="Button-Pages">
                <Link to="/overall"><Button variant='outlined'>Overall Standings</Button></Link>
                <Button variant='outlined'>Billboard 100 Songs</Button>
                <Button variant='outlined'>Billboard 100 Artists</Button>
                <Button variant='outlined'>Billboard 200 Albums</Button>
              </div>
            </header>
            </>
          } />
          <Route path="/overall" element={<OverallStanding />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
