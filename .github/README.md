# GitHub Configuration for social_spam

This directory contains all GitHub-specific configuration files for the social_spam project.

## 📁 Directory Structure

```
.github/
├── workflows/               # GitHub Actions workflows
│   ├── python-tests.yml    # CI/CD for testing on multiple Python versions and OSes
│   ├── publish-to-pypi.yml # Automatic publishing to PyPI on releases
│   └── codeql-analysis.yml # Security vulnerability scanning
│
├── ISSUE_TEMPLATE/         # Issue templates
│   ├── bug_report.yml      # Template for bug reports
│   ├── feature_request.yml # Template for feature requests
│   ├── question.yml        # Template for questions
│   └── config.yml          # Issue template configuration
│
├── CODE_OF_CONDUCT.md      # Code of Conduct
├── CONTRIBUTING.md         # Contributing guidelines
├── SECURITY.md             # Security policy
├── FUNDING.yml             # Funding/sponsorship configuration
├── dependabot.yml          # Dependabot configuration
└── pull_request_template.md # PR template
```

## 🚀 GitHub Actions Workflows

### 1. Python Tests (`python-tests.yml`)

**Triggers:** Push and PR to master/main/develop

**What it does:**
- Tests on Ubuntu, macOS, and Windows
- Tests Python versions 3.8, 3.9, 3.10, 3.11, 3.12
- Runs import tests and version checks
- Performs linting with flake8

**Status Badge:**
```markdown
![Tests](https://github.com/neluckoff/social_spam/workflows/Python%20Tests/badge.svg)
```

### 2. Publish to PyPI (`publish-to-pypi.yml`)

**Triggers:** 
- Automatic on GitHub releases
- Manual workflow dispatch

**What it does:**
- Builds the package
- Checks package validity
- Publishes to PyPI (requires `PYPI_API_TOKEN` secret)

**Setup Required:**
1. Go to PyPI and create an API token
2. Add it to GitHub Secrets as `PYPI_API_TOKEN`
3. Repository Settings → Secrets → Actions → New repository secret

### 3. CodeQL Analysis (`codeql-analysis.yml`)

**Triggers:**
- Push to master/main
- PRs to master/main
- Weekly schedule (Mondays)

**What it does:**
- Scans code for security vulnerabilities
- Generates security alerts
- Integrates with GitHub Security tab

## 🐛 Issue Templates

We have three issue templates:

### Bug Report
- Structured form for bug reports
- Collects version info, OS, reproduction steps
- Helps maintainers quickly understand and fix issues

### Feature Request
- Template for suggesting new features
- Asks for problem description and proposed solution
- Option to indicate willingness to contribute

### Question
- For general usage questions
- Links to documentation and existing resources

## 📝 Pull Request Template

All PRs use a standardized template that asks for:
- Description of changes
- Type of change (bug fix, feature, etc.)
- Related issue reference
- Testing checklist
- Documentation updates

## 🤝 Contributing Guidelines

`CONTRIBUTING.md` provides comprehensive guidance on:
- How to report bugs
- How to suggest enhancements
- Development setup
- Code style guidelines
- Commit message conventions
- Testing procedures

## 📜 Code of Conduct

Based on Contributor Covenant 2.0, defining:
- Expected behavior
- Unacceptable behavior
- Enforcement procedures
- Contact information

## 🔒 Security Policy

`SECURITY.md` covers:
- Supported versions
- How to report vulnerabilities
- Response timeline
- Security best practices for users
- Known security considerations

## 🤖 Dependabot

`dependabot.yml` configures automatic dependency updates:
- Checks pip dependencies weekly
- Checks GitHub Actions weekly
- Creates PRs with proper labels
- Runs on Mondays at 9 AM

## 💰 Funding

`FUNDING.yml` can be configured with:
- GitHub Sponsors
- Patreon
- Ko-fi
- Open Collective
- Custom URLs

**To enable:** Uncomment and add your username/links

## 🎯 Getting Started

### For Maintainers

1. **Enable GitHub Actions:**
   - Go to repository Settings → Actions
   - Enable workflows

2. **Set up PyPI Publishing:**
   - Create PyPI API token
   - Add to GitHub Secrets as `PYPI_API_TOKEN`

3. **Enable Dependabot:**
   - Already configured, will start automatically

4. **Enable Discussions:**
   - Go to Settings → Features
   - Enable Discussions

5. **Enable Security Features:**
   - Enable Dependabot alerts
   - Enable Dependabot security updates
   - Review CodeQL results in Security tab

### For Contributors

1. Read `CONTRIBUTING.md`
2. Read `CODE_OF_CONDUCT.md`
3. Check existing issues before creating new ones
4. Use issue templates when reporting bugs or requesting features
5. Follow PR template when submitting changes

## 📊 Badges for README

Add these badges to your main README.md:

```markdown
![Tests](https://github.com/neluckoff/social_spam/workflows/Python%20Tests/badge.svg)
![CodeQL](https://github.com/neluckoff/social_spam/workflows/CodeQL/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/github/license/neluckoff/social_spam)
![Issues](https://img.shields.io/github/issues/neluckoff/social_spam)
![Stars](https://img.shields.io/github/stars/neluckoff/social_spam)
```

## 🔧 Customization

Feel free to customize these files based on your needs:

- Adjust Python versions in test workflow
- Add more test commands
- Modify issue templates
- Update contributing guidelines
- Add more workflows (e.g., documentation builds)

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [About Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [About Pull Request Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [Dependabot Documentation](https://docs.github.com/en/code-security/dependabot)

---

**Questions?** Open an issue or contact neluckoff@gmail.com

