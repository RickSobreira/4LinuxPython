# importar o módulo pymysql

import pymysql.cursors

try:
    conexao = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "4linux",
        db = "4linux",
        charset = "utf8mb4",
        cursorclass = pymysql.cursors.DictCursor)

except Exception as err:
    print("Não foi localizado o banco de dados!:")
    
else:
    with conexao.cursor() as cursor:
        SQL = "select * from pessoa"
        cursor.execute(SQL)
        for linha in cursor:
            print("-------------------------")
            print("ID :", linha ["id_pessoa"])
            print("NOME: ", linha ["nome_pessoa"])
            print("NACIONALIDADE: ", linha["nac_pessoa"])
            print("IDADE: ", linha["idade_pessoa"])
                      
finally:
    conexao.close()
        
    
            
            
        
        
        
        
