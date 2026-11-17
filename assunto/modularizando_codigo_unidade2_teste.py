odonto_dados = []
secretaria_dados = []
paciente_dados = []
usuario_odonto = []
usuario_secretaria = []
usuario_paciente = []
consultorios = []
consultas = []

esp = ['ortodontia', 'implantodontia', 'endodontia', 'clinica geral',
       'dentistica', 'odontopediatria', 'protese dentaria',
       'estomatologia', 'harmonizacao orofacial', 'bucomaxilo']

odonto_dados.append(['1', 'Ana Lima', '12345', 'ortodontia', True])
odonto_dados.append(['2', 'Bruno Alves', '23456', 'implantodontia', True])
odonto_dados.append(['3', 'Carla Souza', '34567', 'endodontia', True])
odonto_dados.append(['4', 'Diego Rocha', '45678', 'clinica geral', True])
odonto_dados.append(['5', 'Eva Santos', '56789', 'odontopediatria', True])

usuario_odonto.append(['Ana Lima', 'ana', '11111111111', '123456', '1', True])
usuario_odonto.append(['Bruno Alves', 'bruno', '22222222222', '123456', '2', True])
usuario_odonto.append(['Carla Souza', 'carla', '33333333333', '123456', '3', True])
usuario_odonto.append(['Diego Rocha', 'diego', '44444444444', '123456', '4', True])
usuario_odonto.append(['Eva Santos', 'eva', '55555555555', '123456', '5', True])

secretaria_dados.append(['Joao Vitor', 'joaovitor', '66666666666', '123456', '10001', '83999990001', True])
secretaria_dados.append(['Graziela', 'graziela', '77777777777', '123456', '10002', '83999990002', True])
usuario_secretaria.append(['Joao Vitor', 'joaovitor', '66666666666', '123456', '10001', True])
usuario_secretaria.append(['Graziela', 'graziela', '77777777777', '123456', '10002', True])

paciente_dados.append(['Joao Adulto', 'joao', '88888888888', '123456', '83988880001', '25', '', True])
paciente_dados.append(['Lia Crianca', 'lia', '99999999999', '123456', '83988880002', '8', '', True])
usuario_paciente.append(paciente_dados[0])
usuario_paciente.append(paciente_dados[1])

def menu_inicial():
    print('\nclinica odontologica do rene')
    print('1 - cadastro')
    print('2- login')
    print('3 - sair')
    escolha = input('qual opção deseja?: ')
    if escolha == '1':
        print('\n1- paciente')
        print('\n2- adm')
        adm_paci = input('qual sua opção?:')

        if adm_paci == '1':
            nome = input('digite seu nome: ')
            idade = input('digite sua idade: ')
            usuario = input('digite seu nome de usuario: ').lower()

            while True:
                cpf = input('digite seu cpf:')
                if len(cpf) != 11:
                    print('cpf invalido')
                else:
                    break

            senha = input('crie uma senha de 6 digitos: ')
            while len(senha) != 6:
                print('a senha digitada deve conter 6 digitos')
                senha = input('crie uma senha: ')

            telefone = input('digite seu numero de telefone: ')
            cadastro = [nome, usuario, cpf, senha, telefone, idade, '', True]
            paciente_dados.append(cadastro)
            usuario_paciente.append(cadastro)
            print('cadastrado com sucesso:)')

menu_inicial()