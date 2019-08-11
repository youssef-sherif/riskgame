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

  const placeArmies = (territory, armiesCount) => {
    axios.post(`http://localhost:5000/territories/${territory}/place`, {
      'armies_count': armiesCount
    }).then(data => {      
      props.setMap(data.data.map)
      setAvailableArmies(data.data.available_armies)
      fetchNeighboursToBlue()
    })
  }

  /*
  *  after attacking game waits for opponent bot to play
  *  if game is won by either it will alert that the game is over 
  */

  const attack = (attacking_territory, attacked_territory, armiesCount) => {
    axios.post(`http://localhost:5000/territories/${attacked_territory}/attack`, {
      'attacking_territory': attacking_territory,
      'armies_count': armiesCount
    }).then(data => {
      props.setMap(data.data.map)
      if(data.data.winner !== null) {
        alert(data.data.winner + " won the game")
      }
      fetchNeighboursToBlue()
      setAttacking(false)
      setTurn('red')
      axios(
        `http://localhost:5000/opponent-play`
      ).then(data => {      
        props.setMap(data.data.map)
        if(data.data.winner !== null) {
          alert(data.data.winner + " won the game")
        }
        setTurn('blue')
        receiveBlueArmies()
      })
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
  const getAttackButton = () => {
    if (differentColorNeighbours.indexOf(selectedTerritory.id + "") > -1 && selectedTerritory.color === 'red') {
      if (attacking === true) {
        return (
          <div>
            <button onClick={() => {
              attack(attackingTerritory.id, selectedTerritory.id, document.getElementById('attacking-armies').value)
            }}>
              attack {selectedTerritory.color}
            </button>
            <input id='attacking-armies' defaultValue='0' type="number" name="quantity" min="1" max={attackingTerritory.troops - 1} />
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
          you don't have any more troops.
          <br />
          Attack to continue
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
        <svg className="territory-svg" width="800" height="700">
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
        <br />
        available armies: {availableArmies}
        <br />
        <br />
        selected territory:
        <br />
        <span>
          id: {selectedTerritory.id}
          <br />
          troops: {selectedTerritory.troops}
          <br />
          color: {selectedTerritory.color}
          <br />
        </span>
      </div>

      <div className='actions'>
        {getPlaceArmiesButton()}
        <br />
        <br />
        {getAttackButton()}
        <br />
        <br />
      </div>
    </div>
  );
}

export default Game
