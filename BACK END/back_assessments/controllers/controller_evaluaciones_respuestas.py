import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import json

import controllers.controller_ia as controller_ia
import controllers.controllers_preguntas.controller_palabras_clave as controller_palabras_clave
import controllers.controllers_preguntas.controller_descarriladores as controller_descarriladores

# Valida si la respuesta del usuario existe. ***********************************
def validar_si_existe( id_respuesta_candidato: str ):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM respuestas.evaluaciones_respuestas 
        WHERE id_respuesta_candidato = %s 
        AND eliminado=False
    """
    cursor.execute(query, ( id_respuesta_candidato, ))

    evaluation = cursor.fetchall()

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)
    if evaluation:
        return True
    return False


# Función para agregar una evaluación ***************************************************************************
def agregar_evaluacion_respuesta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_respuesta_candidato = info.get("id_respuesta_candidato", None)
    calificacion_del_evaluador = info.get("calificacion_del_evaluador", None)
    observaciones_del_evaluador = info.get("observaciones_del_evaluador", None)
    promedio_de_calificacion = info.get("promedio_de_calificacion", None)
    porcentaje_calificacion_ia  = info.get("porcentaje_calificacion_ia", None)
    porcentaje_calificacion_evaluador  = info.get("porcentaje_calificacion_evaluador", None)

    eliminado = False

    exists = validar_si_existe(id_respuesta_candidato)

    if exists:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
        
        # Si no hay respuesta usuario actualizo el dato para subir el video
        # if exists["data"]["video_respuesta_usuario"] == None:         
        #     return actualizar_respuesta_candidato(info)

        return api_responses.generate_error("Error al agregar la calificación", 400, "Ya existe una calificación agregada a esta pregunta")

    query = """INSERT INTO respuestas.evaluaciones_respuestas  (
                id_respuesta_candidato,
                calificacion_del_evaluador,
                observaciones_del_evaluador,
                promedio_de_calificacion,
                porcentaje_calificacion_ia,
                porcentaje_calificacion_evaluador,
                eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    data = (
        id_respuesta_candidato,
        calificacion_del_evaluador,
        observaciones_del_evaluador,
        promedio_de_calificacion,
        porcentaje_calificacion_ia,
        porcentaje_calificacion_evaluador,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    respuesta_candidato = cursor.fetchone()
    id_evaluacion_respuesta = respuesta_candidato[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        agregar_transcripcion = controller_ia.transcribir_respuesta_candidato({"id_respuesta_candidato":id_respuesta_candidato})

        if agregar_transcripcion["success"] == False:
            update_evaluation = actualizar_evaluacion_respuesta_ia({
                "id_respuesta_candidato": id_respuesta_candidato,
                "transcripcion_respuesta": "Lo sentimos, no se ha podido obtener la transcripción de esta respuesta"
            })

        proceso_emociones = procesar_emociones_respuesta(id_respuesta_candidato)
            
        return api_responses.generate_response("Evaluación agregada de manera exitosa!", {"id_evaluacion_respuesta": id_evaluacion_respuesta})
    else:
        return api_responses.generate_error("Ha ocurrido un error al agregar la calificación", 400, "Error al agregar en la base de datos")
    

# Función para obtener y guardar las emociones de la respuesta del candidato
def procesar_emociones_respuesta (id_respuesta_candidato) :
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """
        SELECT data_emociones FROM respuestas.respuestas 
        WHERE id = %s 
        AND eliminado = False
    """
    data = (id_respuesta_candidato, )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    if result == 1:
        consulta_emociones = cursor.fetchone()
        emociones = consulta_emociones[0]

        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        if emociones and len(emociones) > 0:
            
            # Si hay valores nulos no sumarán al total de emociones
            emociones_validas = 0

            # Inicializar diccionario para almacenar las sumas de cada emoción
            total_emotions = {
                "neutral": 0,
                "happy": 0,
                "sad": 0,
                "angry": 0,
                "fearful": 0,
                "disgusted": 0,
                "surprised": 0
            }

            # Para cada elemento del arreglo acumulo la suma de porcentajes de emociones
            for saved_data in emociones:

                if saved_data and saved_data is not None:
                    emociones_validas += 1

                    expressions = saved_data.get("emotions", None)
                    for emotion, value in expressions.items():
                        total_emotions[emotion] += value

            if emociones_validas == 0 :
                return None

            # Calcular el porcentaje total de cada emoción y encontrar la emoción con el mayor porcentaje
            max_emotion = None
            max_percentage = 0
            percent_emotions = {
                "neutral": 0,
                "happy": 0,
                "sad": 0,
                "angry": 0,
                "fearful": 0,
                "disgusted": 0,
                "surprised": 0
            }

            for emotion, total_value in total_emotions.items():
                percentage = (total_value / emociones_validas) * 100
                percent_emotions[emotion] = percentage
                # print(f"{emotion}: {percentage:.2f}%")
                
                if percentage > max_percentage:
                    max_emotion = emotion
                    max_percentage = percentage

            final_emotions_data = {
                "emociones_vs_tiempo": emociones,
                "porcentajes_emociones": percent_emotions,
                "emocion_prevalente":{
                    "emocion": max_emotion,
                    "porcentaje": max_percentage
                }
            }


            actualizacion_datos = actualizar_evaluacion_respuesta_ia({
                "id_respuesta_candidato": id_respuesta_candidato,
                "emocion_prevalente": max_emotion,
                "data_emociones": json.dumps(final_emotions_data),
            })

            # print('-'*1000)
            # print (actualizacion_datos)

            if actualizacion_datos['success'] == True:
                return actualizacion_datos
            else: 
                return None

    else:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
        return None


# Función para obtener una evaluación  **********************************************************
def obtener_evaluacion_respuesta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_respuesta_candidato = info.get("id_respuesta_candidato", None)

    exists = validar_si_existe(id_respuesta_candidato)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al obtener los datos de la evaluación", 400, "Aún no se ha registrado un proceso de evaluación para la respuesta especificada")


    query = """
        SELECT * FROM respuestas.evaluaciones_respuestas 
        WHERE id_respuesta_candidato = %s 
        AND eliminado = False
    """
    data = (id_respuesta_candidato, )

    cursor.execute(query, data)
    db_evaluation = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
        )
        print("*" * 100)

        if len(db_evaluation) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_evaluation[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos de la evaluación obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos de la evaluación del usuario", 401, "No se han encontrado registros de la evaluación especificada")


# Función para obtener los datos de una evaluación  **********************************************************
def obtener_datos_evaluacion_respuesta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_respuesta_candidato = info.get("id_respuesta_candidato", None)

    exists = validar_si_existe(id_respuesta_candidato)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al obtener los datos de la evaluación", 400, "Aún no se ha registrado un proceso de evaluación para la respuesta especificada")


    query = """
        SELECT evaluacion.*, 
        pregunta.respuesta_sugerida,
        pregunta.umbral_minimo_calificacion,
        pregunta.umbral_maximo_calificacion,
        pregunta.calificacion_con_ia,
        pregunta.pregunta,
        pregunta.id AS id_pregunta
        FROM respuestas.evaluaciones_respuestas AS evaluacion
        JOIN respuestas.respuestas AS respuesta
        ON respuesta.id = evaluacion.id_respuesta_candidato
        JOIN assessments.preguntas AS pregunta
        ON respuesta.id_pregunta = pregunta.id
        WHERE evaluacion.id_respuesta_candidato = %s 
        AND evaluacion.eliminado = False
    """
    data = (id_respuesta_candidato, )

    cursor.execute(query, data)
    db_evaluation = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
        )
        print("*" * 100)

        if len(db_evaluation) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_evaluation[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex, list, dict))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)


            # Obtengo los datos de palabras clave y descarriladores para agregarlos en la consulta***************
            id_pregunta = data.get("id_pregunta", None)
            palabras_clave = []
            descarriladores = []

            if id_pregunta != None:
                # CONSULTA PALABRAS CLAVE
                palabras_clave_request = controller_palabras_clave.obtener_palabras_clave_de_pregunta({"id_pregunta":id_pregunta})
                keywords_list = palabras_clave_request.get("data").get("palabras_clave")
                if palabras_clave_request.get("success") == True and keywords_list:
                    palabras_clave = keywords_list

                # CONSULTA DESCARRILADORES
                descarriladores_request = controller_descarriladores.obtener_descarriladores_de_pregunta({"id_pregunta":id_pregunta})
                derailers_list = descarriladores_request.get("data").get("descarriladores")
                if palabras_clave_request.get("success") == True and derailers_list:
                    descarriladores = derailers_list


            data["palabras_clave"] = palabras_clave
            data["descarriladores"] = descarriladores

            return api_responses.generate_response("Datos de la evaluación obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos de la evaluación del usuario", 401, "No se han encontrado registros de la evaluación especificada")


