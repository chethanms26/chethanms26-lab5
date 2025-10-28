# Static Code Analysis Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
- Easiest: style and formatting issues (missing docstrings, line length, unused imports). These are straightforward, low-risk changes with clear guidance from linters.
- Hardest: refactors for mutable defaults and replacing broad exception handling. They required design changes to avoid subtle bugs and to follow best practices.

## 2. Did the static analysis tools report any false positives? If so, describe one example.
- Yes. Example: Bandit flagged use of `open()` without explicit encoding. In this simple inventory script the risk is low, but the warning is reasonable for broader applications.

## 3. How would you integrate static analysis tools into your development workflow?
- Use pre-commit hooks to run Pylint, Flake8, and Bandit locally on staged files.
- Run the same tools in CI (e.g., GitHub Actions) for every pull request and fail the build on high-severity issues.
- Keep lint rules consistent across local and CI environments to avoid rule drift.

## 4. What tangible improvements did you observe after applying the fixes?
- Readability improved via consistent naming and docstrings.
- Robustness increased by validating inputs and avoiding mutable default arguments.
- Security and reliability improved by removing unsafe constructs (e.g., `eval`) and by using explicit file encodings.
- Overall maintenance burden is reduced and the code is safer to extend.