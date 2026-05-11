# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-05-11

### Added
- Initial MVP release
- Telegram bot with aiogram 3.x
- OpenRouter API integration with free models
- Multi-language support (7 languages): EN, RU, DE, FR, PT, NO, DA
- Auto language detection from Telegram settings
- Crisis detection with 5 risk levels
- LLM safety classifier
- CBT/DBT/Mindfulness knowledge base
- Mood diary functionality
- Safety plan generator
- ModelSelector with smart fallback
- Prometheus metrics and Grafana dashboards
- GitHub Actions CI/CD pipeline
- Docker Compose setup with PostgreSQL and Redis
- Comprehensive test suite

### Security
- Deterministic crisis triggers
- Prompt injection protection
- Output validation
- No medical diagnoses
- No medication advice
- Data minimization

## [0.9.0] - 2026-05-10

### Added
- Project scaffolding
- Basic bot handlers
- OpenRouter client
- Database models

[Unreleased]: https://github.com/Volynskiy-Business/Psychologist-bot/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Volynskiy-Business/Psychologist-bot/compare/v0.9.0...v1.0.0
[0.9.0]: https://github.com/Volynskiy-Business/Psychologist-bot/releases/tag/v0.9.0