# Función para actualizar los datos de una evaluación ***************************************************************************
def actualizar_evaluacion_respuesta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_respuesta_candidato = info.get("id_respuesta_candidato", None)

    exists = validar_si_existe(id_respuesta_candidato)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return agregar_evaluacion_respuesta(info)
        # return api_responses.generate_error("Error al actualizar los datos de la evaluación", 400, "Aún no se ha registrado un proceso de evaluación para la respuesta especificada")

    # Create a list to store the non-null data and the corresponding placeholders
    update_data = []
    placeholders = []

    parameters_to_check = [
        "calificacion_del_evaluador",
        "observaciones_del_evaluador",
        "promedio_de_calificacion",
        "porcentaje_calificacion_ia",
        "porcentaje_calificacion_evaluador"
    ]

    for parameter in parameters_to_check:
        value = info.get(parameter)
        if value is not None:
            update_data.append(value)
            placeholders.append(f"{parameter} = %s")

    if not update_data:
        return api_responses.generate_response("No hay datos para actualizar", {"id_respuesta_candidato": id_respuesta_candidato})

    placeholders_str = ", ".join(placeholders)

    query = f"""UPDATE respuestas.evaluaciones_respuestas SET
                {placeholders_str}
                WHERE id_respuesta_candidato = %s
                RETURNING id;"""
    data = tuple(update_data + [id_respuesta_candidato])

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    respuesta_candidato = cursor.fetchone()
    id_evaluacion_respuesta = respuesta_candidato[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Evaluación actualizada de manera exitosa!", {"id_evaluacion_respuesta": id_evaluacion_respuesta})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar la evaluación", 400, "Error al actualizar en la base de datos")


