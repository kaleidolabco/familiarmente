import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime


# Valida si la palabra ya existe. ***********************************
def validar_si_existe( descarrilador, id_pregunta ):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM preguntas.descarriladores 
        WHERE unaccent(lower(descarrilador)) LIKE unaccent(lower(%s)) 
        AND id_pregunta = %s
        AND eliminado=False
    """
    cursor.execute(query, ( descarrilador, id_pregunta))

    derailers = cursor.fetchall()

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)
    if derailers:
        return True
    return False


# Función para agregar un descarrilador ***************************************************************************
def agregar_descarrilador(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_pregunta = info.get("id_pregunta")
    descarrilador = info.get("descarrilador")

    eliminado = False

    exists = validar_si_existe(descarrilador, id_pregunta)

    if exists == True:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
        
        return api_responses.generate_error("Error al agregar el descarrilador", 400, "Ya existe este descarrilador en la lista")


    query = """INSERT INTO preguntas.descarriladores  (
                id_pregunta,
                descarrilador,
                eliminado) VALUES (%s,%s,%s) RETURNING id;"""
    data = (
        id_pregunta, 
        descarrilador,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    descarrilador = cursor.fetchone()
    id_descarrilador = descarrilador[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Descarrilador agregado de manera exitosa!", {"id_descarrilador": id_descarrilador})
    else:
        return api_responses.generate_error("Ha ocurrido un error al agregar el descarrilador", 400, "Error al agregar en la base de datos")
 

# Función para eliminar un descarrilador
def eliminar_descarrilador(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_descarrilador = info["id_descarrilador"]

    query = """UPDATE preguntas.descarriladores
               SET eliminado = True
               WHERE id = %s
               RETURNING id_pregunta;"""
    data = (id_descarrilador,)

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
        return api_responses.generate_response("Descarrilador eliminado exitosamente!", {"id_pregunta": id_pregunta})
    else:
        return api_responses.generate_error("Error al eliminar el descarrilador", 400, "Error al actualizar la base de datos")


# Función para obtener los descarriladores de una pregunta ***************************************************************************
def obtener_descarriladores_de_pregunta(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_pregunta = info["id_pregunta"]

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT id, descarrilador
        FROM preguntas.descarriladores 
        WHERE id_pregunta = %s 
        AND eliminado = False 
        ORDER BY fecha_de_registro ASC
    """
    data = (id_pregunta,)

    cursor.execute(query, data)
    db_derailers = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) 
        FROM preguntas.descarriladores 
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

        if len(db_derailers) > 0:
            derailers_list = []
            # Crear un diccionario con las llaves y valores
            for db_derailer in db_derailers:
                derailer = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_derailer[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    derailer[column] = value if (is_bool or is_none) else str(value)
                
                derailers_list.append(derailer)
            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "descarriladores": derailers_list,
                "elementos_totales": total_elements
            }
            return api_responses.generate_response("Descarriladores obtenidas de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron descarriladores en esta pregunta", {"descarriladores": []})
