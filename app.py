import streamlit as st
import pandas as pd

# Configura��o da p�gina
st.set_page_config(page_title="Sistema de Homologa��o de Fornecedores", page_icon="??")

# Fun��o para mostrar formul�rio de homologa��o
def form_homologacao():
    st.title("?? Sistema de Homologa��o de Fornecedores")
    st.subheader("Preencha os dados do fornecedor para homologa��o")

    with st.form(key='form_homologacao'):
        nome = st.text_input("Nome do Fornecedor")
        produto = st.text_input("Produto/Servi�o")
        contato = st.text_input("Contato")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        status = st.selectbox("Status", ["Pendente", "Aprovado", "Reprovado"])
        
        submit_button = st.form_submit_button(label='Enviar')

        if submit_button:
            st.success("Dados enviados com sucesso!")
            # C�digo para salvar os dados enviada
            
# Fun��o principal do app
def main():
    st.sidebar.title("?? Menu")
    menu = ["Formul�rio", "Lista de Fornecedores"]
    escolha = st.sidebar.selectbox("Selecione uma op��o", menu)

    if escolha == "Formul�rio":
        form_homologacao()
    elif escolha == "Lista de Fornecedores":
        st.subheader("?? Lista de Fornecedores Homologados")
        # Aqui voc� pode carregar uma tabela existente
        # Exemplo de tabela vazia
        df_fornecedores = pd.DataFrame(columns=["Nome", "Produto", "Contato", "Email", "Telefone", "Status"])
        st.dataframe(df_fornecedores)

if __name__ == '__main__':
    main()