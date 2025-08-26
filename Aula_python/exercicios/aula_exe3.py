# PROGRAMA DE ÍMPAR E PAR
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int =  int(numero)
    numero_par = numero_int % 2 == 0

    if numero_par:   
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')

else: 
    print('Você não digitou um número inteiro')


# PROGRAMA DO HORÁRIO

nome = input('Digite seu nome: ')
entrada = input('Que horas são? ')

try :
    horas = int(entrada)

    if horas >= 0 and horas <= 11 :
        print(f'Bom Dia {nome}!')
    elif horas >= 12 and horas <= 17 :
        print(f'Boa Tarde {nome}!')
    elif horas >= 18 and horas <= 23 :
        print(f'Boa Noite {nome}!')
    else:
        print('Formato inválido')
except:
    print('Por Favor, digite apenas números')

# PROGRAMA DO TAMANHO DO NOME

nome = input('Qual é o seu nome? ')

if  len(nome) <= 4 :
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6 :
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')