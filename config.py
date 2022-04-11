import json
import os

# Read Config Files


class configbackup:

    def __init__(self):
        self._config = {
            "root":{
                "path":os.getcwd()
            },
            "config":{
                "path":"\config",
                "files":["appConfig.json","googleAutho2.json"]
            },
            "section" : dict()
        }

        self.appConfig(self._config["root"]["path"]+self._config["config"]["path"])

    def appConfig(self, configTargets):

        if os.path.isdir(configTargets):
            with os.scandir(configTargets) as cf:
                for file in cf:
                    if file.name not in self._config["section"].keys():
                        with open(file.path) as configDATA:
                            self._config["section"][file.name]= json.load(configDATA)
        else:
            print("SORRY, PATH: ",end='')
            print(self._config["root_path"]+self._config["configFolder_Path"],end=", ")
            print("IS NOT VALID.")

    def printConfig(self):
        print(json.dumps(self._config, indent=4, sort_keys=False))