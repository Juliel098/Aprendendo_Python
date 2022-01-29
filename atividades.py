homem = float(72.7)
mulher = float(62.1)
class atividade:
    def peso_ideal():
        print('-'*60)
        altura = float(input('Informe a sua altura: '))
        peso = (homem*altura)-58
        print('Peso ideal: {}'.format(peso))
        atividade.menu()

    def peso_sexo():
        print('-'*60)
        print('Informe seu sexo:')
        print('1 - Feminino')
        print('2 - Masculino')
        sexo = int(input(':'))
        if sexo == 1:
            print('-'*30,'FEMININO','-'*30)
            altura = float(input('Informe a sua altura: '))
            peso = (mulher*altura)-44.7
            print('Peso ideal: {}'.format(peso))
            atividade.menu()

        elif sexo == 2:
            print('-'*30,'MASCULINO','-'*30)
            altura = float(input('Informe a sua altura: '))
            peso = (homem*altura)-58
            print('Peso ideal: {}'.format(peso))
            atividade.menu()
            
        else:
            print('Valor informado está incorreto')
            atividade.menu()

    def loja():
        print('-'*60)
        area = float(input('Informe a área quadrada que será pintada: '))
        lata = int((area / 3)/18)
        valor = float(lata * 80.00)
        if lata < 1:
            print('Latas: 1')
            print('Valor: R$ 80,00')
            atividade.menu()
        elif lata >= 1:
            print('Latas: {}'.format(lata))
            print('Valor: R$ {}'.format(valor))
            atividade.menu()
        else:
            print('Algo está errado...')
            atividade.menu()

    def menu():
        print('-'*60)
        print('Informe o que deseja:')
        print('1 - Peso (Somente homem)')
        print('2 - Peso por sexo')
        print('3 - Loja de tintas (Compra de tinta / Metro)')
        print('4 - Sair')
        escolha = int(input(': '))
        if escolha == 1:
            atividade.peso_ideal()

        elif escolha == 2:
            atividade.peso_sexo()

        elif escolha == 3:
            atividade.loja()
        else:
            atividade.sair()
    def sair():
        import os
        s = os
        s.system('exit')

atividade.menu()