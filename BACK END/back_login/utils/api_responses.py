
def generate_response(
        message = "La solicitud se ha procesado correctamente",
        data = None
):
    return  {
                "success": True,
                "message": message,
                "data": data,
            }


def generate_error(
        message = "La solicitud ha fallado",
        code = 400,
        error = ""
):
    return  {
                "success": False,
                "message": message,
                "error": { 
                    "code": code, 
                    "error": error
                }
            }


# def generate_controller_response(
#         message = "La solicitud se ha procesado correctamente",
#         data = None
# ):
#     return  {
#                 "success": True,
#                 "message": message,
#                 "data": data,
#             }

# def generate_controller_error(
#         message = "La solicitud ha fallado",
# ):
#     return  {
#                 "success": False,
#                 "message": message,
#                 "data": None
#             }