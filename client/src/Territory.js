import React, { useState } from 'react'

function Territory(props) {

    const [color, setColor] = useState('grey')

    return (        
        <circle className="territory-circle" cx={props.x} cy={props.y} r="5" stroke="green" stroke-width="1" fill={color} />        
    );
}

export default Territory;
