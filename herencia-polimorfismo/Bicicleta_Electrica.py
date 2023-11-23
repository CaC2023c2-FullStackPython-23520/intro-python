from Bicicleta import Bicicleta

class Bicicleta_Electrica(Bicicleta):

    def __init__(self, color, kms, marca, motor, bateria):
        Bicicleta.__init__(self, color, kms, marca)
        self.__motor = motor
        self.__bateria = bateria

    def cumple_requisitos(self):
        return self.motor == "SuperMotors"