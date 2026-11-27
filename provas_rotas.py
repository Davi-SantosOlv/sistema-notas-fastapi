from fastapi import APIRouter
from modelos import Prova
import json_dao as dao

provas_router = APIRouter(prefix="/provas", tags=["provas"])

@provas_router.get("/")
async def exibir_provas():
  """
  Esta função retorna todas as provas cadstradas na base de dados.
  """
  return dao.get_provas()

@provas_router.post("/")
async def cadastrar_provas(prova: Prova):
  """
  Esta função cadastra uma nova prova na base de dados. É necessário preencher as informações da prova no Schema. Não há validações para as digitações além da fornecida pelo próprio FastAPI.
  """
  return dao.post_prova(prova)

@provas_router.delete("/")
async def excluir_provas(id_aluno: int, disciplina: str):
  """
  Esta função exclui uma prova cadastrada da base de dados. É necessário informar o ID do aluno e a disciplina da prova como parâmetros. O sistema valida ambos, e só então faz a exclusão. Se não houver um registro condizente com os dois parâmetros o sistema envia uma mensagem de 'Prova não encontrada', mas continua retornando o código 200.
  """
  return dao.delete_prova(id_aluno, disciplina)