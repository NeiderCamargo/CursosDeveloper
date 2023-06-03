#Se usa cuando ciertos metodos o propiedades sean inmutables
#se ocultan los datos de una clase para proteger los datos de accesos no autorizados

class cuentaBancaria :
    def __init__(self, saldo):
        self._saldo=saldo #el atributo se encapsula con _ al lado de la variable

    def depositar(self,monto):
        self._saldo+=monto#sumamos el monto al saldo

    def retirar(self, monto):
        if self._saldo >= monto:#si el monto es menor o igual al saldo
            self_saldo-=monto
        else:
            print("saldo insuficiente")
    
    def obtener_saldo(self):
        return self._saldo
