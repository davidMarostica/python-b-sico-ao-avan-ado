# Python Básico ao Avançado

Este repositório contém exercícios e projetos de Python, indo do nível básico ao avançado. Ele inclui scripts de aprendizado de conceitos fundamentais, projetos de Flask e Django, manipulação de dados e visualização.

---

## Estrutura do Repositório

- `1_INTRO` até `9_LISTA_DE_COMPRA` → Exercícios introdutórios e fundamentos de Python (tipos de dados, strings, listas, operadores, funções, loops, etc.)
- `10_OPERADORES` até `24_PROG_FUNCIONAL` → Conceitos intermediários (funções, módulos, POO, decoradores, geradores e iteradores)
- `25_MODULOS` até `39_VISUALIZACAO_DE_DADOS` → Exercícios avançados, manipulação de arquivos, tratamento de erros, análise e visualização de dados
- `41_FLASK` e `42_TODO_FLASK` → Projetos completos utilizando Flask
- `43_DJANGO` → Projeto Django para prática de desenvolvimento web
- `README.md` → Documentação do repositório

---

## Requisitos

- Python 3.13 ou superior
- Virtualenv (recomendado)
- Bibliotecas Python:
  - Numpy, Pandas, Matplotlib, Seaborn
  - Requests, BeautifulSoup4, Lxml
  - Flask, Django, FastAPI, Uvicorn
  - SQLAlchemy, Psycopg2-binary, MySQLclient (opcional)
  - Pytest, Black, Pylint, Flake8
  - Python-dotenv, Pillow, Jinja2

---

## Como usar

1. **Clonar o repositório**

```bash
git clone https://github.com/davidMarostica/python-b-sico-ao-amvan-ado.git
cd python-b-sico-ao-amvan-ado

    Criar e ativar o ambiente virtual

python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

    Instalar as dependências

pip install -r requirements.txt

    Obs: Se você não tiver requirements.txt, instale manualmente as bibliotecas listadas na seção "Requisitos".

    Rodar scripts de Python

python caminho/do/script.py

    Rodar projetos Flask

cd 41_FLASK
flask run

    Rodar projeto Django

cd 43_DJANGO/projeto_1
python manage.py runserver

Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request para sugerir melhorias ou corrigir erros.