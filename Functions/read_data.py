# en esta parte voy a importar los datos  y los  voy combertir en dataframes.
import pandas as pd
import numpy as np

datos = pd.read_csv('Files\DDS08.csv')

df = pd.DataFrame(datos)
print(df)