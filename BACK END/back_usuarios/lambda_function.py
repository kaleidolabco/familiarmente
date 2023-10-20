import logging
import utils.api_responses as api_responses
import controllers.controller_usuarios_administradores as controller_administradores
import controllers.controller_usuarios_candidatos as controller_candidatos
import controllers.controller_parametros as controller_parametros
import utils.authentication as auth 


def lambda_handler(event, context):

    # print('*' * 100)
    # print('event' , event)
    # print('context' , context)
    # print('*' * 100)

    try:

        type_action = event["request_data"]["type_action"]
        data = event["request_data"]["data"]

        if type_action == "add_admin":
            try:
                result = controller_administradores.agregar_usuario(dict(data))
                return result

            except Exception as exception:
                raise NameError(f"Ha ocurrido un error al registrar el usuario. {exception}")
            
        elif type_action == "add_candidate":
            try:
                result = controller_candidatos.agregar_usuario(dict(data))
                return result

            except Exception as exception:
                raise NameError(f"Ha ocurrido un error al registrar el usuario. {exception}")
        
        elif type_action == "get_by_name_parameters":
            try:
                result = controller_parametros.obtener_parametros_por_nombre(dict(data))
                return result

            except Exception as exception:
                raise NameError(f"Ha ocurrido un error al obtener los parámetros. {exception}")
        
        elif type_action == "get_parameter":
            try:
                result = controller_parametros.obtener_parametro(dict(data))
                return result

            except Exception as exception:
                raise NameError(f"Ha ocurrido un error al obtener los datos del parámetro. {exception}")
            

        if event["headers"]["Authorization"]:

            try:
                validation_token = auth.validate_token( event["headers"]["Authorization"] )

                if validation_token ["success"] == True:

                    type_action = event["request_data"]["type_action"]
                    data = event["request_data"]["data"]

                    if type_action == "get_user_admin" :
                        return controller_administradores.obtener_usuario(data)
                    
                    elif type_action == "update_user_admin" :
                        return controller_administradores.actualizar_usuario(data)
                    
                    elif type_action == "get_user_candidate" :
                        return controller_candidatos.obtener_usuario(data)
                    
                    elif type_action == "get_user_candidate_profile" :
                        return controller_candidatos.obtener_perfil_usuario(data)
                    
                    elif type_action == "update_user_candidate" :
                        return controller_candidatos.actualizar_usuario(data)
                    
                    elif type_action == "get_url_upload_profile_photo_candidate" :
                        return controller_candidatos.obtener_url_subida_foto_usuario(data)
                    
                    elif type_action == "get_url_upload_curriculum_candidate" :
                        return controller_candidatos.obtener_url_subida_hoja_de_vida_usuario(data)

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
        