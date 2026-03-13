import streamlit as st
import requests

st.set_page_config(page_title="Calculadora API", page_icon="🧮")

st.title("🧮 Dashboard Calculadora")
st.markdown("Interface interativa que utiliza uma API Flask.")

# Sidebar informando as configurações
st.sidebar.header("Configurações da API")
url_api = st.sidebar.text_input("URL da API", "http://127.0.0.1:5000/calcular")

# Layout de colunas para os números
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro Número", value=0.0)
with col2:
    num2 = st.number_input("Segundo Número", value=0.0)

# Escolha da operação
operacao = st.selectbox(
    "Escolha a Operação",
    ("soma", "subtracao", "multiplicacao", "divisao")
)

if st.button("Calcular Resultado", type="primary"):
    # Montando o JSON para API
    payload = {
        "num1": num1,
        "num2": num2,
        "operacao": operacao
    }
    
    try:
        response = requests.post(url_api, json=payload)
        
        if response.status_code == 200:
            res_json = response.json()
            st.success(f"### Resultado: {res_json['resultado']}")
            
            # Exibindo os dados
            with st.expander("Ver detalhes da resposta JSON"):
                st.json(res_json)
        else:
            st.error(f"Erro na API: {response.json().get('erro')}")
            
    except Exception as e:
        st.error(f"Não foi possível conectar na API. Verifique se ela está rodando! Erro: {e}")