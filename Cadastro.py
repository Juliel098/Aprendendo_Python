
participante1 = ['','','']
participante2 = [0,0,0]
participante3 = ['','','']
log = 0
while log <= 4:
    sytembusca1 = [participante1[0] , participante2[0] , participante3[0]]
    sytembusca2 = [participante1[1] , participante2[1] , participante3[1]]
    sytembusca3 = [participante1[2] , participante2[2] , participante3[2]]
    print ('iniciando o sistema de cadastro...')
    print ('')
    print ('1 - Cadastrar participantes ')
    print ('2 - Consultar participantes ')
    print ('3 - Efetuar pesquisa de participantes')
    print ('4 - Remover participante')
    print ('5 - Se desejar sair')
    log = int(input('Qual a seleção : '))
    if log == 1:
        nome1 = str(input('Nome do primeiro participante: ')) 
        idade1 = int(input('Idade de {ida} : '.format(ida = nome1)))
        nome2 = str(input('Nome do segundo participante: '))
        idade2 = int(input('Idade de {ida} : '.format(ida = nome2)))
        nome3 = str(input('Nome do terceiro participante: '))
        idade3 = int(input('Idade de {ida} : '.format(ida = nome3)))
        print ('Segue a lista dos participantes: ') 
        print ('Participante 1 > {} '.format(nome1))
        print ('Participante 2 > {} '.format(nome2))
        print ('Participante 3 > {} '.format(nome3))
        print ('')
        print ('Qual o numero do participante que vamos analisar os dados e concluir o cadastro ?')
        select1 = int(input('>>>'))
        if select1 == 1:
            print ('Valor informado > 1')
            print ('Participante : {}'.format(nome1))
            print ('Idade : {}'.format(idade1))
            endereco1 = str(input('Insira o endereço do participante : '))
            if endereco1 == '':
                print ('Nenhum valor foi informado no endereço ')
            else:
                participante1 = [nome1 , idade1 , endereco1]
                print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante1[0] , pa2 = participante1[1] , pa3 = participante1[2]))
            print ('Cadastro concluido...')

        elif select1 == 2:
            print ('Valor informado > 2')
            print ('Participante : {}'.format(nome2))
            print ('Idade : {}'.format(idade2))
            endereco2 = str(input('Insira o endereço do participante : '))
            if endereco2 == '':
                print ('Nenhum valor foi informado no endereço ')
            else:
                participante2 = [nome2 , idade2 , endereco2]
                print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante2[0] , pa2 = participante2[1] , pa3 = participante2[2]))
            print ('Cadastro concluido...')
        elif select1 == 3:
            print ('Valor informado > 3')
            print ('Participante : {}'.format(nome3))
            print ('Idade : {}'.format(idade3))
            endereco3 = str(input('Insira o endereço do participante : '))
            if endereco3 == '':
                print ('Nenhum valor foi informado no endereço ')
            else:
                participante3 = [nome3 , idade3 , endereco3]
                print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante3[0] , pa2 = participante3[1] , pa3 = participante3[2]))
            print ('Cadastro concluido...')
        else:
            print ('Valor informado não corresponde a nenhuma opção disponível')
        print ('Vamos efetuar mais algum cadastro ?')
        print ('1 - Sim \n2 - Não')
        log1 = int(input('>>> '))
        if log1 == 1 :
            print('Segue a lista de participantes cadastrados')
            print('Participante 1 : {nome1} \nIdade : {idade1} \nEndereço : {endereco1}'.format(nome1 = participante1[0] , idade1 = participante1[1] , endereco1 = participante1[2]))
            print('Participante 2 : {nome2} \nIdade : {idade2} \nEndereço : {endereco2}'.format(nome2 = participante2[0] , idade2 = participante2[1] , endereco2 = participante2[2]))
            print('Participante 3 : {nome3} \nIdade : {idade3} \nEndereço : {endereco3}'.format(nome3 = participante3[0] , idade3 = participante3[1] , endereco3 = participante3[2]))
            print('')
            print('Segue a lista de participantes disponíveis')
            print ('Participante 1 > {} '.format(nome1))
            print ('Participante 2 > {} '.format(nome2))
            print ('Participante 3 > {} '.format(nome3))
            print ('')
            print ('Qual o numero do participante que vamos analisar os dados e concluir o cadastro ?')
            select2 = int(input('>>>'))
            if select2 == 1:
                print ('Valor informado > 1')
                print ('Participante : {}'.format(nome1))
                print ('Idade : {}'.format(idade1))
                endereco1 = str(input('Insira o endereço do participante : '))
                if endereco1 == '':
                    print ('Nenhum valor foi informado no endereço ')
                else:
                    participante1 = [nome1 , idade1 , endereco1]
                    print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante1[0] , pa2 = participante1[1] , pa3 = participante1[2]))
                print ('Cadastro concluido...')

            elif select2 == 2:
                print ('Valor informado > 2')
                print ('Participante : {}'.format(nome2))
                print ('Idade : {}'.format(idade2))
                endereco2 = str(input('Insira o endereço do participante : '))
                if endereco2 == '':
                    print ('Nenhum valor foi informado no endereço ')
                else:
                    participante2 = [nome2 , idade2 , endereco2]
                    print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante2[0] , pa2 = participante2[1] , pa3 = participante2[2]))
                print ('Cadastro concluido...')
            elif select2 == 3:
                print ('Valor informado > 3')
                print ('Participante : {}'.format(nome3))
                print ('Idade : {}'.format(idade3))
                endereco3 = str(input('Insira o endereço do participante : '))
                if endereco3 == '':
                    print ('Nenhum valor foi informado no endereço ')
                else:
                    participante3 = [nome3 , idade3 , endereco3]
                    print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante3[0] , pa2 = participante3[1] , pa3 = participante3[2]))
                print ('Cadastro concluido...')
            else:
                print ('Valor informado não corresponde a nenhuma opção disponível')
        elif log1 == 2:
            print ('Finalizando sistema de cadastro...')
        else:
            print ('O valor informado está incorreto')

        print ('Vamos efetuar mais algum cadastro ?')
        print ('1 - Sim \n2 - Não')
        log1 = int(input('>>> '))
        if log1 == 1 :
            print('Segue a lista de participantes cadastrados')
            print('Participante 1 : {nome1} \nIdade : {idade1} \nEndereço : {endereco1}'.format(nome1 = participante1[0] , idade1 = participante1[1] , endereco1 = participante1[2]))
            print('Participante 2 : {nome2} \nIdade : {idade2} \nEndereço : {endereco2}'.format(nome2 = participante2[0] , idade2 = participante2[1] , endereco2 = participante2[2]))
            print('Participante 3 : {nome3} \nIdade : {idade3} \nEndereço : {endereco3}'.format(nome3 = participante3[0] , idade3 = participante3[1] , endereco3 = participante3[2]))
            print('')
            print('Segue a lista de participantes disponíveis')
            print ('Participante 1 > {} '.format(nome1))
            print ('Participante 2 > {} '.format(nome2))
            print ('Participante 3 > {} '.format(nome3))
            print ('')
            print ('Qual o numero do participante que vamos analisar os dados e concluir o cadastro ?')
            select2 = int(input('>>>'))
            if select2 == 1:
                print ('Valor informado > 1')
                print ('Participante : {}'.format(nome1))
                print ('Idade : {}'.format(idade1))
                endereco1 = str(input('Insira o endereço do participante : '))
                if endereco1 == '':
                    print ('Nenhum valor foi informado no endereço ')
                else:
                    participante1 = [nome1 , idade1 , endereco1]
                    print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante1[0] , pa2 = participante1[1] , pa3 = participante1[2]))
                print ('Cadastro concluido...')

            elif select2 == 2:
                print ('Valor informado > 2')
                print ('Participante : {}'.format(nome2))
                print ('Idade : {}'.format(idade2))
                endereco2 = str(input('Insira o endereço do participante : '))
                if endereco2 == '':
                    print ('Nenhum valor foi informado no endereço ')
                else:
                    participante2 = [nome2 , idade2 , endereco2]
                    print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante2[0] , pa2 = participante2[1] , pa3 = participante2[2]))
                print ('Cadastro concluido...')
            elif select2 == 3:
                print ('Valor informado > 3')
                print ('Participante : {}'.format(nome3))
                print ('Idade : {}'.format(idade3))
                endereco3 = str(input('Insira o endereço do participante : '))
                if endereco3 == '':
                    print ('Nenhum valor foi informado no endereço ')
                else:
                    participante3 = [nome3 , idade3 , endereco3]
                    print ('Nome : {pa1} \n Idade : {pa2} \n Endereço : {pa3}'.format(pa1 = participante3[0] , pa2 = participante3[1] , pa3 = participante3[2]))
                print ('Cadastro concluido...')
            else:
                print ('Valor informado não corresponde a nenhuma opção disponível')
        elif log1 == 2:
            print ('Finalizando sistema de cadastro...')
        else:
            print ('O valor informado está incorreto')
    elif log == 2:
        print ('Analisando banco de dados...')
        print ('Vamos iniciar...')
        print ('Segue a lista dos participantes cadastrados')
        print ('Participante 1 : {nome} \nIdade : {idade} \nEndereço : {endereco}'.format(nome = participante1[0] , idade = participante1[1] , endereco = participante1[2]))
        print ('Participante 2 : {nome} \nIdade : {idade} \nEndereço : {endereco}'.format(nome = participante2[0] , idade = participante2[1] , endereco = participante2[2]))
        print ('Participante 3 : {nome} \nIdade : {idade} \nEndereço : {endereco}'.format(nome = participante3[0] , idade = participante3[1] , endereco = participante3[2]))
    elif log == 3 :
        base = 0
        while base <= 3:
            print('Sistema de busca')
            print('')
            print('Defina o modelo de busca')
            print('1 - Nome')
            print('2 - Idade')
            print('3 - Cidade')
            print('4 - Sair')
            base = int(input('>>> '))
            if base == 1:
                print('Busca por nome')
                buscnome = str(input('Insira o nome para busca : '))
                if buscnome in sytembusca1:
                    print('O nome {} está cadastrado no nosso sistema'.format(buscnome))
                else:
                    print('O nome não se enconta no nosso sistema')
            elif base == 2:
                print('Busca por Idade')
                buscidade = int(input('Insira o idade para busca : '))
                if buscidade in sytembusca2:
                    print('Temos a idade {} cadastrada no nosso sistema'.format(buscidade))
                else:
                    print('A idade não se enconta no nosso sistema')
            elif base == 3:
                print('Busca por Cidade')
                busccidade = str(input('Insira o nome da cidade para busca : '))
                if busccidade in sytembusca3:
                    print('A cidade {} está cadastrado no nosso sistema'.format(busccidade))
                else:
                    print('A cidade não se enconta no nosso sistema')
            else:
                print('Valor informado está incorreto')
    elif log == 4:
        removpar = 0
        while removpar <= 2:
            print('Remover participantes')
            print('1 - Verificar os participantes cadastrados')
            print('2 - Remover os participantes')
            print('3 - Sair')
            removpar = int(input('>>> '))
            if removpar == 1:
                print('Verificar os participantes cadastrados')
                print ('Segue a lista dos participantes cadastrados')
                print ('Participante 1 : {nome} \nIdade : {idade} \nEndereço : {endereco}'.format(nome = participante1[0] , idade = participante1[1] , endereco = participante1[2]))
                print ('Participante 2 : {nome} \nIdade : {idade} \nEndereço : {endereco}'.format(nome = participante2[0] , idade = participante2[1] , endereco = participante2[2]))
                print ('Participante 3 : {nome} \nIdade : {idade} \nEndereço : {endereco}'.format(nome = participante3[0] , idade = participante3[1] , endereco = participante3[2]))
            elif removpar == 2:
                print('Remover participantes')
                removname = str(input('Insira o nome do participante que iremos remover : '))
                if removname in sytembusca1:
                    print('O nome informado consta na lista de cadastro')
                    sytembusca1.remove(removname)
                    print('O nome {} foi retirado do banco de dados'.formart(removname))
                else:
                    print('O nome informado não está registrado em nosso banco de dados')
                removidade = int(input('Insira a idade do participante que iremos remover : '))
                if removidade in sytembusca2:
                    print('A idade informada consta na lista de cadastro')
                    sytembusca2.remove(removidade)
                    print('A idade {} foi retirada do banco de dados'.formart(removidade))
                else:
                    print('A idade informada não está registrada em nosso banco de dados')
                removcidade = str(input('Insira a cidade do participante que iremos remover : '))
                if removcidade in sytembusca3:
                    print('A cidade informada consta na lista de cadastro')
                    sytembusca3.remove(removcidade)
                    print('A cidade {} foi retirada do banco de dados'.formart(removcidade))
                else:
                    print('O nome informado não está registrado em nosso banco de dados')              
            elif removpar == 3:
                print('Retornando ao menu inicial')
            else:
                print('Valor informado incorreto, retornando ao menu inicial')
    else:
        print ('Desligando sistema')