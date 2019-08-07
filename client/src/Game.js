import React from 'react'

function Game(props) {

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
                <circle className="territory-circle" cx={territory.x} cy={territory.y} r="5" stroke="green" strokeWidth="1" fill={territory.color} />
              )
            })

          }
        </svg>
      </div>
    </div>
  );
}

export default Game