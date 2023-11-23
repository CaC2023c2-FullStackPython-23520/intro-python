from Bicicleta import Bicicleta
from Bicicleta_Electrica import Bicicleta_Electrica

una_bici = Bicicleta("Rojo", 450, "Acme")
otra_bici = Bicicleta_Electrica("Azul", 200, "Super", "2313", "superBat")

taller = [una_bici, otra_bici, bici1, bici2, bici3, bici4]

# El taller toma bicis para reparar dependiendo de:
# Si es bici comun, debe tener menos de 300km de uso
# Si es bici electrica, solo recibimos de la marca "SuperMotors"

for bici in taller:
    if bici es de tipo Bicicleta
        if bici.kms < 300:
            print(bici)
    else if bici es de tipo Bicicleta_Electrica:
        if bici.motor == "SuperMotors":
            print(bici)

for bici in taller:
    if bici.cumple_requisitos():
        print(bici)

