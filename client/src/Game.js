import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './Game.css'

function Game(props) {

  const [differentColorNeighbours, setDifferentColorNeighbours] = useState([])
  const [selectedTerritory, setSelectedTerritory] = useState({
    id: 1,
    troops: 0,
    color: 'grey'
  })
  const [turn, setTurn] = useState('blue')
  const [availableArmies, setAvailableArmies] = useState(1)
  const [attacking, setAttacking] = useState(false)
  const [selecAttackingTerritory, setSelectAttackingTerritory] = useState(false)
  const [attackingTerritory, setAttackingTerritory] = useState({})

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

  const placeArmies = (territory, armiesCount) => {
    axios.post(`http://localhost:5000/territories/${territory}/place`, {
      'armies_count': armiesCount
    }).then(data => {
      props.setMap(data.data.map)
      setAvailableArmies(data.data.available_armies)
      fetchNeighboursToBlue()
    })
  }

  const attack = (attacking_territory, attacked_territory, armiesCount) => {
    axios.post(`http://localhost:5000/territories/${attacked_territory}/attack`, {
      'attacking_territory': attacking_territory,
      'armies_count': armiesCount
    }).then(data => {
      props.setMap(data.data.map)
      fetchNeighboursToBlue()
      setAttacking(false)
    })
  }

  const receiveBlueArmies = () => {
    axios(
      `http://localhost:5000/blue-armies`
    )
      .then(data => {
        setAvailableArmies(data.data)
      });
  }

  const receiveRedArmies = () => {
    axios(
      `http://localhost:5000/red-armies`
    )
      .then(data => {
        setAvailableArmies(data.data)
      });
  }

  const getAttackButton = () => {
    if (differentColorNeighbours.indexOf(selectedTerritory.id + "") > -1) {
      if (attacking === true) {
        return (
          <div>
            <button onClick={() => {
              attack(attackingTerritory.id, selectedTerritory.id, document.getElementById('attacking-armies').value)
            }}>
              attack {selectedTerritory.color}
            </button>
            <input id='attacking-armies' defaultValue='1' type="number" name="quantity" min="1" max={attackingTerritory.troops - 1} />
          </div>
        )
      }
      if (selecAttackingTerritory === true) {
        return (
          <div>choose territory to attack from</div>
        )
      }
      return (
        <button onClick={() => {
          setSelectAttackingTerritory(true)
        }}>
          choose territory to attack from
        </button>
      )
    }
    return (
      <div>
        you cannot attack this territory
      </div>
    )
  }

  const getPlaceArmiesButton = () => {
    if (availableArmies <= 0) {
      return (
        <div>
          you don't have any more troops. Attack or change turns
        </div>
      )
    }
    else if (selectedTerritory.color === turn || selectedTerritory.color === 'grey') {
      return (
        <div>
          <button onClick={() => {
            placeArmies(selectedTerritory.id, 1)
            setSelectedTerritory({
              id: selectedTerritory.id,
              troops: selectedTerritory.troops + 1,
              color: turn
            })
          }}>
            click to add more armies
        </button>
        </div>
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
    receiveBlueArmies()
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
                    if (selecAttackingTerritory === true) {
                      setAttackingTerritory(territory)
                      setSelectAttackingTerritory(false)
                      setAttacking(true)
                    } else {
                      setSelectedTerritory(territory)
                    }
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
        available armies: {availableArmies}
        <br />
        selected territory: {selectedTerritory.id}
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
          if (turn === 'blue') {
            fetchNeighboursToRed()
            receiveRedArmies()
            setTurn('red')
          }
          else {
            fetchNeighboursToBlue()
            receiveBlueArmies()
            setTurn('blue')
          }
        }}>
          change turns
        </button>
      </div>
    </div>
  );
}

export default Game
