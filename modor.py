#ler o arquivo sem alterar o conteudo

arquivo = open('diario.txt', 'a', encoding='utf-8')
data = input('Digite a data de hoje: ')
relato = input('Abra seu coração: ')

arquivo.write(data + ': ' + relato + '\n')
arquivo.close()

arquivo = open('diario.txt', 'r', encoding='utf-8')
#criar uma lista com as linhas de texto
texto = arquivo.readlines()
eu = 0
espa = 0
for linha in texto:
    if 'eu' in linha.lower():
        eu += 1
    espa += linha.count(' ')
arquivo.close()

tx_na = eu / espa
print(tx_na * 100)
