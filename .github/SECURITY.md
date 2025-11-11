# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.3.x   | :white_check_mark: |
| 1.2.x   | :x:                |
| < 1.2   | :x:                |

## Reporting a Vulnerability

We take the security of social_spam seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please DO NOT

- **Do not** open a public GitHub issue for security vulnerabilities
- **Do not** post vulnerability details in public forums or social media

### Please DO

1. **Email** security details to: neluckoff@gmail.com
2. **Include** the following information:
   - Type of vulnerability
   - Full paths of source file(s) related to the vulnerability
   - Location of the affected source code (tag/branch/commit)
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the vulnerability
   - How you think we should address the issue

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Communication**: We will keep you informed about our progress in addressing the vulnerability
- **Fix**: We will work to fix confirmed vulnerabilities as quickly as possible
- **Credit**: We will credit you in the security advisory (unless you prefer to remain anonymous)
- **Disclosure**: After a fix is released, we will publicly disclose the vulnerability

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Fix Development**: Varies based on severity and complexity
- **Public Disclosure**: After fix is released and users have had time to update

## Security Best Practices for Users

When using social_spam:

1. **Keep Updated**: Always use the latest version
2. **Secure Credentials**: Never hardcode API keys or passwords in your code
3. **Environment Variables**: Use environment variables for sensitive data
4. **Validate Input**: Always validate and sanitize user input
5. **Rate Limiting**: Implement rate limiting to prevent abuse
6. **Error Handling**: Don't expose sensitive information in error messages

### Example: Secure Credential Handling

```python
import os
from social_spam import Telegram

# ✅ Good: Use environment variables
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone = os.getenv('TELEGRAM_PHONE')

tg = Telegram()
tg.connect_user(api_id=api_id, api_hash=api_hash, phone_number=phone)

# ❌ Bad: Hardcoded credentials
# tg.connect_user(api_id=12345, api_hash="secret", phone_number="+1234567890")
```

## Known Security Considerations

### API Credentials

This library works with messaging APIs that require credentials:
- **Telegram**: Requires API ID and API hash from my.telegram.org
- **VKontakte**: Requires access token
- **Mail**: Requires email credentials

**Important**: Never commit credentials to version control or share them publicly.

### Session Files

Some modules (like Telegram with Pyrogram) create session files:
- Session files contain authentication data
- Keep session files secure and private
- Add `*.session` to your `.gitignore`

### Rate Limiting

When using this library:
- Respect API rate limits to avoid being banned
- Implement proper delays between requests
- Don't use for spam or abuse (as the name suggests, this is for educational purposes)

## Responsible Disclosure

We follow the principle of responsible disclosure:

1. Security researchers report vulnerabilities privately
2. We work to fix the vulnerability
3. We release a security patch
4. After users have had time to update, we publicly disclose the vulnerability with credit to the researcher

## Legal Notice

This project is intended for legitimate use cases only. Users are responsible for ensuring their use of this library complies with:
- Terms of Service of messaging platforms
- Applicable laws and regulations
- Privacy and data protection requirements

## Contact

For security-related inquiries: neluckoff@gmail.com

For general questions: [Open an issue](https://github.com/neluckoff/social_spam/issues)

---

**Thank you for helping keep social_spam and its users safe!** 🔒

