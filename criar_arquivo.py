import datetime

class Registros:
    def criar():
        name = str(input('Defina o nome para o arquivo: '))
        registro1 = open(name+'.txt' , 'a')
        print('Arquivo criado, nome {}.txt'.format(name))
        registro1.close()
    def escrever():
        arquivo = str(input('Informe o nome do arquivo : '))
        registro1 = open(arquivo , 'a')
        print('Arquivo aberto')
        wri = str(input('Informe o que deseja escrever :'))
        registro1.write('\n'+ wri)
    def ler():
        arquivo = str(input('Informe o nome do arquivo : '))
        registro1 = open(arquivo , 'r')
        print('Arquivo aberto')
        registro1.read()
    

