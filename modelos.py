from pydantic import BaseModel

class Aluno(BaseModel): 
  id: int
  nome: str
  classe: str

class Prova(BaseModel):
  id_aluno: int
  disciplina: str
  valor: float
  nota: float