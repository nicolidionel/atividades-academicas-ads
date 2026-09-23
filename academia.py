import os

def exibir_nome_progama():
    os.system('cls')
    print(
        '##########################################\n'
        '                 Academia\n'
        ' Acesso liberado apenas a clientes ativos\n'
        '##########################################\n'
    )

def nome():
    nome = input('Digite o seu nome: ')
    return nome

def cadastro_ativo():
    cadastro = input('O cadastrado está ativo? ')
    if cadastro.lower() != 's' and cadastro.lower() != 'n':
        opcao_invalida()
    return cadastro.lower() == 's'

def mensalidade_paga():
    mensalidade = input('A mensalidade está paga? ')
    if mensalidade.lower() != 's' and mensalidade.lower() != 'n':
         opcao_invalida()
    return mensalidade.lower() == 's'

def opcao_invalida():
    print('Opção inválida.')
    input('Digite apenas s ou n.')

def main():
    exibir_nome_progama()

    nome_cliente = nome()
    ativo = cadastro_ativo()
    pago = mensalidade_paga()

    if ativo:
        if pago:
            print(nome_cliente)
            print('Acesso liberado.')
        else:
            print(nome_cliente)
            print('Mensalidade pendente.')
    else:
        print(nome_cliente)
        print('Cadastro inativo.')

if __name__ == '__main__':
    main()