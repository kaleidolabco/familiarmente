import boto3

AWS_REGION_NAME = 'us-east-1'
AWS_BUCKET_NAME = 'bucket-scenariojobs'
MAX_ATTEMPTS = 1
URL_EXPIRATION_SECONDS = 600 

def solicitar_url_de_subida_de_archivo(file_type: str, file_path_name: str):

    s3 = boto3.client('s3')

    params = {
        'Bucket': AWS_BUCKET_NAME,
        'Key': file_path_name,
        'Expires': URL_EXPIRATION_SECONDS,
        'ContentType': file_type,
        'ACL': 'public-read'  # Agregar ACL para acceso público
    }

    try:
        upload_url = s3.generate_presigned_url('put_object', Params=params)
        public_url = f'https://{AWS_BUCKET_NAME}.s3.{AWS_REGION_NAME}.amazonaws.com/{file_path_name}'

        return { 
            "url_subida": upload_url, 
            "url_lectura": public_url 
        }
    
    except Exception as e:
        # print('*' * 100)
        # print(e)
        # print('*' * 100)
        return None


def eliminar_archivo(file_path_name: str):

    try:
        s3_client = boto3.client("s3")
        response = s3_client.delete_object(Bucket=AWS_BUCKET_NAME, Key=file_path_name)

        # Verificar el código de respuesta para validar el éxito
        if response['ResponseMetadata']['HTTPStatusCode'] == 204:
            return {
                "success": True, 
                "message":f"El archivo {file_path_name} fue eliminado exitosamente."
            }
        else:
            return {
                "success": False, 
                "message": f"Error al eliminar el archivo {file_path_name}. Código de respuesta: {response['ResponseMetadata']['HTTPStatusCode']}"
            }

    except Exception as e:
        return {
            "success": False, 
            "message":f"Error al eliminar el archivo {file_path_name}: {e}"
        }