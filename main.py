import requests
import json
while True:
 comandos = input("De quem você quer saber?")
 resposta = requests.get("https://api.github.com/users/{}".format(comandos))
 conteudo = resposta.json()
 print(json.dumps(conteudo, indent=2))
