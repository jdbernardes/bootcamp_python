# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
#o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
#informando o valor do salário em comparação com o bônus recebido.

nome = input('Digite seu nome: ')
salario_mensal = float(input('Digite seu salario: '))
bonus_percent = float(input('Qual a porcentagem do seu bonus? '))
total_bonus = float(1000 + salario_mensal * bonus_percent) 

print(f'Olá {nome}, seu salario é de {salario_mensal} e seu bonus de {total_bonus}')