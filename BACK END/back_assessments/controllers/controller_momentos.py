import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math


# Valida si el momento ya existe. ***********************************
def validar_si_existe( id_momento ):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.momentos 
        WHERE id = %s 
        AND eliminado=False
    """
    cursor.execute(query, ( id_momento, ))

    user = cursor.fetchall()

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)
    if user:
        return True
    return False


# Función para agregar un momento ***************************************************************************
def agregar_momento(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    nombre = info.get("nombre")
    descripcion = info.get("descripcion")
    id_competencia_assessment = info.get("id_competencia_assessment")

    eliminado = False

    query = """INSERT INTO assessments.momentos (
                nombre,
                descripcion,
                id_competencia_assessment,
                eliminado) VALUES (%s,%s,%s,%s) RETURNING id;"""
    data = (
        nombre, 
        descripcion,
        id_competencia_assessment,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    momento = cursor.fetchone()
    id_momento = momento[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Momento Agregado de manera exitosa!", {"id_momento": id_momento})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear el momento", 400, "Error al agregar en la base de datos")
    

# Función para obtener los datos de un momento **********************************************************
def obtener_momento(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = "SELECT * FROM assessments.momentos WHERE id = %s AND eliminado = False"
    data = (id,)

    cursor.execute(query, data)
    db_moment = cursor.fetchall()

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

        if len(db_moment) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_moment[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Momento obtenido de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener el momento", 401, "No se han encontrado registros de la competencia especificada")


# Función para obtener la lista de momentos de una competencia *************************************************
def obtener_momentos_por_competencia(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_competencia_assessment = info["id_competencia_assessment"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info.get("cantidad_por_pagina", 100)
    pagina = info.get("pagina", 1)

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los momentos de una competencia en un assessment
    query = """
        SELECT id, nombre FROM assessments.momentos 
        WHERE id_competencia_assessment = %s 
        AND eliminado = False 
        ORDER BY fecha_de_registro ASC
        LIMIT %s OFFSET %s
    """
    data = (id_competencia_assessment, limit, offset)

    cursor.execute(query, data)
    db_moments = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM assessments.momentos 
        WHERE id_competencia_assessment = %s 
        AND eliminado = False
    """
    count_data = (id_competencia_assessment,)

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

        if len(db_moments) > 0:
            moments_list = []
            # Crear un diccionario con las llaves y valores
            for db_moment in db_moments:
                moment = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_moment[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    moment[column] = value if (is_bool or is_none) else str(value)
                
                moments_list.append(moment)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "momentos": moments_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Momentos obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron momentos configurados para esta competencia", {"momentos": []})


# Función para actualizar un momento ***************************************************************************
def actualizar_momento(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")
    nombre = info.get("nombre")
    descripcion = info.get("descripcion")

    get_moment = validar_si_existe( id )

    if get_moment == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al actualizar el momento", 400, "El momento especificado no existe en la base de datos")

    query = """UPDATE assessments.momentos SET
                nombre = %s,  
                descripcion = %s
                WHERE id = %s"""
    data = (
        nombre,
        descripcion,
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
        return api_responses.generate_response("Momento actualizado de manera exitosa!", {"id_momento": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el momento", 400, "Error al actualizar en la base de datos")
    

# Función para eliminar una momento de una competencia *******************************************
def eliminar_momento(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")

    get_moment = validar_si_existe( id )

    if get_moment == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al eliminar el momento", 400, "El momento especificado no existe en la base de datos")

    query = "UPDATE assessments.momentos SET eliminado = True WHERE id = %s"

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
        return api_responses.generate_response("El momento ha sido eliminado de la competencia", {"id_momento": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar el momento", 400, "Error al actualizar en la base de datos")
 