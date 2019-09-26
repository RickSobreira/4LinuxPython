import pymysql.cursors

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
        dic = {"nome_pessoa":"",
               "nac_pessoa":"",
               "idade_pessoa":""
        }
        
        dic["nome_pessoa"] = input("Digite o nome: ")
        dic["nac_pessoa"] = input("Digite a nacionalidade: ")
        dic["idade_pessoa"] = input("Digite a idade: ")
            
        with self.conexao.cursor() as cursor:
            SQL = "INSERT INTO pessoa(nome_pessoa, nac_pessoa, idade_pessoa) VALUES ('{}', '{}',{})".format(dic["nome_pessoa"],dic["nac_pessoa"], dic["idade_pessoa"])
                
            cursor.execute(SQL)
            self.conexao.commit()

    def consultaRegistro(self):
         with self.conexao.cursor() as cursor:
             SQL = "select * from pessoa"
             cursor.execute(SQL)
             for linha in cursor:
                 print("-------------------------")
                 print("ID :", linha ["id_pessoa"])
                 print("NOME: ", linha ["nome_pessoa"])
                 print("NACIONALIDADE: ", linha["nac_pessoa"])
                 print("IDADE: ", linha["idade_pessoa"])

    def atualizaRegistro(self):
        with self.conexao.cursor() as cursor:
            idade = input("Informe a Idade: ")
            id_pessoa = input("Informe o ID: ")
            SQL = "Update pessoa set idade_pessoa = {} where id_pessoa = {}".format(idade, id_pessoa)
            
            cursor.execute(SQL)
            self.conexao.commit()
            
    def removeRegistro(self):
        with self.conexao.cursor() as cursor:
            id_pessoa = input("Informe o ID: ")
            SQL = "Delete from pessoa WHERE id_pessoa = {}".format(id_pessoa)
            
            cursor.execute(SQL)
            self.conexao.commit()
        
        







