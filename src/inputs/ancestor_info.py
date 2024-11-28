import streamlit as st


def ancestor_inputs(degree):
    st.text(f"Informações do Grau {degree}")
    name = st.text_input(
        f"Nome completo (Grau {degree}):", key=f"ancestor_name_{degree}")
    date_birth = st.date_input(
        f"Data de nascimento (Grau {degree}):", key=f"ancestor_date_birth_{degree}")
    place_birth = st.text_input(
        f"Local de nascimento (Grau {degree}):", key=f"ancestor_place_birth_{degree}")

    data = {
        "role": f"ancestor_{degree}",
        "name": name,
        "date_birth": date_birth,
        "place_birth": place_birth
    }

    is_deceased = st.checkbox(
        "É falecido(a)?",
        key=f"deceased_ancestor_{degree}"
    )
    if is_deceased:
        date_death = st.date_input(
            f"Data de falecimento (Grau {degree}):", key=f"ancestor_date_death_{degree}")
        place_death = st.text_input(
            f"Local de falecimento (Grau {degree}):", key=f"ancestor_place_death_{degree}")

        data.update({
            "date_death": date_death,
            "place_death": place_death
        })

    is_married = st.checkbox(
        "Adicionar informações de conjuge?",
        key=f"married_ancestor_{degree}"
    )
    if is_married:
        spouse_name = st.text_input(
            "Nome completo do conjuge:", key=f"ancestor_spouse_name_{degree}")
        spouse_date_birth = st.date_input(
            "Data de nascimento:", key=f"ancestor_spouse_date_birth_{degree}")
        spouse_place_birth = st.text_input(
            "Local de nascimento:", key=f"ancestor_spouse_place_birth_{degree}")

        wedding_date = st.date_input(
            "Data de casamento:", key=f"ancestor_wedding_date_{degree}")
        wedding_place = st.text_input(
            "Local de casamento:", key=f"ancestor_wedding_place_{degree}")

        data.update({
            "wedding_date": wedding_date,
            "wedding_place": wedding_place,
            "spouse_name": spouse_name,
            "spouse_date_birth": spouse_date_birth,
            "spouse_place_birth": spouse_place_birth
        })

        spouse_is_deceased = st.checkbox(
            "É falecido?",
            key=f"deceased_ancestor_spouse_{degree}"
        )
        if spouse_is_deceased:
            spouse_date_death = st.date_input("Data de falecimento:")
            spouse_place_death = st.text_input("Local de falecimento:")

            data.update({
                "spouse_date_death": spouse_date_death,
                "spouse_place_death": spouse_place_death
            })

    return data
