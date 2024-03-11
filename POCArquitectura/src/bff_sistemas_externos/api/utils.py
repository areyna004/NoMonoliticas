import requests
from flask import request

def revisar_token(token):
    url_usuarios = 'http://10.182.0.3:5000/autenticador/usuario'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url_usuarios, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False
    
def get_token():
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        partes = authorization_header.split()
        if len(partes) == 2 and partes[0] == 'Bearer':
            token = partes[1]
            return token
        else:
            return None
    else:
        return None
