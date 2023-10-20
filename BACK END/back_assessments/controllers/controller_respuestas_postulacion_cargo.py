import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import controllers.controller_respuestas_candidatos as controller_respuestas_candidatos
import controllers.controller_evaluaciones_respuestas as controller_evaluaciones_respuestas


# Función para obtener los datos del assessment para aplicar a un cargo *************************
def obtener_respuestas_del_candidato(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_cargo = info["id_cargo"]
    id_usuario_candidato = info["id_usuario_candidato"]

    query = """
        SELECT p.id_assessment as id, a.nombre
        FROM cargos.postulaciones AS p
        JOIN assessments.assessments AS a
        ON p.id_assessment = a.id
        WHERE p.id_cargo = %s
        AND p.id_usuario_candidato = %s
        AND p.eliminado = false;
    """

    data = (id_cargo, id_usuario_candidato)

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
                                if preguntas:
                                    for pregunta in preguntas["preguntas"]: 
                                        respuesta = obtener_respuesta_candidato_pregunta(id_usuario_candidato, pregunta["id"])
                                        pregunta["respuesta"] = respuesta 

                                momento["datos_preguntas"] = preguntas
                                
    
            data["datos_competencias"] = competencias

            # Obtengo la calificacion promedio

            return api_responses.generate_response("Datos de respuestas obtenidos de manera exitosa", data)
        
        else:
            return api_responses.generate_error("Error al obtener los datos de las respuestas", 401, "No hay registro de respuestas del usuario especificado al cargo")


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
            SELECT id, pregunta FROM preguntas.preguntas 
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
            SELECT COUNT(*) FROM preguntas.preguntas 
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


# Función para obtener los datos de una respuesta a pregunta  **********************************************************
def obtener_respuesta_candidato_pregunta(id_usuario_candidato: str, id_pregunta: str):
    try:
        consult = db.get_db()
        cursor = consult.get("cursor")
        connection = consult.get("connection")

        exists = controller_respuestas_candidatos.validar_si_existe(id_usuario_candidato, id_pregunta)

        if exists == False:
            if connection:
                cursor.close()
                connection.close()
                print("*" * 100)
                logging.warning(
                    {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
                )
                print("*" * 100)

            return None


        query = """
            SELECT id, video_respuesta_usuario, fecha_de_registro AS fecha_de_respuesta 
            FROM respuestas.respuestas 
            WHERE id_usuario_candidato = %s 
            AND id_pregunta = %s
            AND eliminado = False
        """

        data = (id_usuario_candidato, id_pregunta)

        cursor.execute(query, data)
        deb_answer = cursor.fetchall()

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

            if len(deb_answer) > 0:
                # Crear un diccionario con las llaves y valores
                data = {}
                for i, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = deb_answer[0][i] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    data[column] = value if (is_bool or is_none) else str(value)

                id_respuesta_candidato = data.get("id", None)

                if id_respuesta_candidato:
                    evaluacion_respuesta = obtener_evaluacion_respuesta_candidato(id_respuesta_candidato)
                    data["calificacion"] = evaluacion_respuesta
                else:
                    data["calificacion"] = None

                return data
            
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



# Función para obtener los datos de evaluacion de una respuesta  **********************************************************
def obtener_evaluacion_respuesta_candidato(id_respuesta_candidato: str):
    try:
        consult = db.get_db()
        cursor = consult.get("cursor")
        connection = consult.get("connection")

        exists = controller_evaluaciones_respuestas.validar_si_existe(id_respuesta_candidato)

        if exists == False:
            if connection:
                cursor.close()
                connection.close()
                print("*" * 100)
                logging.warning(
                    {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
                )
                print("*" * 100)

            return None


        # query = """
        #     SELECT promedio_de_calificacion 
        #     FROM respuestas.evaluaciones_respuestas 
        #     WHERE id_respuesta_candidato = %s 
        #     AND eliminado = False
        # """
        query = """
            select er.promedio_de_calificacion, pre.umbral_minimo_calificacion, pre.umbral_maximo_calificacion
            from respuestas.evaluaciones_respuestas er
            INNER JOIN respuestas.respuestas rc ON er.id_respuesta_candidato = rc.id
            INNER JOIN preguntas.preguntas pre ON rc.id_pregunta = pre.id
            WHERE er.id_respuesta_candidato = %s
            AND er.eliminado = False;
        """

        data = (id_respuesta_candidato, )

        cursor.execute(query, data)
        db_evaluation = cursor.fetchall()

        # print('*'*1000)
        # print(db_evaluation)

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

            if len(db_evaluation) > 0:
                # Crear un diccionario con las llaves y valores
                data = {}
                for i, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_evaluation[0][i] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    data[column] = value if (is_bool or is_none) else str(value)

                return data
            
            else:
                return None
            
    except Exception as exception:

        return None
