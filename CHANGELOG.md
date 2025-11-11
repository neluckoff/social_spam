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
- **requirements.txt**: Added for easier development setup
- **Compatibility**: Verified compatibility with Pyrogram 2.0.x
- **Better Error Handling**: Improved error handling in Mail module

### Technical Improvements
- Lazy loading pattern for external dependencies
- Better resource management (SMTP connections)
- Improved code structure and maintainability

## [1.2.4] - 2022

### Initial Features
- Support for Telegram messaging via Pyrogram
- Support for VKontakte messaging via vk-api
- Support for WhatsApp messaging via pywhatkit
- Support for Email messaging via SMTP
- Spam and bombing functionality for all platforms
- Progress bars for batch operations
- Image attachment support

