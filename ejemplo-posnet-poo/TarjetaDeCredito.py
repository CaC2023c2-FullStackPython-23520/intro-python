class TarjetaDeCredito:
    def __init__(self, entidad_bancaria, numero, titular):
        self.__entidad_bancaria = entidad_bancaria
        self.__numero = numero
        self.__saldo = 0
        self.__titular = titular

    def saldo_suficiente(self, monto):
        return self.__saldo >= monto
    
    def recargar_saldo(self, cuanto):
        self.__saldo += cuanto
    
    def descontar_saldo(self, cuanto):
        if cuanto > 0 and self.saldo_suficiente(cuanto):
            self.__saldo -= cuanto

    def nombre_completo_del_titular(self):
        return self.__titular.nombre_completo()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, nuevo_numero):
        if nuevo_numero > 0:
            self.__numero = nuevo_numero