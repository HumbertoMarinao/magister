import kagglehub
import pandas as pd
import os

# Descargar la última versión del dataset
path = kagglehub.dataset_download("redwankarimsony/heart-disease-data")

print("Path to dataset files:", path)

# Construir la ruta completa al archivo CSV
csv_file_path = os.path.join(path, 'heart_disease_uci.csv')

# Importar el dataset a un DataFrame de pandas
df = pd.read_csv(csv_file_path)

# Mostrar las primeras filas del DataFrame
display(df.head())

print("prueba GIT")