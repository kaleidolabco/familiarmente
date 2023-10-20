import React, { useState, useCallback, useRef, useContext, useImperativeHandle, forwardRef, useEffect } from 'react';
import Webcam from 'react-webcam';

import fixWebmDuration from 'webm-duration-fix';

import * as faceapi from 'face-api.js';

const videoConstraints = {
    width: 640,
    height: 360,
    facingMode: "user",//{ exact: "environment" }//"user"
    aspectRatio: 1.777
};


const Camera = forwardRef(( { onCameraReady } , ref) => {

    const webcamRef = useRef(null);
    const AIIntervalRef = useRef(null);
    const mediaRecorderRef = useRef(null);
    const [capturing, setCapturing] = useState(false);
    const [recordedChunks, setRecordedChunks] = useState([]);
    const [emotionsArray, setEmotionsArray] = useState([]);

    // Pasar la referencia al componente padre a través de ref
    useImperativeHandle(ref, () => ({
        handleStartCapture,
        handleStopCapture,
        handleGetVideoAnswer
    }));

    const handleStartCapture = useCallback(() => {
        setCapturing(true);
        // mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, {
        //     mimeType: "video/webm"
        // });

        const options = getCameraOptions();
        mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, options);

        mediaRecorderRef.current.addEventListener(
            "dataavailable",
            handleDataAvailable
        );
        mediaRecorderRef.current.start();
        handleStartAIRecognition();
        
    }, [webcamRef, setCapturing, mediaRecorderRef]);


    const handleStartAIRecognition = () => {

        setEmotionsArray([]);
        const referencia_video = webcamRef?.current?.video;

        let startTime = referencia_video.currentTime;
    
        const interval = setInterval(async () => {
            
            const currentTime = (referencia_video.currentTime - startTime) * 1000;

            // await faceapi.detectAllFaces
            const detections = await faceapi.detectSingleFace(
                referencia_video, 
                new faceapi.TinyFaceDetectorOptions({ 
                    inputSize: 512, //416, //320, 
                    scoreThreshold:0.1 
                }))
                .withFaceExpressions();
            // const detections = await faceapi.detectAllFaces(referencia_video, new faceapi.SsdMobilenetv1Options()).withFaceExpressions();
    
            // 'neutral' | 'happy' | 'sad' | 'angry' | 'fearful' | 'disgusted' | 'surprised'
            if(detections && detections.expressions) {
                // console.log(detections);
                setEmotionsArray((prevState) => [...prevState, {
                    time: currentTime,
                    emotions: detections.expressions,
                }]);
            }
    
        }, 1000);

        AIIntervalRef.current = interval ;
    }


    const getCameraOptions = () => {
        let options = null;

        if (typeof MediaRecorder.isTypeSupported == 'function') {
            /*
              MediaRecorder.isTypeSupported is a function announced in https://developers.google.com/web/updates/2016/01/mediarecorder and later introduced in the MediaRecorder API spec http://www.w3.org/TR/mediastream-recording/
            */
            if (MediaRecorder.isTypeSupported('video/webm;codecs=vp9')) {
                options = { mimeType: 'video/webm;codecs=vp9' };
            } else if (MediaRecorder.isTypeSupported('video/webm;codecs=h264')) {
                options = { mimeType: 'video/webm;codecs=h264' };
            } else if (MediaRecorder.isTypeSupported('video/webm')) {
                options = { mimeType: 'video/webm' };
            } else if (MediaRecorder.isTypeSupported('video/mp4')) {
                //Safari 14.0.2 has an EXPERIMENTAL version of MediaRecorder enabled by default
                containerType = "video/mp4";
                options = { mimeType: 'video/mp4' };
            }
            console.log('Using ' + options.mimeType);
        } else {
            console.log('isTypeSupported is not supported, using default codecs for browser');
            // mediaRecorder = new MediaRecorder(localStream);
        }

        return options;
    }


    const handleDataAvailable = useCallback(
        ({ data }) => {
            if (data.size > 0) {
                setRecordedChunks((prev) => prev.concat(data));
            }
        },
        [setRecordedChunks]
    );


    const handleStopCapture = useCallback(() => {
        
        mediaRecorderRef.current.stop();
        handleStopAIRecognition();

        setCapturing(false);
        
    }, [mediaRecorderRef, webcamRef, setCapturing]);



    const handleStopAIRecognition = () => {

        if (AIIntervalRef.current) clearInterval(AIIntervalRef.current);

    }


    const handleGetVideoAnswer = useCallback(async() => {
        if (recordedChunks.length) {

            const chunks_blob = new Blob(recordedChunks, {
                type: "video/webm"
            })
            
            const blob = await fixWebmDuration(chunks_blob);

            setRecordedChunks([]);
            // console.log(emotionsArray);

            const video_file =  new File(
                [blob],
                `respuesta_candidato`,
                {
                    type: "video/webm",
                    lastModified: new Date().getTime()
                }
            );

            // console.log(blob)
            // const url = URL.createObjectURL(blob);
            // const a = document.createElement("a");
            // document.body.appendChild(a);
            // a.style = "display: none";
            // a.href = url;
            // a.download = "react-webcam-stream-capture.webm";
            // a.click();
            // window.URL.revokeObjectURL(url);
            // setRecordedChunks([]);

            return {
                video_file,
                emotions: emotionsArray
            }
            
        } else {
            return null;
        }
    }, [recordedChunks, emotionsArray]);


    const handlePrepareAIRecognition = async () => {

        await faceapi.loadTinyFaceDetectorModel('/ai/models');
        await faceapi.loadFaceExpressionModel('/ai/models');
        
        // console.log(faceapi.nets);
        onCameraReady();
    
    }


    useEffect( () => {
        handlePrepareAIRecognition();
    }, [])

    return (
        <>
            <Webcam
                audio={true}
                muted={true}
                ref={webcamRef}
                videoConstraints={videoConstraints}
                mirrored={true}
                style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: '1rem', overflow: 'hidden' }}
            />
            {/* {capturing ? (
                <button onClick={handleStopCapture}>Stop Capture</button>
            ) : (
                <button onClick={handleStartCapture}>Start Capture</button>
            )}
            {recordedChunks.length > 0 && (
                <button onClick={handleGetVideoAnswer}>Download</button>
            )} */}
        </>
    );
}
);

export default Camera;