import os

#1 etapa -  ler o titulo

def exibir_nome_programa():
    os.system('cls')
    print('*************************************************\n'
          '            Calculadora de Frete\n'
          'Frete grátis apartir de R$150,00 em compras\n'
          '************************************************\n'
    )

#2 etapa - ler o valor e a região

def valor_regiao():
    valor_compra = float(input('Digite o valor total da compra: R$ '))
    regiao = input('Digite a região da entrega (local ou outra):')
    return valor_compra, regiao

#3 Etapa - calcular o frete

def calcular_frete(valor_compra, regiao):

    if valor_compra > 150:
        frete = 0;
        print('Você recebeu frete grátis!')

    else:
        if regiao == 'local':
            frete = 12

        else:
            frete = 25

    return frete

#5 Etapa - Mostrar os resultados

def mostrar_resultado(valor_produtos, frete):
    total = valor_produtos + frete

    print()
    print(f'Valor do frete: R$ {frete:.2f}')
    print(f'Total da compra: R$ {total:.2f}')


#Programa principal

def main():
    exibir_nome_programa()
    valor_compras, regiao = valor_regiao()
    frete = calcular_frete(valor_compras, regiao)
    mostrar_resultado(valor_compras, frete)

if __name__ == '__main__':
    main()