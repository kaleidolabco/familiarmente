import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math


# Función para obtener los datos del assessment para aplicar a un cargo *************************
def obtener_assessment_del_cargo(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_cargo = info["id_cargo"]

    query = """
        SELECT id, nombre 
        FROM assessments.assessments 
        WHERE id = (SELECT id_assessment FROM cargos.cargos WHERE id =  %s)
        AND eliminado = False
    """
    data = (id_cargo,)

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
            
            # Obtengo la lista de competencias que se evalúan en el assessment
            competencias = obtener_competencias_por_assessment(data["id"])

            if competencias:
                # Para cada competencia obtengo la lista de momentos que tiene
                for competencia in competencias["competencias"]:
                    momentos = obtener_momentos_por_competencia(competencia["id"])
                    competencia["datos_momentos"] = momentos

                    if momentos:
                        for momento in momentos["momentos"]:
                            if momento:
                                preguntas = obtener_preguntas_por_momento(momento["id"])
                                momento["datos_preguntas"] = preguntas
                    
            data["datos_competencias"] = competencias

            return api_responses.generate_response("Datos del assessment obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos del assessment", 401, "No se han encontrado registros del assessment especificado")


# Función para obtener la lista de competencias agregadas a un assessment *************************************
def obtener_competencias_por_assessment(id_assessment: str):
    
    try:
        consult = db.get_db()
        cursor = consult.get("cursor")
        connection = consult.get("connection")

        query = """
            SELECT ca.id, c.nombre
            FROM assessments.competencias c
            JOIN assessments.competencias_assessments ca ON c.id = ca.id_competencia
            WHERE ca.id_assessment = %s 
            AND ca.eliminado = False 
            ORDER BY ca.fecha_de_registro ASC
        """
        data = (id_assessment,)

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
            # print("*" * 100)
            # logging.warning(
            #     {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
            # )
            # print("*" * 100)
            
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


                # Generar la respuesta incluyendo la información de paginación
                response_data = {
                    "competencias": skills_list,
                    "elementos_totales": total_elements
                }
                return response_data
            
            else:
                return None
            
    except Exception as exception:

        # print("*" * 100)
        # logging.error(
        #     {
        #         "error": f"Error: {exception}. Contacta con el administrador"
        #     }
        # )
        # print("*" * 100)

        return None


# Función para obtener la lista de momentos de una competencia *************************************************
def obtener_momentos_por_competencia(id_competencia_assessment: str):

    try:
        consult = db.get_db()
        cursor = consult.get("cursor")
        connection = consult.get("connection")

        # Consulta para obtener los momentos de una competencia en un assessment
        query = """
            SELECT id, nombre FROM assessments.momentos 
            WHERE id_competencia_assessment = %s 
            AND eliminado = False 
            ORDER BY fecha_de_registro ASC
        """
        data = (id_competencia_assessment,)

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
            # print("*" * 100)
            # logging.warning(
            #     {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
            # )
            # print("*" * 100)

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

                # Generar la respuesta incluyendo la información de paginación
                response_data = {
                    "momentos": moments_list,
                    "elementos_totales": total_elements
                }
                return response_data
            
            else:
                return None
    
    except Exception as exception:

        # print("*" * 100)
        # logging.error(
        #     {
        #         "error": f"Error: {exception}. Contacta con el administrador"
        #     }
        # )
        # print("*" * 100)

        return None


# Función para obtener la lista preguntas de un momento *************************************************
def obtener_preguntas_por_momento(id_momento: str):

    try:
        consult = db.get_db()
        cursor = consult.get("cursor")
        connection = consult.get("connection")

        # Consulta para obtener los momentos de una competencia en un assessment
        query = """
            SELECT id, pregunta FROM assessments.preguntas 
            WHERE id_momento = %s 
            AND eliminado = False 
            ORDER BY fecha_de_registro ASC
        """
        data = (id_momento,)

        cursor.execute(query, data)
        db_question = cursor.fetchall()

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        # Consulta para obtener la cantidad total de elementos
        count_query = """
            SELECT COUNT(*) FROM assessments.preguntas 
            WHERE id_momento = %s 
            AND eliminado = False
        """
        count_data = (id_momento,)

        cursor.execute(count_query, count_data)
        total_elements = cursor.fetchone()[0]

        if connection:
            cursor.close()
            connection.close()
            # print("*" * 100)
            # logging.warning(
            #     {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
            # )
            # print("*" * 100)

            if len(db_question) > 0:
                questions_list = []
                # Crear un diccionario con las llaves y valores
                for db_question in db_question:
                    question = {}
                    for j, column in enumerate(column_names):
                        # Valido si hay booleanos o nulos para no convertirlos a string
                        value = db_question[j] 

                        is_bool = isinstance(value, (bool, int, float, complex))
                        is_none = value is None

                        question[column] = value if (is_bool or is_none) else str(value)
                    
                    questions_list.append(question)

                # Generar la respuesta incluyendo la información de paginación
                response_data = {
                    "preguntas": questions_list,
                    "elementos_totales": total_elements
                }
                return response_data
            
            else:
                return None
    
    except Exception as exception:

        # print("*" * 100)
        # logging.error(
        #     {
        #         "error": f"Error: {exception}. Contacta con el administrador"
        #     }
        # )
        # print("*" * 100)

        return None


# Función para obtener la lista preguntas de un momento *************************************************
def obtener_respuesta_pregunta(id_momento: str):

    try:
        consult = db.get_db()
        cursor = consult.get("cursor")
        connection = consult.get("connection")

        # Consulta para obtener los momentos de una competencia en un assessment
        query = """
            SELECT id, pregunta FROM assessments.preguntas 
            WHERE id_momento = %s 
            AND eliminado = False 
            ORDER BY fecha_de_registro ASC
        """
        data = (id_momento,)

        cursor.execute(query, data)
        db_question = cursor.fetchall()

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        # Consulta para obtener la cantidad total de elementos
        count_query = """
            SELECT COUNT(*) FROM assessments.preguntas 
            WHERE id_momento = %s 
            AND eliminado = False
        """
        count_data = (id_momento,)

        cursor.execute(count_query, count_data)
        total_elements = cursor.fetchone()[0]

        if connection:
            cursor.close()
            connection.close()
            # print("*" * 100)
            # logging.warning(
            #     {"message": "=> Conexión a Base de Datos Cerrada", "statusCode": 200}
            # )
            # print("*" * 100)

            if len(db_question) > 0:
                questions_list = []
                # Crear un diccionario con las llaves y valores
                for db_question in db_question:
                    question = {}
                    for j, column in enumerate(column_names):
                        # Valido si hay booleanos o nulos para no convertirlos a string
                        value = db_question[j] 

                        is_bool = isinstance(value, (bool, int, float, complex))
                        is_none = value is None

                        question[column] = value if (is_bool or is_none) else str(value)
                    
                    questions_list.append(question)

                # Generar la respuesta incluyendo la información de paginación
                response_data = {
                    "preguntas": questions_list,
                    "elementos_totales": total_elements
                }
                return response_data
            
            else:
                return None
    
    except Exception as exception:

        # print("*" * 100)
        # logging.error(
        #     {
        #         "error": f"Error: {exception}. Contacta con el administrador"
        #     }
        # )
        # print("*" * 100)

        return None

