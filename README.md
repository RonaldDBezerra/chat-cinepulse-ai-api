# 🎬 CinePulse AI API

Backend inteligente para recomendações de filmes e séries utilizando IA Generativa, agentes com LangGraph e integração com a API do TMDB.

O projeto foi desenvolvido para complementar o aplicativo CinePulse, oferecendo uma experiência conversacional capaz de entender solicitações dos usuários, buscar informações atualizadas sobre filmes e séries e fornecer recomendações personalizadas em tempo real.

---

## 🚀 Funcionalidades

* 🤖 Assistente de IA especializado em filmes e séries
* 🎯 Recomendações personalizadas
* 🔍 Busca de filmes e séries em tempo real via TMDB
* 📈 Consulta de tendências e lançamentos
* 🎬 Informações detalhadas sobre filmes e séries
* 🔐 Autenticação via Firebase Authentication
* ⚡ API construída com FastAPI
* 🕸️ Agentes desenvolvidos com LangGraph

---

## 🏗️ Arquitetura

```text
React Native App
        │
        ▼
Firebase Authentication
        │
        ▼
FastAPI
        │
        ▼
Firebase Token Validation
        │
        ▼
Movie Agent (LangGraph)
        │
 ┌──────┼──────────┐
 ▼                 ▼
TMDB              OpenAI
API                LLM
```

---

## 🛠️ Tecnologias

### Backend

* Python
* FastAPI
* Uvicorn

### IA Generativa

* OpenAI
* LangGraph
* LangChain
* LangSmith

### Infraestrutura

* Firebase Authentication

### APIs Externas

* TMDB API

---

## 🔐 Autenticação

A API utiliza Firebase Authentication para garantir que apenas usuários autenticados possam acessar os recursos da aplicação.

Todas as rotas protegidas exigem um Firebase ID Token válido.

Exemplo:

```http
Authorization: Bearer <firebase_id_token>
```

O token é validado utilizando o Firebase Admin SDK antes da execução do agente.

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=

TMDB_API_KEY=

LANGSMITH_TRACING=

LANGSMITH_ENDPOINT=

LANGSMITH_API_KEY=

LANGSMITH_PROJECT=

```

---

## 🚀 Executando o Projeto

### Instalar dependências

```bash
uv sync
```

### Executar a API

```bash
uv run uvicorn app.main:app --reload
```

Acesse a documentação interativa:

```text
http://localhost:8000/docs
```

---

## 💡 Objetivo

O objetivo deste projeto é explorar conceitos modernos de AI Engineering, incluindo agentes inteligentes, integração com ferramentas externas e geração de recomendações contextualizadas utilizando Large Language Models (LLMs).

---

## 👨‍💻 Autor

**Ronald Damasio**

* GitHub: https://github.com/RonaldDBezerra
* LinkedIn: https://www.linkedin.com/in/ronalddamasio/
