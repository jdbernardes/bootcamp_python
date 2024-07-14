#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
from math import pi
raio = float(input('Digite o raio do circulo: '))
area = pi*raio**2

print(f'A area de um circulo de raio {raio} é igual a: {area}')