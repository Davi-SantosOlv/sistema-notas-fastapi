from fastapi import FastAPI

app = FastAPI()

from alunos_rotas import alunos_router
from provas_rotas import provas_router

app.include_router(alunos_router)
app.include_router(provas_router)