import logo from './logo.png';
import './App.css';
import Button from '@mui/material/Button';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import OverallStandings from './overall.js';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p className="App-title">
            fantasy music
          </p>
          <div className="Button-Pages">
          <Link to="/overall"><Button className="button1" variant="contained">Overall Standings</Button></Link>
          <Link to="/lm"><Button className="button1" variant="contained">Billboard 100 Songs</Button></Link>
          <Link to="/lo"><Button className="button1" variant="contained">Billboard 100 Artists</Button></Link>
          <Link to="/li"><Button className="button1" variant="contained">Billboard 200 Albums</Button></Link>
          </div>
        </header>
        <Routes>
          <Route path="/overall" element={<div>Testing</div>} />
          <Route path="/lm" element={<OverallStandings key="lm"/>} />
          <Route path="/lo" element={<OverallStandings />} />
          <Route path="/li" element={<OverallStandings />} />
          <Route path="/" element={<div>hi</div>} /> {}
        </Routes>
      </div> 
    </Router>
  );
}

export default App;
