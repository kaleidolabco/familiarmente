import base64

def codificar_clave_usuario ( password: str ) -> str:
    clave = password.encode("utf-8")
    clave = base64.b64encode(clave).decode("utf-8")
    return clave

def decodificar_clave_usuario(clave_codificada: str) -> str:
    clave_bytes = base64.b64decode(clave_codificada)
    clave_original = clave_bytes.decode("utf-8")
    return clave_original
