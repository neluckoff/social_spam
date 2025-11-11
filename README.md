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

🎉 **Major Update** - Completely modernized with 15+ new methods!

```diff
+ ✅ 15 new methods across all modules
+ ✅ Email: TLS, CC/BCC, Priority, Templates
+ ✅ Telegram: Documents, Video, Audio, Formatting, User Info
+ ✅ VKontakte: Documents, Audio, Friends, User Info
+ ✅ WhatsApp: File loading, Custom delays
+ ✅ Fixed all import issues (pywhatkit, Mail)
+ ✅ Python 3.8-3.12 support (including latest versions)
+ ✅ Pyrogram 2.0+ compatibility
+ ✅ TgCrypto now optional (better cross-platform support)
+ ✅ All dependencies updated to latest stable versions
+ ✅ Improved error handling and resource management
```

📖 See [CHANGELOG.md](CHANGELOG.md) for complete details

## 🌟 New Features Highlights

### 📧 Email - Enhanced
- **TLS Support** - Gmail, Outlook compatible (`use_tls=True`)
- **Message Priority** - Mark urgent/normal/low
- **CC/BCC** - Send copies to multiple recipients
- **Templates** - Use `{{variables}}` for personalization

### 💬 Telegram - Expanded
- **Documents** - Send PDFs, DOCX, ZIP, any files
- **Video & Audio** - MP4, MP3, and more
- **Text Formatting** - Markdown & HTML support
- **User Info** - Get detailed user profiles

### 🔵 VKontakte - Upgraded
- **Documents** - Share files with contacts
- **Voice Messages** - Send audio messages
- **Friends API** - Get and manage friends list
- **User Profiles** - Fetch detailed user information

### 📲 WhatsApp - Improved
- **File Messages** - Load from .txt/.md files
- **Custom Delays** - Fine-tune timing control

## 📦 Installation

```bash
# Install from PyPI (recommended)
pip install social-spam

# With optional Telegram speedup (TgCrypto)
pip install social-spam[telegram_speedup]

# Or install from GitHub for latest dev version
pip install -U https://github.com/neluckoff/social_spam/archive/master.zip
```

**Requirements:** Python 3.8+

> **Note:** `TgCrypto` is optional. Telegram works fine without it, but it can be 2-3x faster for bulk operations. If installation fails on your system, the base package will work perfectly.

> **macOS users:** Python 3.8 on macOS may have issues with `pywhatkit` dependencies (PyObjC requires 3.9+). We recommend Python 3.9+ for macOS.

---

## 🚀 Quick Start

### 📧 Email Example

```python
from social_spam import Mail

# Initialize and connect (with TLS for Gmail)
mail = Mail()
mail.set_server('smtp.gmail.com', 587, use_tls=True)
mail.connect_mail('your@gmail.com', 'app_password')

# Send a simple message
mail.set_message('Hello!', 'How are you?')
mail.send_message('friend@gmail.com')

# Send with priority and CC
mail.set_message('Urgent!', 'Please review ASAP')
mail.set_priority('urgent')
mail.send_message_with_cc_bcc(
    to='boss@company.com',
    cc=['team@company.com']
)

# Use templates for personalization
template = "Hello {{name}}, your code is {{code}}"
mail.set_template_message('Code', template, {'name': 'John', 'code': '1234'})
mail.send_message('john@example.com')
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

# Send formatted message with document
tg.send_message(
    user_id=123456789,
    message="**Important!** Read the `report.pdf`",
    document="report.pdf",
    parse_mode='markdown'
)

# Send video with caption
tg.send_message(
    user_id=123456789,
    message="Check out this video!",
    video="video.mp4"
)

# Get user information
user_info = tg.get_user_info(123456789)
print(f"User: {user_info['username']}, Premium: {user_info['is_premium']}")

# Mass messaging with formatting
user_ids = [111111, 222222, 333333]
tg.start_selective_spam(
    chats=user_ids,
    message="__Hello__ everyone!",
    parse_mode='markdown'
)
```

### 🔵 VKontakte Example

```python
from social_spam import Vkontakte

# Connect with token
vk = Vkontakte()
vk.connect_user(token="your_vk_token")

# Send document
vk.send_message(
    user_id=123456,
    message="Вот файл",
    document="document.pdf"
)

# Get friends and send to all
friends = vk.get_friends()
friend_ids = [f['id'] for f in friends]
vk.start_selective_spam(
    chats=friend_ids,
    message="Привет всем друзьям!"
)

# Get user info
user_info = vk.get_user_info(123456)
print(f"User: {user_info['first_name']} {user_info['last_name']}")
```

### 📲 WhatsApp Example

```python
from social_spam import WhatsApp

wa = WhatsApp()

# Load message from file
wa.set_file_message('message.txt')
wa.send_message(phone="+1234567890")

# Send with custom delays
wa.start_bombing(
    phone_number="+1234567890",
    amount=5,
    text="Hello!",
    wait_time=10,
    close_time=2
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
<summary><b>Custom SMTP Server with TLS</b></summary>

```python
mail = Mail()
mail.set_server('smtp.gmail.com', 587, use_tls=True)  # TLS support
mail.connect_mail('your@gmail.com', 'app_password')
```
</details>

<details>
<summary><b>Telegram with Formatted Messages</b></summary>

```python
tg = Telegram()
tg.connect_user(api_id=12345, api_hash="hash", phone_number="+123")

# Markdown formatting
message = """
**Important Announcement!**

__Details:__
• Item 1
• Item 2

Check the `report.pdf`
"""

tg.send_message(
    user_id=123456,
    message=message,
    document='report.pdf',
    parse_mode='markdown'
)
```
</details>

<details>
<summary><b>VKontakte Friends Management</b></summary>

```python
vk = Vkontakte()
vk.connect_user(token="your_token")

# Get all friends
friends = vk.get_friends()
print(f"You have {len(friends)} friends")

# Send to specific friends
for friend in friends[:10]:
    vk.send_message(
        user_id=friend['id'],
        message=f"Привет, {friend['first_name']}!"
    )
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
