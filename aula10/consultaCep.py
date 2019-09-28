with open("ceps.txt") as ceps:
    listaCep = ceps.readlines()
    print(listaCep)

import requests , json

for item in listaCep:
        
    destino = "https://viacep.com.br/ws/" + item[0:8] + "/json/"
    resposta = requests.get(destino)
    
    if resposta.status_code == 200: # bem sucedida
        json = resposta.json()
        
        print("CEP:", json['cep'])
        print("Logradouro:", json['logradouro'])
        print("Bairro:", json['bairro'])
        print("Localidade:", json['localidade'])
        print("UF:", json['uf'])
        print("IBGE:", json['ibge'])
        print("GIA:", json['gia'])
        
    else:
        print("Erro desconhecido")
                
        
# http://viacep.com.br/ws/01001000/json/

    
