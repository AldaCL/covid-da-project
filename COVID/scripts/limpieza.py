import pandas as pd
import numpy as np
import os
import csv

def load_data():
    print("Cargando datos")
    i = 0
    with open("../data/220720COVID19MEXICO.csv", "r") as file:
        data_reader = csv.reader(file)
        # Print metadata of first row
        metadata = next(data_reader)
        print(metadata)
        for row in data_reader:
            if(i%1000000 == 0):
                print(i, row)
            i += 1
        print(f"Total de registros: {i}")
        
    print("Datos cargados")

load_data()



