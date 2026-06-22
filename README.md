# 🎬 CinePulse AI API

Backend inteligente para recomendações de filmes e séries utilizando IA Generativa, agentes com LangGraph e integração com a API do TMDB.

Desenvolvido para complementar o [app CinePulse](https://play.google.com/store/apps/details?id=com.cinepulse) (React Native / Expo), oferecendo uma experiência conversacional capaz de entender solicitações dos usuários, buscar informações atualizadas sobre filmes e séries e fornecer recomendações personalizadas em tempo real.

---

## 🚀 Funcionalidades

- 🤖 Assistente de IA especializado em filmes e séries
- 🎯 Recomendações personalizadas por gênero, similaridade e tendências
- 🔍 Busca em tempo real via TMDB (filmes, séries, elenco, pessoas)
- 📈 Consulta de tendências e lançamentos da semana
- 🎬 Informações detalhadas sobre títulos e atores
- 🔐 Autenticação via Firebase Authentication
- 🧠 Memória de conversa persistida no Supabase (PostgreSQL)
- 📊 Observabilidade com LangSmith
- ⚡ API assíncrona construída com FastAPI

---

## 🏗️ Arquitetura

```text
React Native App (CinePulse)
           │
           ▼
 Firebase Authentication
           │
           ▼ Bearer Token
        FastAPI
           │
           ▼
  Firebase Token Validation
           │
           ▼
  Movie Agent (LangGraph)
           │
    ┌──────┴──────────┐
    ▼                 ▼
 TMDB API         OpenAI LLM
                      │
                      ▼
            Supabase / PostgreSQL
            (checkpointer LangGraph)
```

---

## 🛠️ Tecnologias

### Backend
- **Python 3.12**
- **FastAPI** — framework web assíncrono
- **Uvicorn** — servidor ASGI

### IA Generativa
- **OpenAI** — LLM (GPT)
- **LangGraph** — orquestração de agentes com memória stateful
- **LangChain** — integração com ferramentas e modelos
- **LangSmith** — observabilidade e rastreamento de traces

### Persistência
- **Supabase (PostgreSQL)** — checkpointer do LangGraph para memória de conversa

### Infraestrutura
- **Firebase Authentication** — autenticação de usuários
- **Render** — deploy em produção

### APIs Externas
- **TMDB API** — dados de filmes, séries, elenco e tendências

---

## 🔐 Autenticação

Todas as rotas são protegidas por Firebase Authentication. O cliente deve enviar um Firebase ID Token válido no header de cada requisição:

```http
POST /api/chat
Authorization: Bearer <firebase_id_token>
Content-Type: application/json
```

O token é validado pelo Firebase Admin SDK antes de qualquer execução do agente.

---

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/RonaldDBezerra/chat-cinepulse-ai-api.git
cd chat-cinepulse-ai-api
```

### 2. Instale as dependências

```bash
uv sync
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=

TMDB_API_KEY=

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=

DATABASE_URL=postgresql://...

FIREBASE_CREDENTIALS_BASE64=
DB_SSL_CERT_BASE64=
```

**`FIREBASE_CREDENTIALS_BASE64`** — service account do Firebase em base64. Para gerar:

```bash
base64 -w 0 firebase-service-account.json
```

**`DB_SSL_CERT_BASE64`** — certificado CA do Supabase em base64. Para gerar:

```bash
base64 -w 0 prod-ca-2021.crt
```

> ⚠️ Nunca commite os arquivos `.env`, `.json` do service account ou `.crt` no repositório.

---

## 🚀 Executando o Projeto

```bash
uv run uvicorn app.main:app --reload
```

Acesse a documentação interativa em:

```
http://localhost:8000/docs
```

---

## 📁 Estrutura do Projeto

```
app/
├── api/
│   └── chat.py          # endpoint POST /api/chat
├── agents/
│   └── movie_agent.py   # agent LangGraph + system prompt
├── core/
│   ├── auth.py          # validação do Firebase token
│   ├── config.py        # Settings (pydantic-settings)
│   └── firebase.py      # inicialização do Firebase Admin SDK
├── services/
│   └── tmdb_service.py  # client HTTP da TMDB API
├── tools/
│   └── tmdb_tools.py    # ferramentas LangChain para o agent
└── main.py              # FastAPI app + lifespan
```

---

## 💡 Objetivo

Explorar conceitos modernos de AI Engineering na prática: agentes inteligentes com memória persistente, integração com ferramentas externas, autenticação em produção e observabilidade com LangSmith — tudo conectado a um app mobile real disponível na Play Store.

---

## 👨‍💻 Autor

**Ronald Damasio**

- GitHub: [RonaldDBezerra](https://github.com/RonaldDBezerra)
- LinkedIn: [ronalddamasio](https://www.linkedin.com/in/ronalddamasio/)
