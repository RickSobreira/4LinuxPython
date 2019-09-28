#calculadora
def soma (num1, num2):
    print(num1+num2)
    
def sub (num1, num2):
    print(num1-num2)
    
def mult(num1, num2):
    print(num1*num2)
    
def div(num1, num2):
    try:
        res = num1/num2
        print(num1/num2)
    except ZeroDivisionError as err:
            print("Não é possivel divisão por 0")
         
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

while True:
    
    try:
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o próximo valor: "))
        opcao = int(input("Digite a opção desejada: ")) 
    except ValueError as err2:
        print("Digite somente números!")
        break
    
if opcao == 1:
    soma(num1,num2)
elif opcao == 2:
    sub(num1,num2)
elif opcao == 3:
    mult(num1,num2)
elif opcao == 4:
    div(num1,num2)
                    
    







exit()
print("Escolha uma opção:\n1 - Banana\n2 - Melancia\n3 - Sair")
try:
    opcao = int(input(""))
except ValueError as err:
    print("Digite somente números!")
else:
    print(opcao)





def div(x,y):
    try:
        resultado = x/y
    except ZeroDivisionError as err:
            print("Não é possivel divisão por 0")
    else:
        return x/y

div(4,0)





try:
    with open("arquivoinexistente") as f:
        conteudo = f.read()
        
except FileNotFoundError as err:
    print("Arquivo não encontrado")
    #print(err)
    
else:
    
    print(conteudo)
    
    
