from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message

from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', status_code=HTTPStatus.OK, response_model=Message)
def read_html():
    return HTMLResponse(content='<h1>Olá Mundo!</h1>', status_code=200)
