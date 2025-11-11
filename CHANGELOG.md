# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-11-11

### Fixed
- **WhatsApp Module**: Fixed import error caused by `pywhatkit` checking internet connection at import time
  - Implemented lazy loading for `pywhatkit` to avoid connection check during module import
  - WhatsApp class now only checks connection when actually using the module

- **Mail Module**: Fixed SMTP connection initialization
  - Removed automatic SMTP connection on class initialization
  - SMTP connection now created only when needed (lazy initialization)
  - Improved connection handling and cleanup

- **TgCrypto**: Made TgCrypto an optional dependency
  - Fixes installation issues on macOS and other platforms where compilation fails
  - TgCrypto is now in `extras_require` for optional faster Telegram encryption
  - Install with: `pip install social-spam[telegram_speedup]`
  - CI tests now more reliable across all platforms

- **CI/CD**: Improved test matrix
  - Python 3.8 excluded from macOS tests (PyObjC requires 3.9+)
  - All other combinations still fully tested

### Changed
- **Python Support**: Updated minimum Python version to 3.8
  - Added support for Python 3.9, 3.10, 3.11, and 3.12
  - Removed support for Python 3.6 and 3.7 (end of life)

- **Dependencies**: Updated all dependencies to modern versions
  - `alive-progress>=3.0.0` (was unversioned)
  - `pyrogram>=2.0.0` (was unversioned)
  - `vk-api>=11.9.0` (was unversioned)
  - `pywhatkit>=5.0` (was unversioned)
  - `TgCrypto>=1.2.0` (was unversioned)

- **Version**: Bumped version from 1.2.4 to 1.3.0

### Added

#### 📧 Mail Module
- **TLS Support**: Added support for TLS/STARTTLS connections (in addition to SSL)
  - New parameter `use_tls` in `set_server()` method
  - Now supports Gmail and other TLS-only SMTP servers
- **Message Priority**: Added ability to set email priority
  - New method `set_priority()` with options: 'urgent', 'normal', 'low'
- **CC/BCC Support**: Added carbon copy and blind carbon copy functionality
  - New method `set_cc_bcc()` to set CC and BCC recipients
  - New method `send_message_with_cc_bcc()` for direct sending with copies
- **Message Templates**: Added template system with variable substitution
  - New method `set_template_message()` using `{{variable}}` syntax

#### 💬 Telegram Module
- **Document Support**: Added ability to send any file type
  - New method `set_document()`
- **Video Support**: Added video file sending
  - New method `set_video()` (supports mp4, avi, mkv, mov, flv)
- **Audio Support**: Added audio file sending
  - New method `set_audio()` (supports mp3, wav, ogg, m4a, flac)
- **Text Formatting**: Added Markdown and HTML formatting support
  - New method `set_parse_mode()` with options: 'markdown', 'html', None
- **User Information**: Added method to get user details
  - New method `get_user_info()` returns profile information

#### 🔵 VKontakte Module
- **Document Support**: Added document file sending
  - New method `set_document()`
- **Audio Messages**: Added voice message support
  - New method `set_audio_message()`
- **Friends List**: Added ability to get friends list
  - New method `get_friends()`
- **User Information**: Added detailed user info retrieval
  - New method `get_user_info()`

#### 📲 WhatsApp Module
- **File Message Loading**: Added ability to load messages from text files
  - New method `set_file_message()` (supports .txt and .md files)
- **Document Support**: Added document attachment preparation
  - New method `set_document()`
- **Customizable Delays**: Added delay customization
  - New parameters `wait_time` and `close_time` in `start_bombing()` and `start_spamming()`

#### Other
- **requirements.txt**: Added for easier development setup
- **Compatibility**: Verified compatibility with Pyrogram 2.0.x
- **Better Error Handling**: Improved error handling in Mail module

### Technical Improvements
- Lazy loading pattern for external dependencies
- Better resource management (SMTP connections)
- Improved code structure and maintainability
- **Modern Build System**: Migrated to pyproject.toml (PEP 621)
  - Added `pyproject.toml` for modern packaging
  - Added `MANIFEST.in` for proper file inclusion
  - Improved GitHub Actions publish workflow with pre-publish tests
  - Added local build verification scripts
  - Added comprehensive publishing documentation

## [1.2.4] - 2022

### Initial Features
- Support for Telegram messaging via Pyrogram
- Support for VKontakte messaging via vk-api
- Support for WhatsApp messaging via pywhatkit
- Support for Email messaging via SMTP
- Spam and bombing functionality for all platforms
- Progress bars for batch operations
- Image attachment support

