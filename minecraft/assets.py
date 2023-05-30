import json
import os
import threading
import urllib3
from tqdm import tqdm
from config.constants import OBJECTS_DIRECTORY, BASE_ASSETS_URL

MAX_CONCURRENT_DOWNLOADS = 10


def download(url, first_hash, hash, pbar):
    """
    Descarga un archivo desde una URL y lo guarda en la ubicación especificada.

    Parámetros:
        - url (str): URL del archivo a descargar.
        - first_hash (str): Primeros dos caracteres del hash del archivo.
        - hash (str): Hash del archivo.
        - pbar (tqdm.tqdm): Barra de progreso para el seguimiento de la descarga.
    """
    http = urllib3.PoolManager()
    with http.request('get', url, preload_content=False) as r:
        try:
            os.makedirs(os.path.join(OBJECTS_DIRECTORY, first_hash), exist_ok=True)
        except:
            pass
        try:
            with open(os.path.join(OBJECTS_DIRECTORY, first_hash, hash), 'wb') as file:
                for chunk in r.stream():
                    file.write(chunk)
                    pbar.update(len(chunk))
        except:
            pass


def download_assets(version):
    """
    Descarga los assets especificados en el archivo manifest.

    Parámetros:
        - version (str): Versión del archivo manifest a utilizar.

    Retorna:
        - assets_arr (list): Lista de URL de los assets descargados.
    """
    manifest = f"C:\\Users\\titi\\programacion\\MCL\\.minecraft\\versions\\{version}\\{version}.json"

    try:
        os.makedirs(OBJECTS_DIRECTORY, exist_ok=True)
    except FileExistsError:
        pass

    with open(manifest, 'r') as file:
        assets_data = json.load(file)

    assets_url = assets_data['assetIndex']['url']

    http = urllib3.PoolManager()

    with http.request('get', assets_url, preload_content=False) as r:
        assets = json.load(r)

    assets_arr = []
    total_size = len(assets['objects'])

    with tqdm(total=total_size,unit_scale=True, unit='asset', desc='Downloading assets', ncols=80) as pbar:
        threads = []

        for i, asset in enumerate(assets['objects']):
            hash = assets['objects'][asset]['hash']
            base_asset = BASE_ASSETS_URL + hash[:2] + '/' + hash
            assets_arr.append(base_asset)
            x = threading.Thread(target=download, args=(base_asset, hash[:2], hash, pbar))

            threads.append(x)
            x.start()

            # Limitar la cantidad de hilos concurrentes
            if i > 0 and i % MAX_CONCURRENT_DOWNLOADS == 0:
                for thread in threads:
                    thread.join()

                threads = []

        for thread in threads:
            thread.join()

    http.clear()
    
    return assets_arr
