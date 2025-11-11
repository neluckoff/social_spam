# Migration Guide from v1.2.4 to v1.3.0

## Overview

Version 1.3.0 brings important fixes and updates to make the package work with modern Python versions and dependencies. The good news is that **all existing code should continue to work without changes** - we've maintained backward compatibility!

## What Changed?

### 1. Python Version Requirements
- **Old**: Python 3.6+ 
- **New**: Python 3.8+ (3.6 and 3.7 reached end of life)

**Action Required**: If you're using Python 3.6 or 3.7, please upgrade to Python 3.8 or higher.

### 2. Dependencies Updated
All dependencies have been updated to their latest stable versions:
- `pyrogram` → 2.0+
- `alive-progress` → 3.0+
- `vk-api` → 11.9+
- `pywhatkit` → 5.0+
- `TgCrypto` → 1.2+

**Action Required**: None! Just reinstall the package and dependencies will be updated automatically.

### 3. Import Behavior
**Fixed**: Import errors that occurred in v1.2.4 when internet connection was unavailable.

- WhatsApp module no longer checks internet connection on import
- Mail module no longer creates SMTP connection on initialization

**Action Required**: None! Your existing code will work better now.

## How to Upgrade

### Method 1: From PyPI (when published)
```bash
pip install --upgrade social-spam
```

### Method 2: From GitHub
```bash
pip install --upgrade https://github.com/neluckoff/social_spam/archive/master.zip
```

### Method 3: Development Installation
```bash
git clone https://github.com/neluckoff/social_spam.git
cd social_spam
pip install -r requirements.txt
pip install -e .
```

## Testing Your Code

After upgrading, you can verify everything works:

```python
# Test imports
from social_spam import Mail, Telegram, Vkontakte, WhatsApp
print("✅ All imports successful!")

# Test version
import social_spam
print(f"Version: {social_spam.__version__}")  # Should print: 1.3.0
```

## Breaking Changes

**None!** All existing code should work without modifications.

## Bug Fixes

If you experienced any of these issues in v1.2.4, they are now fixed:

1. ✅ "InternetException" when importing WhatsApp module
2. ✅ "[Errno 8] nodename nor servname provided" when importing Mail module  
3. ✅ Compatibility issues with newer Python versions
4. ✅ Dependency conflicts with modern package versions

## Need Help?

If you encounter any issues during migration:

1. Check that you're using Python 3.8 or higher: `python --version`
2. Make sure all dependencies are installed: `pip install -r requirements.txt`
3. Try a clean installation:
   ```bash
   pip uninstall social-spam
   pip install social-spam
   ```
4. Open an issue on [GitHub](https://github.com/neluckoff/social_spam/issues)

## Example Code (Still Works!)

All your existing code continues to work:

```python
# Mail Example
from social_spam import Mail

mail = Mail()
mail.connect_mail('test@inbox.ru', 'my_password')
mail.set_message('Hello', 'This still works!')
mail.send_message('friend@gmail.com')

# Telegram Example  
from social_spam import Telegram

tg = Telegram()
tg.connect_user(api_id=1234, api_hash="hash", phone_number="89261234567")
tg.send_message(user_id=123456, message="Still working!")

# And so on...
```

## What's Next?

We're committed to maintaining this package and keeping it compatible with modern Python and its dependencies. Stay tuned for future updates!

---

**Questions?** Feel free to open an issue on GitHub!

