# 🛒FlashFinds-web
Uma aplicação de loja online robusta, com arquitetura modular e desenvolvida seguindo as melhores práticas do ecossistema Django. O projeto conta com fluxo completo de carrinho, gerenciamento de pedidos, validações customizadas e otimização automatizada de média.

---

## 🚀 Principais Diferenciais Técnicos

* **Arquitetura Modular:** Divisão clara de responsabilidades em múltiplos apps (`produto`, `pedido`, `perfil`), facilitando a manutenção, escrita de testes e evolução do software.
* **Otimização de Imagens Automatizada:** Integração com a biblioteca *Pillow* no backend para redimensionar automaticamente imagens de produtos para um padrão otimizado de 800px, garantindo performance e economia de armazenamento.
* **Validação Robusta de Dados:** O app de perfil gerencia dados detalhados dos clientes com validações estritas de **CPF** e **CEP**, aplicando regras de negócio para evitar duplicidade e entradas inválidas.
* **Foco em SEO e UX:** Geração automatizada de *slugs* únicos para os produtos diretamente no modelo, garantindo URLs amigáveis sem risco de duplicação.

---

## 🛠️ Tecnologias e Ferramentas

* **Backend:** Python, Django 6
* **Processamento de Imagem:** Pillow
* **Frontend & Interface:** Bootstrap 4, Django Crispy Forms (Crispy Bootstrap 4)
* **Segurança:** Variáveis de ambiente para credenciais sensíveis (como `SECRET_KEY`) e Middlewares nativos do Django.

---

## 📦 Estrutura do Projeto e Funcionalidades

### 🔹 App Produto
* Gerenciamento completo de produtos e suas **variações** (tamanhos, cores, etc.).
* Suporte a lógica de preços dinâmicos (Preço Base vs. Preço Promocional).
* Upload de média com tratamento automático de tamanho.

### 🔹 App Perfil
* Cadastro avançado de utilizadores integrado ao sistema de autenticação (`django.contrib.auth`).
* Formulários estilizados com *Crispy Forms* e validação de documentos regulamentares.

### 🔹 App Pedido & Carrinho
* Fluxo completo de e-commerce: adição ao carrinho, checkout e fechamento de pedido.
* Histórico de itens comprados armazenado de forma consistente para auditoria.
* Gerenciamento de status do pedido: `Criado` ➡️ `Pendente` ➡️ `Aprovado` ➡️ `Enviado` ➡️ `Finalizado`.

### 🔹 Configuração Profissional e Interface
* Internacionalização nativa configurada para o português do Brasil (`pt-BR`).
* Estrutura de templates altamente reaproveitável (`base.html`, parciais e páginas específicas por app).
* Configuração rigorosa de diretórios de arquivos estáticos e de média (`MEDIA_ROOT`, `STATIC_ROOT`, `STATICFILES_DIRS`).

---

## ⚙️ Como Executar o Projeto

```bash
# Clonar o repositório

# Entrar na pasta do projeto
$ cd nome-do-repositorio

# Criar um ambiente virtual
$ python -m venv venv

# Ativar o ambiente virtual (Linux)
$ source venv/bin/activate

# Instalar as dependências
$ pip install -r requirements.txt

# Executar as migrações
$ python manage.py migrate

# Iniciar o servidor de desenvolvimento
$ python manage.py runserver
