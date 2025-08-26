nome = 'Jéssica Kauany'
altura = 1.60
peso = 70 
imc = peso / (altura ** 2)

# simples
print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)

# f_strings
print(f'{nome} tem {altura} de altura,\npesa {peso} quilos e seu IMC é \n{imc:.2f}')
