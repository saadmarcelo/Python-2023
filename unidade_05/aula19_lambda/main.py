# Lambda function
    # É uma funcao pequena sem nome
    # Pode ter vairios argumentos mas somente 1 expressão
    # Muito utiulizada dentro de outras funcoes
    # codigo mais 'clean'



# def somar(x):
#     return x + 10


# print(somar(2))



somar10 = lambda x: x + 10
print(somar10(2))

somarxy10 = lambda x,y: x + y + 10
print(somarxy10(2,4))