import os

def exibir_nome_progama():
    os.system('cls')
    print('#############################################\n'
          '       Orçamento de suporte técnico\n'
          '       Calculo de horas trabalhadas\n'
          '#############################################\n'
    )

def nome():
    nome_cliente = input('Nome do cliente: ')
    return nome_cliente

def horas():
    total_horas = int(input('Qual o total de horas: '))
    return total_horas

def main():
    exibir_nome_progama()
    nome_cliente = nome()
    total_horas = horas()

    if total_horas <= 0:
        print('Quantidade inválida')
    else:
        valor = 200 + 150 * (total_horas - 1)
        print(f'Cliente: {nome_cliente}')
        print(f'Orçamento: {valor}')

if __name__ == '__main__':
    main()
