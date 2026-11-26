from fastapi import APIRouter
from modelos import Prova
import json_dao as dao

provas_router = APIRouter(prefix="/provas", tags=["provas"])

@provas_router.get("/")
async def exibir_provas():
  return dao.get_provas()

@provas_router.post("/")
async def cadastrar_provas(prova: Prova):
  return dao.post_prova(prova)

@provas_router.delete("/")
async def excluir_provas(id_aluno: int, disciplina: str):
  return dao.delete_prova(id_aluno, disciplina)