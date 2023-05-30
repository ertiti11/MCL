import os

# Variables de directorio
MC_PATH = os.path.join(os.path.expanduser("~"), "programacion", "MCL", ".minecraft")
ASSETS = os.path.join(MC_PATH, "assets")
OBJECTS = os.path.join(ASSETS, "objects")
LIBRARY_DIRECTORY =os.path.join(MC_PATH, "libraries") 
MANIFEST_DIRECTORY =os.path.join(MC_PATH, "versions")

OBJECTS_DIRECTORY = os.path.join(MC_PATH, "assets","objects")
BASE_ASSETS_URL = "https://resources.download.minecraft.net/"