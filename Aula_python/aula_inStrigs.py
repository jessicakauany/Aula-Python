# operadores in e not inStrings são iteráveis
#   0 1 2 3 4 5
#   O t á v i o
#  -6-5-4-3-2-1
nome = 'Otávio'

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
   print(f'{nome} tem a letra {encontrar}')
else:
   print(f'{nome} não tem a letra {encontrar}')
   
   
