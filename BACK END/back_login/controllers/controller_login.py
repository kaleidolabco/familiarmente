import utils.database as db
import utils.api_responses as api_responses
import logging
import base64
from datetime import timedelta, datetime


def login(user_data):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    correo_usuario = user_data["correo_usuario"]
    correo_usuario = str(correo_usuario).lower()

    clave_usuario = user_data["clave_usuario"].encode("utf-8")
    clave_usuario = base64.b64encode(clave_usuario).decode("utf-8")

    tipo_usuario = user_data["tipo_usuario"]

    query = ""

    if(tipo_usuario == "candidato"):
        query = "SELECT id, nombres, apellidos, foto_de_perfil, correo FROM usuarios.usuarios_candidatos WHERE lower(correo) = %s AND clave = %s AND eliminado=False"

    elif(tipo_usuario == "administrador"):
        query = "SELECT id, nombres, apellidos, foto_de_perfil, correo, empresa FROM usuarios.usuarios_administradores WHERE lower(correo) = %s AND clave = %s AND eliminado=False"

    else:
        return api_responses.generate_error("Tipo de usuario", 400, "No se ha brindado un tipo de usuario correcto")

    cursor.execute(query, (correo_usuario, clave_usuario))

    db_user = cursor.fetchall()
    # print("*" * 100)
    # print(db_user)
    # print("*" * 100)

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]
    # print("*" * 100)
    # print(column_names)
    # print("*" * 100)

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
        )
        print("*" * 100)

        if len(db_user) > 0:
            # Crear un diccionario con las llaves y valores
            data = {}
            for i, column in enumerate(column_names):
                data[column] = db_user[0][i]

            return api_responses.generate_response("Las credenciales son correctas", data)
        
        else:
            return api_responses.generate_error("Credenciales incorrectas", 401, "El correo electrónico o la contraseña son incorrectos")
