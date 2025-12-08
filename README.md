# 🦅 Patri Tech - API Backend

Bem-vindo ao repositório do projeto **Patri Tech**. Este sistema é um backend robusto desenvolvido em **Django**, focado em fornecer uma API RESTful documentada e escalável.

## 📋 Sobre o Projeto

O **Patri Tech** foi desenvolvido para gerenciar dados e prover serviços através de endpoints HTTP. Ele utiliza o **Django REST Framework** para a serialização de dados e **Swagger** para a documentação interativa da API, facilitando o consumo por front-ends ou serviços terceiros.

## 🚀 Tecnologias Utilizadas

* **Python 3.x**: Linguagem base.
* **Django**: Framework web principal.
* **Django REST Framework (DRF)**: Criação da API.
* **drf-yasg / Swagger**: Documentação automática da API.
* **SQLite**: Banco de dados padrão (pode ser configurado para PostgreSQL/MySQL).

## 📂 Estrutura de Pastas

* `projeto/`: Configurações globais do Django (`settings.py`, `urls.py`).
* `core/`: Aplicação principal contendo Models, Views, Serializers e Lógica de Negócio.
* `venv/`: Ambiente virtual Python (Bibliotecas).

---

## ⚙️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente:

### 1. Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/) instalado.

### 2. Clonar/Baixar
Extraia os arquivos do projeto em uma pasta de sua preferência.

### 3. Configurar Ambiente Virtual
Recomendamos criar um novo ambiente virtual limpo para instalar as dependências.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate

python3 -m venv venv
source venv/bin/activate

pip install django djangorestframework drf-yasg django-filter markdown

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

