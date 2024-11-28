import streamlit as st

from cfg import kinship
from src.inputs.ancestor_info import ancestor_inputs
from src.inputs.dante_info import dante_inputs
from src.inputs.user_info import user_inputs

st.title("Progetto di cittadinanza")


if "form_page" not in st.session_state:
    st.session_state.form_page = 0


if "form_data" not in st.session_state:
    st.session_state.form_data = []

if "kinship_selected" not in st.session_state:
    st.session_state.kinship_selected = False


def save_current_page_data(data):
    """Armazena os dados do formulário atual na sessão."""
    if data:
        st.session_state.form_data.append(data)


def reset_form():
    st.session_state.form_page = 0
    st.session_state.kinship_selected = st.session_state.dante_kinship != "Selecione"
    if st.session_state.kinship_selected:
        st.session_state.total_pages = kinship[st.session_state.dante_kinship] + 1
    else:
        st.session_state.total_pages = 0


def next_page():
    if st.session_state.form_page < st.session_state.total_pages - 1:
        current_data = collect_data()
        save_current_page_data(current_data)
        st.session_state.form_page += 1


def previous_page():
    if st.session_state.form_page > 0:
        st.session_state.form_page -= 1


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

    def render_page():
        if st.session_state.form_page == 0:
            return dante_inputs()
        elif st.session_state.form_page == st.session_state.total_pages - 1:
            return user_inputs()
        else:
            degree = st.session_state.total_pages - st.session_state.form_page - 1
            return ancestor_inputs(degree)

    current_data = render_page()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("Voltar", on_click=previous_page,
                  disabled=st.session_state.form_page == 0)
    with col2:
        if st.session_state.form_page < st.session_state.total_pages - 1:
            if st.button("Próxima"):
                # Salva os dados ao mudar de página
                save_current_page_data(current_data)
                st.session_state.form_page += 1
        elif st.session_state.form_page == st.session_state.total_pages - 1:
            if st.button("Finalizar"):
                # Salva os dados da última página
                save_current_page_data(current_data)
                st.success(
                    "Formulário finalizado! Dados coletados com sucesso.")
                # Exibe os dados coletados
                st.write(st.session_state.form_data)
else:
    st.info("Por favor, selecione o grau de parentesco para continuar.")
