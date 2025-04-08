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
# Secrets Scanning
- Github integra una herramienta que escanea el código y encuentra los sitios dónde hay claves privadas expuestas, estas claves privadas pueden ser la contraseña de la base de datos, de una API, de una pasarela de pagos, entre otras.
- Como práctica general, no se recomienda tener estos archivos expuestos directamente en el código sino que se puede utilizar la herramienta de Github Secrets, archivos de entorno u otra alternativa.
- Para reproducir, en la carpeta secret-scanning, crea dos archivos.
- El primer archivo se llamará claves.py, tendrá el siguiente contenido.
```
DB_KEY = "pgsQL2024"
JWT_SECRET = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkZhbHNlIFVzZXIiLCJpYXQiOjE1MTYyMzkwMjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
db = mongodb+srv://jeanpaulsb:1041690395@pollingapp.yvnqz8y.mongodb.net/test
```
- El segundo archivo se llamará servidor.py y tendrá el siguiente contenido.
```
from claves import DB_KEY,JWT_SECRET

class Servidor:
    def __init__(self):
        self.url = "http://localhost"
        self.port = 8080
        self.db_key = DB_KEY
        self.jwt_secret = JWT_SECRET
    
    def run(self):
        print(f"El servidor está corriendo en la dirección {self.url}:{self.port}")

web_app = Servidor()
web_app.run()
```
- Para añadir los cambios, ejecuta los siguientes comandos `git add .`, luego `git commit -m "add env variables"` y finalmente `git push origin main`.

- Una vez se haya hecho el commit, Github te enviará un correo advirtiéndote el riesgo de tener las claves expuestas.

https://user-images.githubusercontent.com/20727908/209115498-a7b8e123-81c3-4ccc-aa99-edae3564c3da.png