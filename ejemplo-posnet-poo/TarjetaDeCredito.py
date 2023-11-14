class TarjetaDeCredito:
    def __init__(self, entidad_bancaria, numero, titular):
        self.entidad_bancaria = entidad_bancaria
        self.numero = numero
        self.saldo = 0
        self.titular = titular

    def saldo_suficiente(self, monto):
        return self.saldo >= monto