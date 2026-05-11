# Contributing to PsySupport AI Bot

First off, thank you for considering contributing to PsySupport AI Bot! It's people like you that make this tool a great resource for psychological self-help.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to:
- **Safety first**: All changes must prioritize user safety
- **Evidence-based**: Psychological techniques should have research backing
- **Privacy**: User data protection is paramount
- **Inclusivity**: Support for multiple languages and cultures

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues. When you create a bug report, include:
- **Title**: Clear description
- **Steps to reproduce**: Numbered steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, bot version

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:
- **Use case**: Why is this needed?
- **Proposed solution**: How should it work?
- **Alternatives**: Other approaches considered

### Pull Requests

1. Fork the repository
2. Create a branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Run linting (`ruff check app/`)
6. Commit (`git commit -m 'feat: add amazing feature'`)
7. Push (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

```bash
# Clone
gh repo fork Volynskiy-Business/Psychologist-bot --clone=true
cd Psychologist-bot

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Tests
pytest

# Linting
ruff check app/
ruff format app/
mypy app/
```

## Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Tests
- `chore:` Maintenance

## Safety Review Process

All changes affecting:
- Crisis detection
- Safety protocols
- AI prompts
- Data handling

Require additional review from maintainers.

## Questions?

Open an issue with the `question` label.

Thank you for contributing! 🙏
