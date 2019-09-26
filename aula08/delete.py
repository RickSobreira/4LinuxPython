# delete

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
    print("*** ERRO AO TENTAR CONECTAR COM O MYSQL")
    print(err)
    
else:
    
    with conexao.cursor() as cursor:
        id_pessoa = input("Informe o ID: ")
        SQL = "Delete from pessoa WHERE id_pessoa = {}".format(id_pessoa)
        
        cursor.execute(SQL)
        conexao.commit()
        
finally:
    conexao.close()
