from fastapi import APIRouter

alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/")
async def buscar_alunos():
  return {"mensagem": "Essa rota retorna todos os alunos"}


@alunos_router.post("/")
async def cadastrar_aluno():
  pass

@alunos_router.put("/")
async def editar_aluno():
  pass

@alunos_router.delete("/")
async def excluir_aluno():
  pass