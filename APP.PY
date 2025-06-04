import streamlit as st
import dados_animes as dados

st.title("animes")

nome = st.text_input('Nome do anime:')
genero = st.text_input('Genero do anime:')
nota = st.slider('Nota do anime', min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    dados.insere_dados(nome, genero, nota)
    st.success("anime cadastrado")

animes = dados.obter_dados()
st.header("Lista de animes")
st.table(animes)