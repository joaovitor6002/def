#crie uma função que receba um numero correspondente a um percentual
#e aplique um desconto num produto de 4000 mil, a função deve exibir o 
#valor na tela

def aplicar_desconto(percentual):
    valor_produto = 4000
    desconto = (percentual / 100) * valor_produto
    valor_final = valor_produto - desconto
    print(f"O valor final do produto com {percentual}% de desconto é: R${valor_final}")

aplicar_desconto(22) 

#rene

def aplicar_desconto(valor):
    desconto = 4000 * (valor / 100)
    final = 4000 - desconto
    print(f'pra vc, meu amigo, fica so {final}')

    aplicar_desconto(2)
    