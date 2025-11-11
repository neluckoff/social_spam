#!/usr/bin/env python3
"""
Simple test script for CI/CD to verify all modules can be imported and instantiated.
Works across all platforms (Linux, macOS, Windows) and Python versions (3.8-3.12).
"""
import sys
import traceback


def test_mail_import():
    """Test Mail module import and instantiation."""
    try:
        from social_spam import Mail
        mail = Mail()
        assert mail is not None
        print("[OK] Mail module imported and instantiated successfully")
        return True
    except Exception as e:
        print(f"[FAIL] Mail module: {e}")
        traceback.print_exc()
        return False


def test_telegram_import():
    """Test Telegram module import and instantiation."""
    try:
        from social_spam import Telegram
        tg = Telegram()
        assert tg is not None
        print("[OK] Telegram module imported and instantiated successfully")
        return True
    except Exception as e:
        print(f"[FAIL] Telegram module: {e}")
        traceback.print_exc()
        return False


def test_vkontakte_import():
    """Test Vkontakte module import and instantiation."""
    try:
        from social_spam import Vkontakte
        vk = Vkontakte()
        assert vk is not None
        print("[OK] Vkontakte module imported and instantiated successfully")
        return True
    except Exception as e:
        print(f"[FAIL] Vkontakte module: {e}")
        traceback.print_exc()
        return False


def test_whatsapp_import():
    """Test WhatsApp module import and instantiation."""
    try:
        from social_spam import WhatsApp
        wa = WhatsApp()
        assert wa is not None
        print("[OK] WhatsApp module imported and instantiated successfully")
        return True
    except Exception as e:
        print(f"[FAIL] WhatsApp module: {e}")
        traceback.print_exc()
        return False


def test_version():
    """Test package version is accessible."""
    try:
        import social_spam
        version = social_spam.__version__
        assert version is not None
        assert isinstance(version, str)
        assert len(version) > 0
        print(f"[OK] Package version: {version}")
        return True
    except Exception as e:
        print(f"[FAIL] Version check: {e}")
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 70)
    print("Running social_spam import tests")
    print("=" * 70)
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print("=" * 70)
    
    results = []
    
    # Run all tests
    results.append(("Version", test_version()))
    results.append(("Mail", test_mail_import()))
    results.append(("Telegram", test_telegram_import()))
    results.append(("Vkontakte", test_vkontakte_import()))
    results.append(("WhatsApp", test_whatsapp_import()))
    
    print("=" * 70)
    print("Test Results Summary:")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for name, result in results:
        status = "PASSED" if result else "FAILED"
        print(f"{name}: {status}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print("=" * 70)
    print(f"Total: {passed} passed, {failed} failed")
    print("=" * 70)
    
    # Exit with appropriate code
    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()

