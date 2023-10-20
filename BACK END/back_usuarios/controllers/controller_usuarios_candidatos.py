import utils.database as db
import utils.api_responses as api_responses
import controllers.controller_archivos as controller_archivos
import logging
import utils.password_decode as password_decode
from datetime import datetime

# Valida si el usuario existe. Útil para evitar crear usuarios o correos ya registrados
def validar_si_existe(email):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = "SELECT * FROM usuarios.usuarios_candidatos WHERE correo = %s"
    cursor.execute(query, (email,))

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


# Función para agregar usuarios
def agregar_usuario(info: dict):

    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    clave = info.get("clave_candidato")
    clave = password_decode.codificar_clave_usuario(clave)
    nombres = info.get("nombres_candidato")
    apellidos = info.get("apellidos_candidato")
    correo = info.get("correo_candidato")
    telefono = info.get("telefono_candidato")
    id_parametro_pais = info.get("id_parametro_pais_candidato")
    fecha_nacimiento_str = info.get("fecha_nacimiento_candidato")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
    id_parametro_genero = info.get("id_parametro_genero_candidato")
    id_parametro_nivel_de_estudios = info.get("id_parametro_nivel_de_estudios_candidato")
    id_parametro_anos_de_experiencia = info.get("id_parametro_anos_de_experiencia_candidato")
    titulo_profesional = info.get("titulo_profesional_candidato")

    foto_de_perfil = None
    descripcion_perfil_usuario = None
    hoja_de_vida_candidato = None
    eliminado = False

    exists = validar_si_existe(correo)

    if exists:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)

        return api_responses.generate_error("Error al crear usuario", 400, "Ya existe un usuario registrado con el correo electrónico ingresado")

    query = """INSERT INTO usuarios.usuarios_candidatos (
            nombres, 
            apellidos, 
            correo, 
            clave, 
            telefono, 
            id_parametro_pais, 
            fecha_de_nacimiento, 
            id_parametro_genero, 
            foto_de_perfil, 
            descripcion_perfil_usuario, 
            id_parametro_nivel_de_estudios,
            id_parametro_anos_de_experiencia,
            titulo_profesional,
            hoja_de_vida,
            eliminado) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    data = (
        nombres,
        apellidos,
        correo,
        clave,
        telefono,
        id_parametro_pais,
        fecha_nacimiento,
        id_parametro_genero,
        foto_de_perfil,
        descripcion_perfil_usuario,
        id_parametro_nivel_de_estudios,
        id_parametro_anos_de_experiencia,
        titulo_profesional,
        hoja_de_vida_candidato,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount
    id_usuario = cursor.fetchone()
    id_usuario = id_usuario[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Usuario registrado de manera exitosa!", {"id_usuario": id_usuario})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear el usuario", 400, "Error al agregar en la base de datos")


# Función para obtener los datos de un usuario administrador
def obtener_usuario(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = "SELECT * FROM usuarios.usuarios_candidatos WHERE id = %s AND eliminado = False"
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

                if column == "clave":
                    value = password_decode.decodificar_clave_usuario(value)

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos del usuario obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos del usuario", 401, "No se han encontrado registros del usuario especificado")


# Función para obtener los datos de un usuario administrador
def obtener_perfil_usuario(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_candidato = info["id_candidato"]

    query = """SELECT cand.nombres,
        cand.apellidos,
        cand.correo,
        cand.telefono,
        cand.foto_de_perfil,
        cand.titulo_profesional,
        cand.hoja_de_vida,
        cand.descripcion_perfil_usuario,
        cand.fecha_de_nacimiento,
        pais.nombre AS pais,
        estudios.nombre AS nivel_de_estudios,
        experiencia.nombre AS anos_de_experiencia,
        genero.nombre AS genero
        FROM usuarios.usuarios_candidatos AS cand
        JOIN parametros pais ON pais.id = cand.id_parametro_pais
        JOIN parametros estudios ON estudios.id = cand.id_parametro_nivel_de_estudios
        JOIN parametros experiencia ON experiencia.id = cand.id_parametro_anos_de_experiencia
        JOIN parametros genero ON genero.id = cand.id_parametro_genero
        WHERE cand.id = %s 
        AND cand.eliminado = False
    """
    data = (id_candidato,)

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

                if column == "clave":
                    value = password_decode.decodificar_clave_usuario(value)

                is_bool = isinstance(value, (bool, int, float, complex))
                is_none = value is None

                data[column] = value if (is_bool or is_none) else str(value)

            return api_responses.generate_response("Datos del usuario obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos del usuario", 401, "No se han encontrado registros del usuario especificado")
      

# Función para actualizar los datos de un usuario 
def actualizar_usuario(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id_candidato")
    clave = info.get("clave_candidato")
    clave = password_decode.codificar_clave_usuario(clave)
    nombres = info.get("nombres_candidato")
    apellidos = info.get("apellidos_candidato")
    # correo = info.get("correo_candidato")
    telefono = info.get("telefono_candidato")
    id_parametro_pais = info.get("id_parametro_pais_candidato")
    fecha_nacimiento_str = info.get("fecha_nacimiento_candidato")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
    id_parametro_genero = info.get("id_parametro_genero_candidato")
    id_parametro_nivel_de_estudios = info.get("id_parametro_nivel_de_estudios_candidato")
    id_parametro_anos_de_experiencia = info.get("id_parametro_anos_de_experiencia_candidato")
    titulo_profesional = info.get("titulo_profesional_candidato")

    foto_de_perfil = info.get("foto_de_perfil_candidato")
    descripcion_perfil_usuario = info.get("descripcion_perfil_usuario_candidato")
    hoja_de_vida = info.get("hoja_de_vida_candidato")

    get_usuario = obtener_usuario( { "id": str(id) } )

    if get_usuario["success"] == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al actualizar los datos del usuario", 400, "El usuario especificado no existe en la base de datos")

    #Valido si no existe foto de perfil para eliminarla de la base de datos
    if foto_de_perfil is None:
        delete_photo_s3 = controller_archivos.eliminar_archivo(f'candidatos/{id}/imagenes/foto_perfil.jpeg')

        if delete_photo_s3["success"] == False:
            return api_responses.generate_error("Error al actualizar los datos del usuario", 400, "No se pudo eliminar la foto de perfil de la base de archivos")


    #Valido si no existe hoja de vida para eliminarla de la base de datos
    if hoja_de_vida is None:
        delete_curriculum_s3 = controller_archivos.eliminar_archivo(f'candidatos/{id}/documentos/hoja_de_vida.pdf')

        if delete_curriculum_s3["success"] == False:
            return api_responses.generate_error("Error al actualizar los datos del usuario", 400, "No se pudo eliminar la hoja de vida de la base de archivos")


    query = """UPDATE usuarios.usuarios_candidatos SET
                nombres = %s, 
                apellidos = %s, 
                clave = %s, 
                telefono = %s, 
                id_parametro_pais = %s, 
                fecha_de_nacimiento = %s, 
                id_parametro_genero = %s, 
                foto_de_perfil = %s, 
                descripcion_perfil_usuario = %s, 
                id_parametro_nivel_de_estudios = %s,
                id_parametro_anos_de_experiencia = %s,
                titulo_profesional = %s,
                hoja_de_vida = %s 
                WHERE id = %s"""
    data = (
        nombres, 
        apellidos, 
        clave,
        telefono,
        id_parametro_pais,
        fecha_nacimiento,
        id_parametro_genero,
        foto_de_perfil,
        descripcion_perfil_usuario,
        id_parametro_nivel_de_estudios,
        id_parametro_anos_de_experiencia,
        titulo_profesional,
        hoja_de_vida,
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
        return api_responses.generate_response("Datos del usuario actualizados de manera exitosa!", {"id_usuario": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar los datos del usuario", 400, "Error al actualizar en la base de datos")
    

# Función para obtener un enlace de subida de la foto de perfil del usuario
def obtener_url_subida_foto_usuario(info: dict):

    id = info.get("id_candidato")

    get_usuario = obtener_usuario( { "id": str(id) } )

    if get_usuario["success"] == False:
        return api_responses.generate_error("Usuario no encontrado", 400, "El usuario especificado no existe en la base de datos")

    upload_data = controller_archivos.solicitar_url_de_subida_de_archivo('image/jpeg', f'candidatos/{id}/imagenes/foto_perfil.jpeg')

    if upload_data != None:
        return api_responses.generate_response("Enlace de subida generado exitosamente", upload_data)
    else:
        return api_responses.generate_error("Error en la solicitud de subida de archivos", 400, "Ha ocurrido un error al obtener el enlace de subida del archivo")
   

# Función para obtener un enlace de subida de la hoja de vida del usuario
def obtener_url_subida_hoja_de_vida_usuario(info: dict):

    id = info.get("id_candidato")

    get_usuario = obtener_usuario( { "id": str(id) } )

    if get_usuario["success"] == False:
        return api_responses.generate_error("Usuario no encontrado", 400, "El usuario especificado no existe en la base de datos")

    upload_data = controller_archivos.solicitar_url_de_subida_de_archivo('application/pdf', f'candidatos/{id}/documentos/hoja_de_vida.pdf')

    if upload_data != None:
        return api_responses.generate_response("Enlace de subida generado exitosamente", upload_data)
    else:
        return api_responses.generate_error("Error en la solicitud de subida de archivos", 400, "Ha ocurrido un error al obtener el enlace de subida del archivo")
   