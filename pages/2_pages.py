import streamlit as st

#Cria variavel para ser usada em todas as páginas do Webapp
df_data = st.session_state['data']

#Cria filtro de clubes
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)
df_player = df_data[df_data['Club'] == club]

#Cria filtro de Jogadores
players = df_player['Name'].value_counts().index
player = st.sidebar.selectbox('Jogador', players)
player_stats = df_data[df_data['Name']== player].iloc[0]

#Seleciona foto do Jogador com base no nome
st.image(player_stats['Photo'])

#Seleciona nome do jogador
st.title(player_stats['Name'])

#Descrição geral do jogador(Clube, posição, Idade, Peso, Overall, etc)
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f" **Posição:** {player_stats['Position']}")


col1, col2, col3, col4 = st.columns(4)

col1.markdown(f" **Idade:** {player_stats['Age']}")
col2.markdown(f" **Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f" **Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()


st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)

col1 = st.metric(label= 'Valor de Mercado', value= f"£{player_stats['Value(£)']:,}")
col2 = st.metric(label= 'Remuneração semanal', value= f"£{player_stats['Wage(£)']:,}")
col3 = st.metric(label= 'Cláusula de recisão', value= f"£{player_stats['Release Clause(£)']:,}")