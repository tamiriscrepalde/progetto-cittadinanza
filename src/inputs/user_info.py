import streamlit as st


def user_inputs():
    st.text("Preencha as suas informações")
    name = st.text_input("Nome completo:", key="user_name")
    date_birth = st.date_input("Data de nascimento:", key="user_date_birth")
    place_birth = st.text_input("Local de nascimento:", key="user_place_birth")

    data = {
        "role": "user",
        "name": name,
        "date_birth": date_birth,
        "place_birth": place_birth
    }

    is_married = st.checkbox(
        "Adicionar informações de conjuge?",
        key="married_user"
    )
    if is_married:
        spouse_name = st.text_input(
            "Nome completo do conjuge:", key="user_spouse_name")
        spouse_date_birth = st.date_input(
            "Data de nascimento:", key="user_spouse_date_birth")
        spouse_place_birth = st.text_input(
            "Local de nascimento:", key="user_spouse_place_birth")

        wedding_date = st.date_input(
            "Data de casamento:", key="user_wedding_date")
        wedding_place = st.text_input(
            "Local de casamento:", key="user_wedding_place")

        data.update({
            "wedding_date": wedding_date,
            "wedding_place": wedding_place,
            "spouse_name": spouse_name,
            "spouse_date_birth": spouse_date_birth,
            "spouse_place_birth": spouse_place_birth
        })

        spouse_is_deceased = st.checkbox(
            "É falecido?",
            key="deceased_user_spouse"
        )
        if spouse_is_deceased:
            spouse_date_death = st.date_input(
                "Data de falecimento:", key="user_spouse_date_death")
            spouse_place_death = st.text_input(
                "Local de falecimento:", key="user_spouse_place_death")

            data.update({
                "spouse_date_death": spouse_date_death,
                "spouse_place_death": spouse_place_death
            })

    return data
