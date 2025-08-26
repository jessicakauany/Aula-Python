"""
Repetições 
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo não tem fim
"""
contador = 0 

while contador < 10:
    contador = contador + 1 #  ou contador += 1
    print(contador)
    

print('Acabou')

#EX:02

senha_salva = '123456'
senha_digitada =''
repeticoes = 0


while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x):')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')