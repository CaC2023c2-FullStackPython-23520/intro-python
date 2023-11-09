class JugadorDeFutbol:
    debe_usar_botines = True # Atributo de clase

    def __init__(self, nombre, apellido, edad, club):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.club = club

    def saludar(self):
        print(f"Hola soy {self.nombre_completo()}, tengo {self.edad} años y juego en el {self.club.nombre}. ¿Uso botines? {JugadorDeFutbol.debe_usar_botines}")
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}"

class Club:
    def __init__(self, nombre, color_camiseta):
        self.nombre = nombre
        self.color_camiseta = color_camiseta

inter_miami = Club("Inter de Miami", "Rosa")
benfica = Club("Benfica", "Rojo")
messi = JugadorDeFutbol("Lionel", "Messi", 36, inter_miami)
fideo = JugadorDeFutbol("Ángel", "Di María", 37, benfica)
otamendi = JugadorDeFutbol("Nicolás", "Otamendi", 35, benfica)

messi.saludar()
fideo.saludar()
otamendi.saludar()

benfica.nombre = "INTER DE PORTUGAL"

messi.saludar()
fideo.saludar()
otamendi.saludar()
#print(messi)
#print(fideo)