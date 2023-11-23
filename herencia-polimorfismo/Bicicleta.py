class Bicicleta:

    def __init__(self, color, kms, marca):
        self.__color = color
        self.__kms = kms
        self.__marca = marca

    def cumple_requisitos(self):
        return self.kms < 300