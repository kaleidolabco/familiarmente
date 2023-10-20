import utils.database as db
import utils.api_responses as api_responses
import logging
import utils.password_decode as password_decode
from datetime import datetime

# Valida si el usuario existe. Útil para evitar crear usuarios o correos ya registrados
def validar_si_existe(email):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = "SELECT * FROM usuarios.usuarios_administradores WHERE correo = %s"
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

    clave = info.get("clave_administrador")
    clave = password_decode.codificar_clave_usuario(clave)
    nombres = info.get("nombres_administrador")
    apellidos = info.get("apellidos_administrador")
    correo = info.get("correo_administrador")
    telefono = info.get("telefono_administrador")
    id_parametro_pais = info.get("id_parametro_pais_administrador")
    fecha_nacimiento_str = info.get("fecha_nacimiento_administrador")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
    id_parametro_genero = info.get("id_parametro_genero_administrador")
    empresa = info.get("empresa_administrador")
    
    foto_de_perfil = ""
    descripcion_de_perfil = ""
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

        return api_responses.generate_error("Error al crear usuario", 400, "El email ingresado ya existe en el sistema")

    query = "INSERT INTO usuarios.usuarios_administradores (nombres, apellidos, correo, clave, telefono, id_parametro_pais, fecha_de_nacimiento, id_parametro_genero, empresa, foto_de_perfil, descripcion_de_perfil, eliminado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"
    data = (
        nombres,
        apellidos,
        correo,
        clave,
        telefono,
        id_parametro_pais,
        fecha_nacimiento,
        id_parametro_genero,
        empresa,
        foto_de_perfil,
        descripcion_de_perfil,
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
        return api_responses.generate_response("Usuario Agregado de manera exitosa!", {"id_usuario": id_usuario})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear el usuario", 400, "Error al agregar en la base de datos")
    

# Función para obtener los datos de un usuario
def obtener_usuario(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info["id"]

    query = "SELECT * FROM usuarios.usuarios_administradores WHERE id = %s AND eliminado = False"
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
        

# Función para actualizar los datos de un usuario 
def actualizar_usuario(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id_administrador")
    clave = info.get("clave_administrador")
    clave = password_decode.codificar_clave_usuario(clave)
    nombres = info.get("nombres_administrador")
    apellidos = info.get("apellidos_administrador")
    telefono = info.get("telefono_administrador")
    id_parametro_pais = info.get("id_parametro_pais_administrador")
    fecha_nacimiento_str = info.get("fecha_nacimiento_administrador")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
    id_parametro_genero = info.get("id_parametro_genero_administrador")
    empresa = info.get("empresa_administrador")
    foto_de_perfil = info.get("foto_de_perfil_administrador")
    descripcion_de_perfil = info.get("descripcion_de_perfil_administrador")

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

    query = """UPDATE usuarios.usuarios_administradores SET
                nombres = %s, 
                apellidos = %s, 
                clave = %s, 
                telefono = %s, 
                id_parametro_pais = %s, 
                fecha_de_nacimiento = %s, 
                id_parametro_genero = %s,
                empresa = %s, 
                foto_de_perfil = %s, 
                descripcion_de_perfil = %s
                WHERE id = %s"""
    data = (
        nombres, 
        apellidos, 
        clave,
        telefono,
        id_parametro_pais,
        fecha_nacimiento,
        id_parametro_genero,
        empresa,
        foto_de_perfil,
        descripcion_de_perfil,
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
    
       