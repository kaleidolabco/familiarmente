import logging
import utils.api_responses as api_responses
import utils.authentication as auth

import controllers.controller_cargos as controller_cargos
import controllers.controller_postulaciones as controller_postulaciones
import controllers.controller_assessments_cargos as controller_assessments_cargos
import controllers.controller_calificacion_final as controller_calificacion_final

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

                    # CARGOS *********************************************************
                    if type_action == "add_job" :
                        return controller_cargos.agregar_cargo(data)
                    
                    elif type_action == "get_job" :
                        return controller_cargos.obtener_cargo(data)
                    
                    elif type_action == "get_all_jobs" :
                        return controller_cargos.obtener_cargos_por_administrador(data) 

                    elif type_action == "get_all_published_jobs" :
                        return controller_cargos.obtener_cargos_publicados(data)
                    
                    elif type_action == "search_by_name_jobs" :
                        return controller_cargos.buscar_cargos_por_nombre(data)
                    
                    elif type_action == "search_by_name_published_jobs" :
                        return controller_cargos.buscar_cargos_publicados_por_nombre(data)
                    
                    elif type_action == "update_job" :
                        return controller_cargos.actualizar_cargo(data)
                    
                    elif type_action == "delete_job" :
                        return controller_cargos.eliminar_cargo(data)  
                    
                    # POSTULACIONES *********************************************************
                    elif type_action == "apply_to_job" :
                        return controller_postulaciones.agregar_postulacion(data)  
                    
                    elif type_action == "get_job_application" :
                        return controller_postulaciones.obtener_postulacion(data) 
                    
                    elif type_action == "get_all_job_applications" :
                        return controller_postulaciones.obtener_postulaciones_por_cargo(data) 
                    
                    elif type_action == "get_all_job_applications_candidate" :
                        return controller_postulaciones.obtener_postulaciones_por_candidato(data)
                    
                    elif type_action == "search_job_applications" :
                        return controller_postulaciones.buscar_postulaciones_por_nombre_de_candidato(data) 
                    
                    elif type_action == "update_job_application" :
                        return controller_postulaciones.actualizar_postulacion(data)
                    
                    elif type_action == "update_job_application_postulated" :
                        return controller_postulaciones.actualizar_postulacion_a_postulado(data) 
                    
                    elif type_action == "update_job_application_completed_assessment" :
                        return controller_postulaciones.actualizar_postulacion_a_assessment_completado(data) 
                    
                    elif type_action == "update_job_application_evaluated" :
                        return controller_postulaciones.actualizar_postulacion_a_evaluado(data) 
                    
                    elif type_action == "update_job_application_completed_proccess" :
                        return controller_postulaciones.actualizar_postulacion_a_proceso_finalizado(data) 
                    
                    elif type_action == "delete_job_application" :
                        return controller_postulaciones.eliminar_postulacion(data) 
                    
                    # ASSESSMENT DEL CARGO *********************************************************
                    elif type_action == "get_job_assessment_data" :
                        return controller_assessments_cargos.obtener_assessment_del_cargo(data) 
                    
                    # CALIFICACIÓN FINAL *********************************************************
                    elif type_action == "get_final_qualification" :
                        return controller_calificacion_final.obtener_calificacion_final(data) 
                    
                    elif type_action == "get_final_ai_resume" :
                        return controller_calificacion_final.obtener_resumen_de_observaciones_con_ia(data) 
                    
                    elif type_action == "update_job_application_final_qualification" :
                        return controller_calificacion_final.actualizar_datos_Postulacion_calificacion_final(data)

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
        