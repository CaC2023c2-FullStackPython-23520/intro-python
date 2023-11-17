# import de la clase Ticket...

class Posnet:

    def efectuar_pago(self, tarjeta, monto, cant_cuotas):
        ticket = None
        if self.datos_validos(tarjeta, monto, cant_cuotas):
            monto_final = monto + monto * self.recargo_segun_cuotas(cant_cuotas)
            if tarjeta.saldo_suficiente(monto_final):
                tarjeta.descontar_saldo(monto)
                ticket = Ticket(tarjeta.nombre_completo_del_titular(), monto_final, monto_final / cant_cuotas)
        return ticket
    
    def datos_validos(self, tarjeta, monto, cant_cuotas):
        return monto > 0 and cant_cuotas >= 1 and cant_cuotas <= 6

    def recargo_segun_cuotas(self, cant_cuotas):
        return (cant_cuotas - 1) * 0.03
