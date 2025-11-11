<div align="center">

# 📬 Social Spam

### *Powerful Python package for messaging across multiple platforms*

[![PyPI version](https://badge.fury.io/py/social-spam.svg)](https://pypi.org/project/social-spam/)
[![Python](https://img.shields.io/pypi/pyversions/social-spam.svg)](https://pypi.org/project/social-spam/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub Repo stars](https://img.shields.io/github/stars/neluckoff/social_spam?style=social)](https://github.com/neluckoff/social_spam/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/neluckoff/social_spam?style=social)](https://github.com/neluckoff/social_spam/network/members)

---

**Simple • Powerful • Cross-Platform • Well-Documented**

Supports: Telegram, VKontakte, WhatsApp, Email

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### 📱 Supported Platforms
- 📧 **Email** - SMTP with attachments
- 💬 **Telegram** - Pyrogram 2.0+ support  
- 🔵 **VKontakte** - Full API integration
- 📲 **WhatsApp** - Web automation

</td>
<td width="50%">

### 🎯 Key Features
- ✅ **Easy to use** - Simple and intuitive API
- 🚀 **Async ready** - Fast and efficient
- 📦 **Bulk sending** - Mass messaging support
- 🎨 **Rich content** - Text, images, files
- 🔄 **Auto-retry** - Built-in error handling
- 📊 **Progress bars** - Visual feedback

</td>
</tr>
</table>

## 🆕 What's New in v1.3.0

🎉 **Major Update** - Completely modernized and fixed!

```diff
+ ✅ Fixed all import issues (pywhatkit, Mail)
+ ✅ Python 3.8-3.12 support (including latest versions)
+ ✅ Pyrogram 2.0+ compatibility
+ ✅ All dependencies updated to latest stable versions
+ ✅ Improved error handling and resource management
+ ✅ Better performance and reliability
```

📖 See [CHANGELOG.md](CHANGELOG.md) for complete details

## 📦 Installation

```bash
# Install from PyPI (recommended)
pip install social-spam

# Or install from GitHub for latest dev version
pip install -U https://github.com/neluckoff/social_spam/archive/master.zip
```

**Requirements:** Python 3.8+

---

## 🚀 Quick Start

### 📧 Email Example

```python
from social_spam import Mail

# Initialize and connect
mail = Mail()
mail.connect_mail('your_email@inbox.ru', 'your_password')

# Send a simple message
mail.set_message('Hello!', 'How are you?')
mail.send_message('friend@gmail.com')

# Send with attachments
mail.set_message('Check this out!', 'See attached files', ['photo.jpg', 'document.pdf'])
mail.send_message('friend@gmail.com')
```

### 💬 Telegram Example

```python
from social_spam import Telegram

# Connect to Telegram
tg = Telegram()
tg.connect_user(
    api_id=12345,
    api_hash="your_api_hash",
    phone_number="+1234567890"
)

# Send a message
tg.send_message(user_id=123456789, message="Hello from social_spam!")

# Send with image
tg.send_message(
    user_id=123456789, 
    message="Check out this image!",
    image="path/to/image.png"
)

# Mass messaging
user_ids = [111111, 222222, 333333]
tg.start_selective_spam(user_ids, message="Hello everyone!")
```

### 🔵 VKontakte Example

```python
from social_spam import Vkontakte

# Connect with token
vk = Vkontakte()
vk.connect_user(token="your_vk_token")

# Send message
vk.send_message(user_id=123456, message="Привет!")

# Send to multiple users
vk.start_selective_spam(
    chats=[111111, 222222], 
    message="Всем привет!"
)
```

### 📲 WhatsApp Example

```python
from social_spam import WhatsApp

wa = WhatsApp()

# Send instant message
wa.send_message(
    phone="+1234567890",
    text="Hello from Python!"
)

# Send with image
wa.send_message(
    phone="+1234567890",
    text="Check this out!",
    image="image.jpg"
)
```

---

## 📚 Documentation & Examples

Detailed examples for each platform:

| Platform | Documentation | Example Code |
|----------|--------------|--------------|
| 📧 **Email** | [Guide](https://github.com/neluckoff/social_spam/blob/master/examples/mail_examples.py) | Full SMTP integration with attachments |
| 💬 **Telegram** | [Guide](https://github.com/neluckoff/social_spam/blob/master/examples/telegram_examples.py) | Pyrogram-based messaging |
| 🔵 **VKontakte** | [Guide](https://github.com/neluckoff/social_spam/blob/master/examples/vkontakte_examples.py) | VK API integration |
| 📲 **WhatsApp** | [Guide](https://github.com/neluckoff/social_spam/blob/master/examples/whatsapp_examples.py) | Web automation |

---

## 🎯 Use Cases

- 📢 **Bulk Notifications** - Send updates to multiple recipients
- 🤖 **Chatbots** - Build automated messaging bots
- 📊 **Marketing** - Automated marketing campaigns
- 🔔 **Alerts** - System notifications and alerts
- 💼 **Business** - Customer communication
- 🎓 **Educational** - Learning messaging APIs

## 🛠️ Advanced Usage

<details>
<summary><b>Email with HTML Templates</b></summary>

```python
mail = Mail()
mail.connect_mail('your_email@mail.ru', 'password')
mail.set_message_html('Newsletter', 'template.html', ['logo.png'])
mail.send_message('subscriber@example.com')
```
</details>

<details>
<summary><b>Telegram Batch Messaging</b></summary>

```python
tg = Telegram()
tg.connect_user(api_id=12345, api_hash="hash", phone_number="+123456")

# Send to all your contacts
tg.start_all_spam(message="Important update!")

# Message bombing (use responsibly!)
tg.start_bombing(user_id=123456, amount=10, message="Hello!")
```
</details>

<details>
<summary><b>Custom SMTP Server</b></summary>

```python
mail = Mail()
mail.set_server('smtp.gmail.com', 587)  # Custom server
mail.connect_mail('your@gmail.com', 'app_password')
```
</details>

---

## 🤝 Contributing

We love contributions! Here's how you can help:

- 🐛 [Report Bugs](https://github.com/neluckoff/social_spam/issues/new?template=bug_report.yml)
- 💡 [Request Features](https://github.com/neluckoff/social_spam/issues/new?template=feature_request.yml)
- 📝 [Improve Documentation](https://github.com/neluckoff/social_spam/blob/master/.github/CONTRIBUTING.md)
- 🔧 [Submit Pull Requests](https://github.com/neluckoff/social_spam/pulls)

**Development Setup:**
```bash
git clone https://github.com/neluckoff/social_spam.git
cd social_spam
pip install -r requirements.txt
pip install -e .
```

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines.

---

## 💬 Community & Support

<div align="center">

| 💬 Type | 🔗 Link |
|---------|---------|
| 🐛 **Bug Reports** | [Create Issue](https://github.com/neluckoff/social_spam/issues/new?template=bug_report.yml) |
| 💡 **Feature Requests** | [Create Issue](https://github.com/neluckoff/social_spam/issues/new?template=feature_request.yml) |
| ❓ **Questions** | [Ask Question](https://github.com/neluckoff/social_spam/issues/new?template=question.yml) |
| 💬 **Discussions** | [Join Discussion](https://github.com/neluckoff/social_spam/discussions) |
| 📧 **Email** | [neluckoff@gmail.com](mailto:neluckoff@gmail.com) |

</div>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for details.

```
Copyright © 2022-2025 neluckoff
```

---

## ⭐ Show Your Support

If you find this project useful, please consider:

- ⭐ **Starring** the repository
- 🐦 **Sharing** it with others
- 💖 **Sponsoring** the development

<div align="center">

**Made with ❤️ by [@neluckoff](https://github.com/neluckoff)**

[⬆ Back to Top](#-social-spam)

</div>
