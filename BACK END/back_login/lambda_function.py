import logging
import utils.api_responses as api_responses
import controllers.controller_login as controller_login
import utils.authentication as auth

def lambda_handler(event, context):

    # print('*' * 100)
    # print('event' , event)
    # print('context' , context)
    # print('*' * 100)

    try:

        if ( event["request_data"]["type_action"] == "login" 
            and event["request_data"]["data"]
        ):
            try:
                login_data = event["request_data"]["data"]

                result = controller_login.login(login_data)

                if(result["success"] == False):
                    return result
                else:
                    user_data = result["data"]

                    token = auth.generate_token(user_data)

                    return api_responses.generate_response("Inicio de sesión correcto", {
                        "token": token,
                        "user_data": user_data
                    })

            except Exception as exception:
                raise NameError(f"Ha ocurrido un error al iniciar sesión. {exception}")

        elif ( event["request_data"]["type_action"] == "validate_token" 
            and event["request_data"]["data"]
        ):
            try:
                validation_data = event["request_data"]["data"]
                token = validation_data["token"]

                result = auth.validate_token(token)

                return result

                # if(result["success"] == False):
                    
                # else:
                #     user_data = result["data"]

                #     token = auth.generate_token(user_data)

                #     return api_responses.generate_response("Inicio de sesión correcto", {
                #         "token": token,
                #         "user_data": user_data
                #     })

            except Exception as exception:
                raise NameError(f"Ha ocurrido un error al iniciar sesión. {exception}") 

        # if event["headers"]["Authorization"]:
            
        #     try:
        #         print('Autorizacion', event["headers"]["Authorization"])
        #         return api_responses.generate_response()

        #     except Exception as exception:
        #         print("*" * 100)
        #         logging.error(
        #             {
        #                 "message": f"Error: {exception}, contacta con el administrador",
        #                 "status": "failed",
        #             }
        #         )
        #         print("*" * 100)

        #         raise NameError(f"Error: {exception}, contacta con el administrador")
        
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
        