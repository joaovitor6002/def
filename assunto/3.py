#4 tipos de funções 
#tipo 2: com parametros entrada, sem retorno

def descobrir_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    print(f'voce tem {idade} anos')

descobrir_idade(2006)

#--------------------------------------#

def descobrir_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    print(f'voce tem {idade} anos')

ano = int(input('digite o ano de nascimento: '))
descobrir_idade(ano)
