import streamlit as st
import requests

url = "https://hp-api.onrender.com/api/characters"

resposta = requests.get(url)
dados = resposta.json()

nomes = []
for personagem in dados: 
    nomes.append(personagem['name'])
nomes.sort()

st.title("Personagens de Harry Potter 🪄")
with st.sidebar:
    st.header("Escolha um personagem")
    st.image("logo.png")
    nome_escolhido = st.selectbox('Selecione:', nomes)

personagem = None 
for p in dados: 
    if p['name'] == nome_escolhido:
        personagem = p
        break 

st.header(personagem['name'])


if personagem['image'] and personagem['image'] != "":
    st.image(personagem['image'], width=300)
else:
    st.write("📸 Este personagem nao possui imagem. ")
    st.divider()

st.write(f"**Casa:** {personagem['house']}")
st.write(f"**Especie:** {personagem['species']}")
st.write(f"**Genero:** {personagem['gender']}")
st.write(f"**Data de Nascimento:** {personagem['dateOfBirth']}")
st.write(f"**Ano de Nascimento:** {personagem['yearOfBirth']}")

st.write("**VArinha:**")
st.write(f"- Madeira: {personagem['wand']['wood']}")
st.write(f"- Nucleo: {personagem['wand']['core']}")
st.write(f"- Tamanho: {personagem['wand']['length']} polegadas")

st.write(f"**Patrono:** {personagem['patronus']}")
st.write(f"**Ator/Atriz:** {personagem['actor']}")

if personagem['alive']:
    st.write(f"**Esta Vivo?** Sim")
else:
    st.write(f"**Esta vivo?** Nao.")