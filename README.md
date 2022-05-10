# Blog Simples

## Descrição
Projeto desenvolvido como parte do processo seletivo da Ivory It.

O sistema tem por objetivo ser um simples blog, onde um usuário anônimo pode ler e comentar posts. Além disso, o gestor pode criar novos posts, editá-los e apagá-los.

## Configuração do projeto

### Tecnologias

O sistema foi inteiramente desenvolvida usando Python 3.7, com o framework Django 3.2.3. O banco de dados escolhido foi o PostgreSQL 13.3.

### Instruções de execução

Primeiramente, após clonar o repositório, é preciso criar o ambiente virtual e instalar as dependências do projeto Python:
> python -m venv venv
> 
> pip install -r requirements.txt

Após isso, ajuste o arquivo [settings.py](sistemablogs/settings.py) para as configurações de banco de dados desejadas (nome do DB, porta, senha, etc.). Além disso, não esqueça de incluir uma variável de ambiente chamada SECRET_KEY para que o projeto possa ser executado! É possível criar uma SECRET_KEY pelo shell do seu projeto, com o seguinte código:
> from django.core.management.utils import get_random_secret_key
>
> print(get_random_secret_key())

Então, efetue a migração dos models:
> python manage.py migrate

Para iniciar o projeto, utilize o seguinte comando:
> python manage.py runserver

Após iniciar o projeto, acesse a seguinte URL para ter acesso à lista de posts:
> http://localhost:8000/blog/posts/

Para a criação de novos posts, é necessário ter acesso ao Django Admin. Para criar um novo usuário, utilize o seguinte comando e siga as instruções:
> python manage.py createsuperuser

Após isso, é possível acessar o Admin através da seguinte URL:
> http://localhost:8000/admin/

### Docker

O projeto possui configurações para criar o container do banco de dados! Caso deseje utilizá-lo, na raiz do projeto crie um arquivo chamado .env e adicione as variáveis necessárias. É possível encontrar um arquivo de exemplo em [.env_example](.env_example). Após a criação desse arquivo, rode o seguinte comando:
> docker-compose up -d db

Após criação do container, lembre de configurar o banco de dados criado ao projeto, como explicado no passo "Instruções de execução"!



