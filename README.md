
# Pytest automation

## Description:

Playwright + pytest for [Automation exercise website](https://automationexercise.com/)

Framework utilises functionality of the Allure reporter. Reports are stored and displayed via GitHub Pages. Also, there is an integrated Slack notification when GitHub Actions runs.

---

## 1. Install environment:

```bash
python -m pip install --upgrade pip  
pip install pipenv  
pipenv install --system  
playwright install chromium
```

---

## 2. Run playwright tests:

**Run all set of tests:**
```bash
pytest
```

**Run one particular test:**
```bash
pytest -k <name of the test>
```

---

## 3. Generate allure report:

Test report is generated automatically after each test run overriding the previous report. Use this command to see the report:
```bash
allure serve reports
```
