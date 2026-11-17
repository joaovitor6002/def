#escopo local = global
#1 regra: escopo local é acessado dentro do local
#2 regra: variaveis declarados local nao existe no global
#3 regra: estrutura de dados modificadoas em escopo local se 

#global
time = 'gremio'

#local
def oi():
    cidade = 'cz'
    time = 'vasco'
    print(f'local: {time}')
    print(cidade)

oi()
print(cidade)
print(f'global: {time}')


#3 regra
alunos = ['matheus lucas', 'arthur sabino']
def mudar_ordens(lista):
    aux = lista [0]
    lista[0] = lista [1]
    lista[1] = aux

print(alunos)
mudar_ordens(alunos)
print(alunos)