# 🤖 PsySupport AI Bot

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange)](https://openrouter.ai)

[English](README.md) | [Русский](README.ru.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Português](README.pt.md) | **Norsk**

AI-assistent for psykologisk selvhjelp, psykouddanning og emosjonell støtte på Telegram.

## ⚠️ Viktig

Denne boten **er IKKE**:
- Lege eller psykiater
- Psykoterapeut
- Krisetjeneste
- Diagnostisk verktøy

Boten er designet kun for **selvhjelp** og **emosjonell støtte**.

## ✨ Funksjoner

- 🗣 **Sikker dialog** med AI
- 🧠 **CBT-øvelser**
- 🧘 **Mindfulness** og grounding
- 📊 **Humørdagbok**
- 📋 **Sikkerhetsplan**
- 🆘 **Kriseomdirigering**
- 🤖 **OpenRouter** — gratis LLM-modeller
- 🌍 **Flerspråklig** — automatisk språkgjenkjenning

## 🚀 Hurtigstart

### 1. Få API-nøkler

**Telegram Bot Token:**
1. Send melding til [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Kopier tokenet

**OpenRouter API Key:**
1. Registrer deg på [openrouter.ai/keys](https://openrouter.ai/keys)
2. Opprett en nøkkel (gratis)

### 2. Installasjon

```bash
git clone https://github.com/vmn2014/Psychologist-bot.git
cd Psychologist-bot

# Opprett virtuelt miljø (anbefalt)
python3 -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate

# Installer avhengigheter
pip install -r requirements.txt
```

### 3. Konfigurasjon

```bash
cp .env.example .env
# Rediger .env, legg til nøklene dine
```

### 4. Kjøring

```bash
# Lokal (med aktivert venv)
python -m app.main

# Eller med Docker (trenger ikke venv)
docker-compose up --build
```

## 🌍 Språk

Boten gjenkjenner automatisk brukerens språk fra Telegram-innstillinger:

| Språk | Kode | Status |
|----------|------|--------|
| English | `en` | ✅ Full |
| Русский | `ru` | ✅ Full |
| Deutsch | `de` | ✅ Full |
| Français | `fr` | ✅ Full |
| Português | `pt` | ✅ Full |
| Norsk | `no` | ✅ Full |
| Dansk | `da` | ✅ Full |

## 🛡️ Sikkerhet

- 5-nivå krisdeteksjon
- Automatisk omdirigering til live-hjelp
- Beskyttelse mot prompt injection
- AI-responsvalidering
- Ingen diagnoser
- Ingen medisinske råd

## 🔒 Personvern

- Eksplisitt samtykke ved `/start`
- `/delete_my_data`-kommando
- Dataminimering
- Krypterte hemmeligheter via env

## 📄 Lisens

[MIT License](LICENSE) © 2026
