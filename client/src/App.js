import React, { useState } from 'react';
import axios from 'axios'
import Egypt from './Egypt'
import './App.css'

function App() {

  const [map, setMap] = useState([])
  const [country, setCountry] = useState("Egypt")
  const [mode, setMode] = useState("playing")
  const [opponent, setOpponent] = useState()
  const [agent1, setAgent1] = useState()
  const [agent2, setAgent2] = useState()

  const newGame = (opponent, country) => {
    axios(
      `http://localhost:5000/new_game?opponent_type=${opponent}&country=${country}`
    )
      .then(data => {    
        setMap(data.data)
      });
  }

  const newSimulation = (agent1, agent2, country) => {
    axios(
      `http://localhost:5000/new_simulation?agent1_type=${agent1}&agent2_type=${agent2}&country=${country}`
    )
      .then(data => {
        setMap(data)
      });
  }

  return (
    <div className="App">
      <label htmlFor="mode-select">Choose a mode:</label>
      <select id="mode-select" onChange={(e) => {
        setMode(e.target.value);
      }}>
        <option value="">--Please choose an option--</option>
        <option value="playing">Playing</option>
        <option value="simulation">Simulation</option>
      </select>

      <label htmlFor="map-select">Choose a map:</label>
      <select id="map-select" onChange={(e) => {
        setCountry(e.target.value);
      }}>
        <option value="">--Please choose an option--</option>
        <option value="Egypt">Egypt</option>
        <option value="USA">USA</option>
      </select>

      <br />

      {mode === 'playing' ?
        <div>
          <label htmlFor="opponent-select">Choose opponent:</label>
          <select id="opponent-select" onChange={(e) => {
            setOpponent(e.target.value)
          }}>
            <option value="">--Please choose an option--</option>
            <option value="passive">Passive</option>
          </select>
        </div>
        :
        <div>
          <label htmlFor="agent1-select">Choose agent1:</label>
          <select id="agent1-select" onChange={(e) => {
            setAgent1(e.target.value)
          }}>
            <option value="">--Please choose an option--</option>
            <option value="Passive">Playing</option>
          </select>

          <label htmlFor="agent1-select">Choose agent1:</label>
          <select id="agent1-select" onChange={(e) => {
            setAgent2(e.target.value)
          }}>
            <option value="">--Please choose an option--</option>
            <option value="Passive">Playing</option>
          </select>
        </div>
      }

      <button onClick={() => {
        if (mode === 'playing') {
          newGame(opponent, country)
        } else {
          newSimulation(agent1, agent2, country)
        }
      }}>start game</button>
      
      <br />

      {country === 'Egypt' ?
        <Egypt map={map} />
        :
        <div>not yet</div>
      }
    </div>
  );
}

export default App
