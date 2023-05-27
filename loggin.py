import requests, json, os, urllib3

# variable de prueba para distinas funcionalidades


http = urllib3.PoolManager()
MC_PATH = "C:\\Users\\titi\\programacion\\MCL\\.minecraft\\"
# archivo de maniefiestos de todas las versiones del juego
manifest  = "C:\\Users\\titi\\programacion\\MCL\\.minecraft\\versions\\1.19.4\\1.19.4.json"

with open (manifest, 'r') as file:
    data = json.loads(file.read())
print(data["mainClass"])
data = data["logging"]["client"]["file"]["url"]

r = http.request('get', data)
logginFile = r.data

with open ("C:\\Users\\titi\\programacion\\MCL\\.minecraft\\versions\\1.19.4\\log4j2.xml", 'wb') as file:
    file.write(logginFile)
