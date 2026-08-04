# 🖥️ Gear Hub

> Marketplace C2C acadêmico para compra e venda de hardware, periféricos, consoles, notebooks e acessórios.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-orange?logo=cloudinary)
![Railway](https://img.shields.io/badge/Deploy-Railway-purple?logo=railway)

> ⚠️ **Projeto acadêmico para fins de portfólio. Não realize transações reais.**
### Acesse em: https://gear-hub-production.up.railway.app/
---

## 📋 Sobre o Projeto

O **Gear Hub** é um marketplace C2C (consumidor para consumidor) voltado ao segmento de tecnologia, desenvolvido como projeto de portfólio. A plataforma permite que usuários cadastrem e anunciem produtos como hardware, periféricos, consoles, notebooks e acessórios, além de favoritar anúncios e gerenciar seus perfis.

> 🐳 Esta branch (`docker`) contém a versão containerizada do projeto, com Dockerfile e Docker Compose para rodar a aplicação e o banco PostgreSQL isolados em containers, sem depender de instalação manual de dependências no host.

---

## ✨ Funcionalidades

- 🔐 **Autenticação completa** — cadastro, login e logout de usuários
- 👤 **Perfil de usuário** — criado automaticamente ao registrar, editável pelo próprio usuário
- 📦 **Listagem de produtos** — visualização paginada com filtros por categoria e marca
- 🔍 **Busca** — pesquisa por título, modelo e marca
- ❤️ **Favoritos** — salvar e remover produtos de uma lista pessoal
- ➕ **Anunciar produto** — formulário completo com upload de imagem via Cloudinary
- ✏️ **Editar e excluir anúncios** — restrito ao vendedor ou superusuário
- 🛡️ **Painel administrativo** — gerenciamento via Django Admin

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Django 6.0 (Python 3.12) |
| Banco de Dados | PostgreSQL 16 |
| Containerização | Docker + Docker Compose |
| Armazenamento de Mídia | Cloudinary |
| Deploy | Railway |
| Frontend | HTML, CSS (sem frameworks) |
| Fontes | DM Sans + DM Serif Display |

---

## 🏗️ Arquitetura

O projeto segue a arquitetura padrão do Django (MTV):

```
Gear-Hub/
├── gearhub/           # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/          # App de produtos
│   ├── models.py
│   ├── views.py       # Class-Based Views
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── users/             # App de usuários e perfis
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── static/            # CSS e assets estáticos
├── Dockerfile         # Imagem da aplicação
├── docker-compose.yml # Orquestração web + banco
├── .dockerignore
├── manage.py
└── requirements.txt
```

---

## ⚙️ Padrões Técnicos

- **Class-Based Views** com `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`
- **Permissões** via `UserPassesTestMixin` com bypass para superusuário
- **Formulários** com validação customizada em `clean_*`
- **Relacionamentos** — `ForeignKey` para marca/categoria, `ManyToManyField` para favoritos
- **Filtros múltiplos** via `request.GET.getlist()`
- **Atribuição automática do vendedor** via `form_valid()`
- **Signals** para criação automática de `Profile` ao registrar usuário

---

## 🚀 Como Rodar Localmente

Existem duas formas de rodar o projeto localmente: com **Docker** (recomendada, ambiente isolado e reprodutível) ou de forma **manual** (ambiente virtual Python direto no host).

### 🐳 Opção 1 — Com Docker (recomendado)

#### Pré-requisitos
- Docker
- Docker Compose
- Git

#### Passo a passo

```bash
# Clone o repositório e entre na branch docker
git clone https://github.com/ErickMazur29/Gear-Hub.git
cd Gear-Hub
git checkout docker

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais (veja a seção "Variáveis de Ambiente" abaixo)

# Suba a aplicação e o banco PostgreSQL
docker compose up --build
```

Com os containers rodando, em outro terminal:

```bash
# Rode as migrations
docker compose exec gearhub_web python manage.py migrate

# Crie um superusuário
docker compose exec gearhub_web python manage.py createsuperuser
```

A aplicação estará disponível em `http://localhost:8000`.

**Comandos úteis:**

```bash
docker compose up -d              # Sobe em background
docker compose down               # Para os containers (mantém os dados do banco)
docker compose down -v            # Para os containers e apaga os dados do banco
docker compose logs -f            # Acompanha os logs em tempo real
docker compose exec gearhub_web bash  # Abre um shell dentro do container da aplicação
```

> Sair do shell do container ou fechar o terminal não derruba a aplicação — ela continua rodando em background. Só é necessário rodar `docker compose up --build` novamente se os containers forem parados/removidos (`docker compose down`).

---

### 🐍 Opção 2 — Manual (sem Docker)

#### Pré-requisitos

- Python 3.12+
- PostgreSQL
- Git

#### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/ErickMazur29/Gear-Hub.git
cd Gear-Hub

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais

# Rode as migrations
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz com as seguintes variáveis:

```env
SECRET_KEY=sua-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Usada pelo docker-compose.yml (via dj-database-url)
# Host = nome do serviço no Compose (gearhub_db), não localhost
DATABASE_URL=postgres://postgres:postgres@gearhub_db:5432/gearhub

```

> Rodando sem Docker (Opção 2), troque o host do `DATABASE_URL` para `localhost` (ou o host do seu PostgreSQL local).

---

## 🎨 Design System

| Token | Valor |
|---|---|
| Cor primária (navy) | `#0f1f3d` |
| Cor de borda | `#e5e7eb` |
| Border radius | `12px – 16px` |
| Fonte display | DM Serif Display |
| Fonte corpo | DM Sans |

---


## 📄 Licença

Este projeto é acadêmico e de uso livre para fins de estudo.

---

<p align="center">Desenvolvido por <strong>Erick Mazur</strong> · Portfólio Django</p>

<p align="center">Um projeto full-stack em django no desenvolvimento de um site c2c focado na area tech.</p>
