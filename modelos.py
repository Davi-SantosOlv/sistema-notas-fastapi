from pydantic import BaseModel

class Aluno(BaseModel):
  TOTAL_ALUNOS = 0
  
  id: int
  nome: str
  classe: str

  def __init__(self, nome: str, classe: str):
    TOTAL_ALUNOS += 1
    self.id = TOTAL_ALUNOS
    self.nome = nome
    self.classe = classe

class Prova(BaseModel):
  id_aluno: int
  disciplina: str
  valor: float
  nota: float

  def __init__(self, id_aluno: int, disciplina: str, valor: float, nota: float):
    self.id_aluno = id_aluno
    self.disciplina = disciplina
    self.valor = valor
    self.nota = nota