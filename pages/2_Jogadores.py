import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Jogadores - Dashboard",
    page_icon="🎮",
    layout="wide"
)

df_data = st.session_state["data"]
df_data2 = st.session_state["data2"]
team = df_data["Team"].value_counts().index
times = st.sidebar.selectbox("Times", team)
df_players = df_data[df_data["Team"] == times]

Players = df_players["Player"].value_counts().index
Players = st.sidebar.selectbox("Player", Players)
player_stats = df_data[df_data["Player"]==Players].iloc[0]
col1, col2 = st.columns([1, 8]) 
with col1:
    st.image(player_stats["Player_image"], width=100)
with col2:
    st.title(f"{player_stats['Player']}")

st.markdown(f"**Time:** {player_stats['Team']}")
st.markdown(f"**Lane:** {player_stats['Pos']}")

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.markdown(f"**Games:** {player_stats['GP']}")
col2.markdown(f"**KDA:** {player_stats['KDA']}")
col3.markdown(f"**XP@10:** {player_stats['XPD10']}")
col4.markdown(f"**Gold@10:** {player_stats['GD10']}")
col5.markdown(f"**CS@10:** {player_stats['CSD10']}")
col6.markdown(f"**CSPM:** {player_stats['CSPM']}")
st.divider()

def euclidean_distance(player1, player2):
    player1_stats = player1[5:28].apply(lambda x: float(x.strip('%')) if isinstance(x, str) and '%' in x else float(x))
    player2_stats = player2[5:28].apply(lambda x: float(x.strip('%')) if isinstance(x, str) and '%' in x else float(x))
    return np.linalg.norm(player1_stats - player2_stats)

# Filtrar jogadores com a mesma posição
players_same_position = df_data2[df_data2["Pos"] == player_stats["Pos"]]

distances = []
for index, row in players_same_position.iterrows():
    distance = euclidean_distance(player_stats, row)
    distances.append((row["Player"], distance))
distances.sort(key=lambda x: x[1])
st.title(f"Jogadores Semelhantes a {Players}")

# Criar um DataFrame para exibir os jogadores semelhantes em uma tabela
similar_players_df = pd.DataFrame(distances[:5], columns=["Jogador", "Distância Euclidiana"])

# Exibir a tabela no Streamlit
st.dataframe(similar_players_df)
st.sidebar.markdown("Desenvolvido por [Matzin](https://twitter.com/simplesmentmat)")