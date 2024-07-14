#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, 
#em seguida, imprima o dia, o mês e o ano separadamente.

data = input('Digite uma data no formado dd/mm/aaaa')
valores = data.split('/')
print(f'O dia é {valores[0]} do mês {valores[1]} e ano {valores[-1]}')