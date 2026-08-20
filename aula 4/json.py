import json

configuração = {
    "versao" : "1.0",
    "debug":False
}
with open("config.json", "w", encoding="UTF=8") as file:
    json.dump(configuração,file,indent=4)

with open("config.json", "r",encoding="UTF = 8")as file:
    configuração = json.load()
    