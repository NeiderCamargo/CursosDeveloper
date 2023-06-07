# Definir la clase CuentaBancaria
class CuentaBancaria:
  # Constructor con los dos atributos privados
  def __init__(self, titular, saldo):
    self.__titular = titular
    self.__saldo = saldo

  # Método público para consultar el titular
  def get_titular(self):
    return self.__titular

  # Método público para consultar el saldo
  def get_saldo(self):
    return self.__saldo

  # Método público para ingresar una cantidad
  def ingresar(self, cantidad):
    # Validar que la cantidad sea positiva
    if cantidad > 0:
      # Llamar al método privado para modificar el saldo
      self.__modificar_saldo(cantidad)

  # Método público para retirar una cantidad
  def retirar(self, cantidad):
    # Validar que la cantidad sea positiva y no mayor que el saldo
    if cantidad > 0 and cantidad <= self.__saldo:
      # Llamar al método privado para modificar el saldo
      self.__modificar_saldo(-cantidad)

  # Método privado para modificar el saldo
  def __modificar_saldo(self, cambio):
    # Sumar el cambio al saldo actual
    self.__saldo += cambio

# Crear un objeto de la clase CuentaBancaria con datos de ejemplo
cuenta1 = CuentaBancaria("Pedro", 1000)

# Consultar el titular y el saldo de la cuenta
print(f"Titular: {cuenta1.get_titular()}")
print(f"Saldo: {cuenta1.get_saldo()}")

# Ingresar una cantidad a la cuenta
cuenta1.ingresar(500)
print(f"Saldo después de ingresar: {cuenta1.get_saldo()}")

# Retirar una cantidad de la cuenta
cuenta1.retirar(300)
print(f"Saldo después de retirar: {cuenta1.get_saldo()}")



    
