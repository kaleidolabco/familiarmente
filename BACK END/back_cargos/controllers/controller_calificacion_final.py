import utils.database as db
import utils.api_responses as api_responses
import logging
from datetime import datetime
import math
import openai
import requests

import utils.constants as constants
import controllers.controller_postulaciones as controller_postulaciones

openai.api_key = constants.OPENAI_API_KEY

# Función para obtener los datos finales de evaluación y promedio
def obtener_calificacion_final(info: dict):
    
    id_usuario_candidato = info.get("id_usuario_candidato", None)
    id_cargo = info.get("id_cargo", None)

    exists = controller_postulaciones.validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        return api_responses.generate_error(
            "Ha ocurrido un error al acceder a la información de las respuestas del candidato.", 
            400, 
            "No se han encontrado registros de una postulación al cargo por parte del candidato"
        )
    
    # Busco primero registros en la base de datos
    db_response = obtener_calificacion_final_base_de_datos(info)
    db_promedio = obtener_calificacion_promedio(id_usuario_candidato, id_cargo)
    
    if db_response is not None and db_promedio is not None:

        premedio_parcial = db_promedio.get("promedio")
        completado = db_promedio.get("calificaciones_completadas")
        
        db_response["calificaciones_completadas"] = completado

        if (db_response["calificacion_final"] is None)  :
            db_response["calificacion_final"] = premedio_parcial

        return api_responses.generate_response(
            "¡Datos de calificaciones obtenidos de manera exitos!", 
            db_response
        )
        
        # if (db_response["calificacion_final"] is not None and 
        #     db_response["observaciones_finales"] is not None and
        #     db_response["mensaje_final_para_candidato"] is not None and
        #     db_response["observaciones_finales_ia"] is not None)  :
            
        #     # db_response["data"]["calificaciones_completadas"] 
        #     return db_response
        
            
    else:
        return api_responses.generate_error(
            "Error al procesar la solicitud ",
            400,
            "No se encontraron datos de postulación. Contacta con el administrador"
        )
    

