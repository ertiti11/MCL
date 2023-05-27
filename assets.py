# añadir barra de progreso de descarga
import json,  os, threading
import urllib3
from config import OBJECTS
# creamos el directorio de objetos
try:
    os.makedirs('.minecraft\\assets\\objects')
except:
    pass


# funcion que va a ser threading 
def download(link, firstHash, hash):
    http = urllib3.PoolManager()
    r = http.request('get', link)

    data = r.data
    
    try: 
        os.mkdir('.minecraft\\assets\\objects\\'+firstHash)  
    except FileExistsError:
        pass
    try:
        with open(OBJECTS+'\\'+ firstHash+'\\'+hash, 'wb') as file:
            file.write(data)
    except:
        print("error al guardar un archivo ASSET: \n" + data)
            
    


# base de url de donde descargamos los assets
baseAssetsUrl = "https://resources.download.minecraft.net/"
# ruta de manifiesto del juego
manifest  = "C:\\Users\\titi\\programacion\\MCL\\.minecraft\\versions\\1.19.4\\1.19.4.json"

# array de url de assets
assetsArr = []


with open(manifest, 'r') as f:
    assets = f.read()

assetsUrl = json.loads(assets)
assetsUrl = assetsUrl['assetIndex']['url']
print(assetsUrl)

http = urllib3.PoolManager()
r = http.request('get', assetsUrl)
assets = json.loads(r.data)




threads = list()

for asset in assets['objects']:
    hash = assets['objects'][asset]['hash']
    baseAsset = baseAssetsUrl+ hash[:2] + '/' + hash
    assetsArr.append(baseAsset)
    x = threading.Thread(target=download, args=(baseAsset,hash[:2],hash))
    threads.append(x)
    x.start()
   
    
    
    
    


