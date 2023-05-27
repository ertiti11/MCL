import subprocess
from JVM import JVM
from config import ASSETS, MC_PATH

version = '1.19.4'
a = JVM(version)

command = ["java.exe",
           "-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump",
           "-Dos.name=Windows 10",
           "-Dos.version=10.0",
           "-Djava.library.path=" + str(a.natives_directory),
           "-Dminecraft.launcher.brand=" + str(a.launcher_name),
           "-Dminecraft.launcher.version="+ str(a.launcher_version),
           "-cp", a.classpath.replace("\\\\", "\\"),
           "net.minecraft.client.main.Main",
           "--username", "guest",
           "--version",
           version,
           "--gameDir",
           MC_PATH,
           "--assetsDir",
           ASSETS,
           "--assetIndex",
           "3",
           "--uuid",
           "{uuid}",
           "--accessToken",
           "{token}",
           "--clientId",
           "${clientid}",
           "--xuid",
           "${auth_xuid}",
           "--userType",
           "mojang",
           "--versionType",
           "release"



           ]


print("----------------------------------------------")
print(command)
print("----------------------------------------------")
subprocess.call(command)
