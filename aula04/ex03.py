#with open("novo2.txt") as new:
#    conteudo = new.read()


with open("novo2.txt") as new:
    dic = {"ID": "", "Nome": "","Idade": "","Sexo": "","País" ""}    
    conteudo = new.read() + "\n"
    
    dic["ID"] = input("Digite o código ID: ")
    dic["Nome"] = input("Digite o nome do cliente: ")
    dic["Idade"] = input("Digite a idade: ")
    dic["Sexo"] = input("Digite o sexo do cliente: ")
    dic["País"] = input("Digite a nacionalidade do cliente: ")
    
    for item in dic.values():
        conteudo += item + ";"
        


    
