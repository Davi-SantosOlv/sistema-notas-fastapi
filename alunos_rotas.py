from fastapi import APIRouter
from modelos import Aluno
import json_dao as dao

alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/")
async def buscar_alunos():
  """
  Esta função retorna todos os alunos cadstrados na base de dados.
  """
  return dao.get_alunos()

@alunos_router.post("/")
async def cadastrar_aluno(aluno: Aluno):
  """
  Esta função cadastra um novo aluno na base de dados. É necessário preencher as informações do aluno no Schema. Não há validações para as digitações além da fornecida pelo próprio FastAPI.
  """
  return dao.post_aluno(aluno)

@alunos_router.put("/")
async def editar_aluno(aluno: Aluno):
  """
  Esta função edita as informações de um aluno cadastrado. É necessário preencher as informações do aluno no Schema. O sistema valida o ID digitado, e substitui o antigo cadastro pelo novo. Se o ID for inválido o sistema envia uma mensagem de 'Aluno não encontrado', mas continua retornando o código 200.
  """
  return dao.put_aluno(aluno)

@alunos_router.delete("/")
async def excluir_aluno(id: int):
  """
  Esta função exclui um aluno cadastrado da base de dados. É necessário informar o ID do aluno como um parâmetro. O sistema valida o ID digitado, e só então faz a exclusão. Se o ID for inválido o sistema envia uma mensagem de 'Aluno não encontrado', mas continua retornando o código 200.
  """
  return dao.delete_aluno(id)