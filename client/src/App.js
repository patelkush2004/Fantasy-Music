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
        <Button className="button1" variant="contained">Overall Standings</Button>
        <Button className="button1" variant="contained">Billboard 100 Songs</Button>
        <Button className="button1" variant="contained">Billboard 100 Artists</Button>
        <Button className="button1" variant="contained">Billboard 200 Albums</Button>
        </div>
      </header>
    </div>
  );
}

export default App;
