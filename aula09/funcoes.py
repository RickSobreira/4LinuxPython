class BancoDeDados:
    def __init__(self):
        
        self.host = "localhost"
        self.usuario = "root"
        self.senha = "4linux"
        self.banco = "4linux"
        self.charset = "utf8mb4"
        self.conexao = ""
        
    def iniciaConexao(self):
        self.conexao = pymysql.connect(
            host = self.host,
            user = self.usuario,
            password = self.senha,
            db = self.banco,
            charset = self.charset,
            cursorclass = pymysql.cursors.DictCursor)


def insereRegistro(self):
    dic = {"CPF":"",
           "NOME":"",
           "ENDEREÇO":""
           "TELEFONE":""
           "IDADE": "" 
    }
    
    dic["CPF"] = input("Digite o CPF: ")
    dic["NOME"] = input("Digite o nome: ")
    dic["ENDEREÇO"] = input("Digite a endereço: ")
    dic["TELEFONE"] = input("Digite o telefone: ")
    dic["IDADE"] = input("Digite a idade: ")
        
def consultaNome(self):
    dic["NOME"] = input("Digite o nome do usário: ")

def resetarTentativas(self):
    
    
        
        
        
