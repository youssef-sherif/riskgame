import React from 'react'

function Territory(props) {

    return (        
        <circle className="territory-circle" cx={props.x} cy={props.y} r="5" stroke="green" stroke-width="1" fill={props.color} />        
    );
}

export default Territory;
