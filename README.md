<div align="center">
    <h1>Social Spam</h1>
    Package for convenient work with messages in all popular instant messengers
</div>
&nbsp;

<div align="center">
    <a href="https://github.com/neluckoff/social_spam/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/neluckoff/social_spam?style=flat-square"></a>
    <a href="https://github.com/neluckoff/social_spam/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/neluckoff/social_spam?style=flat-square"></a>
    <a href="https://github.com/neluckoff/social_spam"><img alt="GitHub license" src="https://img.shields.io/github/license/neluckoff/social_spam?style=flat-square"></a>
    <a href="https://github.com/neluckoff/social_spam/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/neluckoff/social_spam?style=flat-square"></a>
</div>
&nbsp;

<i>On the current version, you have access to the following messengers: Telegram, WhatsApp, Vkontakte, Email.</i>

## What's New in v1.3.0

✨ **Major Update** - The package has been fully updated and modernized!

- ✅ Fixed all import issues with `pywhatkit` and `Mail` modules
- ✅ Updated to support Python 3.8+ (including Python 3.12)
- ✅ Compatible with Pyrogram 2.0+ 
- ✅ All dependencies updated to latest versions
- ✅ Better error handling and resource management

See [CHANGELOG.md](CHANGELOG.md) for full details.

## Requirements

- Python 3.8 or higher
- Active internet connection
- API credentials for the services you want to use

## Documentation
If you want to get acquainted with examples of using this package, you can follow the link of interest.

- [Examples of interaction with Telegram](https://github.com/neluckoff/social_spam/blob/master/examples/telegram_examples.py)
- [Examples of interaction with Vkontakte](https://github.com/neluckoff/social_spam/blob/master/examples/vkontakte_examples.py)
- [Examples of interaction with WhatsApp](https://github.com/neluckoff/social_spam/blob/master/examples/whatsapp_examples.py)
- [Examples of interaction with Email](https://github.com/neluckoff/social_spam/blob/master/examples/mail_examples.py)

## Installation
You can install the latest version with the command:

```shell
pip install social-spam
```
Or you can install from GitHub:

```shell
pip install -U https://github.com/neluckoff/social_spam/archive/master.zip
```

## Sending an email
**[More examples here!](https://github.com/neluckoff/social_spam/blob/master/examples/)**

```python
from social_spam import Mail

mail = Mail()
mail.connect_mail('test@inbox.ru', 'my_password')

mail.set_message('Message from luckoff', 'How are you?', ['image.png'])
mail.send_message('friend@gmail.com')
```

## Development

If you want to contribute to this project, here's how to set up your development environment:

```shell
# Clone the repository
git clone https://github.com/neluckoff/social_spam.git
cd social_spam

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](.github/CONTRIBUTING.md) for details on:

- How to report bugs
- How to suggest enhancements
- How to submit pull requests
- Development setup
- Code style guidelines

Before contributing, please read:
- [Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [Security Policy](.github/SECURITY.md)

### Maintainers
- Creator: [@neluckoff](https://github.com/neluckoff)
- Updated for modern Python (v1.3.0): [@neluckoff](https://github.com/neluckoff)

## Community & Support

- 🐛 [Report a Bug](https://github.com/neluckoff/social_spam/issues/new?template=bug_report.yml)
- 💡 [Request a Feature](https://github.com/neluckoff/social_spam/issues/new?template=feature_request.yml)
- ❓ [Ask a Question](https://github.com/neluckoff/social_spam/issues/new?template=question.yml)
- 💬 [Join Discussions](https://github.com/neluckoff/social_spam/discussions)

## License

- Copyright © 2022-2025 [neluckoff](https://github.com/neluckoff).
- This project is [MIT](https://github.com/neluckoff/social_spam/blob/master/LICENSE.md) licensed.
