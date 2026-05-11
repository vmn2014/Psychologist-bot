# 🤖 PsySupport AI Bot

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange)](https://openrouter.ai)

AI-помощник для психологической самопомощи, психообразования и эмоциональной поддержки в Telegram.

## ⚠️ Важно

Этот бот **не является**:
- Врачом или психиатром
- Психотерапевтом
- Кризисной службой
- Инструментом для диагностики

Бот предназначен только для **самопомощи** и **эмоциональной поддержки**.

## ✨ Возможности

- 🗣 **Безопасный диалог** с AI
- 🧠 **CBT/КПТ** упражнения
- 🧘 **Mindfulness** и grounding
- 📊 **Дневник настроения**
- 📋 **План безопасности**
- 🆘 **Кризисная маршрутизация**
- 🤖 **OpenRouter** — бесплатные LLM-модели

## 🚀 Быстрый старт

### 1. Получение API ключей

**Telegram Bot Token:**
1. Напишите [@BotFather](https://t.me/BotFather)
2. Отправьте `/newbot`
3. Скопируйте токен

**OpenRouter API Key:**
1. Зарегистрируйтесь на [openrouter.ai/keys](https://openrouter.ai/keys)
2. Создайте ключ (бесплатно)

### 2. Установка

```bash
git clone https://github.com/vmn2014/Psychologist-bot.git
cd Psychologist-bot
pip install -r requirements.txt
```

### 3. Настройка

```bash
cp .env.example .env
# Отредактируйте .env, добавив свои ключи
```

### 4. Запуск

```bash
# Локально
python -m app.main

# Или через Docker
docker-compose up --build
```

## 📁 Структура проекта

```
psy-support-bot/
├── app/
│   ├── main.py              # Точка входа
│   ├── config.py            # Конфигурация
│   ├── ai/
│   │   ├── openrouter_client.py
│   │   └── prompts/
│   │       ├── system_prompt.py
│   │       └── safety_classifier_prompt.py
│   ├── bot/
│   │   └── handlers/
│   │       ├── start.py
│   │       ├── chat.py
│   │       └── mood.py
│   ├── safety/
│   │   ├── crisis_detector.py
│   │   ├── safety_classifier.py
│   │   └── safety_protocols.py
│   ├── db/
│   │   ├── models.py
│   │   └── session.py
│   └── psychology/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

## 🛡️ Безопасность

- Детекция кризисных ситуаций (5 уровней риска)
- Автоматическая маршрутизация к живой помощи
- Защита от prompt injection
- Валидация ответов AI
- Не ставит диагнозы
- Не даёт медицинских советов

## 🔒 Приватность

- Явное согласие при `/start`
- Команда `/delete_my_data`
- Минимизация данных
- Шифрование секретов через env

## 📚 Доказательная база

Бот использует подходы, рекомендованные:
- [WHO](https://www.who.int)
- [NICE](https://www.nice.org.uk)
- [SAMHSA](https://www.samhsa.gov)

## 📝 Команды

| Команда | Описание |
|---------|----------|
| `/start` | Начало работы |
| `/mood` | Дневник настроения |
| `/chat` | Свободный разговор |
| `/delete_my_data` | Удалить данные |
| `/privacy` | Политика приватности |

## ⚠️ Ограничения

- Бесплатные модели OpenRouter имеют rate limits
- Бот не заменяет профессиональную помощь
- При кризисе обращайтесь к специалистам

## 🤝 Участие

Приветствуются pull requests! См. [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Лицензия

[MIT License](LICENSE) © 2026
