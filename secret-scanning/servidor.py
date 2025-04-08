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