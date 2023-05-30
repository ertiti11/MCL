from minecraft.manifest import get_minecraft_version
from minecraft.libraries import get_libraries
from minecraft.assets import download_assets
from minecraft.command import get_command
import subprocess
version = input("version: ")
get_minecraft_version(version)
get_libraries(version)
download_assets(version)
command = get_command(version)

subprocess.call(command)