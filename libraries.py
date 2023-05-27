import json
import os
import urllib3
import threading
import re
from tqdm import tqdm

library_directory = 'C:\\Users\\titi\\AppData\\Roaming\\.minecraft\\libraries\\'

def download(url, paths, fileName, pbar):
    """
    Descarga un archivo desde una URL y lo guarda en la ubicación especificada.

    Parámetros:
        - url (str): URL del archivo a descargar.
        - paths (list): Lista de directorios en la ubicación donde se guardará el archivo.
        - fileName (str): Nombre del archivo.
        - pbar (tqdm.tqdm): Barra de progreso para el seguimiento de la descarga.
    """
    http = urllib3.PoolManager()
    with http.request('get', url, preload_content=False) as r:
        total_size = int(r.headers['Content-Length'])
        data = []
        for chunk in r.stream(1024):
            data.append(chunk)
            pbar.update(len(chunk))

    tmpPath = os.path.join(library_directory, *paths)
    os.makedirs(tmpPath, exist_ok=True)

    with open(os.path.join(tmpPath, fileName), 'wb') as file:
        for chunk in data:
            file.write(chunk)

def main(version):
    """
    Función principal que realiza la descarga de bibliotecas para una versión específica.

    Parámetros:
        - version (str): Versión del archivo manifest a utilizar.

    Retorna:
        - libstring (str): Cadena que representa las bibliotecas descargadas.
    """
    manifest = f"C:\\Users\\titi\\AppData\\Roaming\\.minecraft\\versions\\{version}\\{version}.json"

    try:
        os.makedirs(library_directory, exist_ok=True)
    except FileExistsError:
        pass

    with open(manifest, 'r') as file:
        libraries = file.read().replace("'", '"')

    libraries = json.loads(libraries)
    threads = []

    total_size = sum(int(library['downloads']['artifact']['size']) for library in libraries['libraries'])

    with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc='Downloading', ncols=80) as pbar:
        for library in libraries['libraries']:
            paths = library['downloads']['artifact']['path'].split("/")[:-1]
            url = library['downloads']['artifact']['url']
            fileName = library['downloads']['artifact']['path'].split("/")[-1]
            x = threading.Thread(target=download, args=(url, paths, fileName, pbar))
            threads.append(x)
            x.start()

        for thread in threads:
            thread.join()

    libstring = ";".join(os.path.join(library_directory, library['downloads']['artifact']['path']) for library in libraries['libraries'])
    libstring = re.sub(r'[\\/]+', r'\\\\', libstring)

    return libstring

# Ejemplo de uso:
version = "1.19.4"
result = main(version)

