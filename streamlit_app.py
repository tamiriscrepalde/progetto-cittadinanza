import streamlit as st

st.title("Progetto di cittadinanza")

st.markdown(
    "<h3 style='font-size:20px; color:white; text-align:left;'>Preencha as informações abaixo para gerar sua árvore genealógica.</h3>",
    unsafe_allow_html=True
)
st.divider()


if "form_page" not in st.session_state:
    st.session_state.form_page = 0

if "total_pages" not in st.session_state:
    st.session_state.total_pages = 0


def next_page():
    st.session_state.form_page += 1


def previous_page():
    st.session_state.form_page -= 1


kinship = {
    "Selecione": 0,
    "Pai/Mãe": 1,
    "Avô/Avó": 2,
    "Bisavô/Bisavó": 3,
    "Triavô/Triavó": 4,
    "Tetravô/Tetravó": 5,
}

dante_kinship = st.selectbox(
    "Informe o grau de parentesco relativo ao seu Dante Causa:",
    list(kinship.keys())
)

if dante_kinship != "Selecione":
    st.session_state.kinship_selected = True
    st.session_state.total_pages = kinship[dante_kinship] + 1
else:
    st.session_state.kinship_selected = False

if st.session_state.kinship_selected:
    if st.session_state.form_page > 0:
        st.text(f"Page {st.session_state.form_page}")

        degree = st.session_state.total_pages - st.session_state.form_page + 1

        name = st.text_input(
            f"Nome completo (Grau {degree}):")
        date_birth = st.date_input(
            f"Data de nascimento (Grau {degree}):")
        place_birth = st.text_input(
            f"Local de nascimento (Grau {degree}):")

        is_deceased = st.checkbox("É falecido(a)?")
        if is_deceased:
            date_death = st.date_input(
                f"Data de falecimento (Grau {degree}):")
            place_death = st.text_input(
                f"Local de falecimento (Grau {degree}):")

        is_married = st.checkbox("Adicionar informações de conjuge?")
        if is_married:
            spouse_name = st.text_input("Nome completo do conjuge:")
            spouse_date_birth = st.date_input("Data de nascimento:")
            spouse_place_birth = st.text_input("Local de nascimento:")

            spouse_is_deceased = st.checkbox("É falecido?")
            if spouse_is_deceased:
                spouse_date_death = st.date_input("Data de falecimento:")
                spouse_place_death = st.text_input("Local de falecimento:")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Voltar") and st.session_state.form_page > 1:
                previous_page()
        with col2:
            if st.session_state.form_page < st.session_state.total_pages:
                if st.button("Próxima"):
                    next_page()
            elif st.session_state.form_page == st.session_state.total_pages:
                if st.button("Finalizar"):
                    st.success("Formulário enviado com sucesso!")
                    st.session_state.form_page = 0
else:
    st.info("Por favor, selecione o grau de parentesco para continuar.")
