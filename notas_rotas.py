from fastapi import APIRouter

notas_router = APIRouter(prefix="/notas", tags=["notas"])

@notas_router.get("/")
async def exibir_notas():
  return {"mensagem": "Essa rota retorna todos os alunos"}


@notas_router.post("/")
async def cadastrar_nota():
  pass

@notas_router.put("/")
async def editar_nota():
  pass

@notas_router.delete("/")
async def excluir_nota():
  pass