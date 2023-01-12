from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo del area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# Se modifica el mro, por la clase abstracta
print(Cuadrado.mro())