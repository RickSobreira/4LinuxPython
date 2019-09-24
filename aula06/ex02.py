from classCarro import Carro
import unittest

class TestaCarro (unittest.TestCase):
       
    def testeAcelerar(self):
        carro = Carro()
        carro.acelerar()
        self.assertEqual(10,carro.velocidade)
        
        
if __name__=="__main__":
    unittest.main()
    
        
        
