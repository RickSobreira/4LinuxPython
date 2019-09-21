# Criar class Onibus
#atributos:
#    ano:
#    modelo:
#    nlugares:
#    capacidade_atual:
        
#metodos:
#    validacao -- if nlugares
#    embarquepassegiro()
#    embarquepassageiro()


class Onibus:
    
    def __init__(self):
        self.cor = "" 
        self.modelo = "" 
        self.nlugares = 0 
        self.capacidade_atual = 0
            
    # comportamentos
           
#if assentos in nlugares <= 


#    def embarques(self):
#        self.capacidade_atual +=10
        
#    def desembarques(self):
#        self.capacidade_atual -=30
        
def main():

    #Objeto da classe

    mercedes = Onibus()
    mercedes.cor = "Azul"
    mercedes.modelo = "M2019"
    mercedes.lugares = 45
        
if __name__== " __main__":
    main()
