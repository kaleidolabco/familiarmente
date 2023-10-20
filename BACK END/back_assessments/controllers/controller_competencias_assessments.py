import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math

# Este controlador se encarga de la gestión de relaciones de assessments y competencias
# Cada assessment puede contener varias competencias para evaluar
# A su vez, cada competencia puede usarse en varios assessments a la vez

# Valida si la relación competencia - assessment ya existe. ***********************************
def validar_si_existe(id_competencia_assessment):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.competencias_assessments 
        WHERE id = %s 
        AND eliminado=False
    """
    cursor.execute(query, (id_competencia_assessment,))

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


# Valida si la la competencia ya se agregó al assessment. ***********************************
def validar_si_existe_en_assessment(id_competencia, id_assessment):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    query = """SELECT id 
        FROM assessments.competencias_assessments 
        WHERE id_competencia = %s 
        AND id_assessment = %s
        AND eliminado=False
    """
    cursor.execute(query, (id_competencia, id_assessment))

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


# Función para obtener la lista de competencias agregadas a un assessment *************************************
def obtener_competencias_por_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_assessment = info["id_assessment"]

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    cantidad_por_pagina =  info.get("cantidad_por_pagina", 100)
    pagina = info.get("pagina", 1)

    # Calcular el desplazamiento (offset) y el límite (limit) para la paginación
    offset = (pagina - 1) * cantidad_por_pagina
    limit = cantidad_por_pagina

    query = """
        SELECT ca.id, c.nombre, 
            (SELECT COUNT(*) FROM assessments.momentos m 
                WHERE m.id_competencia_assessment = ca.id) AS cantidad_momentos
        FROM assessments.competencias c
        JOIN assessments.competencias_assessments ca ON c.id = ca.id_competencia
        WHERE ca.id_assessment = %s 
        AND ca.eliminado = False 
        ORDER BY ca.fecha_de_registro ASC
        LIMIT %s OFFSET %s;
    """

    data = (id_assessment, limit, offset)

    cursor.execute(query, data)
    db_skills = cursor.fetchall()

    # Obtener los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]


    # Consulta para obtener la cantidad total de elementos
    count_query = """
        SELECT COUNT(*) FROM assessments.competencias_assessments 
        WHERE id_assessment = %s 
        AND eliminado = False
    """
    count_data = (id_assessment,)

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
            return api_responses.generate_response("No se encontraron competencias cagregadas en este assessment", {"competencias": []})


# Función para agregar una competencia a un assessment *****************************************
def agregar_competencia_al_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_assessment = info.get("id_assessment")
    id_competencia = info.get("id_competencia")

    eliminado = False

    competencia_existe_en_assessment = validar_si_existe_en_assessment(id_competencia, id_assessment)

    if competencia_existe_en_assessment == True:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al agregar la competencia", 400, "Esta competencia ya ha sido agregada en el assessment")


    query = """INSERT INTO assessments.competencias_assessments (
                id_assessment,
                id_competencia,
                eliminado) VALUES (%s,%s,%s) RETURNING id;"""
    data = (
        id_assessment, 
        id_competencia,
        eliminado
    )

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    competencia_assessment = cursor.fetchone()
    id_competencia_assessment = competencia_assessment[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Competencia agregada al assessment de manera exitosa!", {"id_competencia_assessment": id_competencia_assessment})
    else:
        return api_responses.generate_error("Ha ocurrido un error al crear la competencia al assessment", 400, "Error al agregar en la base de datos")
    

# Función para agregar varias competencias a un assessment *****************************************
def agregar_competencias_al_assessment(lista_de_competencias: set):
    resultados = []

    for competencia in lista_de_competencias:
        resultado = agregar_competencia_al_assessment(competencia)
        resultados.append(resultado)

    return resultados


# Función para eliminar una competencia de un assessment *******************************************
def eliminar_competencia_del_assessment(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id = info.get("id_competencia_assessment")

    get_competencia_assessment = validar_si_existe( id )

    if get_competencia_assessment == False:
        if connection:
            cursor.close()
            connection.close()
            print("*" * 100)
            logging.warning(
                {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
            )
            print("*" * 100)
            
        return api_responses.generate_error("Error al eliminar la competencia", 400, "La competencia especificada no existe en la base de datos")

    query = "UPDATE assessments.competencias_assessments SET eliminado = True WHERE id = %s"

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
        return api_responses.generate_response("La competencia ha sido eliminada del assessment", {"id_competencia_assessment": id})
    else:
        return api_responses.generate_error("Ha ocurrido un error al eliminar la competencia del assessment", 400, "Error al actualizar en la base de datos")
 