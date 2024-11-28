import streamlit as st


def user_inputs():
    st.text("Preencha as suas informações")
    name = st.text_input("Nome completo:")
    date_birth = st.date_input("Data de nascimento:")
    place_birth = st.text_input("Local de nascimento:")

    is_married = st.checkbox("Adicionar informações de conjuge?")
    if is_married:
        spouse_name = st.text_input("Nome completo do conjuge:")
        spouse_date_birth = st.date_input("Data de nascimento:")
        spouse_place_birth = st.text_input("Local de nascimento:")

        wedding_date = st.date_input("Data de casamento:")
        wedding_place = st.text_input("Local de casamento:")

        spouse_is_deceased = st.checkbox("É falecido?")
        if spouse_is_deceased:
            spouse_date_death = st.date_input("Data de falecimento:")
            spouse_place_death = st.text_input("Local de falecimento:")

    return {
        "name": name,
        "date_birth": date_birth,
        "place_birth": place_birth}
