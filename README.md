# invoice-automation

## Sobre o projeto

Este projeto tem como objetivo automatizar o processamento de faturas (Invoices) em formato PDF. A aplicação realiza a leitura de múltiplos arquivos, extrai as informações relevantes, valida os dados utilizando Pydantic, armazena as informações em um arquivo JSON e disponibiliza consultas analíticas utilizando Pandas.

Os arquivos PDF utilizados foram obtidos do dataset público **Company Documents Dataset**, conforme especificado no enunciado do desafio.

---

## Funcionalidades

* Leitura automática de múltiplos arquivos PDF.
* Extração das seguintes informações:

  * Order ID
  * Order Date
  * Customer ID
  * Lista de produtos
  * Quantidade
  * Preço Unitário
* Validação dos dados utilizando Pydantic.
* Armazenamento dos dados em `database.json`.
* Verificação de duplicidade utilizando o Order ID.
* Consultas analíticas com Pandas:

  * Média do valor total das faturas.
  * Produto com maior frequência de compra.
  * Valor total gasto por cada produto.
  * Listagem de produtos contendo nome e preço unitário.

---

## Estrutura do projeto

```text
.
├── data/
│   ├── invoices/
│   └── database.json (gerado automaticamente)
│
├── models/
│   ├── invoice.py
│   └── item.py
│
├── services/
│   ├── analytics.py
│   ├── database.py
│   ├── invoice_parser.py
│   └── pdf_reader.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tecnologias utilizadas

* Python 3.13
* Pydantic
* Pandas
* pdfplumber

---

## Como executar

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Acesse a pasta do projeto

```bash
cd invoice-automation
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python main.py
```

---

## Resultado

Ao executar o projeto, a aplicação:

* Processa automaticamente todos os arquivos PDF presentes em `data/invoices`;
* Extrai e valida as informações de cada fatura;
* Gera automaticamente o arquivo `database.json`;
* Evita o armazenamento de faturas duplicadas;
* Exibe no terminal os resultados das consultas analíticas solicitadas no desafio.

---

## Arquitetura

O projeto foi estruturado utilizando Orientação a Objetos, separando as responsabilidades em diferentes classes:

* **PDFReader:** realiza a leitura dos arquivos PDF.
* **InvoiceParser:** converte o conteúdo extraído em objetos validados pelo Pydantic.
* **Database:** realiza o armazenamento dos dados e impede registros duplicados.
* **Analytics:** executa as consultas analíticas utilizando Pandas.

Essa separação permite que a etapa de ingestão de dados e a etapa de consultas possam evoluir de forma independente, facilitando a manutenção e a reutilização do código.

---

## Observações

* O arquivo `database.json` é gerado automaticamente durante a execução da aplicação e, por esse motivo, não faz parte do repositório.
* Os arquivos PDF utilizados para teste foram obtidos do dataset público **Company Documents Dataset**, conforme especificado no enunciado do desafio.

---

## Autora

Laura Miranda
