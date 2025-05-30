class CuentaBancaria:
    def __init__(self, titular, saldoInicial):
        self.__titular = titular  # Usando __ dos guiones hacemos privado el atributo
        self.__saldo = saldoInicial  # Usando __ dos guiones hacemos privado el atributo

    # Setter (editor/configurador) de saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de ${cantidad} exitoso")
        else:
            print("Error: no se puede depositar un saldo negativo.")
            
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} exitosamente.")
            print(f"Saldo restante: ${self.__saldo}")
        else:
            print("Error: no hay sufiente saldo disponible para realizar este retiro.")
            
    # Getter (obetener información privada a través de un método público)
    
    def get_saldo(self):
        return f"El saldo actual de la cuenta es ${self.__saldo}"


            