# Archivo de manifiesto de versión

en el archivo localizado en **/versions/1.19.4/1.19.4.json** encontraremos información
para poder ejecutar el juego, decarga de datos etc.

## Arguments

### GAME
+ **${auth_player_name}**: el nombre de usuario del jugador

+ **${version_name}**: el nombre de la versión (p. ej. 1.18.2)

+ **${game_directory}**: igual que JVM

+ **${assets_root}**: la carpeta raíz de los activos descargados, normalmente.minecraft/assets

+ **${assets_index_name}**: la versión del índice de activos a utilizar, normalmente la versión + secundaria (p. ej. 1.18, )

+ **${auth_uuid}**: el UUID de autenticación proporcionado por MSA

+ **${user_type}**: todo mojanghoy en dia

+ **${version_type}**: el tipo de versión, lanzamiento o instantánea (aunque esto puede mostrar cualquier cadena)

### JVM 

aqui tenemos:

+ **${natives_directory}**: el directorio de los nativos de la plataforma (que se mencionará más adelante)

+ **${launcher_name}**: el nombre del lanzador

+ **${launcher_version}**: la versión del lanzador

+ **${classpath}**: una lista de las rutas de todos los JAR de la biblioteca y el JAR principal descargado junto con :s

+ **${classpath_separator}**: :

+ **${primary_jar}**: la ruta al JAR principal

+ **${library_directory}**: la carpeta general en la que se descargaron las bibliotecas

+ **${game_directory}**: el "directorio de trabajo" mencionado antes


## AssetIndex

Las texturas, la música y los controles de la interfaz de usuario son activos y, por lo general, hay un índice de activos para cada versión secundaria. Este objeto tiene la siguiente definición de tipo:

```java 
interface AssetIndex {
  id: string;
  sha1: string;
  size: number;
  totalSize: number;
  url: string;
}
```

> donde "sha1" es el hash SHA-1 del archivo, "size" es el tamaño del archivo JSON, "totalSize" es el tamaño de todos los activos combinados y "url" es otro archivo JSON para obtener los activos.


## DOWNLOADS

Estos son los principales JAR a descargar
Esto incluye los JAR con los que realmente llamará java en el lanzamiento. Es un objeto que contiene descargas tanto para clientes como para servidores en formato { sha1: string; size: number; url: string; }. Nuevamente, se proporciona el hash SHA-1. El archivo en "url"se descarga en .minecraft/versions/<version>/<version>.jar. Para clientes, el archivo a descargar es ["downloads"]["client"]["url"].





- project_folder
  - config
    - __init__.py
    - constants.py
  - minecraft
    - __init__.py
    - assets.py
    - jvm.py
    - execute.py
  - main.py
