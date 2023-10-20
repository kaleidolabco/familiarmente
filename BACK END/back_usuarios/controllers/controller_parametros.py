import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math

# Función para obtener la lista de parametros por nombre del tipo *********************************************************************
def obtener_parametros_por_nombre(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    nombre_tipo_parametro = info["nombre_tipo_parametro"]

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT id, nombre, descripcion FROM parametros 
        WHERE id_tipo_parametro = 
        (SELECT id from tipos_parametros WHERE lower(nombre) = lower(%s) )
        AND eliminado = False
    """
    data = (nombre_tipo_parametro, )

    cursor.execute(query, data)
    db_parameters = cursor.fetchall()

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

        if len(db_parameters) > 0:
            parameters_list = []
            # Crear un diccionario con las llaves y valores
            for deb_parameter in db_parameters:
                job = {}
                for j, column in enumerate(column_names):
                    job[column] = str(deb_parameter[j])
                
                parameters_list.append(job)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "parametros": parameters_list
            }
            return api_responses.generate_response("Parámetros obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron parámetros", {"parametros": []})

# Función para obtener la información de un parámetro************************************************
def obtener_parametro(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = """
        SELECT * FROM parametros 
        WHERE id = %s 
        AND eliminado = False
    """
    data = (id,)

    cursor.execute(query, data)
    db_parameter = cursor.fetchall()

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

        if len(db_parameter) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_parameter[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos del parámetro obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos del parámetro", 401, "No se han encontrado registros del parámetro especificado")
