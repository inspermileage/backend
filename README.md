# Backend

Este repositório contém o código do backend, que implementa uma API RESTful para servir os dados do 
veículo. Esta aplicação foi feita utilizando FastAPI, SQLAlchemy e PostgreSQL.

## Como executar
### Requerimentos
- Obrigatórios: [Python 3.6 (ou superior)](https://www.python.org/downloads/), pipenv
 (`pip install pipenv`) e [PostgreSQL](https://www.postgresql.org/download/)
- Opcionais: [Docker](https://www.docker.com/products/docker-desktop) e 
[Docker Compose](https://docs.docker.com/compose/install/)

### Ambiente virtual
Após instalar os requerimentos obrigatórios, é necessário instalar as dependências do projeto. Isso 
é feito por meio do Pipenv, uma ferramenta que realiza a gestão de pacotes e ambiente virtual. Para 
utilizá-la, é preciso criar o ambiente com os pacotes. No terminal, na pasta *./backend*, onde se 
encontra o arquivo *Pipfile*, execute o seguinte comando: 
- `pipenv install --dev`

Isto criará um ambiente virtual com todas as dependências do projeto e as variáveis ambiente 
declaradas no arquivo *.env*. Para utilizar este ambiente, é preciso ativá-lo executando o comando:
- `pipenv shell`

Este comando mudará a linha do terminal para: `(backend-XXXXXXXX) <diretório>/backend/`. Isso 
significa que todos os comandos Python que forem executados, utilizaram o interpretador criado pelo 
Pipenv, que utilizará todas as dependências listadas no arquivo Pipfile, instaladas nesse ambiente.  
 
### Variáveis ambiente
O projeto faz uso de algumas variáveis ambiente, que não expõem nenhum segredo, mas que facilitam o 
desenvolvimento. Elas estão declaradas no arquivo: `.env` e são carregadas automaticamente na 
execução da aplicação pelo Pipenv. 

Por *default* a variável ambiente **POSTGRES_SERVER** é pré-definida para utilizar o banco de dados 
criado no Docker Compose, portanto para executar o projeto sem Docker, é preciso modificá-la para 
receber o valor do ambiente local.  
- Descomente a linha 2.
- Comente a linha 8.

### Banco de dados
O banco de dados da aplicação, PostgreSQL, deve estar instalado e em execução no seu computador. Uma
boa ferramenta para administrar o banco de dados é o Dbeaver, use-o para realizar o monitoramento e
desenvolvimento.

### Executando
Após organizar todo o ambiente de desenvolvimento, a aplicação pode ser executada via terminal pelo
comando:
- `pipenv run python main.py` (Certifique-se que o ambiente virtual está sendo utilizado)

### Docker
O projeto também pode ser executado via Docker (Docker Compose), que orquestra três containers:
- Servidor (FastAPI)
- Banco de dados (PostgreSQL)
- PgAdmin (Equivalente ao Dbeaver)

Para isso, execute seguinte comando:
- `docker-compose up -d --build`

## Rotas da aplicação
Com o servidor de FastAPI executando e conectado ao banco de dados, a documentação das rotas é
apresentada em: `localhost:8000/docs`.

A rota base da API é dada por `localhost:8000/api/`.

## Testes
Os testes de unidade presentes na pasta */teste* podem ser verificados pelo seguinte comando:
- `pipenv run pytest`

## Linting
Para verificar a qualidade do código, usa-se o *Pylint* e o *isort*. Eles podem ser executados pelos
seguintes comandos:
- `pipenv run flake8 --ignore=E501` (ignora warnings de linhas > 79 chars)
- `pipenv run isort -y`

## Contribuindo
Siga os passos abaixo para realizar contribuições no projeto, 

- Faça um Fork do projeto
- Crie uma Branch para sua Feature (`git checkout -b feature/<nome_feature>`)
- Adicione suas mudanças (`git add .`)
- Comite suas mudanças (`git commit -m 'Adicionando feature`)
- Faça o Push da Branch (`git push origin feature/<nome_feature>`)
- Abra um Pull Request no Github