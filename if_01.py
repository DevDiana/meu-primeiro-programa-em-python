nota = float( input('Informe a nota do aluno: '))

if nota >= 9:
    print('Duas palavras: para bens" :P')
    print('Quadro de honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
else:
    print('Reprovado')
print(nota)