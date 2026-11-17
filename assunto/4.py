#4 tipos de funções
#tipo 3: com parametros entarda, com retorno

def calc_media(n1, n2, n3):
    final = n1 + n2 + n3
    return final
def calc_media2(n1, n2, n3):
    final = n1 + n2 + n3

calc_media(8, 13, 88)
print(calc_media)
calc_media2(8, 13, 88)
print(calc_media2)

#-------------------------------------#

def buscar(lista , nome):
    achei = False
    for aluno in lista:
        if nome in aluno:
            achei = True
            break
    return achei

alunos = [['matheus ' , 20],['maria' , 22],['joao' , 19],['tomaz' , 21]]
if buscar(alunos, 'joao'):
    print('eitcha, achou')
else:
    print('deu ruim, ta aq n')


#--------------------------------------#
#4 tipos de funções
#tipo 4: com parametros entarda, com retorno

def menu():
    print('MENU')
    print('1 - cadastrar')
    print('2 - listar')
    print('3 - buscar')
    op = int(input('Digite a opção:'))
    return op
