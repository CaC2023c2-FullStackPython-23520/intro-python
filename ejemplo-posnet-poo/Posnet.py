class Posnet:

    def efectuar_pago(self, tarjeta, monto, cant_cuotas):
        ticket = None
        if datos_validos(tarjeta, monto, cant_cuotas):
            monto_final = monto + monto * recargo_segun_cuotas(cant_cuotas)
            if tarjeta.saldo_suficiente(monto_final):
                # Seguir adelante con el pago
                """"""
        return ticket
    
    def datos_validos(self, tarjeta, monto, cant_cuotas):
        # pendiente

    def recargo_segun_cuotas(self, cant_cuotas):
        # pendiente
