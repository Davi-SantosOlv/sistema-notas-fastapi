from fastapi import APIRouter
from modelos import Aluno
import json_dao as dao

alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/")
async def buscar_alunos():
  return dao.get_alunos()

@alunos_router.post("/")
async def cadastrar_aluno(aluno: Aluno):
  return dao.post_aluno(aluno)

@alunos_router.put("/")
async def editar_aluno(aluno: Aluno):
  return dao.put_aluno(aluno)

@alunos_router.delete("/")
async def excluir_aluno(id: int):
  return dao.delete_aluno(id)