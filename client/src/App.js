import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import logo from './logo.png';
import './App.css';
import Button from '@mui/material/Button';
import OverallStanding from './components/overallStanding';
import BillboardArtists from './components/billboardArtists';
import BillboardSongs from './components/billboardSongs';
import BillboardAlbums from './components/billboardAlbums';

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
                <Link to="/billboard-artists"><Button variant='outlined'>Billboard 100 Artists</Button></Link>
                <Link to="/billboard-songs"><Button variant='outlined'>Billboard 200 Songs</Button></Link>
                <Link to="/billboard-albums"><Button variant='outlined'>Billboard 200 Albums</Button></Link>
              </div>
            </header>
            </>
          } />
          <Route path="/overall" element={<OverallStanding />} />
          <Route path="/billboard-artists" element={<BillboardArtists />} />
          <Route path="/billboard-songs" element={<BillboardSongs />} />
          <Route path="/billboard-albums" element={<BillboardAlbums />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