# Función para actualizar los datos de una evaluación internamente ***************************************
def actualizar_evaluacion_respuesta_ia(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_respuesta_candidato = info.get("id_respuesta_candidato", None)

    exists = validar_si_existe(id_respuesta_candidato)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar los datos de la evaluación", 400, "Aún no se ha registrado un proceso de evaluación para la respuesta especificada")

    update_data = []
    placeholders = []

    parameters_to_check = [
        "calificacion_del_evaluador",
        "observaciones_del_evaluador",
        "calificacion_de_ia",
        "observaciones_de_ia",
        "porcentaje_coincidencia_con_respuesta_correcta",
        "promedio_de_calificacion",
        "porcentaje_calificacion_ia",
        "porcentaje_calificacion_evaluador",
        "transcripcion_respuesta",
        "emocion_prevalente",
        "data_emociones",
        "respuesta_ia",
    ]

    for parameter in parameters_to_check:
        value = info.get(parameter)
        if value is not None:
            update_data.append(value)
            placeholders.append(f"{parameter} = %s")

    if not update_data:
        return api_responses.generate_response("No hay datos para actualizar", {"id_respuesta_candidato": id_respuesta_candidato})

    placeholders_str = ", ".join(placeholders)
    query = f"""UPDATE respuestas.evaluaciones_respuestas SET
                {placeholders_str}
                WHERE id_respuesta_candidato = %s
                RETURNING id;"""
    data = tuple(update_data + [id_respuesta_candidato])

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    evaluacion_respuesta = cursor.fetchone()
    id_evaluacion_respuesta = evaluacion_respuesta[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Evaluación actualizada de manera exitosa!", {"id_evaluacion_respuesta": id_evaluacion_respuesta})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar la evaluación", 400, "Error al actualizar en la base de datos")
