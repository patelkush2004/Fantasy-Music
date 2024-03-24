import logo from './logo.png';
import './App.css';
import Button from '@mui/material/Button';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
          <p className="App-title">
            fantasy music
          </p>
        <div className="Button-Pages">
          <Button variant='outlined' to='/overall'>Overall Standings</Button>
          <Button variant='outlined'>Billboard 100 Songs</Button>
          <Button variant='outlined'>Billboard 100 Artists</Button>
          <Button variant='outlined'>Billboard 200 Albums</Button>
        </div>
      </header>
    </div>
  );
}

export default App;
