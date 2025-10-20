## How to run

### 1 Clone repository

git clone https://github.com/PiotrBystron/pytest-calculator-tests.git
cd pytest-calculator-tests


### 2 Create and activate a virtual environment

python -m venv .venv
.venv\Scripts\activate


### 3 Install dependencies

pip install -r requirements.txt


### 4 Run the tests

pytest --html=report.html --self-contained-html

A detailed report will be generated as report.html in the project folder.