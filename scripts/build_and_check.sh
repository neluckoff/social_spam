#!/bin/bash
# Script to build and verify the package locally before publishing

set -e  # Exit on error

echo "🔨 Building social_spam package..."
echo "=================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/
echo ""

# Install build tools
echo "📦 Installing build tools..."
python -m pip install --upgrade pip build twine check-wheel-contents --quiet
echo ""

# Build the package
echo "🏗️  Building package..."
python -m build
echo ""

# Check build files
echo "📋 Built files:"
ls -lh dist/
echo ""

# Verify package integrity
echo "✅ Checking package integrity..."
twine check dist/*
echo ""

# Check wheel contents
echo "🔍 Checking wheel contents..."
check-wheel-contents dist/*.whl
echo ""

# Show wheel contents
echo "📦 Wheel contents:"
unzip -l dist/*.whl
echo ""

# Test installation in virtual environment
echo "🧪 Testing installation..."
python -m venv test_venv
source test_venv/bin/activate

pip install --quiet dist/*.whl
echo ""

# Test imports
echo "🔬 Testing imports..."
python -c "
from social_spam import Mail, Telegram, Vkontakte, WhatsApp
print('✅ All imports successful!')
print('  - Mail:', Mail)
print('  - Telegram:', Telegram)
print('  - Vkontakte:', Vkontakte)
print('  - WhatsApp:', WhatsApp)
"
echo ""

# Cleanup
deactivate
rm -rf test_venv

echo ""
echo -e "${GREEN}✅ Build verification complete!${NC}"
echo ""
echo "📦 Package files:"
ls -lh dist/
echo ""
echo "🚀 Ready to publish!"
echo ""
echo "To publish to PyPI:"
echo "  twine upload dist/*"
echo ""
echo "Or create a GitHub release to trigger automatic publishing"

