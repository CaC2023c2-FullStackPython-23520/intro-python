from Persona import Persona
from TarjetaDeCredito import TarjetaDeCredito

juan = Persona("3431123", "Juan", "Perez", "3423423432", "juan@fake.com")
tarjeta = TarjetaDeCredito("Banco Fake", "1324342342435", juan)

print(juan.nombre_completo())
print(tarjeta.titular.nombre_completo())
