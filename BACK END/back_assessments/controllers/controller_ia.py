import logging
import json
import openai
import requests
import os
import utils.constants as constants
import utils.api_responses as api_responses

import controllers.controller_respuestas_candidatos as controller_respuestas_candidatos
import controllers.controller_evaluaciones_respuestas as controller_evaluaciones_respuestas

openai.api_key = constants.OPENAI_API_KEY

# Función para generar la transcripción de la respuesta de un usuario
def transcribir_respuesta_candidato(info: dict):

    id_respuesta_candidato = info["id_respuesta_candidato"]

    respuesta_candidato = controller_respuestas_candidatos.obtener_video_respuesta_candidato(info)

    if respuesta_candidato == None or respuesta_candidato == "":
        return api_responses.generate_error("Error al obtener el video de la respuesta", 400, "Aún no existe un registro de video para la respuesta especificada")

    # video_path_name = "video.webm"
    video_path_name = "/tmp/video.webm"

    response = requests.get(respuesta_candidato)

    with open(video_path_name, mode="wb") as file:
        file.write(response.content)

    audio_file = open(video_path_name, "rb")

    try: 
        transcript = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file,
            response_format="text",
            language="es"
        )
    except Exception as exception:

        print("*" * 100)
        logging.error(
            {
                "code": 400,
                "error": f"Error: {exception}. Contacta con el administrador"
            }
        )
        print("*" * 100)

        audio_file.close()  # Cierra el archivo de audio antes de eliminarlo
        os.remove(video_path_name)

        return api_responses.generate_error(
            "Error al procesar la respuesta del candidato",
            400,
            f"Error: {exception}. Contacta con el administrador"
        )


    audio_file.close()  # Cierra el archivo de audio antes de eliminarlo
    os.remove(video_path_name)

    update_evaluation = controller_evaluaciones_respuestas.actualizar_evaluacion_respuesta_ia({
        "id_respuesta_candidato": id_respuesta_candidato,
        "transcripcion_respuesta": transcript
    })

    return api_responses.generate_response("¡Transcripción generada con éxito!", {"transcripcion": transcript, "actualizacion": update_evaluation})


# FUnción para obtener la respuesta a una pregunta generada por IA
def obtener_respuesta_de_la_ia(info: dict):

    pregunta = info["pregunta"]
    prompt = f"Ponte en el rol de un headhunter. Te presentaré una pregunta o situación problema que se le presentará a un entrevistado y desde tu rol de hedhunter necesito que me brindes una respuesta que consideres correcta y acertada. Preferiblemente debe ser una respuesta corta y clara. La pregunta es: {pregunta}"
    model = "gpt-3.5-turbo"
    
    try:
        # completion = openai.ChatCompletion.create(
        #     model=model,
        #     messages=[
        #         {"role": "system", "content": "Eres un headhunter"},
        #         {"role": "user", "content": prompt}
        #     ]
        # )

        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.3,
        )

        # print(completion.choices[0].message)
        answer = completion.choices[0].text.lstrip()
        return api_responses.generate_response("¡Respuesta obtenida con éxito!", {"respuesta": answer })
    
    except Exception as exception:
        print("error gpt: {exception}")
        logging.error(
            "Ha ocurrido un error al obtener la respuesta de la IA",
            f", revisa {exception}"
        )
        return api_responses.generate_error("Ha ocurrido un error al obtener la respuesta de la IA", 400, "")


# Función para obtener la calificación de la IA
def obtener_calificacion_de_la_ia(info: dict):

    id_respuesta_candidato = info["id_respuesta_candidato"]

    #Busco los datos de la respuesta del usuario
    datos_evaluacion = controller_evaluaciones_respuestas.obtener_datos_evaluacion_respuesta(info)

    if datos_evaluacion["success"] == True:

        data = datos_evaluacion["data"]
        pregunta = data["pregunta"]
        respuesta_correcta = data["respuesta_sugerida"]
        respuesta_candidato = data["transcripcion_respuesta"]
        umbral_minimo_calificacion = data["umbral_minimo_calificacion"]
        umbral_maximo_calificacion = data["umbral_maximo_calificacion"]

        prompt = f""" 
            A un candidato postulante a un cargo se le presentó la pregunta: {pregunta}.
            La respuesta del candidato fué: {respuesta_candidato}.
            La respuesta establecida como correcta para la pregunta es: {respuesta_correcta}.

            Ponte en el rol de un evaluador de una entrevista para candidatos a un cargo.
            Necesito que como evaluador me brindes una calificación de {umbral_minimo_calificacion} a {umbral_maximo_calificacion}
            de la respuesta del entrevistado con relación a la respuesta establecida como correcta para la pregunta, 
            siendo {umbral_minimo_calificacion} la calificación para una respuesta totalmente incorrecta y {umbral_maximo_calificacion} para una respuesta acertada.
            Sé estricto con la calificación.

            Además, quisiera que me brindes un porcentaje de similitud entre la respuesta del candidato y la respuesta establecida como correcta para la pregunta. Sólo necesito el valor numérico del porcentaje sin el simbolo %.

            Quiero la respuesta en formato JSON con la siguiente estructura:
            {{'calificacion': 'CALIFICACIÓN DE SIMILITUD ENTRE LA RESPUESTA CORRECTA E INCORRECTA', 'observaciones': 'TEXTO CORTO QUE EXPLICA LA RAZÓN POR LA CUAL LA RESPUESTA DEL USUARIO SE CONSIDERA CORRECTA O INCORRECTA', 'similitud': 'PORCENTAJE DE SIMILITUD ENTRE LAS RESPUESTAS'}}
        """
    
        try:
            # completion = openai.ChatCompletion.create(
            #     model=model,
            #     messages=[
            #         {"role": "system", "content": "Eres un headhunter"},
            #         {"role": "user", "content": prompt}
            #     ]
            # )

            completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.3,
            )

            # print(completion.choices[0].message)
            calification = completion.choices[0].text.lstrip()
            json_acceptable_string = calification.replace("'", "\"")
            json_qualification = json.loads(json_acceptable_string)
            

            update_evaluation = controller_evaluaciones_respuestas.actualizar_evaluacion_respuesta_ia({
                "id_respuesta_candidato": id_respuesta_candidato,
                "calificacion_de_ia": json_qualification.get("calificacion"),
                "observaciones_de_ia": json_qualification.get("observaciones"),
                "porcentaje_coincidencia_con_respuesta_correcta": json_qualification.get("similitud")
            })

            return api_responses.generate_response("¡Calificación de la IA obtenida con éxito!", {"calificacion_ia": json_qualification })
        
        except Exception as exception:
            print("error gpt: {exception}")
            logging.error(
                "Ha ocurrido un error al obtener la calificación de la IA",
                f", revisa {exception}"
            )
            return api_responses.generate_error("Ha ocurrido un error al obtener la calificación de la IA", 400, "")
    else:
        return api_responses.generate_error("Ha ocurrido un error al obtener la calificación de la IA", 400, "No se han encontrado datos de evaluación")




