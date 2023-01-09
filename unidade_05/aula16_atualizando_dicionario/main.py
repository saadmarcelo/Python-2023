# Dicionarios
    # Utiliza index no formato de keys e Values
    # Aceita string, integer, float, boolean


aluno = {'nome': 'ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

aluno['nome'] = "José"

print(aluno)

aluno.update({'nome': 'Marcelo', 'idade':40})

print(aluno)

print(aluno.get('endereco', 'Não existe'))

del(aluno['nota_final'])
print(aluno)