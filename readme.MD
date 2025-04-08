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

