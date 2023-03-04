import pandas as pd
import json
import os

class Lector:
    def __init__(self, path: str):
        self.path = path

    def _comprueba_extension(self, extension):
        file_extension = os.path.splitext(self.path)[1]
        if file_extension != extension:
            print("El archivo no tiene la extension correcta")

    def lee_archivo(self):
        pass

    @staticmethod
    def convierte_dict_a_csv(data: dict):
        df = pd.DataFrame(data)
        return df


class LectorCSV(Lector):
    def __init__(self, path: str):
        super.__init__(path)
        self.path = os.path.abspath('../data/vuelos_2.csv')

    def lee_archivo(self, datetime_columns=[]):
        return df = pd.read_csv(self.path)

class LectorJSON(Lector):
    def __init__(self, path: str):
        pass

    def lee_archivo(self):
        pass


class LectorTXT(Lector):
    def __init__(self, path: str):
        pass

    def lee_archivo(self):
        pass






