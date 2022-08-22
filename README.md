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

## Contributing
I have a positive attitude towards PR and pull requests. Glad to see that people like the package.

- Creator: [@neluckoff](https://github.com/neluckoff)

## License

- Copyright © 2022 [neluckoff](https://github.com/neluckoff).
- This project is [MIT](https://github.com/neluckoff/social_spam/blob/master/LICENSE.md) licensed.
