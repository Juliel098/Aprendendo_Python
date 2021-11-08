import os

class Arquivos:
    def acessar_cmd(self):
        print('-'*120)
        if self == '':
            name_ark = str(input('Informe o comando : '))
            s = os
            s.system(name_ark)
        else:
            s = os
            s.system(self)
        print('-'*120)

    def abrir_arquivo ():
        print('Informe o nome do arquivo:')

chama = Arquivos
valor = input('Informe o comando : ')
chama.acessar_cmd(valor)