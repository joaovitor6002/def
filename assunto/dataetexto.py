
arquivo = open('diario.txt', 'a', encoding='utf-8')
data = input('Digite a data de hoje: ')
relato = input('Abra seu coração: ')

arquivo.write(data + ': ' + relato + '\n')
arquivo.close()