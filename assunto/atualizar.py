arquivo = open('exemplo2.txt', 'a', encoding='utf-8')
texto = input('Digite um texto: ')
arquivo.write('\n' + texto)
arquivo.close()