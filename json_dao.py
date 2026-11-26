import json
from modelos import Aluno
from modelos import Prova

def get_alunos():
  with open("database.json", "r") as arq:
    db = json.load(arq)
    alunos = db["alunos"]
  return alunos

def post_aluno(aluno: Aluno):
  with open("database.json", "r") as arq:
    db = json.load(arq)

  novo_aluno = {
    "id": aluno.id,
    "nome": aluno.nome,
    "classe": aluno.classe
  }

  db["alunos"].append(novo_aluno)

  with open("database.json", "w", encoding="utf-8") as arq:
    json.dump(db, arq, indent=2, ensure_ascii=False)
  return {"mensagem": "Aluno cadastrado com sucesso!"}

def put_aluno(aluno: Aluno):
  with open("database.json", "r") as arq:
    db = json.load(arq)
  
  aluno_editado = {
    "id": aluno.id,
    "nome": aluno.nome,
    "classe": aluno.classe
  }

  for i, aluno_cadastrado in enumerate(db["alunos"]):
    if aluno_cadastrado["id"] == aluno_editado["id"]:
      db["alunos"][i] = aluno_editado
      with open("database.json", "w", encoding="utf-8") as arq:
        json.dump(db, arq, indent=2, ensure_ascii=False)
      return {"mensagem": "Alterações concluídas com sucesso!"}

  return {"mensagem": "Aluno não encontrado..."}

def delete_aluno(id: int):
  with open("database.json", "r") as arq:
    db = json.load(arq)
  
  for i, aluno in enumerate(db["alunos"]):
    if aluno["id"] == id:
      del db["alunos"][i]
      with open("database.json", "w", encoding="utf-8") as arq:
        json.dump(db, arq, indent=2, ensure_ascii=False)
      return {"mensagem": "Cadastro excluído com sucesso!"}
  
  return {"mensagem": "Aluno não encontrado..."}

def get_provas():
  with open("database.json", "r") as arq:
    db = json.load(arq)
  provas = db["provas"]
  return provas

def post_prova(prova: Prova):
  with open("database.json", "r") as arq:
    db = json.load(arq)
  
  nova_prova = {
    "id_aluno": prova.id_aluno,
    "disciplina": prova.disciplina,
    "valor": prova.valor,
    "nota": prova.nota
  }
  
  db["provas"].append(nova_prova)
  
  with open("database.json", "w", encoding="utf-8") as arq:
    json.dump(db, arq, indent=2, ensure_ascii=False)
  return {"mensagem": "Prova cadastrada com sucesso!"}

def put_prova(prova: Prova):
  with open("database.json", "r") as arq:
    db = json.load(arq)
  
  prova_editada = {
    "id_aluno": prova.id_aluno,
    "disciplina": prova.disciplina,
    "valor": prova.valor,
    "nota": prova.nota
  }

  for i, prova_cadastrada in enumerate(db["provas"]):
    if prova_cadastrada["id_aluno"] == prova_editada["id_aluno"] and prova_cadastrada["disciplina"] == prova_editada["disciplina"]:
      db["provas"][i] = prova_editada
      with open("database.json", "w", encoding="utf-8") as arq:
        json.dump(db, arq, indent=2, ensure_ascii=False)
      return {"mensagem": "Alterações concluídas com sucesso!"}

  return {"mensagem": "Prova não encontrada..."}

def delete_prova(id_aluno: int, disciplina: str):
  with open("database.json", "r") as arq:
    db = json.load(arq)
    
  for i, prova in enumerate(db["provas"]):
    if prova["id_aluno"] == id_aluno and prova["disciplina"] == disciplina:
      del db["provas"][i]
      with open("database.json", "w", encoding="utf-8") as arq:
        json.dump(db, arq, indent=2, ensure_ascii=False)
      return {"mensagem": "Cadastro excluído com sucesso!"}
    
  return {"mensagem": "Prova não encontrada..."}