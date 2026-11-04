#sem pedir entrada de dados do usuario
def aplicar_desconto(percentual, valor_prod, nome):
    desconto = valor_prod * (percentual / 100)
    final = valor_prod - desconto
    print(f'pra vc, {nome}, fica só {final}')

aplicar_desconto(22, 4000, 'joao')

#pedindo entrada de dados do usuario
def aplicar_desconto(percentual, valor_prod, nome):
    desconto = valor_prod * (percentual / 100)
    final = valor_prod - desconto
    print(f'pra vc, {nome}, fica só {final}')

desconto = float(input('digite o valor do desconto:'))
valor = float(input('digite o valor do produto:'))
nome = input('digite seu nome:')
aplicar_desconto(desconto, valor, nome)