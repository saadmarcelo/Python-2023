# publicar um produto com comissão de 10% se for acima de R$20


valor = int(input('digite o valor do produto: '))


while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produro será de R${valor}')
    break