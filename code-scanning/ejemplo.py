import re

texto = "Este es un ejemplo de texto con una expresión regular."

patron = r'^_(__|.)+_$'

vulnerabilidad = re.findall(patron,texto)

