# Verifieds commits (commits firmados)
- En la carpeta de verified-commits, crea un archivo con nombre *main.py*
- Luego, añade al archivo la siguiente línea de código.
```
class MyCommit():
    def __init__(self):
        _content = ""
        _date = "none"

    def set_content(self,content):
        print(f"Commit set to: {content}")
        self._content = content

MyCommit().set_content("Mi primer commit")
```
- Para añadir el commit, ejecuta las siguientes líneas de código.
` git add .`, luego
` git commit -S -m "añadir clase commit"`
- En este caso, la S mayúscula indica que el commit se va a firmar.
- Cuando el commit se haya realizado, quedará algo como este.
- <code>añadir clase commit <br>
    Signed-off-by:jjquirogam25 jjquirogam@udistrital.edu.co
</code>
- Los commits firmados verifican la identidad del autor del commit mediante GPG o SSH.  
- El commit ahora aparece así.

![alt text](/verified-commits/image.png)
# Code-scanning
- Para este ejercicio, dirigee a la carpeta code-scanning.
- Crea un archivo con nombre `ejemplo.py`
- En el archivo, escribe el siguiente contenido.
```
import re
texto = "Este es un ejemplo de texto con una expresión regular."
patron = r'^_(__|.)+_$'
vulnerabilidad = re.findall(patron,texto)
```
- Luego, realiza el commit con los siguientes comandos.
- `git add .`, luego `git commit -S -m "add sample code"` y finalmente, `git push origin main`
- Github en el repositorio lanzará el code scanner, es una herramienta que responde a el evento de 'push' que acabamos de hacer y analiza el código de forma estática para evaluar vulnerabilidades.
- En el repositorio, se pueden apreciar los resultados del análisis.
![alt text](/code-scanning/image.png)