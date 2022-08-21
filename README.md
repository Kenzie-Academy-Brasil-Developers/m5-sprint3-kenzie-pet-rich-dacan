# Kenzie Pet 🐶😺🐓

# Tabela de Conteúdos:


  - [Documentação da API](#documentação-da-api)
      - [A URL base da aplicação: https://solid-control-api.herokuapp.com/](#a-url-base-da-aplicação-httpssolid-control-apiherokuappcom)
  - [1. Visão Geral](#1-visão-geral)
  - [2. Diagrama ER](#2-diagrama-er)
  - [3. Início Rápido](#3-início-rápido)
    - [3.1. Instalando Dependências](#31-instalando-dependências)
    - [3.2. Variáveis de Ambiente](#32-variáveis-de-ambiente)
    - [3.3. Migrations](#33-migrations)
  - [5. Endpoints](#5-endpoints)
    - [Índice](#índice)
  - [5.1 Animals](#51-animals)
---




## Documentação da API

#### A URL base da aplicação: https://localhost:8000/

## 1. Visão Geral

Tecnologias e ferramentas usadas:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [SqLite](https://www.sqlite.org/index.html)
- [IPython](https://ipython.org/)
- [PyCodestyle](https://pypi.org/project/pycodestyle/)
- [Python Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/)

---

## 2. Diagrama ER

[ Voltar para o topo ](#tabela-de-conteúdos)

Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados.

![DER](./KPet(DER).png)

---

## 3. Início Rápido

[ Voltar para o topo ](#tabela-de-conteúdos)

### 3.1. Crie o ambiente virtual

## Instruções:

```
python -m venv venv
```
### Ative o venv
```bash
# linux: 

source venv/bin/activate

```

### Instale as dependências 
```
pip install -r requirements.txt
```
### Execute as migrações
```
./manage.py migrate
```

---

## 5. Endpoints

[ Voltar para o topo ](#tabela-de-conteúdos)

### Índice

- [Animals](#5.0-Animals)

  - [POST - api/animals/](#)
  - [GET - api/animals/](#)
  - [GET - api/animals/:animal_id](#)
  - [PATCH - api/animals/:animal_id](#)
  - [DELETE - api/animals/:animal_id](#)

---

## 5.1 Animals

Animals é a tabela responsavel por armazenar os dados de todos os animais que já passaram ou ainda estão em nosso empreendimento.

| Name       | Description                       | Type    |
| ---------- | --------------------------------- | ------- |
| name       | Nome                              | String  |
| age        | Idade                             | Number  |
| weight     | Peso                              | Number  |
| sex        | Sexo                              | String  |
| group      | Grupo                             | String  |
| traits     | Características                   | String  |

<br>

<span style="background:green; color: black; font-weight: bold; padding: 2px 5px;">POST</span> **/api/animals/**
---

Rota criada para podermos criar um novo animal.

Corpo da requisição:

```JSON
{
	"name": "Gohan",
	"age": 3,
	"weight": 8,
	"sex": "Macho",
	"group": {"name": "gato", "scientific_name": "felis catus"},
  "traits": [
		{"name": "pelo curto"}, {"name": "pequeno porte"}
	]
}
```

Resposta da requisição:

```JSON
{
	"id": 11,
	"name": "Gohan",
	"age": 3,
	"weight": 8.0,
	"sex": "Macho",
	"group": {
		"id": 4,
		"name": "gato",
		"scientific_name": "felis catus"
	},
	"traits": [
		{
			"id": 5,
			"name": "pelo curto"
		},
		{
			"id": 6,
			"name": "pequeno porte"
		}
	],
	"age_in_human_years": 49
}
```
---

<span style="background:purple; color: black; font-weight: bold; padding: 2px 5px;">GET</span> **/api/animals/**
---

Rota criada para listar todos os animais cadastrados.

Resposta da requisição:

```JSON
[
    {
		"id": 1,
		"name": "Gohan",
		"age": 3,
		"weight": 8.0,
		"sex": "Macho",
		"group": {
			"id": 4,
			"name": "gato",
			"scientific_name": "felis catus"
		},
		"traits": [
			{
				"id": 5,
				"name": "pelo curto"
			},
			{
				"id": 6,
				"name": "pequeno porte"
			}
		],
		"age_in_human_years": 49
	},
	{
		"id": 2,
		"name": "Brutus Spike",
		"age": 3,
		"weight": 30.0,
		"sex": "Macho",
		"group": {
			"id": 2,
			"name": "cão",
			"scientific_name": "canis familiaris"
		},
		"traits": [
			{
				"id": 3,
				"name": "Bravo"
			}
		],
		"age_in_human_years": 49
	},
    {
		"id": 3,
		"name": "Ragnar",
		"age": 3,
		"weight": 12.0,
		"sex": "Macho",
		"group": {
			"id": 3,
			"name": "galo",
			"scientific_name": "gallus gallus"
		},
		"traits": [
			{
				"id": 4,
				"name": "gigante"
			}
		],
		"age_in_human_years": 49
	},
    {
		"id": 4,
		"name": "Pan",
		"age": 13,
		"weight": 10.0,
		"sex": "Fêmea",
		"group": {
			"id": 1,
			"name": "cão",
			"scientific_name": "canis familiaris"
		},
		"traits": [
			{
				"id": 5,
				"name": "pelo curto"
			},
			{
				"id": 6,
				"name": "pequeno porte"
			}
		],
		"age_in_human_years": 72
	},
```

---

<span style="background:purple; color: black; font-weight: bold; padding: 2px 5px;">GET</span> **/api/animals/:animal_id**
---

Rota criada para ler um animal específico informando o seu id na url.

Resposta da requisição:

```JSON
{
	"id": 11,
	"name": "Goku",
	"age": 3,
	"weight": 8.0,
	"sex": "Macho",
	"group": {
		"id": 4,
		"name": "gato",
		"scientific_name": "felis catus"
	},
	"traits": [
		{
			"id": 5,
			"name": "pelo curto"
		},
		{
			"id": 6,
			"name": "pequeno porte"
		}
	],
	"age_in_human_years": 49
}
```

---

<span style="background:yellow; color: black; font-weight: bold; padding: 2px 5px;">PATCH</span> **/api/animals/:animal_id**
---

Rota criada para permitir a atualização dos dados cadastrais do animal. 
Será necessário passar o id do animal que será atualizado.

Exemplo de corpo da requisição:

```JSON
{
	"name": "Esmeralda"
}
```
Exemplo de resposta caso o animal não conste no banco de dados:

```JSON
{
	"detail": "Animal not found."
}

```

### Dados que não poderão ser modificados: "group", "traits" e "sex". 
Caso haja uma tentativa de alteração destes dados, o seguinte erro será reportado na resposta da requisição:


```JSON
{
	"group": "You can not update group property.",
   	"traits": "You can not update traits property.",
    	"sex": "You can not update sex property."
}


```

---

<span style="background:red; color: black; font-weight: bold; padding: 2px 5px;">DELETE</span> **/providers/:provider_id**
---

Rota criada para permitir a deleção total dos dados cadastrais do animal. 
Será necessário passar o id do animal que será deletado.


Exemplo de resposta caso o animal não conste no banco de dados:

```JSON
{
	"detail": "Animal not found."
}

```
