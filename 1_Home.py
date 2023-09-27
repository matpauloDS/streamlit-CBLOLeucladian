import streamlit as st
import pandas as pd
import webbrowser
st.set_page_config(
    page_title="Home - Dashboard",
    page_icon="🎮",
    layout="wide"
)
if "data"  not in st.session_state:
    df_raw  = pd.read_csv("datasets/Dados.csv")
    df_raw['team_image'] = 'img/' + df_raw['Team'] + '.png'
    st.session_state["data"] = df_raw
    df_raw_cblol  = pd.read_csv("datasets/Dados2.csv")
    st.session_state["data2"] = df_raw_cblol
    df_raw['Player_image'] = 'img/' + df_raw['Player'] + '.png'

st.write("# Projeto - CBLoL Academy x CBLoL: Encontrando Semelhanças ")
st.sidebar.markdown("Desenvolvido por [Matzin](https://twitter.com/simplesmentmat)")
btn = st.button("Dados da Oracle Elixir")
if btn:
    webbrowser.open_new_tab("https://oracleselixir.com/")

st.markdown(
    """
    A Distância Euclidiana é uma medida matemática que quantifica a diferença entre dois pontos em um espaço multidimensional. Em nosso estudo comparativo entre o CBLoL Academy e o CBLoL, usamos essa ferramenta para avaliar quão semelhantes são os jogadores em termos de estatísticas. Quanto menor a distância, maior a similaridade. Isso nos ajuda a descobrir conexões surpreendentes e insights valiosos sobre o desempenho dos jogadores em ambos os campeonatos.    """
)