import streamlit as st
import pandas as pd

# Dados fornecidos
dados = {
    'ano': [2000, 2001, 2002, 2003],
    'vendas': [1000, 20000, 3000, 5000]
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Título da aplicação
st.title("Análise de Vendas por Ano")

# Mostrar dados
st.subheader("Tabela de Dados")
st.write(df)

# Estatísticas básicas
st.subheader("Estatísticas")
st.write(df.describe())

# Filtro por ano
st.subheader("Filtrar por Ano")
ano_selecionado = st.selectbox("Escolha um ano", df['ano'])
st.write(df[df['ano'] == ano_selecionado])

# Gráfico
st.subheader("Gráfico de Vendas")
st.line_chart(df.set_index('ano'))

# Métricas
st.subheader("Resumo")
st.metric("Total de Vendas", df['vendas'].sum())
st.metric("Média de Vendas", int(df['vendas'].mean()))