

# criar uma funcao q soma varios numeros

def soma(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado

x = soma(2,3,4,5)
print(soma(2,5))
print(x)



def sub(n,*numeros):
    resultado = n
    for i in numeros:
        resultado -= i
    return resultado

print(sub(5,2))


def mult(n,*numeros):
    resultado = n
    for i in numeros:
        resultado *= i
    return resultado

print(mult(5,5))

def div(n,*numeros):
    resultado = n
    for i in numeros:
        resultado /= i
    return resultado

print(div(5,5))