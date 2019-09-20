# consulta em um arquivo
# Passo 1: Abrir o arquivo

with open("novo2.txt") as new:
    conteudo = new.readlines()
    
print(conteudo)

# Passo: Capturar o ID a ser procurado

id = input("Digite o ID para busca: ")

# Passo 3: Busca

for linha in conteudo:
    if id in linha:
        lista = linha.split(";")
        print("ID : {}".format(lista[0]))
        print("Nome : {}".format(lista[1]))
        print("Idade : {}".format(lista[2]))
        print("Sexo : {}".format(lista[3]))
        print("País : {}".format(lista[4]))
        
    
