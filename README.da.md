# 🤖 PsySupport AI Bot

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange)](https://openrouter.ai)

[English](README.md) | [Русский](README.ru.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Português](README.pt.md) | [Norsk](README.no.md) | **Dansk**

AI-assistent til psykologisk selvhjælp, psykoudannelse og følelsesmæssig støtte på Telegram.

## ⚠️ Vigtigt

Denne bot **er IKKE**:
- Læge eller psykiater
- Psykoterapeut
- Krisetjeneste
- Diagnostisk værktøj

Botten er designet kun til **selvhjælp** og **følelsesmæssig støtte**.

## ✨ Funktioner

- 🗣 **Sikker dialog** med AI
- 🧠 **CBT-øvelser**
- 🧘 **Mindfulness** og grounding
- 📊 **Humørdagbog**
- 📋 **Sikkerhedsplan**
- 🆘 **Kriseomdirigering**
- 🤖 **OpenRouter** — gratis LLM-modeller
- 🌍 **Flersproget** — automatisk sprogdetektion

## 🚀 Hurtig start

### 1. Få API-nøgler

**Telegram Bot Token:**
1. Send besked til [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Kopier tokenet

**OpenRouter API Key:**
1. Tilmeld dig på [openrouter.ai/keys](https://openrouter.ai/keys)
2. Opret en nøgle (gratis)

### 2. Installation

```bash
git clone https://github.com/vmn2014/Psychologist-bot.git
cd Psychologist-bot

# Opret virtuelt miljø (anbefalet)
python3 -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate

# Installer afhængigheder
pip install -r requirements.txt
```

### 3. Konfiguration

```bash
cp .env.example .env
# Rediger .env, tilføj dine nøgler
```

### 4. Kørsel

```bash
# Lokal (med aktiveret venv)
python -m app.main

# Eller med Docker (behøver ikke venv)
docker-compose up --build
```

## 🌍 Sprog

Botten registrerer automatisk brugerens sprog fra Telegram-indstillinger:

| Sprog | Kode | Status |
|----------|------|--------|
| English | `en` | ✅ Fuld |
| Русский | `ru` | ✅ Fuld |
| Deutsch | `de` | ✅ Fuld |
| Français | `fr` | ✅ Fuld |
| Português | `pt` | ✅ Fuld |
| Norsk | `no` | ✅ Fuld |
| Dansk | `da` | ✅ Fuld |

## 🛡️ Sikkerhed

- 5-niveau krisdetektion
- Automatisk omdirigering til live-hjælp
- Beskyttelse mod prompt injection
- AI-svarvalidering
- Ingen diagnoser
- Ingen medicinske råd

## 🔒 Privatliv

- Udtrykkeligt samtykke ved `/start`
- `/delete_my_data`-kommando
- Dataminimering
- Krypterede hemmeligheder via env

## 📄 Licens

[MIT License](LICENSE) © 2026
