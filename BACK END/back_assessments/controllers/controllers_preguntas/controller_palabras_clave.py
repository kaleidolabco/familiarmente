import utils.database as db
import utils.api_responses as api_responses
import controllers.controller_archivos as controller_archivos
import controllers.controller_assessments as controller_assessments
import logging
from datetime import datetime
import math


# Valida si la palabra ya existe. ***********************************
def validar_si_existe( palabra, id_pregunta ):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM preguntas.palabras_clave 
        WHERE unaccent(lower(palabra)) LIKE unaccent(lower(%s)) 
        AND id_pregunta = %s
        AND eliminado=False
    """
    cursor.execute(query, ( palabra, id_pregunta))

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


# Función para agregar una palabra clave ***************************************************************************
def agregar_palabra_clave(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_pregunta = info.get("id_pregunta")
    palabra = info.get("palabra")

    eliminado = False

    exists = validar_si_existe(palabra, id_pregunta)

    if exists == True:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
        
        return api_responses.generate_error("Error al agregar la palabra clave", 400, "Ya existe esta palabra clave en la lista")


    query = """INSERT INTO preguntas.palabras_clave  (
                id_pregunta,
                palabra,
                eliminado) VALUES (%s,%s,%s) RETURNING id;"""
    data = (
        id_pregunta, 
        palabra,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    palabra_clave = cursor.fetchone()
    id_palabra_clave = palabra_clave[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("palabra clave agregada de manera exitosa!", {"id_palabra_clave": id_palabra_clave})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear la palabra clave", 400, "Error al agregar en la base de datos")
 


def eliminar_palabra_clave(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_palabra_clave = info["id_palabra_clave"]

    query = """UPDATE preguntas.palabras_clave
               SET eliminado = True
               WHERE id = %s
               RETURNING id_pregunta;"""
    data = (id_palabra_clave,)

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    id_pregunta = cursor.fetchone()[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Palabra clave eliminada exitosamente!", {"id_pregunta": id_pregunta})
    else:
        return api_responses.generate_error("Error al eliminar la palabra clave", 400, "Error al actualizar la base de datos")


# Función para obtener las palabras clave de una pregunta ***************************************************************************
def obtener_palabras_clave_de_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_pregunta = info["id_pregunta"]

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT id, palabra
        FROM preguntas.palabras_clave 
        WHERE id_pregunta = %s 
        AND eliminado = False 
        ORDER BY fecha_de_registro ASC
    """
    data = (id_pregunta,)

    cursor.execute(query, data)
    db_keywords = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) 
        FROM preguntas.palabras_clave 
        WHERE id_pregunta = %s 
        AND eliminado = False
    """
    count_data = (id_pregunta,)

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

        if len(db_keywords) > 0:
            keywords_list = []
            # Crear un diccionario con las llaves y valores
            for db_keyword in db_keywords:
                keyword = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_keyword[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    keyword[column] = value if (is_bool or is_none) else str(value)
                
                keywords_list.append(keyword)
            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "palabras_clave": keywords_list,
                "elementos_totales": total_elements
            }
            return api_responses.generate_response("Palabras clave obtenidas de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron palabras clave en esta pregunta", {"palabras_clave": []})
