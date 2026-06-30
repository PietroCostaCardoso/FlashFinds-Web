# FlashFinds
![Autor](https://img.shields.io/badge/Autor-Pietro%20Costa%20Cardoso-blue?style=flat-square&logo=github)
![Licença](https://img.shields.io/badge/Licença-MIT-yellow.svg?style=flat-square)
![Status](https://img.shields.io/badge/Status-Original%20Repo-green?style=flat-square)

> **Aviso:** Este é o repositório original. Se você encontrar este código em outro perfil sem os devidos créditos, ele foi plagiado.
---
🌐 [Português](#português) | [English](#english)

## Português

# 🛒 E-Commerce Django

Uma aplicação de loja online robusta, com arquitetura modular e desenvolvida seguindo as melhores práticas do ecossistema Django. O projeto conta com fluxo completo de carrinho, gerenciamento de pedidos, validações customizadas e otimização automatizada de mídia.

---

### Principais Diferenciais Técnicos

* **Arquitetura Modular:** Divisão clara de responsabilidades em múltiplos apps (`produto`, `pedido`, `perfil`), facilitando a manutenção, escrita de testes e evolução do software.
* **Otimização de Imagens Automatizada:** Integração com a biblioteca *Pillow* no backend para redimensionar automaticamente imagens de produtos para um padrão otimizado de 800px, garantindo performance e economia de armazenamento.
* **Validação Robusta de Dados:** O app de perfil gerencia dados detalhados dos clientes com validações estritas de **CPF** e **CEP**, aplicando regras de negócio para evitar duplicidade e entradas inválidas.
* **Foco em SEO e UX:** Geração automatizada de *slugs* únicos para os produtos diretamente no modelo, garantindo URLs amigáveis sem risco de duplicação.

---

### Tecnologias e Ferramentas

* **Backend:** Python, Django 6
* **Processamento de Imagem:** Pillow
* **Frontend & Interface:** Bootstrap 4, Django Crispy Forms (Crispy Bootstrap 4)
* **Segurança:** Variáveis de ambiente para credenciais sensíveis (como `SECRET_KEY`) e Middlewares nativos do Django.

---

### Estrutura do Projeto e Funcionalidades

**🔹 App Produto**
* Gerenciamento completo de produtos e suas variações (tamanhos, cores, etc.).
* Suporte a lógica de preços dinâmicos (Preço Base vs. Preço Promocional).
* Upload de mídia com tratamento automático de tamanho.

**🔹 App Perfil**
* Cadastro avançado de utilizadores integrado ao sistema de autenticação (`django.contrib.auth`).
* Formulários estilizados com Crispy Forms e validação de documentos regulamentares.

**🔹 App Pedido & Carrinho**
* Fluxo completo de e-commerce: adição ao carrinho, checkout e fechamento de pedido.
* Histórico de itens comprados armazenado de forma consistente para auditoria.
* Gerenciamento de status do pedido: `Criado` ➡️ `Pendente` ➡️ `Aprovado` ➡️ `Enviado` ➡️ `Finalizado`.

**🔹 Configuração Profissional e Interface**
* Internacionalização nativa configurada para o português do Brasil (`pt-BR`).
* Estrutura de templates altamente reaproveitável (`base.html`, parciais e páginas específicas por app).
* Configuração rigorosa de diretórios de arquivos estáticos e de mídia (`MEDIA_ROOT`, `STATIC_ROOT`, `STATICFILES_DIRS`).

---
### ⚙️ Como Executar o Projeto

#### Pré-requisitos
* Python 3.10+
* Git
* (Opcional) PostgreSQL, se não for usar o SQLite padrão

#### Passo a passo
#### 1. Clonar o repositório
$ git clone 
$ cd nome-do-repositorio

#### 2. Criar e ativar o ambiente virtual
$ python -m venv venv
$ source venv/bin/activate        # Linux/macOS
$ venv\Scripts\activate           # Windows

#### 3. Instalar as dependências
$ pip install -r requirements.txt

#### 4. Configurar as variáveis de ambiente
$ cp .env.example .env
#### Edite o arquivo .env e preencha SECRET_KEY, DEBUG, etc.

#### 5. Executar as migrações do banco de dados
$ python manage.py migrate

#### 8. Iniciar o servidor de desenvolvimento
$ python manage.py runserver
\`\`\`

---

## English

# 🛒 Django E-Commerce

A robust online store application with modular architecture, built following Django ecosystem best practices. The project features a complete cart flow, order management, custom validations, and automated media optimization.

---

### Key Technical Highlights

* **Modular Architecture:** Clear separation of responsibilities across multiple apps (`produto`, `pedido`, `perfil`), making maintenance, test writing, and software evolution easier.
* **Automated Image Optimization:** Backend integration with the Pillow library to automatically resize product images to an optimized 800px standard, ensuring performance and storage savings.
* **Robust Data Validation:** The profile app manages detailed customer data with strict CPF (Brazilian taxpayer ID) and CEP (postal code) validations, applying business rules to prevent duplication and invalid entries.
* **SEO and UX Focus:** Automated generation of unique product slugs directly in the model, ensuring friendly URLs with no risk of duplication.

---

### Technologies and Tools

* **Backend:** Python, Django 6
* **Image Processing:** Pillow
* **Frontend & Interface:** Bootstrap 4, Django Crispy Forms (Crispy Bootstrap 4)
* **Security:** Environment variables for sensitive credentials (such as `SECRET_KEY`) and native Django middlewares.

---

### Project Structure and Features

**🔹 Produto App (Product)**
* Full management of products and their variations (sizes, colors, etc.).
* Support for dynamic pricing logic (Base Price vs. Promotional Price).
* Media upload with automatic size handling.

**🔹 Perfil App (Profile)**
* Advanced user registration integrated with the authentication system (`django.contrib.auth`).
* Forms styled with Crispy Forms and validation of regulatory documents.

**🔹 Pedido & Carrinho App (Order & Cart)**
* Complete e-commerce flow: adding to cart, checkout, and order completion.
* Purchase item history stored consistently for auditing.
* Order status management: `Created` ➡️ `Pending` ➡️ `Approved` ➡️ `Shipped` ➡️ `Completed`.

**🔹 Professional Configuration and Interface**
* Native internationalization configured for Brazilian Portuguese (`pt-BR`).
* Highly reusable template structure (`base.html`, partials, and app-specific pages).
* Strict configuration of static and media file directories (`MEDIA_ROOT`, `STATIC_ROOT`, `STATICFILES_DIRS`).

---

### ⚙️ How to Run the Project

#### Prerequisites
* Python 3.10+
* Git
* (Optional) PostgreSQL, if not using the default SQLite

#### Step by step
#### 1. Clone the repository
$ git clone 
$ cd repository-name

#### 2. Create and activate the virtual environment
$ python -m venv venv
$ source venv/bin/activate        # Linux/macOS
$ venv\Scripts\activate           # Windows

#### 3. Install dependencies
$ pip install -r requirements.txt

#### 4. Set up environment variables
$ cp .env.example .env
#### Edit the .env file and fill in SECRET_KEY, DEBUG, etc.

#### 5. Run database migrations
$ python manage.py migrate

#### 8. Start the development server
$ python manage.py runserver
\`\`\`
