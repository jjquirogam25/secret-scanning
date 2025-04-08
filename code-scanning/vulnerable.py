import re

texto = "Este es un ejemplo de una vulnerabilidad presente en la siguiente expresión regular."

patron = r'^_(__|.)+_$'

vulnerabilidad = re.findall(patron,text)