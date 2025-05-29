import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Olá Josir, aqui está meu gráfico!")

df = pd.read_csv('https://perfil-i.ibict.br/media/uploads/user_sum.csv')

if 'total' in df.columns and 'month' in df.columns:
    df = df.sort_values(by='total')

    categories = df['month']
    values = df['total']
    N = len(df)

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

    fig, ax = plt.subplots(figsize=(10,10), subplot_kw={'polar': True})

    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')

    colors = plt.cm.rainbow(np.linspace(0, 1, N))

    bars = ax.bar(angles, values, width=2*np.pi/N, bottom=10, color=colors, edgecolor='white')

    ax.set_xticks(angles)
    ax.set_xticklabels(categories, fontsize=12, color='white')

    ax.set_yticklabels([])

    ax.set_title("Circular bar plot do arco-íris!", y=1.08,
                 fontsize=18, color='white')

    ax.tick_params(axis='x', colors='white')

    plt.tight_layout()
    st.pyplot(fig)
else:
    st.warning("As colunas 'month' e 'total' não estão disponíveis.")


st.subtitle("Avaliação do gráfico")

opcao = st.radio("O gráfico foi criativo?", ('Sim', 'Não'))

if opcao == 'Sim':
    st.success("Uhuuuul! Obrigada professor!")
else:
    st.info("Poxa, tentei.... Da próxima vez faço um gráfico com as cores do América")
