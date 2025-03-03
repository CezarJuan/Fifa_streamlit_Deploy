import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

#importa dados selecionando valores filtrados
import streamlit as st
import pandas as pd

st.title("Upload do Arquivo de Dados")
uploaded_file = st.file_uploader("Carregue o arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df_data = pd.read_csv(uploaded_file)
    st.success("Arquivo carregado com sucesso!")


#Titulo da Home
st.markdown('# FIFA 2023 OFFICIAL DATASET')

#Botão de redirecionamento para o site da base de dados
btn = st.button("Acesse os Dados no Kaggle")

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

#Descrição dos dados
st.markdown('''
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e
    afiliações de clubes. 
    Com * mais de 17.000 registros *, este conjunto de dados oferece um recurso valioso para
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e
    desenvolvimento do jogador ao longo do tempo
            
            ''')