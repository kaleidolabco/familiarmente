import React, { useEffect, useRef } from 'react'

const VideoQuestion = ({ urlVideo = "" }) => {

    const videoRef = useRef();

    useEffect( () => {
        videoRef.current?.load();
    }, [urlVideo]);

    return (
        <video 
            ref={videoRef}
            width="100%" 
            height="100%" 
            controls={false} 
            autoPlay 
            style={{objectFit:'cover', borderRadius:'1rem', overflow:'hidden' }}>
            <source src={urlVideo} type="video/mp4"/>
            Tu navegador no soporta la reproducción de video de un avatar
        </video>
    )
}

export default VideoQuestion;