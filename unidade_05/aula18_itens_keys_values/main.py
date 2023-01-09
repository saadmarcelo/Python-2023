# Dicionarios
    # Utiliza index no formato de keys e Values
    # Aceita string, integer, float, boolean


aluno = {'nome': 'ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True, 'materias': ['fisica', 'matematica', 'ingles']}

print(aluno)


aluno1 = {
    'nome': 'ana',
    'idade': 16,
    'nota_final': 'A',
    'aprovacao': True,
    'materias': ['fisica', 'matematica', 'ingles']
}

print(aluno1)

print(aluno1.get('materias'))
print(len(aluno))

print(aluno.items())
print(aluno.keys())
print(aluno.values())
