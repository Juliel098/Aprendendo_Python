dado1 = 0
dado2 = 0
dado3 = 0
nome1 = ''
nome2 = ''
nome3 = ''
print ('Vamos iniciar a aula dos conjuntos')
print ('Conseguimos efetuar algumas atividades com os conjuntos, tais como, união, interceção e separação')
dado1 = input('Informe um valor : ')
dado2 = input('Informe um valor : ')
dado3 = input('Informe um valor : ')
conjunto1 = {dado1 , dado2 , dado3}
print('Conjunto 1 : {}'.format(conjunto1))
nome1 = (input('Informe um valor : '))
nome2 = (input('Informe um valor : '))
nome3 = (input('Informe um valor : '))
conjunto2 = {nome1 , nome2 , nome3}
print('Conjunto 2 : {}'.format(conjunto2))
conjunto_uniao = conjunto1.union(conjunto2)
print('União : {}'.format(conjunto_uniao))
conjunto_intersecao = conjunto1.intersection(conjunto2)
print('Intersecção : {}'.format(conjunto_intersecao))
conjunto_diferenca = conjunto1.difference(conjunto2)
print('Diferença : {}'.format(conjunto_diferenca))
conjunto_subset = conjunto1.issubset(conjunto2)
print(conjunto_subset)
conjunto_supset = conjunto1.issuperset(conjunto2)
print(conjunto_supset)