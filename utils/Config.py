import json
import os

from utils.common import genMd5


class Config(object):
    @staticmethod
    def writeConfig(config):
        assert isinstance(config, dict)
        file = open('./config.json', 'w', encoding='utf-8')
        json.dump(config, file)
        file.flush()
        file.close()

    @staticmethod
    def readConfig():
        try:
            file = open('./config.json', 'r', encoding='utf-8')
            config = json.load(file)
            return config
        except:
            return {}

    @staticmethod
    def readJsons():
        files = []
        try:
            files = os.listdir('./history')
            files = list(filter(map(lambda f: f[0] != '~' and f[-4:] == 'json', files)))
            files.sort()
            files.reverse()
        except:
            os.mkdir('history')
        return files



