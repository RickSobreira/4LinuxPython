# criar 3 classes:
# 1) classe pai
# 2) classe mãe
# 3) classe flha com herança múltipla

class Pai:
    
    def __init__(self):
        self.nome = "Antonio"
        self.nacionalidade = "Brasileira"
        
    def falarItaliano():
        return "Olá, tudo com você?"
        
class Mae:
    
    def __init__(self):
        self.nome = "Giovanna"
        self.nacionalidade = "Italiana"
        
    def falarItaliano():
        
    
class Filha (Pai, Mae):
    def __init__(self):
         self.nome = "Pamela"
         self.nacionalidade = "Brasileira"
    
    def main():
        pam = Filha() # criar um objeto da classe
        pam.falarItaliano
        
        
        
    
             



    
         
         

         
         
         
         
         
         
         
    
    
    
    
