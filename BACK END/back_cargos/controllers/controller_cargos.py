import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math

# Valida si el cargo existe. Útil para evitar crear cargos sin nombres repetidos ***********************************
def validar_si_existe(nombre_cargo, id_usuario):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM cargos.cargos 
        WHERE nombre = %s 
        AND id_usuario_administrador = %s 
        AND eliminado=False
    """
    cursor.execute(query, (nombre_cargo, id_usuario))

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


# Función para agregar cargos ***************************************************************************
def agregar_cargo(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    nombre = info.get("nombre")
    titulo_profesional_requerido = info.get("titulo_profesional_requerido")
    empresa_oferente = info.get("empresa_oferente")
    minimo_salario_mensual = info.get("minimo_salario_mensual")
    maximo_salario_mensual = info.get("maximo_salario_mensual")
    id_parametro_moneda = info.get("id_parametro_moneda")
    ubicacion = info.get("ubicacion")
    trabajo_remoto = info.get("trabajo_remoto")
    descripcion = info.get("descripcion")
    requisitos = info.get("requisitos")
    proceso_de_contratacion = info.get("proceso_de_contratacion")
    id_assessment = info.get("id_assessment")
    id_usuario_administrador = info.get("id_usuario_administrador")
    vacantes = info.get("vacantes")

    publicado = False
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

        return api_responses.generate_error("Error al crear el cargo", 400, "Ya existe un cargo con ese nombre")

    query = """INSERT INTO cargos.cargos (
                nombre, 
                titulo_profesional_requerido, 
                empresa_oferente,
                minimo_salario_mensual, 
                maximo_salario_mensual,
                id_parametro_moneda,
                ubicacion,
                trabajo_remoto,
                descripcion,
                requisitos,
                proceso_de_contratacion,
                id_assessment,
                id_usuario_administrador,
                vacantes,
                publicado,
                eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    data = (
        nombre, 
        titulo_profesional_requerido, 
        empresa_oferente,
        minimo_salario_mensual, 
        maximo_salario_mensual,
        id_parametro_moneda,
        ubicacion,
        trabajo_remoto,
        descripcion,
        requisitos,
        proceso_de_contratacion,
        id_assessment,
        id_usuario_administrador,
        vacantes,
        publicado,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    cargo = cursor.fetchone()
    id_cargo = cargo[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Cargo Agregado de manera exitosa!", {"id_cargo": id_cargo})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear el cargo", 400, "Error al agregar en la base de datos")
    


# Función para obtener un cargo con su id ***************************************************************************
def obtener_cargo(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    # query = "SELECT * FROM cargos.cargos WHERE id = %s AND eliminado = False"
    query = """
        SELECT 
        c.*,
        (SELECT p.nombre FROM parametros AS p WHERE p.id = c.id_parametro_moneda) AS moneda
        FROM cargos.cargos AS c
        WHERE c.id = %s AND c.eliminado = false;
    """
    data = (id,)

    cursor.execute(query, data)
    db_job = cursor.fetchall()

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

        if len(db_job) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_job[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Cargo obtenido de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener el cargo", 401, "No se han encontrado registros del cargo especificado")


# Función para obtener la lista de cargos de un usuario ***************************************************************************
def obtener_cargos_por_administrador(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_administrador = info["id_usuario_administrador"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    id_usuario_administrador = info["id_usuario_administrador"]
    cantidad_por_pagina =  info["cantidad_por_pagina"]
    pagina = info["pagina"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    # query = """
    #     SELECT id, nombre, publicado, fecha_de_registro FROM cargos.cargos 
    #     WHERE id_usuario_administrador = %s 
    #     AND eliminado = False 
    #     ORDER BY fecha_de_registro DESC
    #     LIMIT %s OFFSET %s
    # """

    query = """
        SELECT c.id, c.nombre, c.publicado, c.fecha_de_registro,
        (SELECT COUNT(*) FROM cargos.postulaciones p WHERE p.id_cargo = c.id) AS numero_de_postulaciones
        FROM cargos.cargos c
        WHERE c.id_usuario_administrador = %s
        AND c.eliminado = False
        ORDER BY c.fecha_de_registro DESC
        LIMIT %s OFFSET %s;
    """
    data = (id_usuario_administrador, limit, offset)

    cursor.execute(query, data)
    db_jobs = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM cargos.cargos 
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

        if len(db_jobs) > 0:
            jobs_list = []
            # Crear un diccionario con las llaves y valores
            for db_job in db_jobs:
                job = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_job[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    job[column] = value if (is_bool or is_none) else str(value)
                
                jobs_list.append(job)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "cargos": jobs_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Cargos obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron cargos creados por este usuario", {"cargos": []})


# Función para obtener la lista de cargos publicados ***************************************************************************
def obtener_cargos_publicados(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info["cantidad_por_pagina"]
    pagina = info["pagina"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT id, nombre, empresa_oferente, descripcion, ubicacion, trabajo_remoto, vacantes, fecha_de_registro FROM cargos.cargos 
        WHERE publicado = true 
        AND eliminado = False 
        ORDER BY fecha_de_registro DESC
        LIMIT %s OFFSET %s
    """
    data = ( limit, offset)

    cursor.execute(query, data)
    db_jobs = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM cargos.cargos 
        WHERE publicado = true 
        AND eliminado = False
    """

    cursor.execute(count_query, )
    total_elements = cursor.fetchone()[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
        )
        print("*" * 100)

        if len(db_jobs) > 0:
            jobs_list = []
            # Crear un diccionario con las llaves y valores
            for db_job in db_jobs:
                job = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_job[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    job[column] = value if (is_bool or is_none) else str(value)
                
                jobs_list.append(job)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "cargos": jobs_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Cargos obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron cargos creados por este usuario", {"cargos": []})


# Función para obtener los cargos por coincidencias de nombre ***************************************************************************
def buscar_cargos_por_nombre(info: dict):
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
    #     SELECT id, nombre, publicado, fecha_de_registro FROM cargos.cargos 
    #     WHERE id_usuario_administrador = %s 
    #     AND unaccent(lower(nombre)) LIKE unaccent(lower(%s)) 
    #     AND eliminado = False 
    #     ORDER BY fecha_de_registro DESC
    #     LIMIT %s OFFSET %s
    # """
    query = """
        SELECT c.id, c.nombre, c.publicado, c.fecha_de_registro,
        (SELECT COUNT(*) FROM cargos.postulaciones p WHERE p.id_cargo = c.id) AS numero_de_postulaciones
        FROM cargos.cargos c
        WHERE c.id_usuario_administrador = %s
        AND unaccent(lower(c.nombre)) LIKE unaccent(lower(%s)) 
        AND c.eliminado = False
        ORDER BY c.fecha_de_registro DESC
        LIMIT %s OFFSET %s;
    """
    data = (id_usuario_administrador, nombre_buscado, limit, offset)

    cursor.execute(query, data)
    db_jobs = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) 
        FROM cargos.cargos 
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

        if len(db_jobs) > 0:
            jobs_list = []
            # Crear un diccionario con las llaves y valores
            for db_job in db_jobs:
                job = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_job[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    job[column] = value if (is_bool or is_none) else str(value)
                
                jobs_list.append(job)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "cargos": jobs_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Cargos obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron resultados para esta búsqueda", {"cargos": []})


# Función para obtener los cargos por coincidencias de nombre ***************************************************************************
def buscar_cargos_publicados_por_nombre(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    nombre_buscado = info["nombre_buscado"]

    # Se agrega el comodín % para permitir coincidencias en cualquier parte del nombre
    nombre_buscado = f"%{nombre_buscado}%"

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info["cantidad_por_pagina"]
    pagina = info["pagina"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT id, nombre, empresa_oferente, descripcion, ubicacion, vacantes, fecha_de_registro FROM cargos.cargos 
        WHERE publicado = true 
        AND unaccent(lower(nombre)) LIKE unaccent(lower(%s)) 
        AND eliminado = False 
        ORDER BY fecha_de_registro DESC
        LIMIT %s OFFSET %s
    """
    data = (nombre_buscado, limit, offset)

    cursor.execute(query, data)
    db_jobs = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) 
        FROM cargos.cargos 
        WHERE publicado = true 
        AND unaccent(lower(nombre)) LIKE unaccent(lower(%s)) 
        AND eliminado = False
    """
    count_data = ( nombre_buscado, )

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

        if len(db_jobs) > 0:
            jobs_list = []
            # Crear un diccionario con las llaves y valores
            for db_job in db_jobs:
                job = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_job[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    job[column] = value if (is_bool or is_none) else str(value)
                
                jobs_list.append(job)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "cargos": jobs_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Cargos obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron resultados para esta búsqueda", {"cargos": []})



# Función para actualizar un cargo ***************************************************************************
def actualizar_cargo(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")
    nombre = info.get("nombre")
    titulo_profesional_requerido = info.get("titulo_profesional_requerido")
    empresa_oferente = info.get("empresa_oferente")
    minimo_salario_mensual = info.get("minimo_salario_mensual")
    maximo_salario_mensual = info.get("maximo_salario_mensual")
    id_parametro_moneda = info.get("id_parametro_moneda")
    ubicacion = info.get("ubicacion")
    trabajo_remoto = info.get("trabajo_remoto")
    descripcion = info.get("descripcion")
    requisitos = info.get("requisitos")
    proceso_de_contratacion = info.get("proceso_de_contratacion")
    id_assessment = info.get("id_assessment")
    vacantes = info.get("vacantes")
    publicado = info.get("publicado")

    get_cargo = obtener_cargo( { "id": str(id) } )

    if get_cargo["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al actualizar el cargo", 400, "El cargo especificado no existe en la base de datos")

    query = """UPDATE cargos.cargos SET
                nombre = %s,  
                titulo_profesional_requerido = %s,  
                empresa_oferente = %s,
                minimo_salario_mensual = %s,  
                maximo_salario_mensual = %s, 
                id_parametro_moneda = %s, 
                ubicacion = %s, 
                trabajo_remoto = %s, 
                descripcion = %s, 
                requisitos = %s, 
                proceso_de_contratacion = %s, 
                id_assessment = %s, 
                vacantes = %s, 
                publicado = %s
                WHERE id = %s"""
    data = (
        nombre, 
        titulo_profesional_requerido, 
        empresa_oferente, 
        minimo_salario_mensual, 
        maximo_salario_mensual,
        id_parametro_moneda,
        ubicacion,
        trabajo_remoto,
        descripcion,
        requisitos,
        proceso_de_contratacion,
        id_assessment,
        vacantes,
        publicado,
        id
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
        return api_responses.generate_response("Cargo actualizado de manera exitosa!", {"id_cargo": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el cargo", 400, "Error al actualizar en la base de datos")
    


# Función para eliminar un cargo ***************************************************************************
def eliminar_cargo(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id")

    get_cargo = obtener_cargo( { "id": str(id) } )

    if get_cargo["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al eliminar el cargo", 400, "El cargo especificado no existe en la base de datos")

    query = "UPDATE cargos.cargos SET eliminado = True WHERE id = %s"

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
        return api_responses.generate_response("Cargo eliminado de manera exitosa!", {"id_cargo": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar el cargo", 400, "Error al actualizar en la base de datos")
    

