import os

def exibir_nome_programa():
    os.system('cls')
    print('#############################################\n'
          '              Lista de compras\n'
          '         atualizar lista de compras\n'
          '#############################################\n')

lista = ['arroz', 'leite', 'pão']

def lista_produtos():
    print('Lista:', lista)

def opcoes_lista():
    opcao = input('\nVocê deseja adicionar ou remover um item da lista? ')

    if opcao.lower() == 'adicionar':
        item = input('\nDigite o nome do produto que deseja adicionar a lista: ')
        lista.append(item)

    if opcao.lower() == 'remover':
        item = input('\nDigite o nome do produto que deseja remover: ')

        if item in lista:
            lista.remove(item)

        else:
            print('Esse produto não está na lista.')

    if opcao.lower() != 'adicionar' and opcao.lower() != 'remover':
        print('Opção inválida.')

def main():
    exibir_nome_programa()
    lista_produtos()
    opcoes_lista()

    print('\nLista:', lista)


if __name__ == '__main__':
    main()