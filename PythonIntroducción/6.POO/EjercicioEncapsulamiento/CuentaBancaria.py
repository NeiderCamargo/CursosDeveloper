#Crea una clase CuentaBancaria que tenga un atributo privado saldo y dos métodos públicos: 
# depositar y retirar, que permitan modificar el saldo de la cuenta. 
# Además, crea un método público consultar_saldo que devuelva el saldo actual de la cuenta.#

class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo= saldo
    
    def saldo(self):
        return self._saldo
    
    def depositar(self, deposito):
        if deposito > 0:
            self.consultar_saldo(deposito)
    
    def retirar(self, retiro):
        if retiro <= self._saldo:
            self.consultar_saldo(-retiro)
        else:
            print("Su retiro es mayor al saldo")
    
    def consultar_saldo(self,cambio):
        self._saldo+=cambio

a1=CuentaBancaria(200)
print(f"Saldo: {a1.saldo()}")

a1.depositar(100)
print(f"saldo despues de depositar: {a1.saldo()}")

a1.retirar(300)
print(f"cuent bancaria luego de depositar: {a1.saldo()}")

