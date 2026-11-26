from fastapi import FastAPI

app = FastAPI()

from alunos_rotas import alunos_router
from notas_rotas import notas_router

app.include_router(alunos_router)
app.include_router(notas_router)