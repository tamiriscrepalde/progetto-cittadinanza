import streamlit as st

from cfg import kinship
from src.inputs.ancestor_info import ancestor_inputs
from src.inputs.dante_info import dante_inputs
from src.inputs.user_info import user_inputs

st.title("Progetto di cittadinanza")

# Inicializa as variáveis de estado da sessão
if "form_page" not in st.session_state:
    st.session_state.form_page = 0

if "kinship_selected" not in st.session_state:
    st.session_state.kinship_selected = False


# Funções para controle de navegação
def reset_form():
    st.session_state.form_page = 0
    st.session_state.kinship_selected = st.session_state.dante_kinship != "Selecione"
    if st.session_state.kinship_selected:
        # +2 para o Dante e o usuário
        st.session_state.total_pages = kinship[st.session_state.dante_kinship] + 2
    else:
        st.session_state.total_pages = 0


def next_page():
    if st.session_state.form_page < st.session_state.total_pages - 1:
        st.session_state.form_page += 1


def previous_page():
    if st.session_state.form_page > 0:
        st.session_state.form_page -= 1


# Menu suspenso com callback para redefinir o formulário
if 'dante_kinship' not in st.session_state:
    st.session_state.dante_kinship = 'Selecione'

st.selectbox(
    "Informe o grau de parentesco relativo ao seu Dante Causa:",
    options=list(kinship.keys()),
    key='dante_kinship',
    on_change=reset_form
)

if st.session_state.kinship_selected:
    st.text(
        f"Página {st.session_state.form_page + 1} de {st.session_state.total_pages}.")

    # Lógica para determinar qual formulário exibir
    if st.session_state.form_page == 0:
        # Primeira página: informações do Dante
        data = dante_inputs()
    elif st.session_state.form_page == st.session_state.total_pages - 1:
        # Última página: informações do usuário
        data = user_inputs()
    else:
        # Páginas intermediárias: informações dos ancestrais
        degree = st.session_state.total_pages - st.session_state.form_page - 1
        data = ancestor_inputs(degree)

    # Botões de navegação
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("Voltar", on_click=previous_page,
                  disabled=st.session_state.form_page == 0)
    with col2:
        if st.session_state.form_page < st.session_state.total_pages - 1:
            st.button("Próxima", on_click=next_page)
        elif st.session_state.form_page == st.session_state.total_pages - 1:
            st.button("Finalizar", on_click=next_page)
else:
    st.info("Por favor, selecione o grau de parentesco para continuar.")
