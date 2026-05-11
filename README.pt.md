# 🤖 PsySupport AI Bot

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange)](https://openrouter.ai)

[English](README.md) | [Русский](README.ru.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | **Português**

Assistente de IA para autoajuda psicológica, psicoeducação e apoio emocional no Telegram.

## ⚠️ Importante

Este bot **NÃO é**:
- Médico ou psiquiatra
- Psicoterapeuta
- Serviço de crise
- Ferramenta de diagnóstico

O bot é projetado apenas para **autoajuda** e **apoio emocional**.

## ✨ Funcionalidades

- 🗣 **Diálogo seguro** com IA
- 🧠 **Exercícios CBT**
- 🧘 **Mindfulness** e grounding
- 📊 **Diário de humor**
- 📋 **Plano de segurança**
- 🆘 **Encaminhamento de crise**
- 🤖 **OpenRouter** — modelos LLM gratuitos
- 🌍 **Multilingue** — deteção automática de idioma

## 🚀 Início Rápido

### 1. Obter Chaves API

**Token do Bot Telegram:**
1. Envie mensagem para [@BotFather](https://t.me/BotFather)
2. Envie `/newbot`
3. Copie o token

**Chave API OpenRouter:**
1. Registe-se em [openrouter.ai/keys](https://openrouter.ai/keys)
2. Crie uma chave (grátis)

### 2. Instalação

```bash
git clone https://github.com/vmn2014/Psychologist-bot.git
cd Psychologist-bot

# Criar ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configuração

```bash
cp .env.example .env
# Editar .env, adicionar as suas chaves
```

### 4. Execução

```bash
# Local (com venv ativado)
python -m app.main

# Ou com Docker (não precisa de venv)
docker-compose up --build
```

## 🌍 Idiomas

O bot deteta automaticamente o idioma do utilizador a partir das definições do Telegram:

| Idioma | Código | Estado |
|----------|------|--------|
| English | `en` | ✅ Completo |
| Русский | `ru` | ✅ Completo |
| Deutsch | `de` | ✅ Completo |
| Français | `fr` | ✅ Completo |
| Português | `pt` | ✅ Completo |
| Norsk | `no` | ✅ Completo |
| Dansk | `da` | ✅ Completo |

## 🛡️ Segurança

- Deteção de crise em 5 níveis
- Encaminhamento automático para ajuda presencial
- Proteção contra prompt injection
- Validação de respostas da IA
- Não faz diagnósticos
- Não dá conselhos médicos

## 🔒 Privacidade

- Consentimento explícito em `/start`
- Comando `/delete_my_data`
- Minimização de dados
- Segredos encriptados via env

## 📄 Licença

[MIT License](LICENSE) © 2026
