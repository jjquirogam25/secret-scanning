"""
La función eval en Python es extremadamente peligrosa porque el usuario puede
incluir aquí cualquier expresión de Python, pudiendo de esta manera tener acceso
a los archivos del sistema o servidor.
"""

entrada = eval(input("Ingresa un código malicioso: "))