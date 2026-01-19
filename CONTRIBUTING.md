# Contributing to AEVA Core

Thank you for your interest in contributing to AEVA! We are building the standard interface for general-purpose physical AI, and your help is valuable.

## Code of Conduct

All contributors are expected to adhere to our Code of Conduct. Please be professional, respectful, and focused on technical excellence.

## How to Contribute

### 1. Reporting Bugs
- Ensure the bug is reproducible.
- Check existing issues.
- detailed description of the environment and steps to reproduce.

### 2. Proposing Features
- We value **stability** and **backward compatibility** above all else.
- Open an RFC (Request for Comments) issue before writing code.

### 3. Pull Requests
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

## Development Setup

```bash
# Clone the repo
git clone https://github.com/your-username/aeva-core.git

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## Style Guide
- We use `black` for formatting.
- Type hints are **mandatory** for all public interfaces.
- Docstrings must follow Google style.
