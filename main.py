from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Sarlavha', version='0.0.1', description='Sarlavha')

users = [{"login": "test", "password": "test"}]


class LoginBody(BaseModel):
    login: str
    password: str


@app.post("/login/")
async def login(body: LoginBody):
    for user in users:
        if user['login'] == body.login and user['password'] == body.password:
            return user
    return {"error": "Invalid Credentials"}


# @app.get('/users', description='all users')
# async def root():
#     return users


# @app.get('/', description='all users')
# async def root():
#     return {'status': 'ok'}


# @app.post('/create/')
# async def create(item: dict):
#     users.append(item)
#     return users[-1]