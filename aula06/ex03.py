class CC:
    def __init__(self):
        agencia = "0001"
        conta = "22210"
        saldo = "1000"
        titular = "Ricardo Sobreira"
        
        def verificarSaldo(self):
            print(self.saldo)
        
        def saque(self,valor):
            self.saldo -= valor
            
        def deposito(self,valor):
            self.saldo +=valor
            
        def transferencia(self,valor,cc):
            self.saldo -=valor
            cc.saldo +=valor

            
            
            
            
            
        
    

