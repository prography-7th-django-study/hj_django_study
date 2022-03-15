from datetime import datetime, timedelta

import jwt
from config.settings import SECRET_KEY

def encode_jwt(data):
    data = jwt.encode(data, SECRET_KEY, 'HS256')
    return data


def decode_jwt(access_token):
    data = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
    print(data)
    return data

def generate_access_token(email):
    iat = datetime.now()
    exp = iat + timedelta(days=7)

    data = {
        "iat": iat.timestamp(),
        "exp": exp.timestamp(),
        "aud": email,
    }

    return encode_jwt(data)