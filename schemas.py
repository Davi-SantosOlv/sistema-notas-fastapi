from pydantic import BaseModel

class Aluno(BaseModel):
  nome: str
  classe: str

class Prova(BaseModel):
  aluno: Aluno
  disciplina: str
  valor: float
  nota: float