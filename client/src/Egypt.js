import React from 'react'
import Territory from './Territory'
import egyptMap from './egypt-map.png'

function Egypt() {
  return (
    <div>
      <div className={"egypt-map"}>
        <img alt="egypt-map" src={egyptMap} />
      </div>
      <div className={"egypt-map"}>
        <svg className="territory-svg" width="450" height="415">
          <Territory x={70} y={70}  id={1} />
          <Territory x={188} y={44} id={2} />
          <Territory x={205} y={55} id={3} />
          <Territory x={225} y={28} id={4} />
          <Territory x={245} y={33} id={5} />
          <Territory x={255} y={25} id={6} />
          <Territory x={278} y={35} id={7} />
          <Territory x={320} y={55} id={8} />
          <Territory x={228} y={42} id={9} />
          <Territory x={228} y={57} id={10} />
          <Territory x={238} y={67} id={11} />
          <Territory x={255} y={57} id={12} />
          <Territory x={278} y={49} id={13} />
          <Territory x={188} y={105} id={14} />
          <Territory x={210} y={105} id={15} />
          <Territory x={250} y={90} id={16} />
          <Territory x={275} y={100} id={17} />
          <Territory x={330} y={100} id={18} />
          <Territory x={210} y={160} id={20} />
          <Territory x={70} y={300}  id={21} />
          <Territory x={228} y={180} id={22} />
          <Territory x={300} y={180} id={23} />
          <Territory x={250} y={210} id={24} />
          <Territory x={290} y={230} id={25} />
          <Territory x={290} y={245} id={26} />
          <Territory x={300} y={330} id={27} />          
        </svg>
      </div>
    </div>
  );
}

export default Egypt;
