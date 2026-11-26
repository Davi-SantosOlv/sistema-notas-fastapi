from fastapi import APIRouter
import json_dao as dao

provas_router = APIRouter(prefix="/provas", tags=["provas"])

@provas_router.get("/")
async def exibir_provas():
  return dao.get_provas()


@provas_router.post("/")
async def cadastrar_provas():
  pass

@provas_router.put("/")
async def editar_provas():
  pass

@provas_router.delete("/")
async def excluir_provas():
  pass