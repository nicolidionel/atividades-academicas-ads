import os

def exibir_nome_programa():
    os.system('cls')
    print(
        '#############################################################\n'
        '                Calculadora Papelaria \n'
        'Receba 10% de desconto nas suas compras acima de 100 reais\n'
        '#############################################################\n'
    )

#Etapa 1: Entrada dos dados
#Tipo dos dados: String, Float, Interger

def nome_produto():
    produto = input('Digite o nome do produto: ')
    return produto

def preco_unitario():
    preco = float(input('Digite o preço do produto: R$ '))
    return preco

def quantidade_produto():
    quantidade = int(input('Quantos produtos são: '))
    return quantidade

#Etapa 2: Processamento

def calcular_subtotal(preco, quantidade):
    return preco * quantidade


def calcular_desconto(subtotal):
    if subtotal >= 100:
        return subtotal * 0.10
    else:
        return 0

#Etapa 3: Saída

def calcular_total(subtotal, desconto):
    return subtotal - desconto

def main():
    exibir_nome_programa()

    # Entrada
    produto = nome_produto()
    preco = preco_unitario()
    quantidade = quantidade_produto()

    # Processamento
    subtotal = calcular_subtotal(preco, quantidade)
    desconto = calcular_desconto(subtotal)
    total = calcular_total(subtotal, desconto)

    # Saída
    print('\n---------------- RESULTADO ----------------')
    print(f'Produto: {produto}')
    print(f'Subtotal: R$ {subtotal:.2f}')
    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Total: R$ {total:.2f}')
    print('--------------------------------------------')
    
if __name__ == '__main__':
    main()