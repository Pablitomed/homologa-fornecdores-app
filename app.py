import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Sistema de Homologação de Fornecedores", page_icon="??")

# Função para mostrar formulário de homologação
def form_homologacao():
    st.title("?? Sistema de Homologação de Fornecedores")
    st.subheader("Preencha os dados do fornecedor para homologação")

    with st.form(key='form_homologacao'):
        nome = st.text_input("Nome do Fornecedor")
        produto = st.text_input("Produto/Serviço")
        contato = st.text_input("Contato")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        status = st.selectbox("Status", ["Pendente", "Aprovado", "Reprovado"])
        
        submit_button = st.form_submit_button(label='Enviar')

        if submit_button:
            st.success("Dados enviados com sucesso!")
            # Código para salvar os dados enviada
            
# Função principal do app
def main():
    st.sidebar.title("?? Menu")
    menu = ["Formulário", "Lista de Fornecedores"]
    escolha = st.sidebar.selectbox("Selecione uma opção", menu)

    if escolha == "Formulário":
        form_homologacao()
    elif escolha == "Lista de Fornecedores":
        st.subheader("?? Lista de Fornecedores Homologados")
        # Aqui você pode carregar uma tabela existente
        # Exemplo de tabela vazia
        df_fornecedores = pd.DataFrame(columns=["Nome", "Produto", "Contato", "Email", "Telefone", "Status"])
        st.dataframe(df_fornecedores)

if __name__ == '__main__':
    main()