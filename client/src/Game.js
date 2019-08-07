import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './Game.css'

function Game(props) {

  const [differentColorNeighbours, setDifferentColorNeighbours] = useState([]) 

  const [selectedTerritory, setSelectedTerritory] = useState({
    troops: 0,
    color: 'grey'
  })

  const [turn, setTurn] = useState('blue')  

  const fetchNeighboursToBlue = () => {
    axios(
      `http://localhost:5000/neighbours_to_blue`
    )
      .then(data => {    
        setDifferentColorNeighbours(data.data)
      });
  }

  const fetchNeighboursToRed = () => {
    axios(
      `http://localhost:5000/neighbours_to_red`
    )
      .then(data => {    
        setDifferentColorNeighbours(data.data)
      });
  }

  const getAttackButton = () => {        
    if (selectedTerritory.color !== 'grey' && differentColorNeighbours.indexOf(selectedTerritory.id + "") > -1) {
      return (
        <button>attack {selectedTerritory.color}</button>
      )
    }
    return (
      <div>
        you cannot attack this territory
      </div>
    )
  }

  const getPlaceArmiesButton = () => {
    if (selectedTerritory.color === turn || selectedTerritory.color === 'grey') {
      return (
        <button>place armies</button>
      )
    }
    return (
      <div>
        you cannot place armies on this territory
      </div>
    )
  }

  useEffect(() => {
    fetchNeighboursToBlue()    
  }, [])

  return (
    <div>
      <div className={"map"}>
        <img alt="map" src={props.imgSrc} />
      </div>
      <div className={"map"}>
        <svg className="territory-svg" width="450" height="415">
          {
            props.map.map(territory => {
              return (
                <circle
                  onClick={() => {
                    setSelectedTerritory(territory)
                  }}
                  key={territory.id} className="territory-circle" cx={territory.x} cy={territory.y} r="5" stroke="green" strokeWidth="1" fill={territory.color} />
              )
            })

          }
        </svg>
      </div>
      <div className='selected-territory'>
        currently playing: {turn}
        <br />
        troops: {selectedTerritory.troops}
        <br />
        color: {selectedTerritory.color}
        <br />
        {getPlaceArmiesButton()}
        <br />
        {getAttackButton()}        
        <br />
        <button onClick={() => {
          if(turn === 'blue') {
            setTurn('red')
            fetchNeighboursToRed()
          }
          else {
            setTurn('blue')
            fetchNeighboursToBlue()
          } 
        }}>
          change turns
        </button>
      </div>
    </div>
  );
}

export default Game