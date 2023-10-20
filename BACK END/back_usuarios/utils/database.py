import psycopg2
import logging
import utils.constants as constants

def get_db():
    try:
        db_data = constants.get_db_data('prod')

        connection = psycopg2.connect(
            host = db_data['db_host'],
            user = db_data['db_user'],
            password = db_data['db_password'],
            database = db_data['db_database'],
            port = db_data['db_port']
        )

        cursor = connection.cursor()

        print("*" * 100)
        print("connection & cursor")

        logging.debug({"cursor": cursor, "connection": connection})

        return {"cursor": cursor, "connection": connection} 

    except (Exception, psycopg2.Error) as error:
        print("*" * 100)
        logging.error(
            {
                "message": "=> Error obteniendo la información de la base de datos",
                "error": f"Contacte al administrador: {error}",
                "statusCode": 401,
            }
        )
        print("*" * 100)
        raise NameError(f"Contacte al administrador: {error}")