import urllib3, json, re

manifest  = "C:\\Users\\titi\\AppData\\Roaming\\.minecraft\\versions\\1.19.4\\1.19.4.json"
MC_PATH = "C:\\Users\\titi\\AppData\\Roaming\\.minecraft\\"
LibraryPath = MC_PATH + '\\libraries\\'


class JVM:
    def __init__(self, version):
        
        self.natives_directory = MC_PATH + 'versions\\{}\\natives'.format(version)
        self.launcher_name = "MCL"
        self.launcher_version = "1.0"
        self.classpath = ""
        self.classpath_separator =";"
        self.OS_extra = ""

        with open (manifest, 'r') as file:
            args = json.loads(file.read())
            
        for library in range(len(args['libraries'])):
            library_path = LibraryPath + args['libraries'][library]['downloads']['artifact']['path']
            self.classpath += library_path.replace("\\", "\\\\")  # Reemplazar "\\" por "\\\\" en la ruta de la biblioteca

            if library < len(args['libraries']) - 1:
                self.classpath += self.classpath_separator
        self.classpath +=";C:\\Users\\titi\\AppData\\Roaming\\.minecraft\\versions\\1.19.4\\1.19.4.jar"

        self.classpath = re.sub(r'[\\/]+', r'\\\\', self.classpath)
    def __str__(self):
        res = "natives: " + self.natives_directory
        res  += "\n\nclasspath: "+ self.classpath
        res  +="\n\nLauncher Name: " + self.launcher_name
        res  +="\n\nLauncher Version: " + self.launcher_version
        res  +="\n\nOS extra: " + self.OS_extra
        return res
