import streamlit as st


def ancestor_inputs(degree):
    st.text(f"Informações do Grau {degree}")
    name = st.text_input(f"Nome completo (Grau {degree}):")
    date_birth = st.date_input(f"Data de nascimento (Grau {degree}):")
    place_birth = st.text_input(f"Local de nascimento (Grau {degree}):")

    is_deceased = st.checkbox("É falecido(a)?")
    if is_deceased:
        date_death = st.date_input(f"Data de falecimento (Grau {degree}):")
        place_death = st.text_input(f"Local de falecimento (Grau {degree}):")

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
        "place_birth": place_birth
    }
