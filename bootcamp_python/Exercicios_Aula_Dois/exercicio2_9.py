#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura_celsius = float(input('Digite a temperatura em graus celsius'))
conversao = (temperatura_celsius * (9/5)) + 32
print(f'{temperatura_celsius} graus celcius, representam {conversao} Fahrenheit')