import React from 'react'
import Territory from './Territory'
import egyptMap from './egypt-map.png'

function Egypt(props) {

  return (
    <div>
      <div className={"egypt-map"}>
        <img alt="egypt-map" src={egyptMap} />
      </div>
      <div className={"egypt-map"}>
        <svg className="territory-svg" width="450" height="415">
            {
              props.map.map(territory => {
                return (
                  <Territory key={territory.id} x={territory.x} y={territory.y} id={territory.id} color={territory.color} />             
                )
              })

            }
        </svg>
      </div>
    </div>
  );
}

export default Egypt