# Función para obtener la calificación final de la base de datos
def obtener_calificacion_final_base_de_datos(info: dict):
    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    id_usuario_candidato = info.get("id_usuario_candidato")
    id_cargo = info.get("id_cargo")

    # query = "SELECT * FROM cargos.cargos WHERE id = %s AND eliminado = False"
    query = """
        SELECT p.calificacion_final,
        p.observaciones_finales,
        p.mensaje_final_para_candidato,
        p.observaciones_finales_ia,
        par.nombre as estado_de_postulacion
        FROM cargos.postulaciones p
        JOIN parametros par 
        ON par.id = p.id_parametro_estado_de_postulacion_candidato
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

            return data
        
        else:
            return None


# Función para obtener un promedio parcial de todas las calificaciones guardadas
def obtener_calificacion_promedio (id_usuario_candidato, id_cargo):

    query = """
        SELECT p.pregunta,
            p.umbral_minimo_calificacion,
            p.umbral_maximo_calificacion,
            er.promedio_de_calificacion,
            er.calificacion_del_evaluador,
            er.observaciones_del_evaluador,
            er.calificacion_de_ia,
            er.observaciones_de_ia
        FROM assessments.preguntas AS p
        LEFT JOIN respuestas.respuestas_candidatos AS r
            ON p.id = r.id_pregunta
            AND r.id_usuario_candidato = %s
        LEFT JOIN respuestas.evaluaciones_respuestas AS er
            ON r.id = er.id_respuesta_candidato
        WHERE p.id_momento IN (
            SELECT m.id AS id_momento
            FROM assessments.momentos AS m
            WHERE m.id_competencia_assessment IN (
                SELECT ca.id AS id_competencia_assessment
                FROM assessments.competencias_assessments AS ca
                WHERE ca.id_assessment IN (
                    SELECT p.id_assessment
                    FROM cargos.postulaciones AS p
                    WHERE p.id_cargo = %s
                    AND p.id_usuario_candidato = %s
                    AND p.eliminado = false
                )
            )
        );
    """
    data = (
        id_usuario_candidato,
        id_cargo,
        id_usuario_candidato
    )

    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    cursor.execute(query, data)
    db_answers = cursor.fetchall()

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

        answers_list = []

        if len(db_answers) > 0:
            
            # Crear un diccionario con las llaves y valores
            for db_answer in db_answers:
                answer = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_answer[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    answer[column] = value if (is_bool or is_none) else str(value)
                
                answers_list.append(answer)

        else: return None

    if len(answers_list) > 0:

        suma_calificaciones = 0
        calificaciones_terminadas = True

        for calificacion in answers_list:

            if calificacion.get("promedio_de_calificacion") is not None:

                calificacion_mapeada = mapear_calificacion(
                    float(calificacion.get("promedio_de_calificacion")),
                    float(calificacion.get("umbral_minimo_calificacion")),
                    float(calificacion.get("umbral_maximo_calificacion")),
                    0,
                    5
                )

                suma_calificaciones += calificacion_mapeada
            else:
                # Si hay una respuesta sin evaluarse se informa que no se han completado las evaluaciones
                calificaciones_terminadas = False

        promedio_calificacion = round(suma_calificaciones / len(answers_list), 2)
                
        return {
            "promedio" : promedio_calificacion,
            "calificaciones_completadas": calificaciones_terminadas
        }
    
    else :
        return None
    

# Función para convertir escala de calificación a otra
def mapear_calificacion(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


# Función para obtener resumen de observaciones de la IA
def obtener_resumen_de_observaciones_con_ia(info: dict):

    id_usuario_candidato = info.get("id_usuario_candidato", None)
    id_cargo = info.get("id_cargo", None)

    exists = controller_postulaciones.validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        return api_responses.generate_error(
            "Ha ocurrido un error al acceder a la información de las respuestas del candidato.", 
            400, 
            "No se han encontrado registros de una postulación al cargo por parte del candidato"
        )
    

    query = """
        SELECT p.pregunta,
            er.promedio_de_calificacion,
            er.observaciones_del_evaluador,
            er.observaciones_de_ia
        FROM assessments.preguntas AS p
        LEFT JOIN respuestas.respuestas_candidatos AS r
            ON p.id = r.id_pregunta
            AND r.id_usuario_candidato = %s
        LEFT JOIN respuestas.evaluaciones_respuestas AS er
            ON r.id = er.id_respuesta_candidato
        WHERE p.id_momento IN (
            SELECT m.id AS id_momento
            FROM assessments.momentos AS m
            WHERE m.id_competencia_assessment IN (
                SELECT ca.id AS id_competencia_assessment
                FROM assessments.competencias_assessments AS ca
                WHERE ca.id_assessment IN (
                    SELECT p.id_assessment
                    FROM cargos.postulaciones AS p
                    WHERE p.id_cargo = %s
                    AND p.id_usuario_candidato = %s
                    AND p.eliminado = false
                )
            )
        );
    """
    data = (
        id_usuario_candidato,
        id_cargo,
        id_usuario_candidato
    )

    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    cursor.execute(query, data)
    db_answers = cursor.fetchall()

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

        answers_list = []

        if len(db_answers) > 0:
            
            # Crear un diccionario con las llaves y valores
            for db_answer in db_answers:
                answer = {}
                for j, column in enumerate(column_names):
                    # Valido si hay booleanos o nulos para no convertirlos a string
                    value = db_answer[j] 

                    is_bool = isinstance(value, (bool, int, float, complex))
                    is_none = value is None

                    answer[column] = value if (is_bool or is_none) else str(value)
                
                answers_list.append(answer)

        if len(answers_list) > 0:
            calificaciones_terminadas = True

            for calificacion in answers_list:
                if calificacion.get("promedio_de_calificacion") is None:
                    calificaciones_terminadas = False
            
            if calificaciones_terminadas == True:
                return procesar_resumen_observaciones_ia(answers_list, id_usuario_candidato, id_cargo)
            
            else: 
                return api_responses.generate_error(
                    "Ha ocurrido un error al obtener el resumen de observaciones de la IA", 
                    400, 
                    "Aún no se ha completado el proceso de evaluación de las respuestas del candidato"
                )

        else: 
            return api_responses.generate_error(
                "Ha ocurrido un error al obtener el resumen de observaciones de la IA", 
                400, 
                "No se encontraron registros de respuestas del candidato ni evaluaciones"
            )         
            
    return None



def procesar_resumen_observaciones_ia (lista_observaciones, id_usuario_candidato, id_cargo):

    prompt = f"Tengo un objeto JSON con una lista observaciones que se le hicieron a un usuario que respondió las preguntas de un assessment. Dentro del objeto de cada elemento de la lista están: la calificación promedio (promedio_de_calificacion) que los evaluadores le dieron a la respuesta del usuario, las observaciones ante dicha calificación (observaciones_del_evaluador) y unas observaciones dada por inteligencia artificial ante la respuesta del usuario (observaciones_de_ia). Ponte en el rol de un headhunter evaluador del assessment y bríndame conclusiones acerca de las observaciones del evaluador y las observaciones de la inteligencia artificial. Ten en cuenta que las observaciones del evaluador son más confiables que las brindadas por inteligencia artificial. Las conclusiones no deben superar las 200 palabras y deben brindar un corto resumen acerca del desempeño del usuario en el assessment y posibles recomendaciones para mejora del usuario. Evita incluir calificaciones y promedios en el resumen. El objeto JSON es: {lista_observaciones}"

    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.3,
        )

        # print(completion.choices[0].message)
        resumen = completion.choices[0].text.lstrip()
        actualizar_datos_Postulacion_calificacion_final({
            "id_usuario_candidato":id_usuario_candidato,
            "id_cargo":id_cargo,
            "observaciones_finales_ia" : resumen
        })
        return api_responses.generate_response("¡Resumen de observaciones obtenido con éxito!", {"resumen": resumen })
    
    except Exception as exception:
        print("*"*1000)
        print("error gpt: {exception}")
        logging.error(
            "Ha ocurrido un error al obtener la respuesta de la IA",
            f", revisa {exception}"
        )
        return api_responses.generate_error("Ha ocurrido un error al obtener el resumen de observaciones de la IA", 400, "Error al procesar la solicitud")


# Función para actualizar el estado de una postulacion ***************************************************************************
def actualizar_datos_Postulacion_calificacion_final(info: dict):

    id_usuario_candidato = info["id_usuario_candidato"]
    id_cargo = info["id_cargo"]

    exists = controller_postulaciones.validar_si_existe(id_usuario_candidato, id_cargo)

    if exists == False:
        return api_responses.generate_error("Error al actualizar los datos de la postulación", 400, "No se ha encontrado un proceso de postulación del candidato al cargo especificado")

    # Create a list to store the non-null data and the corresponding placeholders
    update_data = []
    placeholders = []

    parameters_to_check = [
        "calificacion_final",
        "observaciones_finales",
        "observaciones_finales_ia",
        "mensaje_final_para_candidato"
    ]

    for parameter in parameters_to_check:
        value = info.get(parameter)
        if value is not None:
            update_data.append(value)
            placeholders.append(f"{parameter} = %s")

    if not update_data:
        return api_responses.generate_error("No se han incluido datos para actualizar", 400, "Se esperaba uno o varios campos para actualizar")

    placeholders_str = ", ".join(placeholders)

    query = f"""UPDATE cargos.postulaciones SET
                {placeholders_str}
                WHERE id_usuario_candidato = %s
                AND id_cargo = %s
                RETURNING id;"""
    data = tuple(update_data + [id_usuario_candidato, id_cargo])

    consult = db.get_db()
    cursor = consult.get("cursor")
    connection = consult.get("connection")

    cursor.execute(query, data)
    connection.commit()
    result = cursor.rowcount

    respuesta_candidato = cursor.fetchone()
    id_postulacion = respuesta_candidato[0]

    if connection:
        cursor.close()
        connection.close()
        print("*" * 100)
        logging.warning(
            {"message": "=> Conexión a Base de Datos Cerrada", "status": "success"}
        )
        print("*" * 100)

    if result == 1:
        return api_responses.generate_response("Datos de evaluación actualizados de manera exitosa!", {"id_postulacion": id_postulacion})
    else:
        return api_responses.generate_error("Ha ocurrido un error al actualizar la evaluación", 400, "Error al actualizar en la base de datos")

