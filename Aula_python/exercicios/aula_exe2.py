"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
    Digite seu nome:[nome]
    Digite sua idade: 20
    Seu nome é [nome]
    Seu nome invertido é [nome invertido]
    Seu nome não contém espaços
    Seu nome tem [letras] letras
    A primeira letra do seu nome é  
    A última letra do seu nome é  
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

 
    if " " in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]} ')
    print(f'A última letra do seu nome é {nome[-1]} ')
 
else:
   print('Desculpe, você deixou campos vazios.')


  