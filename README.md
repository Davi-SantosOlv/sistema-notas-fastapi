# 👨‍🏫 API de Notas Escolares com FastAPI

Esta é a primeira API que desenvolvo. Ela possui rotas para o cadastro, busca, edição e exclusão de Alunos e Provas. Os campos destas classes não possuem validações além das nativas do FastAPI.

## 📚 Conceitos praticados

- **FastAPI, Uvicorn e Pydantic:** Instalação de ferramentas dentro do `.venv` do projeto.
- **Frameworks:** Primeiro contato e leitura da documentação oficial.
- **APIs REST:** Conceitos básicos, rotas e códigos.
- **Decorators:** Ferramenta da linguagem com aplicações dentro do framework estudado.
- **Boas práticas de documentação:** Breve explicação das rotas.

## 🚀 Como executar

1. **Clone o repositório e acesse a pasta:**
   ```bash
   git clone https://github.com/Davi-SantosOlv/sistema-notas-fastapi.git
   cd sistema-notas-fastapi
   ```

2. **Crie e ative um ambiente virtual (`.venv`):**
   * **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * **Linux/macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Inicie o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa:**
   Abra o navegador em [http://127.0.0](http://127.0.0) para testar as rotas diretamente pelo Swagger UI.

## 🎯 Objetivo

Descobrir como o FastAPI funciona de forma prática; aprender sobre APIs REST, seus códigos e como se estruturam.

---

_Projeto desenvolvido para fins de aprendizado._
