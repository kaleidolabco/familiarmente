import utils.database as db
import utils.api_responses as api_responses
import controllers.controller_archivos as controller_archivos
import controllers.controller_assessments as controller_assessments
import logging
from datetime import datetime
import math


# Valida si la pregunta existe. ***********************************
def validar_si_existe( id_pregunta ):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.preguntas 
        WHERE id = %s 
        AND eliminado=False
    """
    cursor.execute(query, ( id_pregunta, ))

    question = cursor.fetchall()

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)
    if question:
        return True
    return False


# Función para agregar un momento ***************************************************************************
def agregar_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

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

    query = """INSERT INTO assessments.preguntas  (
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
                eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    data = (
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

    query = "SELECT * FROM assessments.preguntas WHERE id = %s AND eliminado = False"
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


# Función para obtener los datos de una pregunta para candidatos. útil para no exponer la respuesta sugerida ***
def obtener_pregunta_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = """
        SELECT id, 
        pregunta, 
        texto_avatar, 
        duracion_maxima_de_respuesta, 
        id_parametro_tipo_avatar, 
        video_avatar_pregunta,
        id_avatar_virtual,
        nombre_avatar
        FROM assessments.preguntas 
        WHERE id = %s 
        AND eliminado = False
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



# Función para obtener la lista preguntas de un momento *************************************************
def obtener_preguntas_por_momento(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_momento = info["id_momento"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info.get("cantidad_por_pagina", 100)
    pagina = info.get("pagina", 1)

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los momentos de una competencia en un assessment
    query = """
        SELECT id, pregunta FROM assessments.preguntas 
        WHERE id_momento = %s 
        AND eliminado = False 
        ORDER BY fecha_de_registro ASC
        LIMIT %s OFFSET %s
    """
    data = (id_momento, limit, offset)

    cursor.execute(query, data)
    db_question = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM assessments.preguntas 
        WHERE id_momento = %s 
        AND eliminado = False
    """
    count_data = (id_momento,)

    cursor.execute(count_query, count_data)
    total_elements = cursor.fetchone()[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
        )
        print("*" * 100)

        if len(db_question) > 0:
            questions_list = []
            # Crear un diccionario con las llaves y valores
            for db_question in db_question:
                question = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_question[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    question[column] = value if (is_bool or is_none) else str(value)
                
                questions_list.append(question)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "preguntas": questions_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Preguntas obtenidas de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron preguntas configuradas", {"preguntas": []})


# Función para actualizar los datos de una pregunta ***************************************************************************
def actualizar_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")
    pregunta = info.get("pregunta")
    texto_avatar = info.get("texto_avatar")
    respuesta_sugerida = info.get("respuesta_sugerida")
    umbral_minimo_calificacion = info.get("umbral_minimo_calificacion")
    umbral_maximo_calificacion = info.get("umbral_maximo_calificacion")
    duracion_maxima_de_respuesta = info.get("duracion_maxima_de_respuesta")
    peso_calificacion_evaluador = info.get("peso_calificacion_evaluador")
    peso_calificacion_ia = info.get("peso_calificacion_ia")
    id_parametro_tipo_avatar = info.get("id_parametro_tipo_avatar")
    video_avatar_pregunta = info.get("video_avatar_pregunta")
    id_avatar_virtual = info.get("id_avatar_virtual")
    nombre_avatar = info.get("nombre_avatar")

    get_question = validar_si_existe( id )

    if get_question == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al actualizar la pregunta", 400, "La pregunta especificada no existe en la base de datos")

    query = """UPDATE assessments.preguntas SET
                pregunta = %s,
                texto_avatar = %s,
                respuesta_sugerida = %s,
                umbral_minimo_calificacion = %s,
                umbral_maximo_calificacion = %s,
                peso_calificacion_evaluador = %s,
                peso_calificacion_ia = %s,
                duracion_maxima_de_respuesta = %s,
                id_parametro_tipo_avatar = %s,
                video_avatar_pregunta = %s,
                id_avatar_virtual = %s,
                nombre_avatar = %s
                WHERE id = %s"""
    data = (
        pregunta,
        texto_avatar,
        respuesta_sugerida,
        umbral_minimo_calificacion,
        umbral_maximo_calificacion,
        peso_calificacion_evaluador,
        peso_calificacion_ia,
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
   

# Función para eliminar una pregunta de un momento *******************************************
def eliminar_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")

    get_question = validar_si_existe( id )

    if get_question == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al eliminar la pregunta", 400, "La pregunta especificada no existe en la base de datos")

    query = "UPDATE assessments.preguntas SET eliminado = True WHERE id = %s"

    cursor.execute(query, (id,))
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
        return api_responses.generate_response("La pregunta ha sido eliminada", {"id_pregunta": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar la pregunta", 400, "Error al actualizar en la base de datos")
 

# Función para obtener un enlace de subida de video de una pregunta
def obtener_url_subida_video_pregunta(info: dict):

    id_pregunta = info["id_pregunta"]
    id_assessment= info["id_assessment"]
    id_usuario_administrador = info["id_usuario_administrador"]
    tamano_archivo = info["tamano_archivo"]

    MAX_FILE_SIZE_MEGA_BYTES = 40
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MEGA_BYTES * 1024 * 1024  # 20 MB in bytes

    # valido si el archivo que se subirá excede el tamaño permitido
    if tamano_archivo > MAX_FILE_SIZE_BYTES:
        return api_responses.generate_error("Archivo demasiado pesado", 400, f'El archivo de video de la pregunta supera el límite de tamaño de {MAX_FILE_SIZE_MEGA_BYTES} MB')

    # Valido si la pregunta existe
    get_pregunta = validar_si_existe( id_pregunta )
    if get_pregunta == False:
        return api_responses.generate_error("Pregunta no encontrada", 400, "La pregunta especificada no existe en la base de datos")

    # Valido si el assessment existe
    get_assessment = controller_assessments.validar_si_existe_id_en_usuario( id_assessment, id_usuario_administrador )
    if get_assessment == False:
        return api_responses.generate_error("No cuentas con un assessment con los datos especificados", 400, "El assessment no existe en la base de datos")
    

    upload_data = controller_archivos.solicitar_url_de_subida_de_archivo(
        'video/mp4', 
        f'administradores/{id_usuario_administrador}/videos/assessments/{id_assessment}/preguntas/{id_pregunta}.mp4'
    )

    if upload_data != None:
        return api_responses.generate_response("Enlace de subida generado exitosamente", upload_data)
    else:
        return api_responses.generate_error("Error en la solicitud de subida de archivos", 400, "Ha ocurrido un error al obtener el enlace de subida del archivo")
   