class CuentaBancaria:
    cuentas_bancarias = []
    def __init__(self, tasa_interes = 1 , balance = 0):
        self.tasa_interes = float(tasa_interes / 100)
        self.balance = balance
        CuentaBancaria.cuentas_bancarias.append(self)
    
    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        self.balance -= amount
        if(self.balance - amount < 0):
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def generar_interes(self):
        if(self.balance > 0):
            self.balance += self.balance * self.tasa_interes
        return self
    
    @classmethod 
    def imprimir_instancias(cls):
        for x in range (len(cls.cuentas_bancarias)):
            print(f"Balance: {str(cls.cuentas_bancarias[x].balance)}, Tasa de interés: {str(cls.cuentas_bancarias[x].tasa_interes * 100)}")

cuenta1 = CuentaBancaria(1, 500)
cuenta2 = CuentaBancaria(3, 200)

cuenta1.deposito(50).deposito(20).deposito(10).retiro(30).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(70).deposito(130).retiro(70).retiro(30).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_instancias()