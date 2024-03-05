import requests
from flask import request

def revisar_token():
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        partes = authorization_header.split()
        if len(partes) == 2 and partes[0] == 'Bearer':
            token = partes[1]
            url_otra_api = 'http://127.0.0.1:3000/autenticador/usuario'
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url_otra_api, headers=headers)
            if response.status_code == 200:
                return token
            else:
                return None
        else:
            return None
    else:
        return None
