import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math


# Valida si el assessment ya existe. Útil para evitar crear assessments con el mismo nombre ***********************************
def validar_si_existe(nombre_assessment, id_usuario):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.assessments 
        WHERE nombre = %s 
        AND id_usuario_administrador = %s 
        AND eliminado=False
    """
    cursor.execute(query, (nombre_assessment, id_usuario))

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


# Valida si el id del assessment existe.
def validar_si_existe_id_en_usuario(id_assessment, id_usuario_administrador):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.assessments 
        WHERE id = %s
        AND id_usuario_administrador = %s
        AND eliminado=False
    """
    cursor.execute(query, (id_assessment, id_usuario_administrador))

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


# Función para agregar un assessment ***************************************************************************
def agregar_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    nombre = info.get("nombre")
    descripcion = info.get("descripcion")
    id_usuario_administrador = info.get("id_usuario_administrador")

    eliminado = False

    exists = validar_si_existe(nombre, id_usuario_administrador)

    if exists:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al crear el assessment", 400, "Ya existe un assessment con ese nombre")

    query = """INSERT INTO assessments.assessments (
                nombre,
                descripcion,
                id_usuario_administrador,
                eliminado) VALUES (%s,%s,%s,%s) RETURNING id;"""
    data = (
        nombre, 
        descripcion,
        id_usuario_administrador,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    assessment = cursor.fetchone()
    id_assessment = assessment[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Assessment creado de manera exitosa!", {"id_assessment": id_assessment})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear el assessment", 400, "Error al agregar en la base de datos")
    

# Función para obtener un assessment con su id ***************************************************************************
def obtener_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = "SELECT * FROM assessments.assessments WHERE id = %s AND eliminado = False"
    data = (id,)

    cursor.execute(query, data)
    db_assessment = cursor.fetchall()

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

        if len(db_assessment) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_assessment[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Assessment obtenida de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener el assessment", 401, "No se han encontrado registros del assessment especificado")


# Función para obtener la lista de assessments de un usuario ***************************************************************************
def obtener_assessments_por_administrador(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_administrador = info["id_usuario_administrador"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info["cantidad_por_pagina"]
    pagina = info["pagina"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    # query = """
    #     SELECT id, nombre, fecha_de_registro FROM assessments.assessments 
    #     WHERE id_usuario_administrador = %s 
    #     AND eliminado = False 
    #     ORDER BY fecha_de_registro DESC
    #     LIMIT %s OFFSET %s
    # """

    query = """
        SELECT a.id, a.nombre, a.fecha_de_registro,
            (SELECT COUNT(*) FROM cargos.cargos c WHERE c.id_assessment = a.id) AS numero_de_cargos
        FROM assessments.assessments a
        WHERE a.id_usuario_administrador = %s
        AND a.eliminado = False
        ORDER BY a.fecha_de_registro DESC
        LIMIT %s OFFSET %s;
    """
    data = (id_usuario_administrador, limit, offset)

    cursor.execute(query, data)
    db_assessments = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM assessments.assessments 
        WHERE id_usuario_administrador = %s 
        AND eliminado = False
    """
    count_data = (id_usuario_administrador,)

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

        if len(db_assessments) > 0:
            assessments_list = []
            # Crear un diccionario con las llaves y valores
            for db_assessment in db_assessments:
                assessment = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_assessment[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    assessment[column] = value if (is_bool or is_none) else str(value)
                
                assessments_list.append(assessment)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "assessments": assessments_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Assessments obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron assessments creados por este usuario", {"assessments": []})


# Función para obtener los assessments por coincidencias de nombre ***************************************************************************
def buscar_assessments_por_nombre(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_administrador = info["id_usuario_administrador"]
    nombre_buscado = info["nombre_buscado"]

    # Se agrega el comodín % para permitir coincidencias en cualquier parte del nombre
    nombre_buscado = f"%{nombre_buscado}%"

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    id_usuario_administrador = info["id_usuario_administrador"]
    cantidad_por_pagina =  info["cantidad_por_pagina"]
    pagina = info["pagina"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    # query = """
    #     SELECT id, nombre, fecha_de_registro FROM assessments.assessments 
    #     WHERE id_usuario_administrador = %s 
    #     AND unaccent(lower(nombre)) LIKE unaccent(lower(%s)) 
    #     AND eliminado = False 
    #     ORDER BY fecha_de_registro DESC
    #     LIMIT %s OFFSET %s
    # """

    query = """
        SELECT a.id, a.nombre, a.fecha_de_registro,
            (SELECT COUNT(*) FROM cargos.cargos c WHERE c.id_assessment = a.id) AS numero_de_cargos
        FROM assessments.assessments a
        WHERE a.id_usuario_administrador = %s
        AND unaccent(lower(a.nombre)) LIKE unaccent(lower(%s)) 
        AND a.eliminado = False
        ORDER BY a.fecha_de_registro DESC
        LIMIT %s OFFSET %s;
    """
    data = (id_usuario_administrador, nombre_buscado, limit, offset)

    cursor.execute(query, data)
    db_assessments = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) 
        FROM assessments.assessments 
        WHERE id_usuario_administrador = %s 
        AND unaccent(lower(nombre)) LIKE unaccent(lower(%s)) 
        AND eliminado = False
    """
    count_data = (id_usuario_administrador, nombre_buscado)

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

        if len(db_assessments) > 0:
            assessments_list = []
            # Crear un diccionario con las llaves y valores
            for db_assessment in db_assessments:
                assessment = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_assessment[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    assessment[column] = value if (is_bool or is_none) else str(value)
                
                assessments_list.append(assessment)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "assessments": assessments_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Assessments obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron resultados para esta búsqueda", {"assessments": []})


# Función para actualizar un assessments ***************************************************************************
def actualizar_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")
    nombre = info.get("nombre")
    descripcion = info.get("descripcion")

    get_assessment = obtener_assessment( { "id": str(id) } )

    if get_assessment["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al actualizar el assessment", 400, "El assessment especificado no existe en la base de datos")

    query = """UPDATE assessments.assessments SET
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
        return api_responses.generate_response("Assessment actualizado de manera exitosa!", {"id_assessment": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el assessment", 400, "Error al actualizar en la base de datos")
    

# Función para eliminar un assessment ***************************************************************************
def eliminar_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")

    get_assessment = obtener_assessment( { "id": str(id) } )

    if get_assessment["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al eliminar el assessment", 400, "El assessment especificado no existe en la base de datos")

    query = "UPDATE assessments.assessments SET eliminado = True WHERE id = %s"

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
        return api_responses.generate_response("Assessment eliminado de manera exitosa!", {"id_assessment": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar el assessment", 400, "Error al actualizar en la base de datos")
    
