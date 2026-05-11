# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via:
- Email: security@psy-support-bot.dev (placeholder)
- Or create a private security advisory on GitHub

We will respond within 48 hours and work with you to understand and resolve the issue.

## Security Measures

### Data Protection
- No storage of sensitive personal data by default
- Encrypted environment variables
- Optional conversation storage (disabled by default)
- Data deletion via `/delete_my_data`

### AI Safety
- Deterministic crisis detection
- LLM safety classification
- Output validation
- No medical advice or diagnoses

### Infrastructure
- Rate limiting
- Anti-abuse measures
- Prompt injection protection
- Dependency scanning via GitHub Actions

## Best Practices for Deployment

1. Use strong, unique API keys
2. Enable HTTPS/TLS
3. Regular dependency updates
4. Monitor logs for anomalies
5. Keep `.env` file secure and never commit it

## Acknowledgments

We thank security researchers who help keep our users safe.
