import React from 'react'
import { useState, useEffect } from 'react';

// material-ui
import { Typography } from '@mui/material';

const Timer = ({ seconds = 30, onTimeFinalized }) => {
    const [timeLeft, setTimeLeft] = useState(seconds);
    const [minutos, setMinutos] = useState(Math.floor((seconds / (60)) % 60));
    const [segundos, setSegundos] = useState(Math.floor((seconds) % 60));

    useEffect(() => {
        if (!timeLeft) {
            if (onTimeFinalized) {
                onTimeFinalized()
            }
            return;
        }

        const intervalId = setInterval(() => {
            setTimeLeft(timeLeft - 1);
            setMinutos(Math.floor(((timeLeft - 1) / (60)) % 60));
            setSegundos(Math.floor((timeLeft - 1) % 60));
        }, 1000);

        return () => clearInterval(intervalId);

    }, [timeLeft]);

    return (
        <div>
            {/*<h1>{minutos>0? minutos + "min " + segundos + "seg" : segundos + "seg"}</h1>*/}
            {
                timeLeft != 0 ? (minutos + " : " + segundos) : '¡ Se acabó el tiempo, apresúrate !'
                    // <Typography variant="h3" color='primary'>{minutos + " : " + segundos}</Typography>
                    // :
                    // <Typography variant="h4" color='error'>¡ Se acabó el tiempo, apresúrate !</Typography>
            }

        </div>
    );
};

export default Timer;
