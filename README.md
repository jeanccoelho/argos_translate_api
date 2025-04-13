
# 🧠 Argos Translate API (Offline e Gratuito)

Tradução automática de textos usando [Argos Translate](https://www.argosopentech.com/) com uma API REST leve via [FastAPI](https://fastapi.tiangolo.com/). Ideal para aplicações que precisam de tradução offline, sem depender de serviços pagos como Google Translate ou DeepL.

> 🔒 Suporte a autenticação via API Key incluído.

---

## 🚀 Funcionalidades

- ✅ Tradução 100% offline (usa modelos OPUS-MT)
- ✅ Roda em container Docker
- ✅ Tradução entre +20 idiomas (pt, en, es, fr, de, etc)
- ✅ API REST com FastAPI
- ✅ Autenticação via API Key (segurança pronta para produção)
- ✅ Suporte a `.env` para fácil configuração

---

## 📦 Pré-requisitos

- Docker ou Python 3.10+
- Para rodar com Docker:
  ```bash
  docker compose up -d
  ```

- Para rodar com Python localmente:
  ```bash
  pip install -r requirements.txt
  uvicorn translate_api:app --host 0.0.0.0 --port 8000
  ```

---

## 🧪 Exemplo de uso

### Requisição:

```http
POST /translate HTTP/1.1
Host: localhost:8000
x-api-key: sua-chave-aqui
Content-Type: application/json

{
  "text": "Olá, tudo bem?",
  "from_lang": "pt",
  "to_lang": "en"
}
```

### Resposta:

```json
{
  "translated": "Hello, how are you?"
}
```

---

## 🔐 Configuração de Segurança

Adicione sua chave de API no arquivo `.env`:

```env
ARGOS_API_KEY=sua-chave-super-secreta
```

Ou, no Docker Compose:

```yaml
environment:
  - ARGOS_API_KEY=sua-chave-super-secreta
```

No código cliente, envie como header:

```http
x-api-key: sua-chave-super-secreta
```

---

## 🧰 Arquitetura do Projeto

```
argos-api/
├── translate_api.py       # API principal com FastAPI
├── requirements.txt       # Dependências do projeto
├── Dockerfile             # Para containerizar o serviço
├── docker-compose.yml     # Executa com Docker Compose
└── .env                   # Chave de API (não versionar)
```

---

## 📈 Benchmarks de Performance

- Tradução de textos curtos (5–10 palavras): ~150–400ms
- Ideal para mensagens de erro, botões, textos dinâmicos
- Consumo de memória leve (~150MB por container)

---

## 🌍 Idiomas Suportados

A lista completa de pares de idiomas disponíveis pode ser consultada [aqui](https://www.argosopentech.com/argospm/index/). Exemplos populares:

- pt → en, es, fr
- en → pt, es, de
- es → pt, en, fr

---

## 🛠 Recursos adicionais (futuros)

- [ ] Cache de traduções (opcional)
- [ ] Upload manual de modelos `.argosmodel`
- [ ] Painel web para testar traduções
- [ ] Healthcheck e monitoramento básico

---

## 👨‍💻 Contribuindo

Pull Requests são bem-vindos! Sinta-se à vontade para melhorar o projeto, criar issues ou sugerir ideias.

---

## 📄 Licença

Este projeto é open source, licenciado sob a [MIT License](LICENSE).

---

## ❤️ Criado por

Feito com ❤️ por [ChatGPT + Jean Carlos] — inspirado na necessidade de uma alternativa livre, offline e leve para internacionalização automatizada.
