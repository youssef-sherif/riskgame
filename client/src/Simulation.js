import React from 'react'
import io from 'socket.io-client'
import './Game.css'

function Simulation(props) {           

    setInterval(() => {
        const socket = io.connect('http://localhost:5000/simulation')                                

        socket.emit('time interval')        

        socket.on("simulation change", data => {
            console.log('received data')
            if (typeof data !== 'undefined') {                    
                props.setMap(data.map)
            }
        })                        
    }, 5000)

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
                                    key={territory.id} className="territory-circle" cx={territory.x} cy={territory.y} r="5" stroke="green" strokeWidth="1" fill={territory.color} />
                            )
                        })

                    }
                </svg>
            </div>
        </div>
    );
}

export default Simulation
