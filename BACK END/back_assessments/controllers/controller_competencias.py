import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math


# Valida si la competencia ya existe. Útil para evitar crear competencias con el mismo nombre ***********************************
def validar_si_existe(nombre_competencia, id_usuario):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.competencias 
        WHERE nombre = %s 
        AND id_usuario_administrador = %s 
        AND eliminado=False
    """
    cursor.execute(query, (nombre_competencia, id_usuario))

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


# Función para agregar una competencia ***************************************************************************
def agregar_competencia(info: dict):
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

        return api_responses.generate_error("Error al crear la competencia", 400, "Ya existe una competencia con ese nombre")

    query = """INSERT INTO assessments.competencias (
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

    competencia = cursor.fetchone()
    id_competencia = competencia[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Competencia Agregada de manera exitosa!", {"id_competencia": id_competencia})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear la competencia", 400, "Error al agregar en la base de datos")
    

# Función para obtener una competencia con su id ***************************************************************************
def obtener_competencia(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = "SELECT * FROM assessments.competencias WHERE id = %s AND eliminado = False"
    data = (id,)

    cursor.execute(query, data)
    db_skill = cursor.fetchall()

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

        if len(db_skill) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_skill[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Competencia obtenida de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener la competencia", 401, "No se han encontrado registros de la competencia especificada")


# Función para obtener la lista de competencias de un usuario ***************************************************************************
def obtener_competencias_por_administrador(info: dict):
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
    query = """
        SELECT id, nombre, fecha_de_registro FROM assessments.competencias 
        WHERE id_usuario_administrador = %s 
        AND eliminado = False 
        ORDER BY fecha_de_registro DESC
        LIMIT %s OFFSET %s
    """
    data = (id_usuario_administrador, limit, offset)

    cursor.execute(query, data)
    db_skills = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM assessments.competencias 
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

        if len(db_skills) > 0:
            skills_list = []
            # Crear un diccionario con las llaves y valores
            for db_skill in db_skills:
                skill = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_skill[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    skill[column] = value if (is_bool or is_none) else str(value)
                
                skills_list.append(skill)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "competencias": skills_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Competencias obtenidas de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron competencias creadas por este usuario", {"competencias": []})


# Función para obtener las competencias por coincidencias de nombre ***************************************************************************
def buscar_competencias_por_nombre(info: dict):
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
    query = """
        SELECT id, nombre, fecha_de_registro FROM assessments.competencias 
        WHERE id_usuario_administrador = %s 
        AND unaccent(lower(nombre)) LIKE unaccent(lower(%s)) 
        AND eliminado = False 
        ORDER BY fecha_de_registro DESC
        LIMIT %s OFFSET %s
    """
    data = (id_usuario_administrador, nombre_buscado, limit, offset)

    cursor.execute(query, data)
    db_skills = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) 
        FROM assessments.competencias 
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

        if len(db_skills) > 0:
            skills_list = []
            # Crear un diccionario con las llaves y valores
            for db_skill in db_skills:
                skill = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_skill[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    skill[column] = value if (is_bool or is_none) else str(value)
                
                skills_list.append(skill)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "competencias": skills_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Competencias obtenidas de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron resultados para esta búsqueda", {"competencias": []})


# Función para actualizar una competencia ***************************************************************************
def actualizar_competencia(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")
    nombre = info.get("nombre")
    descripcion = info.get("descripcion")

    get_competencia = obtener_competencia( { "id": str(id) } )

    if get_competencia["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al actualizar la competencia", 400, "La competencia especificada no existe en la base de datos")

    query = """UPDATE assessments.competencias SET
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
        return api_responses.generate_response("Competencia actualizada de manera exitosa!", {"id_competencia": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar la competencia", 400, "Error al actualizar en la base de datos")
    

# Función para eliminar un cargo ***************************************************************************
def eliminar_competencia(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")

    get_competencia = obtener_competencia( { "id": str(id) } )

    if get_competencia["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al eliminar la competencia", 400, "La competencia especificada no existe en la base de datos")

    query = "UPDATE assessments.competencias SET eliminado = True WHERE id = %s"

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
        return api_responses.generate_response("Competencia eliminada de manera exitosa!", {"id_competencia": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar la competencia", 400, "Error al actualizar en la base de datos")
    
