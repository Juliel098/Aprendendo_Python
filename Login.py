
bdusuario =[]
bdsenha =[]

if __name__ == '__main__':
    log = 0
    while log <= 2:
        print('')
        print('Bem vindo!!!')
        print('Iniciando o ERP')
        print('1 - Cadastrar usuário')
        print('2 - Efetuar login')
        print('3 - Sair')
        log = int(input('>>> '))
        if log == 1:
            user = input('Nome de Usuário : ')
            passw = input('Senha : ')
            bdusuario.append(user)
            bdsenha.append(passw)
        elif log == 2:
            print('Efetuar o login')
            print('Informe o nome de usuario :')
            user = input('Nome de Usuário : ')
            if user in bdusuario:
                passw = input('Senha : ')
                if passw in bdsenha:
                    while logg <= 2:
                        print('Menu ERP')
                        print('1 - Participantes')
                        print('2 - Armazenar registros')
                        logg = int(input('Selecione : '))
                        if logg == 1:
                            print('1 - Participante')
                            import Cadastro
                        elif logg == 2:
                            print('2 - Criar registros')
                            import criar_arquivo
                        else:
                            print('Valor incorreto')
                else:
                    print('Senha incorreta')
            else:
                print('Usuario incorreto')
        else:
            print('Desligando sistema')