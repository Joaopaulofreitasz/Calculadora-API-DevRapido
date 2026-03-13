# Calculadora API com Interface Streamlit
Este projeto consiste em uma API desenvolvida em Flask que processa operações matemáticas básicas e um dashboard em Streamlit que serve como interface para o usuário. A comunicação entre as duas frentes é feita via requisições HTTP POST com payloads em formato JSON.

# Estrutura do Projeto
O sistema é dividido em duas partes independentes:

**api.py**: Servidor Flask que contém a lógica de cálculo e exposição dos endpoints.

**app_dashboard.py**: Interface visual que coleta os dados do usuário e consome a API.

# Tecnologias Utilizadas
**Python 3.x**
**Flask (Processamento de requisições)**
**Flask-CORS (Liberação de acessos entre portas diferentes)**
**Streamlit (Interface de usuário)**
**Requests (Consumo da API pelo front-end)**

# Configuração do Ambiente
Certifique-se de ter o Python instalado em sua máquina.
Instale as dependências necessárias utilizando o gerenciador de pacotes pip:

**Bash**
**pip install flask flask-cors streamlit requests**

# Execução
Para rodar o projeto completo, é necessário manter dois terminais abertos simultaneamente.

**1. Iniciar o Back-end**
No primeiro terminal, execute o servidor Flask:

Bash
python api.py
O servidor iniciará por padrão no endereço http://127.0.0.1:5000.

**2. Iniciar o Front-end**
No segundo terminal, execute o dashboard:

Bash
streamlit run app_dashboard.py
Endpoints da API
POST /calcular
Envia dados para processamento.

# Corpo da requisição (JSON):

JSON
{
  "num1": 10,
  "num2": 5,
  "operacao": "soma"
}
Operações aceitas: soma, subtracao, multiplicacao, divisao.

# Observações Técnicas:

A API foi configurada com CORS para permitir chamadas originadas de portas diferentes (comum em ambiente de desenvolvimento local onde o Streamlit roda na porta 8501 e o Flask na 5000). Caso mude a porta do servidor Flask, lembre-se de atualizar a URL no código do dashboard.