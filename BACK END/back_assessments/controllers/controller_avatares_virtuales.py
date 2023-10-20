import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math

# Función para obtener la lista de avatares virtuales disponibles ***************************************************************************
def obtener_avatares_virtuales(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT * FROM assessments.avatares_virtuales 
        WHERE eliminado = False 
    """

    cursor.execute(query)
    db_avatares = cursor.fetchall()

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

        if len(db_avatares) > 0:
            avatars_list = []
            # Crear un diccionario con las llaves y valores
            for db_avatar in db_avatares:
                avatar = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_avatar[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    avatar[column] = value if (is_bool or is_none) else str(value)
                
                avatars_list.append(avatar)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "avatares": avatars_list,
            }
            return api_responses.generate_response("Avatares obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron avatares creados", {"avatares": []})

# Función para obtener la información de un avatar ***************************************************************************
def obtener_avatar_virtual(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = """
        SELECT * FROM assessments.avatares_virtuales 
        WHERE id = %s 
        AND eliminado = False
    """
    data = (id,)

    cursor.execute(query, data)
    db_avatar_virtual = cursor.fetchall()

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

        if len(db_avatar_virtual) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_avatar_virtual[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Información del avatar virtual obtenida de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener la información del avatar virtual", 401, "No se han encontrado registros del avatar especificado")
