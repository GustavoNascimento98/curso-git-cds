import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def create_dataframe_section(df):
    st.title("Database Section")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos por mês |
                        | company | Fabricanete da Motocicleta |
    """

    col_2.markdown(data_description)

    return None

def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")

    st.subheader("How many bikes are being sold are bikes from a unique owner?")

    st.subheader("Are high kilometer bikes more expensive than bikes with lower kilometer?")

    st.subheader("Are the bikes with a unique owner more expense on avarege than the other bikes?")

    st.subheader("Are the bikes that have more owners also the bikes with more kilometers traveled on avarege?")

    st.subheader("Which company has the most bikes registered?")

    st.subheader("Which company has the most expensive bikes on avarege?")

    st.subheader("Are the company that has the most expensive bikes registered also the company with the most bikes registered?")

    st.subheader("Which bikes are good for buying?")
    
    return None


def main():
    df_raw = load_data()

    create_dataframe_section(df_raw)
    
    st.dataframe(df_raw)

if __name__ == '__main__':
    main()

