from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
import utils.constants as constants
import utils.api_responses as api_responses


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days=days)
    return new_date


def generate_token(data: dict):
    token = encode(
        payload={**data, "exp": expire_date(constants.ACCESS_TOKEN_EXPIRE_DAYS)},
        key=constants.JWT_SECRET_KEY,
        algorithm=constants.JWT_ALGORITHM,
    )
    return token


def validate_token(token):
    try:
        decoded_data =  decode(
            token,
            key=constants.JWT_SECRET_KEY,
            algorithms=[constants.JWT_ALGORITHM],
        )

        return api_responses.generate_response("Token válido", decoded_data)
    except exceptions.DecodeError:
        return api_responses.generate_error("El token es inválido", 401, "El token es inválido")

    except exceptions.ExpiredSignatureError:
        return api_responses.generate_error("El token es inválido", 401, "El token ha expirado")
