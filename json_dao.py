import json

def get_alunos():
  with open("database.json", "r") as arq:
    db = json.load(arq)
    alunos = db["alunos"]
  return alunos

def post_aluno():
  pass

def put_aluno():
  pass

def delete_aluno():
  pass

def get_provas():
  with open("database.json", "r") as arq:
    db = json.load(arq)
  provas = db["provas"]
  return provas

def post_prova():
  pass

def put_prova():
  pass

def delete_prova():
  pass