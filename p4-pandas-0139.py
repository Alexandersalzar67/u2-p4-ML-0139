import pandas as pd
import numpy as np
# Alexander Salazar nc = 0139
n_filas = 5
n_columnas = 5
tag_columna = tuple("ABCDE") # etiqueta para las columnas
print(tag_columna)
matriz=np.random.randint(1, 7, size=(n_filas, n_columnas))
print("genera matriz de filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es data DataFrame 
df = pd.DataFrame(matriz,columns=tag_columna)
print("-----La Tabla o dataframe-----nc = 0139")
print(df)
print("-----genera matriz nc = 0139")