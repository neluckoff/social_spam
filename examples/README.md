# 📚 Social Spam - Examples & Tutorials

Welcome to the examples directory! Here you'll find comprehensive code examples for all supported platforms.

## 📋 Table of Contents

| Platform | File | Description |
|----------|------|-------------|
| 📧 **Email** | [`mail_examples.py`](mail_examples.py) | SMTP email sending with attachments and HTML templates |
| 💬 **Telegram** | [`telegram_examples.py`](telegram_examples.py) | Telegram messaging via Pyrogram API |
| 🔵 **VKontakte** | [`vkontakte_examples.py`](vkontakte_examples.py) | VK messaging and mass mailing |
| 📲 **WhatsApp** | [`whatsapp_examples.py`](whatsapp_examples.py) | WhatsApp web automation |

---

## 🚀 Quick Start Examples

### 📧 Email - Simple Example

```python
from social_spam import Mail

mail = Mail()
mail.connect_mail('your_email@mail.ru', 'your_password')
mail.set_message('Hello!', 'This is a test message')
mail.send_message('recipient@gmail.com')
```

[See full email examples →](mail_examples.py)

---

### 💬 Telegram - Simple Example

```python
from social_spam import Telegram

tg = Telegram()
tg.connect_user(
    api_id=12345,
    api_hash="your_hash",
    phone_number="+1234567890"
)
tg.send_message(user_id=123456789, message="Hello!")
```

[See full Telegram examples →](telegram_examples.py)

---

### 🔵 VKontakte - Simple Example

```python
from social_spam import Vkontakte

vk = Vkontakte()
vk.connect_user(token="your_vk_token")
vk.send_message(user_id=123456, message="Привет!")
```

[See full VKontakte examples →](vkontakte_examples.py)

---

### 📲 WhatsApp - Simple Example

```python
from social_spam import WhatsApp

wa = WhatsApp()
wa.send_message(
    phone="+1234567890",
    text="Hello from Python!"
)
```

[See full WhatsApp examples →](whatsapp_examples.py)

---

## 📖 Detailed Examples

Each file contains multiple examples covering:

### 📧 Email (`mail_examples.py`)
- ✅ Basic email sending
- ✅ Email with attachments
- ✅ HTML email templates
- ✅ Mass mailing (spam to multiple recipients)
- ✅ Email bombing (multiple messages to one recipient)
- ✅ Custom SMTP server configuration

### 💬 Telegram (`telegram_examples.py`)
- ✅ Connect to Telegram account
- ✅ Send text messages
- ✅ Send messages with images
- ✅ Get user ID by phone number
- ✅ Mass messaging to multiple users
- ✅ Message all contacts
- ✅ Message bombing

### 🔵 VKontakte (`vkontakte_examples.py`)
- ✅ Connect with VK token
- ✅ Send text messages
- ✅ Send messages with images
- ✅ Get chat IDs
- ✅ Selective spam to specific users
- ✅ Spam to all conversations
- ✅ Message bombing

### 📲 WhatsApp (`whatsapp_examples.py`)
- ✅ Send instant messages
- ✅ Send messages with images
- ✅ Mass messaging
- ✅ Message bombing

---

## 🔑 Getting API Credentials

### Telegram
1. Go to https://my.telegram.org/auth
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create an application
5. Copy `api_id` and `api_hash`

### VKontakte
1. Go to https://vkhost.github.io/
2. Select required permissions:
   - Messages
   - Friends
   - Access at any time
3. Click "Get Token"
4. Copy the token

### Email
- Use your email credentials
- For Gmail: Use [App Passwords](https://support.google.com/accounts/answer/185833)
- For Mail.ru/Yandex: Enable IMAP/SMTP in settings

### WhatsApp
- No credentials needed
- Opens browser automation
- Keep WhatsApp Web open during execution

---

## ⚠️ Important Notes

### Security
- 🔒 **Never commit credentials** to version control
- 🔒 Use environment variables for sensitive data
- 🔒 Keep your API keys and tokens private

### Rate Limiting
- ⏱️ **Telegram**: ~20-30 messages per minute
- ⏱️ **VKontakte**: ~20 messages per minute
- ⏱️ **Email**: Depends on SMTP server
- ⏱️ **WhatsApp**: Be careful to avoid bans

### Best Practices
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variables
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
```

---

## 🆘 Need Help?

- 📖 [Main Documentation](../README.md)
- 🐛 [Report Issues](https://github.com/neluckoff/social_spam/issues)
- 💬 [Ask Questions](https://github.com/neluckoff/social_spam/discussions)

---

## 📝 Running Examples

1. **Install the package:**
   ```bash
   pip install social-spam
   ```

2. **Navigate to examples:**
   ```bash
   cd examples/
   ```

3. **Edit credentials in the example file**

4. **Run the example:**
   ```bash
   python mail_examples.py
   # or
   python telegram_examples.py
   # etc.
   ```

---

## 🎓 Learning Path

**Recommended order for beginners:**

1. 📧 Start with **Email** - easiest to set up
2. 🔵 Try **VKontakte** - simple token-based auth
3. 💬 Move to **Telegram** - requires API credentials
4. 📲 Finally **WhatsApp** - requires browser automation

---

## 💡 Tips & Tricks

### Delay Between Messages
Always add delays to avoid being banned:

```python
import time

for user in users:
    send_message(user, "Hello!")
    time.sleep(2)  # Wait 2 seconds
```

### Error Handling
Wrap your code in try-except:

```python
try:
    tg.send_message(user_id, "Hello!")
except Exception as e:
    print(f"Error: {e}")
```

### Progress Tracking
The library includes `alive_progress` for visual feedback:

```python
# Already built-in for mass operations!
tg.start_selective_spam(users, message="Hi")
# Shows progress bar automatically
```

---

## 📜 License

All examples are provided under MIT License and are free to use and modify.

**Happy Messaging!** 🎉

<div align="center">

[⬆ Back to Main Documentation](../README.md)

</div>

