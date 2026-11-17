from pathlib import Path

import pandas as pd
import streamlit as st

ARQUIVO_CSV = Path(__file__).with_name("gastos.csv")

st.title("Meus gastos")
st.write("Registre seus gastos e acompanhe o total por categoria.")

if "gastos" not in st.session_state:
    if ARQUIVO_CSV.exists():
        gastos_salvos = pd.read_csv(ARQUIVO_CSV)
        gastos_salvos["Data"] = pd.to_datetime(gastos_salvos["Data"]).dt.date
        st.session_state.gastos = gastos_salvos.to_dict("records")
    else:
        st.session_state.gastos = []

with st.form("formulario_gasto"):
    categoria = st.text_input("Categoria", placeholder="Ex.: Alimentação")
    valor = st.number_input("Valor (R$)", min_value=0.01, step=0.01)
    data = st.date_input("Data")
    adicionar = st.form_submit_button("Adicionar gasto")

if adicionar:
    categoria = categoria.strip()
    if categoria:
        st.session_state.gastos.append(
            {"Categoria": categoria, "Valor": valor, "Data": data}
        )
        pd.DataFrame(st.session_state.gastos).to_csv(ARQUIVO_CSV, index=False)
        st.success("Gasto adicionado!")
    else:
        st.error("Digite uma categoria para adicionar o gasto.")

if st.session_state.gastos:
    if st.button("Limpar tudo"):
        st.session_state.gastos.clear()
        pd.DataFrame(
            columns=["Categoria", "Valor", "Data"]
        ).to_csv(ARQUIVO_CSV, index=False)
        st.rerun()

    gastos_df = pd.DataFrame(st.session_state.gastos)

    st.subheader("Lista de gastos")
    st.dataframe(gastos_df, width="stretch")

    total = gastos_df["Valor"].sum()
    st.metric("Total gasto", f"R$ {total:.2f}")

    st.subheader("Gastos por categoria")
    gastos_por_categoria = (
        gastos_df.groupby("Categoria", as_index=False)["Valor"].sum()
    )
    st.bar_chart(
        gastos_por_categoria,
        x="Categoria",
        y="Valor",
        color="Categoria",
    )
else:
    st.info("Seus gastos aparecerão aqui depois que você adicionar o primeiro.")
