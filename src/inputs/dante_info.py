import streamlit as st


def dante_inputs():
    st.text("Informações do Dante Causa:")

    name = st.text_input("Nome completo:", key="dante_name")
    date_birth = st.date_input("Data de nascimento:", key="dante_date_birth")
    place_birth = st.text_input(
        "Local de nascimento:", key="dante_place_birth")

    data = {
        "role": "dante_causa",
        "name": name,
        "date_birth": date_birth,
        "place_birth": place_birth
    }

    is_deceased = st.checkbox(
        "É falecido(a)?",
        key="deceased_dante"
    )
    if is_deceased:
        date_death = st.date_input(
            f"Data de falecimento (Grau {degree}):", key="dante_date_death")
        place_death = st.text_input(
            f"Local de falecimento (Grau {degree}):", key="dante_place_death")

        data.update({
            "date_death": date_death,
            "place_death": place_death
        })

    is_married = st.checkbox(
        "Adicionar informações de conjuge?",
        key="married_dante"
    )
    if is_married:
        spouse_name = st.text_input(
            "Nome completo do conjuge:", key="dante_spouse_name")
        spouse_date_birth = st.date_input(
            "Data de nascimento:", key="dante_spouse_date_birth")
        spouse_place_birth = st.text_input(
            "Local de nascimento:", key="dante_spouse_place_birth")

        wedding_date = st.date_input(
            "Data de casamento:", key="dante_wedding_date")
        wedding_place = st.text_input(
            "Local de casamento:", key="dante_wedding_place")

        data.update({
            "wedding_date": wedding_date,
            "wedding_place": wedding_place,
            "spouse_name": spouse_name,
            "spouse_date_birth": spouse_date_birth,
            "spouse_place_birth": spouse_place_birth
        })

        spouse_is_deceased = st.checkbox(
            "É falecido?",
            key="deceased_dante_spouse"
        )
        if spouse_is_deceased:
            spouse_date_death = st.date_input(
                "Data de falecimento:", key="dante_spouse_date_death")
            spouse_place_death = st.text_input(
                "Local de falecimento:", key="dante_spouse_place_death")

            data.update({
                "spouse_date_death": spouse_date_death,
                "spouse_place_death": spouse_place_death
            })

    return data
