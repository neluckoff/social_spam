# GitHub Setup Checklist

Quick guide to set up your GitHub repository after pushing the `.github` configuration.

## ✅ Immediate Setup (Required)

### 1. Push Changes to GitHub
```bash
git add .github/ README.md
git commit -m "Add: GitHub infrastructure for open-source project"
git push origin master
```

### 2. Enable GitHub Actions
1. Go to your repository on GitHub
2. Click **Settings** → **Actions** → **General**
3. Under "Actions permissions", select:
   - ✅ Allow all actions and reusable workflows
4. Click **Save**

## 🔧 Optional Setup (Recommended)

### 3. Enable GitHub Discussions
1. Go to **Settings** → **Features**
2. Check ✅ **Discussions**
3. Click **Set up discussions**
4. Create initial categories (Q&A, Ideas, General, etc.)

### 4. Enable Security Features
1. Go to **Settings** → **Code security and analysis**
2. Enable:
   - ✅ Dependency graph (usually already enabled)
   - ✅ Dependabot alerts
   - ✅ Dependabot security updates
   - ✅ CodeQL analysis (will start after first push)

### 5. Set Up PyPI Auto-Publishing
Only needed if you want automatic publishing to PyPI:

#### On PyPI:
1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
   - Name: `social_spam-github-actions`
   - Scope: `Project: social_spam` (or entire account)
3. Copy the token (starts with `pypi-...`)

#### On GitHub:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `PYPI_API_TOKEN`
4. Value: paste your PyPI token
5. Click **Add secret**

### 6. Configure Funding (Optional)
If you want to receive sponsorships:

1. Edit `.github/FUNDING.yml`
2. Uncomment and add your details:
   ```yaml
   github: neluckoff  # Your GitHub username
   # patreon: your-patreon
   # ko_fi: your-kofi
   ```
3. Commit and push changes

## 🎯 Post-Setup Verification

### Check Workflows
1. Go to **Actions** tab
2. You should see workflows running after your next push
3. Workflows:
   - ✅ Python Tests
   - ✅ CodeQL

### Check Issue Templates
1. Go to **Issues** → **New issue**
2. You should see:
   - 🐛 Bug Report
   - 💡 Feature Request
   - ❓ Question

### Check Security Tab
1. Go to **Security** tab
2. You should see:
   - Code scanning alerts (CodeQL)
   - Dependabot alerts
   - Security advisories

## 📊 Add Badges to README (Optional)

Add these to the top of your README.md:

```markdown
<div align="center">
    <h1>Social Spam</h1>
    
![Tests](https://github.com/neluckoff/social_spam/workflows/Python%20Tests/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/github/license/neluckoff/social_spam)
![Issues](https://img.shields.io/github/issues/neluckoff/social_spam)
![Stars](https://img.shields.io/github/stars/neluckoff/social_spam)
![PyPI](https://img.shields.io/pypi/v/social-spam)
![Downloads](https://img.shields.io/pypi/dm/social-spam)
</div>
```

## 🚀 How to Release

When you're ready to release a new version:

1. **Update version numbers:**
   ```bash
   # Update in setup.py and social_spam/__init__.py
   # Update CHANGELOG.md
   ```

2. **Commit and push:**
   ```bash
   git add .
   git commit -m "Bump version to X.Y.Z"
   git push
   ```

3. **Create a release on GitHub:**
   - Go to **Releases** → **Create a new release**
   - Tag: `vX.Y.Z` (e.g., `v1.3.0`)
   - Title: `vX.Y.Z`
   - Description: Copy from CHANGELOG.md
   - Click **Publish release**

4. **Automatic publishing:**
   - GitHub Actions will automatically build and publish to PyPI
   - Check the Actions tab for progress

## 📋 Regular Maintenance

### Weekly
- Review Dependabot PRs
- Check and merge security updates

### Monthly
- Review open issues and PRs
- Update documentation if needed
- Check analytics and downloads

### Per Release
- Update CHANGELOG.md
- Test on all supported Python versions
- Update documentation with new features

## 🆘 Troubleshooting

### Workflows Not Running
- Check if Actions are enabled in Settings
- Verify YAML syntax with online validator
- Check Actions tab for error messages

### PyPI Publishing Fails
- Verify `PYPI_API_TOKEN` is set correctly
- Check token has correct permissions
- Ensure package version is incremented

### Dependabot Not Creating PRs
- May take 24-48 hours after first push
- Check Settings → Code security and analysis
- Ensure dependabot.yml is valid

## 📚 Documentation Links

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [Dependabot](https://docs.github.com/en/code-security/dependabot)
- [CodeQL](https://docs.github.com/en/code-security/code-scanning)
- [PyPI Publishing](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

## ✨ You're All Set!

Your repository now has professional-grade GitHub infrastructure. Everything should work automatically from now on!

**Questions?** Open an issue or check `.github/README.md` for more details.

