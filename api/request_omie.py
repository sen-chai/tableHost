import requests
import json
import os

DB_DIR = './db/development/'
DB_DIR = './db/production/'
API_KEY = os.getenv('OMIE_TEST_KEY')
API_SECRET = os.getenv('OMIE_TEST_SECRET')

# todo PRODUCTION
# API_KEY = os.getenv('OMIE_PROD_KEY')
# API_SECRET = os.getenv('OMIE_PROD_SECRET')
# todo PRODUCTION


def omie_request_one(end_point, call, param):
    url = f"https://app.omie.com.br/api/v1/{end_point}"
    headers = {"Content-Type": "application/json"}
    body = {
        "call": call,
        "app_key": API_KEY,
        "app_secret": API_SECRET,
        "param": [
            param
        ],
    }
    res = requests.post(url, headers=headers, data=json.dumps(body))
    dict = res.json()
    return dict


# * Snake Case
def omie_request_all_pages(PAGE_SIZE,  end_point,  call, extra_params, return_field, case="snake"):
    db = []
    pagina = 1

    # * snake or camel case for basic
    if case == "snake":
        key_pagina = "pagina"
        key_registro_por_pagina = "registros_por_pagina"
        total_de_paginas = "total_de_paginas"
    elif case == "camel":
        key_pagina = "nPagina"
        key_registro_por_pagina = "registrosPorPagina"
        total_de_paginas = "nTotPaginas"

    while True:
        response = omie_request_one(end_point, call, {
            **{key_pagina: pagina,
               key_registro_por_pagina: PAGE_SIZE}, **extra_params})

        total_paginas = response[total_de_paginas]
        db += response[return_field]

        if pagina >= total_paginas:
            return db
        else:
            pagina += 1