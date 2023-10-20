import utils.database as db
import utils.api_responses as api_responses
import controllers.controller_archivos as controller_archivos
import controllers.controller_preguntas as controller_preguntas
import logging
from datetime import datetime
import math
import json


# Valida si la respuesta del usuario existe. ***********************************
def validar_si_existe( id_usuario_candidato, id_pregunta ):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM respuestas.respuestas
        WHERE id_usuario_candidato = %s 
        AND id_pregunta = %s
        AND eliminado=False
    """
    cursor.execute(query, ( id_usuario_candidato, id_pregunta ))

    answer = cursor.fetchall()

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)
    if answer:
        return True
    return False


# Función para agregar un momento ***************************************************************************
def agregar_respuesta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato", None)
    id_pregunta = info.get("id_pregunta", None)
    video_respuesta_usuario = info.get("video_respuesta_usuario", None)
    data_emociones = info.get("data_emociones", None)

    # Convertir el diccionario data_emociones a una cadena JSON
    data_emociones_json = json.dumps(data_emociones)

    eliminado = False

    exists = obtener_respuesta_candidato(info)

    if exists["success"] == True:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
        
        # Si no hay respuesta usuario actualizo el dato para subir el video
        if exists["data"]["video_respuesta_usuario"] == None:         
            return actualizar_respuesta_candidato(info)

        return api_responses.generate_error("Error al enviar la respuesta", 400, "Ya tienes una respuesta agregada a esta pregunta")


    query = """INSERT INTO respuestas.respuestas (
                id_usuario_candidato,
                id_pregunta,
                video_respuesta_usuario,
                data_emociones,
                eliminado) VALUES (%s,%s,%s,%s,%s) RETURNING id;"""
    data = (
        id_usuario_candidato,
        id_pregunta,
        video_respuesta_usuario,
        data_emociones_json,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    respuesta_candidato = cursor.fetchone()
    id_respuesta_candidato = respuesta_candidato[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Respuesta enviada de manera exitosa!", {"id_respuesta_candidato": id_respuesta_candidato})
    else:
        return api_responses.generate_error("Ha ocurrido un error al enviar la respuesta a la pregunta", 400, "Error al agregar en la base de datos")


# Función para obtener los datos de una respuesta  **********************************************************
def obtener_respuesta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato", None)
    id_pregunta = info.get("id_pregunta", None)

    exists = validar_si_existe(id_usuario_candidato, id_pregunta)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al obtener los datos de la respuesta", 400, "El usuario aún no ha agregado una respuesta la pregunta especificada")


    query = """
        SELECT * FROM respuestas.respuestas
        WHERE id_usuario_candidato = %s 
        AND id_pregunta = %s
        AND eliminado = False
    """
    data = (id_usuario_candidato, id_pregunta)

    cursor.execute(query, data)
    deb_answer = cursor.fetchall()

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

        if len(deb_answer) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = deb_answer[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos de la respuesta obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos de la respuesta del usuario", 401, "No se han encontrado registros de la respuesta especificada")


# Función para actualizar los datos de una respuesta ***************************************************************************
def actualizar_respuesta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato", None)
    id_pregunta = info.get("id_pregunta", None)
    video_respuesta_usuario = info.get("video_respuesta_usuario", None)
    data_emociones = info.get("data_emociones", None)

    data_emociones_json = json.dumps(data_emociones)

    exists = validar_si_existe(id_usuario_candidato, id_pregunta)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar los datos de la respuesta", 400, "El usuario aún no ha agregado una respuesta la pregunta especificada")

    query = """UPDATE respuestas.respuestas SET
                video_respuesta_usuario = %s,
                data_emociones = %s
                WHERE id_usuario_candidato = %s
                AND id_pregunta= %s
                RETURNING id;"""
    data = (
        video_respuesta_usuario,
        data_emociones_json,
        id_usuario_candidato,
        id_pregunta,
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    respuesta_candidato = cursor.fetchone()
    id_respuesta_candidato = respuesta_candidato[0]


    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Respuesta del candidato actualizada de manera exitosa!", {"id_respuesta_candidato": id_respuesta_candidato})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar la respuesta del candidato", 400, "Error al actualizar en la base de datos")


# Función para eliminar los datos de una respuesta ***************************************************************************
def Eliminar_respuesta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato", None)
    id_pregunta = info.get("id_pregunta", None)

    exists = validar_si_existe(id_usuario_candidato, id_pregunta)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al intentar eliminar la respuesta del candidato", 400, "El usuario aún no ha agregado una respuesta la pregunta especificada")

    query = """UPDATE respuestas.respuestas SET
                eliminado = True
                WHERE id_usuario_candidato = %s
                AND id_pregunta= %s
                RETURNING id;"""
    data = (
        id_usuario_candidato,
        id_pregunta,
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    respuesta_candidato = cursor.fetchone()
    id_respuesta_candidato = respuesta_candidato[0]


    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Respuesta del candidato eliminada de manera exitosa!", {"id_respuesta_candidato": id_respuesta_candidato})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar la respuesta del candidato", 400, "Error al actualizar en la base de datos")


# Función para obtener un enlace de subida de video de una pregunta
def obtener_url_subida_video_respuesta_candidato(info: dict):

    id_usuario_candidato= info["id_usuario_candidato"]
    id_pregunta = info["id_pregunta"]
    id_assessment= info["id_assessment"]
    tamano_archivo = info["tamano_archivo"]

    # Valido primero si ya existe una respuesta subida
    exists = obtener_respuesta_candidato(info)

    if exists["success"] == True:
        # Valido que no haya un video ya subido en la respuesta
        if exists["data"]["video_respuesta_usuario"] != None:         
            return api_responses.generate_error("Error al enviar la respuesta", 400, "Ya tienes una respuesta agregada a esta pregunta")



    MAX_FILE_SIZE_MEGA_BYTES = 100
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MEGA_BYTES * 1024 * 1024  # 20 MB in bytes

    # valido si el archivo que se subirá excede el tamaño permitido
    if tamano_archivo > MAX_FILE_SIZE_BYTES:
        return api_responses.generate_error("Archivo demasiado pesado", 400, f'El archivo de video de la respuesta supera el límite de tamaño de {MAX_FILE_SIZE_MEGA_BYTES} MB')

    # Valido si la pregunta existe
    get_pregunta = controller_preguntas.validar_si_existe( id_pregunta )
    if get_pregunta == False:
        return api_responses.generate_error("Pregunta no encontrada", 400, "La pregunta especificada no existe en la base de datos")

    upload_data = controller_archivos.solicitar_url_de_subida_de_archivo(
        'video/webm', 
        f'candidatos/{id_usuario_candidato}/videos/respuestas_assessments/{id_assessment}/preguntas/{id_pregunta}.webm'
    )

    if upload_data != None:
        return api_responses.generate_response("Enlace de subida generado exitosamente", upload_data)
    else:
        return api_responses.generate_error("Error en la solicitud de subida de archivos", 400, "Ha ocurrido un error al obtener el enlace de subida del archivo")
 


# Función para obtener el video de una respuesta dada
def obtener_video_respuesta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_respuesta_candidato = info.get("id_respuesta_candidato", None)

    query = """
        SELECT video_respuesta_usuario 
        FROM respuestas.respuestas 
        WHERE id = %s 
        AND eliminado = False
    """
    data = (id_respuesta_candidato, )

    cursor.execute(query, data)
    deb_answer = cursor.fetchone()

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
        )
        print("*" * 100)

        if len(deb_answer) > 0:
            return deb_answer[0]
        
        else:
            return None

  