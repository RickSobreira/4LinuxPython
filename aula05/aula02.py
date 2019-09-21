#import aula01 # importa todo o pacote
from aula01 import Carro # importa somente o Carro

escort = Carro()
verona = Carro()

escort.cor = "azul"
escort.acelerar()
print(escort.velocidade)

verona.cor = "vermelho"
verona.acelerar()
print(verona.velocidade)



