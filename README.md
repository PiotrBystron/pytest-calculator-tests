## How to run

### 1 Clone repository

```bash
git clone https://github.com/PiotrBystron/pytest-calculator-tests.git
```

```bash
cd pytest-calculator-tests
```

### 2 Create and activate a virtual environment

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### 3 Install dependencies

```bash
pip install -r requirements.txt
```

### 4 Run the tests

```bash
pytest --html=report.html --self-contained-html
```

A detailed report will be generated as report.html in the project folder.