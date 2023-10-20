# FALTA VALIDAR QUE EL ADMIN QUE CONSULTA POR UN ASSESSMENT O UN CARGO ES EL CREADOR O
# TIENE LOS PERMISOS PARA OBTENER LA INFORMACIÓN

import logging
import utils.api_responses as api_responses
import utils.authentication as auth

import controllers.controller_competencias as controller_competencias
import controllers.controller_assessments as controller_assessments
import controllers.controller_competencias_assessments as controller_competencias_assessments
import controllers.controller_momentos as controller_momentos
import controllers.controllers_preguntas.controller as controller_preguntas
import controllers.controller_avatares_virtuales as controller_avatares_virtuales
import controllers.controller_respuestas_candidatos as controller_respuestas_candidatos
import controllers.controller_respuestas_postulacion_cargo as controller_respuestas_postulacion_cargo
import controllers.controller_evaluaciones_respuestas as controller_evaluaciones_respuestas
import controllers.controllers_preguntas.controller_palabras_clave as controller_palabras_clave
import controllers.controllers_preguntas.controller_descarriladores as controller_descarriladores
import controllers.controller_ia as controller_ia

def lambda_handler(event, context):

    # print('*' * 100)
    # print('event' , event)
    # print('context' , context)
    # print('*' * 100)

    try:    

        if event["headers"]["Authorization"]:

            try:
                validation_token = auth.validate_token( event["headers"]["Authorization"] )

                if validation_token ["success"] == True:

                    type_action = event["request_data"]["type_action"]
                    data = event["request_data"]["data"]

                    # COMPETENCIAS *****************************************************************
                    if type_action == "add_skill" :
                        return controller_competencias.agregar_competencia(data)
                    
                    elif type_action == "get_skill" :
                        return controller_competencias.obtener_competencia(data)
                    
                    elif type_action == "get_all_skills" :
                        return controller_competencias.obtener_competencias_por_administrador(data)
                    
                    elif type_action == "search_by_name_skills" :
                        return controller_competencias.buscar_competencias_por_nombre(data)
                    
                    elif type_action == "update_skill" :
                        return controller_competencias.actualizar_competencia(data)
                    
                    elif type_action == "delete_skill" :
                        return controller_competencias.eliminar_competencia(data)  
                    
                    # ASSESSMENTS *****************************************************************
                    elif type_action == "add_assessment" :
                        return controller_assessments.agregar_assessment(data)
                    
                    elif type_action == "get_assessment" :
                        return controller_assessments.obtener_assessment(data)
                    
                    elif type_action == "get_all_assessments" :
                        return controller_assessments.obtener_assessments_por_administrador(data)
                    
                    elif type_action == "search_by_name_assessments" :
                        return controller_assessments.buscar_assessments_por_nombre(data)
                    
                    elif type_action == "update_assessment" :
                        return controller_assessments.actualizar_assessment(data)
                    
                    elif type_action == "delete_assessment" :
                        return controller_assessments.eliminar_assessment(data)  
                    
                    # COMPETENCIAS - ASSESSMENTS *****************************************************
                    elif type_action == "add_skill_to_assessment" :
                        return controller_competencias_assessments.agregar_competencia_al_assessment(data)
                    
                    elif type_action == "get_all_skill_of_assessment" :
                        return controller_competencias_assessments.obtener_competencias_por_assessment(data)
                    
                    elif type_action == "delete_skill_from_assessment" :
                        return controller_competencias_assessments.eliminar_competencia_del_assessment(data)
                    
                    # MOMENTOS *****************************************************
                    elif type_action == "add_moment" :
                        return controller_momentos.agregar_momento(data)
                    
                    elif type_action == "get_moment" :
                        return controller_momentos.obtener_momento(data)
                    
                    elif type_action == "get_all_moments_of_skill" :
                        return controller_momentos.obtener_momentos_por_competencia(data)
                    
                    elif type_action == "update_moment" :
                        return controller_momentos.actualizar_momento(data)
                    
                    elif type_action == "delete_moment" :
                        return controller_momentos.eliminar_momento(data)
                    
                    # PREGUNTAS *****************************************************
                    elif type_action == "add_question" :
                        return controller_preguntas.agregar_pregunta(data)
                    
                    elif type_action == "get_question" :
                        return controller_preguntas.obtener_pregunta(data)
                    
                    elif type_action == "get_question_candidate" :
                        return controller_preguntas.obtener_pregunta_candidato(data)
                    
                    elif type_action == "get_all_questions_of_moment" :
                        return controller_preguntas.obtener_preguntas_por_momento(data)
                    
                    elif type_action == "update_question" :
                        return controller_preguntas.actualizar_pregunta(data)
                    
                    elif type_action == "delete_question" :
                        return controller_preguntas.eliminar_pregunta(data)
                    
                    # AVATARES VIRTUALES *****************************************************
                    elif type_action == "get_avatares" :
                        return controller_avatares_virtuales.obtener_avatares_virtuales(data)
                    
                    elif type_action == "get_avatar" :
                        return controller_avatares_virtuales.obtener_avatar_virtual(data)
                    
                    # RESPUESTAS CANDIDATOS ***************************************************
                    elif type_action == "add_answer_candidate" :
                        return controller_respuestas_candidatos.agregar_respuesta_candidato(data)
                    
                    elif type_action == "get_answer_candidate" :
                        return controller_respuestas_candidatos.obtener_respuesta_candidato(data)
                    
                    elif type_action == "get_all_answers_candidate" :
                        return controller_respuestas_postulacion_cargo.obtener_respuestas_del_candidato(data)
                    
                    elif type_action == "update_answer_candidate" :
                        return controller_respuestas_candidatos.actualizar_respuesta_candidato(data)
                    
                    elif type_action == "delete_answer_candidate" :
                        return controller_respuestas_candidatos.Eliminar_respuesta_candidato(data)
                    

                    # EVALUACIONES RESPUESTAS ***************************************************
                    elif type_action == "add_evaluation" :
                        return controller_evaluaciones_respuestas.agregar_evaluacion_respuesta(data)
                    
                    elif type_action == "get_evaluation" :
                        return controller_evaluaciones_respuestas.obtener_datos_evaluacion_respuesta(data)
                    
                    elif type_action == "update_evaluation" :
                        return controller_evaluaciones_respuestas.actualizar_evaluacion_respuesta(data)

                    # ARCHIVOS ***************************************************************
                    elif type_action == "get_url_upload_question_video" :
                        return controller_preguntas.obtener_url_subida_video_pregunta(data)
                    
                    elif type_action == "get_url_upload_answer_video_candidate" :
                        return controller_respuestas_candidatos.obtener_url_subida_video_respuesta_candidato(data)
                    

                    # PALABRAS CLAVE ***************************************************************
                    elif type_action == "add_keyword" :
                        return controller_palabras_clave.agregar_palabra_clave(data)
                    
                    elif type_action == "delete_keyword" :
                        return controller_palabras_clave.eliminar_palabra_clave(data)
                    
                    elif type_action == "get_all_question_keywords" :
                        return controller_palabras_clave.obtener_palabras_clave_de_pregunta(data)
                    
                    # DESCARRILADORES ***************************************************************
                    elif type_action == "add_derailer" :
                        return controller_descarriladores.agregar_descarrilador(data)
                    
                    elif type_action == "delete_derailer" :
                        return controller_descarriladores.eliminar_descarrilador(data)
                    
                    elif type_action == "get_all_question_derailers" :
                        return controller_descarriladores.obtener_descarriladores_de_pregunta(data)

                    # INTELIGENCIA ARTIFICIAL ******************************************************
                    elif type_action == "transcribe_answer" :
                        return controller_ia.transcribir_respuesta_candidato(data)
                    
                    elif type_action == "generate_ai_answer" :
                        return controller_ia.obtener_respuesta_de_la_ia(data)
                    
                    elif type_action == "generate_ai_qualification" :
                        return controller_ia.obtener_calificacion_de_la_ia(data)

                else:
                    return validation_token
                

            except Exception as exception:
                print("*" * 100)
                logging.error(
                    {
                        "message": f"Error: {exception}, contacta con el administrador",
                        "status": "failed",
                    }
                )
                print("*" * 100)

                raise NameError(f"Error: {exception}, contacta con el administrador")
        
    except Exception as exception:

        print("*" * 100)
        logging.error(
            {
                "code": 400,
                "error": f"Error: {exception}. Contacta con el administrador"
            }
        )
        print("*" * 100)

        return api_responses.generate_error(
            "Error al procesar la solicitud ",
            400,
            f"Error: {exception}. Contacta con el administrador"
        )
        