a = int(input('Primeiro bimestre'))
if a > 10:
    a = int(input('Voce digitou errado!!!'))
b = int(input('Segundo bimenstre'))
if b > 10:
    b = int(input('Voce digitou errado. Segundo bimestre!!!'))
c = int(input('Terceiro bimenstre'))
if c > 10:
    c = int(input('Voce digitou errado!!!'))
d = int(input('Quarto bimenstre')) 
if d > 10:
    d = int(input('Voce digitou errado!!!'))
media = (a + b + c + d) /4
print('media: {}' .format(media))

