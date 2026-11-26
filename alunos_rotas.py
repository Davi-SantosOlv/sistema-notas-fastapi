from fastapi import APIRouter
import json_dao as dao

alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/")
async def buscar_alunos():
  return dao.get_alunos()


@alunos_router.post("/")
async def cadastrar_aluno():
  pass

@alunos_router.put("/")
async def editar_aluno():
  pass

@alunos_router.delete("/")
async def excluir_aluno():
  pass