# pylint: disable-all
"""Archivo para seleccionar la versión a jugar."""
import requests
import json
import os
import urllib3
from config import MC_PATH

# Variable de prueba para distintas funcionalidades
http = urllib3.PoolManager()

# URL del archivo de manifiestos de todas las versiones del juego
MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"


def get_json(url):
    """
    Realiza una solicitud GET a la URL especificada y devuelve el contenido JSON como un diccionario.

    Args:
        url (str): La URL a la que realizar la solicitud.

    Returns:
        dict: El contenido JSON de la respuesta como un diccionario.
    """
    response = http.request("GET", url)
    return json.loads(response.data)


def download_file(url, path):
    """
    Descarga un archivo desde la URL especificada y lo guarda en la ubicación especificada.

    Args:
        url (str): La URL del archivo a descargar.
        path (str): La ruta de destino donde se guardará el archivo descargado.
    """
    response = http.request("GET", url)
    with open(path, "wb") as file:
        file.write(response.data)


def create_directory(path):
    """
    Crea un directorio en la ruta especificada.

    Args:
        path (str): La ruta del directorio a crear.
    """
    try:
        os.makedirs(path)
    except:
        pass


def save_json(data, path):
    """
    Guarda el contenido JSON en un archivo en la ruta especificada.

    Args:
        data (dict): El contenido JSON a guardar.
        path (str): La ruta del archivo donde se guardará el contenido JSON.
    """
    with open(path, "w") as file:
        file.write(json.dumps(data, indent=4))


def main():
    """
    Función principal que realiza el proceso de descarga y guardado de archivos de Minecraft.
    Permite al usuario ingresar la versión de Minecraft a descargar.
    """
    manifest = get_json(MANIFEST_URL)
    releases = {}

    # Coge todas las versiones de "release" del archivo de manifiestos
    for version in manifest["versions"]:
        if version["type"] == "release":
            releases[version["id"]] = version["url"]

    input_version = input("version: ")

    if input_version in releases:
        release_data = get_json(releases[input_version])
        launcher_url = release_data["downloads"]["client"]["url"]

        # Crea la carpeta de versiones y su versión
        create_directory(os.path.join(MC_PATH, "versions", input_version))

        # Guarda el archivo de manifiesto de la versión
        manifest_path = os.path.join(
            MC_PATH, "versions", input_version, input_version + ".json"
        )
        save_json(release_data, manifest_path)

        # Descarga el archivo launcher.jar
        launcher_path = os.path.join(
            MC_PATH, "versions", input_version, input_version + ".jar"
        )
        download_file(launcher_url, launcher_path)
    else:
        print("La versión ingresada no es una versión de lanzamiento.")


def get_minecraft_version(version="1.19.4"):
    """
    Descarga y guarda los archivos de la versión especificada de Minecraft.
    Utiliza la versión "1.19.4" por defecto si no se especifica ninguna.

    Args:
        version (str, optional): Versión de Minecraft a descargar. Defaults to "1.19.4".
    """
    manifest = get_json(MANIFEST_URL)
    releases = {}

    # Coge todas las versiones de "release" del archivo de manifiestos
    for v in manifest["versions"]:
        if v["type"] == "release":
            releases[v["id"]] = v["url"]

    if version in releases:
        release_data = get_json(releases[version])
        launcher_url = release_data["downloads"]["client"]["url"]

        # Crea la carpeta de versiones y su versión
        create_directory(os.path.join(MC_PATH, "versions", version))

        # Guarda el archivo de manifiesto de la versión
        manifest_path = os.path.join(MC_PATH, "versions", version, version + ".json")
        save_json(release_data, manifest_path)

        # Descarga el archivo launcher.jar
        launcher_path = os.path.join(MC_PATH, "versions", version, version + ".jar")
        download_file(launcher_url, launcher_path)
    else:
        print("La versión ingresada no es una versión de lanzamiento.")
