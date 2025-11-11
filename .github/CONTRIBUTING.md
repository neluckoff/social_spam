# Contributing to social_spam

First off, thank you for considering contributing to social_spam! 🎉

The following is a set of guidelines for contributing to social_spam. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to neluckoff@gmail.com.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code samples)
- **Describe the behavior you observed** and what you expected
- **Include error messages and stack traces**
- **Specify your environment** (OS, Python version, social_spam version)

Use our [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.yml) when creating issues.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **Provide examples** of how the feature would be used

Use our [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.yml).

### Pull Requests

1. **Fork the repository** and create your branch from `master`
2. **Make your changes** following our style guidelines
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** using our template

#### Pull Request Guidelines

- Keep PRs focused on a single concern
- Include tests for new functionality
- Update the documentation
- Follow the existing code style
- Write clear commit messages
- Reference related issues in your PR description

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/social_spam.git
cd social_spam
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install development dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### 4. Create a Branch

```bash
git checkout -b feature/my-new-feature
# or
git checkout -b fix/my-bug-fix
```

### 5. Make Your Changes

- Write clear, readable code
- Add comments for complex logic
- Follow Python best practices
- Keep functions small and focused

### 6. Test Your Changes

```bash
# Test imports
python -c "from social_spam import Mail, Telegram, Vkontakte, WhatsApp"

# Run your specific tests
python your_test_script.py
```

### 7. Commit and Push

```bash
git add .
git commit -m "Add: brief description of changes"
git push origin feature/my-new-feature
```

### 8. Create Pull Request

Go to GitHub and create a pull request from your branch to `master`.

## Style Guidelines

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: Maximum 120 characters (soft limit)
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Single quotes for strings (unless double quotes avoid escaping)
- **Imports**: Organized in groups (standard library, third-party, local)

#### Example

```python
import os
import sys

from alive_progress import alive_bar
import pyrogram

from .mail import Mail


class MyClass:
    """Class docstring following Google style."""
    
    def __init__(self, param: str) -> None:
        """
        Initialize the class.
        
        Args:
            param (str): Description of parameter
        """
        self.param = param
    
    def my_method(self) -> bool:
        """
        Method docstring.
        
        Returns:
            bool: Description of return value
        """
        return True
```

### Documentation

- Add docstrings to all public classes and methods
- Follow Google docstring style
- Update README.md if adding new features
- Add examples for new functionality

### Type Hints

Use type hints where appropriate:

```python
def send_message(self, recipient: str, message: str) -> None:
    """Send a message to recipient."""
    pass
```

## Commit Messages

### Format

```
Type: Brief description (50 chars or less)

More detailed explanation if needed (wrap at 72 chars)
- Bullet points are okay
- Use present tense: "Add feature" not "Added feature"

Fixes #123
```

### Types

- **Add**: New feature or functionality
- **Fix**: Bug fix
- **Update**: Changes to existing functionality
- **Refactor**: Code restructuring without changing behavior
- **Docs**: Documentation changes
- **Style**: Formatting, missing semicolons, etc.
- **Test**: Adding or updating tests
- **Chore**: Maintenance tasks

### Examples

```
Add: Lazy loading for pywhatkit module

Implement lazy loading pattern to avoid internet connection
check during module import. This fixes the InternetException
that occurred when importing WhatsApp class.

Fixes #42
```

```
Fix: SMTP connection handling in Mail class

- Move SMTP connection to lazy initialization
- Add proper connection cleanup
- Improve error handling

Fixes #38
```

## Testing

### Manual Testing

Before submitting a PR, test your changes:

```python
# Test basic imports
from social_spam import Mail, Telegram, Vkontakte, WhatsApp

# Test your specific changes
mail = Mail()
# ... test your code
```

### Test on Multiple Python Versions

If possible, test on:
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

## Questions?

Feel free to:
- Open an issue with the "question" label
- Contact the maintainer: neluckoff@gmail.com
- Start a discussion on GitHub Discussions

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes for significant contributions
- README.md acknowledgments section

---

Thank you for contributing to social_spam! 🙏

Your efforts help make this project better for everyone.

