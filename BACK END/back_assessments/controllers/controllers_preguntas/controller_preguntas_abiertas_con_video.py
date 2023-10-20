import utils.database as db
import utils.api_responses as api_responses
import controllers.controller_archivos as controller_archivos
import controllers.controller_assessments as controller_assessments
import logging
from datetime import datetime
import math


# Función para agregar una pregunta ***************************************************************************
def agregar_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_parametro_tipo_de_pregunta = info.get("id_parametro_tipo_de_pregunta")
    id_momento = info.get("id_momento")
    pregunta = info.get("pregunta", "¿? nueva pregunta")
    texto_avatar = info.get("texto_avatar", None)
    respuesta_sugerida = info.get("respuesta_sugerida", None)
    umbral_minimo_calificacion = info.get("umbral_minimo_calificacion", None)
    umbral_maximo_calificacion = info.get("umbral_maximo_calificacion", None)
    duracion_maxima_de_respuesta = info.get("duracion_maxima_de_respuesta", None)
    id_parametro_tipo_avatar = info.get("id_parametro_tipo_avatar", None)
    video_avatar_pregunta = info.get("video_avatar_pregunta", None)
    id_avatar_virtual = info.get("id_avatar_virtual", None)
    nombre_avatar = info.get("nombre_avatar", None)

    eliminado = False

    query = """INSERT INTO preguntas.preguntas_abiertas_con_video  (
                id_parametro_tipo_de_pregunta,
                id_momento,
                pregunta,
                texto_avatar,
                respuesta_sugerida,
                umbral_minimo_calificacion,
                umbral_maximo_calificacion,
                duracion_maxima_de_respuesta,
                id_parametro_tipo_avatar,
                video_avatar_pregunta,
                id_avatar_virtual,
                nombre_avatar,
                eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    data = (
        id_parametro_tipo_de_pregunta,
        id_momento, 
        pregunta,
        texto_avatar,
        respuesta_sugerida,
        umbral_minimo_calificacion,
        umbral_maximo_calificacion,
        duracion_maxima_de_respuesta,
        id_parametro_tipo_avatar,
        video_avatar_pregunta,
        id_avatar_virtual,
        nombre_avatar,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    pregunta = cursor.fetchone()
    id_pregunta = pregunta[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Pregunta agregada de manera exitosa!", {"id_pregunta": id_pregunta})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear la pregunta", 400, "Error al agregar en la base de datos")
    

# Función para obtener los datos de una pregunta **********************************************************
def obtener_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = """
        SELECT p.*, 
        par.nombre as nombre_tipo_de_pregunta, 
        par.descripcion as descripcion_tipo_de_pregunta
        FROM preguntas.preguntas_abiertas_con_video as p
        JOIN parametros par
        ON par.id = p.id_parametro_tipo_de_pregunta
        WHERE p.id = %s AND p.eliminado = False;
    """
    data = (id,)

    cursor.execute(query, data)
    db_question = cursor.fetchall()

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

        if len(db_question) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_question[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos de la pregunta obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos de la pregunta", 401, "No se han encontrado registros de la pregunta especificada")


# Función para obtener los datos de una pregunta para candidatos. útil para no exponer las respuestas ***
def obtener_pregunta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = """
        SELECT p.id, 
        p.pregunta, 
        p.texto_avatar, 
        p.duracion_maxima_de_respuesta, 
        p.id_parametro_tipo_avatar, 
        p.video_avatar_pregunta,
        p.id_avatar_virtual,
        p.nombre_avatar, 
        par.nombre as nombre_tipo_de_pregunta, 
        par.descripcion as descripcion_tipo_de_pregunta
        FROM preguntas.preguntas_abiertas_con_video as p
        JOIN parametros par
        ON par.id = p.id_parametro_tipo_de_pregunta
        WHERE p.id = %s AND p.eliminado = False;
    """
    data = (id,)

    cursor.execute(query, data)
    db_question = cursor.fetchall()

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

        if len(db_question) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_question[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos de la pregunta obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos de la pregunta", 401, "No se han encontrado registros de la pregunta especificada")


# Función para actualizar los datos de una pregunta ***************************************************************************
def actualizar_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")
    id_parametro_tipo_de_pregunta = info.get("id_parametro_tipo_de_pregunta")
    pregunta = info.get("pregunta")
    texto_avatar = info.get("texto_avatar")
    respuesta_sugerida = info.get("respuesta_sugerida")
    umbral_minimo_calificacion = info.get("umbral_minimo_calificacion")
    umbral_maximo_calificacion = info.get("umbral_maximo_calificacion")
    duracion_maxima_de_respuesta = info.get("duracion_maxima_de_respuesta")
    id_parametro_tipo_avatar = info.get("id_parametro_tipo_avatar")
    video_avatar_pregunta = info.get("video_avatar_pregunta")
    id_avatar_virtual = info.get("id_avatar_virtual")
    nombre_avatar = info.get("nombre_avatar")

    query = """UPDATE preguntas.preguntas_abiertas_con_video SET
                id_parametro_tipo_de_pregunta = %s,
                pregunta = %s,
                texto_avatar = %s,
                respuesta_sugerida = %s,
                umbral_minimo_calificacion = %s,
                umbral_maximo_calificacion = %s,
                duracion_maxima_de_respuesta = %s,
                id_parametro_tipo_avatar = %s,
                video_avatar_pregunta = %s,
                id_avatar_virtual = %s,
                nombre_avatar = %s
                WHERE id = %s"""
    data = (
        id_parametro_tipo_de_pregunta,
        pregunta,
        texto_avatar,
        respuesta_sugerida,
        umbral_minimo_calificacion,
        umbral_maximo_calificacion,
        duracion_maxima_de_respuesta,
        id_parametro_tipo_avatar,
        video_avatar_pregunta,
        id_avatar_virtual,
        nombre_avatar,
        id,
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Pregunta actualizada de manera exitosa!", {"id_pregunta": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar los datos de la pregunta", 400, "Error al actualizar en la base de datos")
   
