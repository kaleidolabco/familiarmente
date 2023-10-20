# CORREGIR LA BÚSQUEDA DE POSTULACIONES
# SE DEBERÍA BUSCAR POR CONINCIDENCIA DE NOMBRES, APELLIDOS Y CORRE 
# HAY UN ERROR DE BÚSQUEDA Y NO ARROJA RESULTADOS SI EL STRING NO COINCIDE EXACTAMENTE

import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math

# Valida si un usuario ya postuló a un cargo ***********************************
def validar_si_existe(id_usuario_candidato, id_cargo):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM cargos.postulaciones 
        WHERE id_usuario_candidato = %s 
        AND id_cargo = %s 
        AND eliminado=False
    """
    cursor.execute(query, (id_usuario_candidato, id_cargo))

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


# Función para agregar postulacion a  un cargo ***************************************************************************
def agregar_postulacion(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")
    id_assessment = info.get("id_assessment", None)
    # id_parametro_estado_de_postulacion_candidato = info.get("id_parametro_estado_de_postulacion_candidato", None)
    
    eliminado = False

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al postular", 400, "Ya tienes un proceso de postluación a este cargo")

    query = """
        WITH estado_postulacion AS (
            SELECT id 
            FROM parametros 
            WHERE nombre = 'Postulado' 
            AND id_tipo_parametro = (SELECT id FROM tipos_parametros WHERE nombre = 'estado_postulacion_candidato')
        )
        INSERT INTO cargos.postulaciones (
            id_usuario_candidato,
            id_cargo,
            id_assessment,
            id_parametro_estado_de_postulacion_candidato,
            eliminado
        ) 
        VALUES (
            %s, %s, %s,
            (SELECT id FROM estado_postulacion),
            %s
        ) 
        RETURNING id;
    """
    data = (
        id_usuario_candidato,
        id_cargo,
        id_assessment,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    postulacion = cursor.fetchone()
    id_postulacion = postulacion[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Postulación completada de manera exitosa", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al postular a este cargo", 400, "Error al agregar en la base de datos")


# Función para obtener la lista de postulaciones para un cargo ****************************************************
def obtener_postulaciones_por_cargo(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_cargo = info["id_cargo"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info.get("cantidad_por_pagina", 100)
    pagina = info.get("pagina", 1)

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT post.id AS id_postulacion,
        cand.id AS id_usuario_candidato,
        cand.nombres AS nombres_candidato, 
        cand.apellidos AS apellidos_candidato, 
        cand.correo AS correo_candidato, 
        cand.foto_de_perfil AS foto_candidato,
        cand.titulo_profesional,
        post.id_parametro_estado_de_postulacion_candidato, 
        post.calificacion_final,
        par.nombre AS estado_postulacion,
        post.fecha_de_registro AS fecha_de_postulacion
        FROM cargos.postulaciones AS post
        JOIN usuarios.usuarios_candidatos AS cand
        ON cand.id = post.id_usuario_candidato
        JOIN parametros AS par 
        ON post.id_parametro_estado_de_postulacion_candidato = par.id
        WHERE post.id_cargo = %s
        AND post.eliminado = false
        ORDER BY post.fecha_de_registro ASC
        LIMIT %s OFFSET %s;
    """
    data = (id_cargo, limit, offset)

    cursor.execute(query, data)
    db_postulaciones = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM cargos.postulaciones 
        WHERE id_cargo = %s
        AND eliminado = false
    """
    count_data = (id_cargo,)

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

        if len(db_postulaciones) > 0:
            applications_list = []
            # Crear un diccionario con las llaves y valores
            for db_application in db_postulaciones:
                application = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_application[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    application[column] = value if (is_bool or is_none) else str(value)
                
                applications_list.append(application)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "postulaciones": applications_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Datos de postulaciones obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron postulaciones a este cargo", {"postulaciones": []})


# Función para obtener la lista de postulaciones de un candidato ****************************************************
def obtener_postulaciones_por_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info["id_usuario_candidato"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info.get("cantidad_por_pagina", 100)
    pagina = info.get("pagina", 1)

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT post.id AS id_postulacion,
        post.id_parametro_estado_de_postulacion_candidato, 
        par.nombre AS estado_postulacion,
        car.id AS id_cargo,
        car.nombre,
        car.ubicacion,
        car.empresa_oferente,
        post.fecha_de_registro AS fecha_de_postulacion
        FROM cargos.postulaciones AS post
        JOIN cargos.cargos AS car
        ON car.id = post.id_cargo
        JOIN parametros AS par 
        ON post.id_parametro_estado_de_postulacion_candidato = par.id
        WHERE post.id_usuario_candidato = %s
        AND post.eliminado = false
        ORDER BY post.fecha_de_registro ASC
        LIMIT %s OFFSET %s;
    """
    data = (id_usuario_candidato, limit, offset)

    cursor.execute(query, data)
    db_postulaciones = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM cargos.postulaciones 
        WHERE id_usuario_candidato = %s
        AND eliminado = false
    """
    count_data = (id_usuario_candidato,)

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

        if len(db_postulaciones) > 0:
            applications_list = []
            # Crear un diccionario con las llaves y valores
            for db_application in db_postulaciones:
                application = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_application[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    application[column] = value if (is_bool or is_none) else str(value)
                
                applications_list.append(application)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "postulaciones": applications_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Datos de postulaciones obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron postulaciones realizadas aún", {"postulaciones": []})



# Función para obtener las postulaciones por coincidencias de nombre del candidato********************************
def buscar_postulaciones_por_nombre_de_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_cargo = info["id_cargo"]
    nombre_buscado = info["nombre_buscado"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info.get("cantidad_por_pagina", 100)
    pagina = info.get("pagina", 1)

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    # Consulta para obtener los cargos de la página actual
    query = """
        SELECT post.id AS id_postulacion,
        cand.id AS id_usuario_candidato,
        cand.nombres AS nombres_candidato, 
        cand.apellidos AS apellidos_candidato, 
        cand.correo AS correo_candidato, 
        cand.foto_de_perfil AS foto_candidato,
        cand.titulo_profesional,
        post.id_parametro_estado_de_postulacion_candidato, 
        post.calificacion_final,
        par.nombre AS estado_postulacion,
        post.fecha_de_registro AS fecha_de_postulacion
        FROM cargos.postulaciones AS post
        JOIN usuarios.usuarios_candidatos AS cand
        ON cand.id = post.id_usuario_candidato
        JOIN parametros AS par 
        ON post.id_parametro_estado_de_postulacion_candidato = par.id
        WHERE post.id_cargo = %s
        AND unaccent(lower(cand.nombres)) LIKE unaccent(lower(%s))
        AND post.eliminado = false
        ORDER BY post.fecha_de_registro ASC
        LIMIT %s OFFSET %s;
    """
    data = (id_cargo, nombre_buscado, limit, offset)

    cursor.execute(query, data)
    db_postulaciones = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM cargos.postulaciones AS post
        JOIN usuarios.usuarios_candidatos AS cand
        ON cand.id = post.id_usuario_candidato
        WHERE id_cargo = %s
        AND unaccent(lower(cand.nombres)) LIKE unaccent(lower(%s))
        AND post.eliminado = false
    """
    count_data = (id_cargo, nombre_buscado)

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

        if len(db_postulaciones) > 0:
            applications_list = []
            # Crear un diccionario con las llaves y valores
            for db_application in db_postulaciones:
                application = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_application[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    application[column] = value if (is_bool or is_none) else str(value)
                
                applications_list.append(application)

            # Calcular el número total de páginas
            total_pages = math.ceil(total_elements / cantidad_por_pagina)

            # Generar la respuesta incluyendo la información de paginación
            response_data = {
                "postulaciones": applications_list,
                "elementos_totales": total_elements,
                "paginas_totales": total_pages,
                "pagina_actual": pagina,
                "cantidad_por_pagina": cantidad_por_pagina
            }
            return api_responses.generate_response("Datos de postulaciones obtenidos de manera exitosa", response_data)
        
        else:
            return api_responses.generate_response("No se encontraron candidatos postulados en la búsqueda realizada", {"postulaciones": []})


# Función para obtener los datos de una postulación ***************************************************************************
def obtener_postulacion(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")

    # query = "SELECT * FROM cargos.cargos WHERE id = %s AND eliminado = False"
    query = """
        SELECT p.*, 
        pr.nombre AS estado_postulacion,
        car.id AS id_cargo,
        car.nombre AS nombre_cargo,
        car.empresa_oferente AS empresa_cargo,
        car.ubicacion AS ubicacion_cargo
        FROM cargos.postulaciones p
        JOIN parametros pr ON p.id_parametro_estado_de_postulacion_candidato = pr.id
        JOIN cargos.cargos car ON car.id = p.id_cargo
        WHERE p.id_usuario_candidato = %s
        AND p.id_cargo = %s
        AND p.eliminado = false;
    """
    data = (id_usuario_candidato, id_cargo)

    cursor.execute(query, data)
    db_application = cursor.fetchall()

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

        if len(db_application) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                # Valido si hay booleanos o nulos para no convertirlos a string
                value = db_application[0][i] 

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos de postulación obtenidos de forma correcta", data)
        
        else:
            return api_responses.generate_error("Error al obtener el estado de la postulación", 401, "No se han encontrado postulaciones del usuario al cargo especificado")


# Función para actualizar el estado de una postulacion ***************************************************************************
def actualizar_postulacion(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")
    id_assessment = info.get("id_assessment", None)
    id_parametro_estado_de_postulacion_candidato = info.get("id_parametro_estado_de_postulacion_candidato", None)

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar el estado de la postulación", 400, "No se ha encontrado una postulación creada para este cargo")

    query = """UPDATE cargos.postulaciones SET
                id_parametro_estado_de_postulacion_candidato = %s,
                id_assessment = %s 
                WHERE id_usuario_candidato = %s
                AND id_cargo = %s"""
    data = (
        id_parametro_estado_de_postulacion_candidato,
        id_assessment,
        id_usuario_candidato,
        id_cargo
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
        return api_responses.generate_response("Postulación actualizada de manera exitosa!", {"id_cargo": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el estado de la postulación", 400, "Error al actualizar en la base de datos")
    

# Función para actualizar el estado de una postulacion ***************************************************************************
def actualizar_postulacion(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")
    id_assessment = info.get("id_assessment", None)
    id_parametro_estado_de_postulacion_candidato = info.get("id_parametro_estado_de_postulacion_candidato", None)

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar el estado de la postulación", 400, "No se ha encontrado una postulación creada para este cargo")

    query = """UPDATE cargos.postulaciones SET
                id_parametro_estado_de_postulacion_candidato = %s,
                id_assessment = %s 
                WHERE id_usuario_candidato = %s
                AND id_cargo = %s"""
    data = (
        id_parametro_estado_de_postulacion_candidato,
        id_assessment,
        id_usuario_candidato,
        id_cargo
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
        return api_responses.generate_response("Postulación actualizada de manera exitosa!", {"id_cargo": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el estado de la postulación", 400, "Error al actualizar en la base de datos")
    

# Función para actualizar el estado de una postulacion a Postulado ***************************************************************************
def actualizar_postulacion_a_postulado(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar el estado de la postulación", 400, "No se ha encontrado una postulación creada para este cargo")
    
    query = """
        WITH estado_postulacion AS (
            SELECT id 
            FROM parametros 
            WHERE nombre = 'Postulado' 
            AND id_tipo_parametro = (SELECT id FROM tipos_parametros WHERE nombre = 'estado_postulacion_candidato')
        )
        UPDATE cargos.postulaciones SET
            id_parametro_estado_de_postulacion_candidato = (SELECT id FROM estado_postulacion)
            WHERE id_usuario_candidato = %s
            AND id_cargo = %s
            RETURNING id;
    """
    data = (
        id_usuario_candidato,
        id_cargo
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    postulacion = cursor.fetchone()
    id_postulacion = postulacion[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Postulación actualizada de manera exitosa!", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el estado de la postulación", 400, "Error al actualizar en la base de datos")


# Función para actualizar el estado de una postulacion a Assessment Completado ***************************************************************************
def actualizar_postulacion_a_assessment_completado(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")
    id_assessment = info["id_assessment"]

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar el estado de la postulación", 400, "No se ha encontrado una postulación creada para este cargo")
    
    query = """
        WITH estado_postulacion AS (
            SELECT id 
            FROM parametros 
            WHERE nombre = 'Assessment Completado' 
            AND id_tipo_parametro = (SELECT id FROM tipos_parametros WHERE nombre = 'estado_postulacion_candidato')
        )
        UPDATE cargos.postulaciones SET
            id_parametro_estado_de_postulacion_candidato = (SELECT id FROM estado_postulacion),
            id_assessment = %s
            WHERE id_usuario_candidato = %s
            AND id_cargo = %s
            RETURNING id;
    """
    data = (
        id_assessment,
        id_usuario_candidato,
        id_cargo
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    postulacion = cursor.fetchone()
    id_postulacion = postulacion[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Postulación actualizada de manera exitosa!", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el estado de la postulación", 400, "Error al actualizar en la base de datos")


# Función para actualizar el estado de una postulacion a Evaluado ***************************************************************************
def actualizar_postulacion_a_evaluado(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar el estado de la postulación", 400, "No se ha encontrado una postulación creada para este cargo")
    
    query = """
        WITH estado_postulacion AS (
            SELECT id 
            FROM parametros 
            WHERE nombre = 'Evaluado' 
            AND id_tipo_parametro = (SELECT id FROM tipos_parametros WHERE nombre = 'estado_postulacion_candidato')
        )
        UPDATE cargos.postulaciones SET
            id_parametro_estado_de_postulacion_candidato = (SELECT id FROM estado_postulacion)
            WHERE id_usuario_candidato = %s
            AND id_cargo = %s
            RETURNING id;
    """

    data = (
        id_usuario_candidato,
        id_cargo
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    postulacion = cursor.fetchone()
    id_postulacion = postulacion[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Postulación actualizada de manera exitosa!", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el estado de la postulación", 400, "Error al actualizar en la base de datos")


# Función para actualizar el estado de una postulacion a Proceso Finalizado ***************************************************************************
def actualizar_postulacion_a_proceso_finalizado(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al actualizar el estado de la postulación", 400, "No se ha encontrado una postulación creada para este cargo")
    
    query = """
        WITH estado_postulacion AS (
            SELECT id 
            FROM parametros 
            WHERE nombre = 'Proceso Finalizado' 
            AND id_tipo_parametro = (SELECT id FROM tipos_parametros WHERE nombre = 'estado_postulacion_candidato')
        )
        UPDATE cargos.postulaciones SET
            id_parametro_estado_de_postulacion_candidato = (SELECT id FROM estado_postulacion)
            WHERE id_usuario_candidato = %s
            AND id_cargo = %s
            RETURNING id;
    """
    data = (
        id_usuario_candidato,
        id_cargo
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    postulacion = cursor.fetchone()
    id_postulacion = postulacion[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Postulación actualizada de manera exitosa!", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar el estado de la postulación", 400, "Error al actualizar en la base de datos")


# Función para eliminar una postulación a un cargo ***************************************************************************
def eliminar_postulacion(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")

    exists = validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al intentar eliminar la postulación", 400, "No se ha encontrado una postulación creada para este cargo")

    query = """UPDATE cargos.postulaciones 
            SET eliminado = True 
            WHERE id_usuario_candidato = %s
            AND id_cargo = %s
            RETURNING id;
    """

    cursor.execute(query, (id_usuario_candidato, id_cargo))
    connection.commit()
    result = cursor.rowcount

    postulacion = cursor.fetchone()
    id_postulacion = postulacion[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Postulación al cargo eliminada de manera exitosa!", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar la postulación", 400, "Error al actualizar en la base de datos")
    
