import pandas as pd
from pandas import Series, DataFrame

precios_productos = pd.read_excel("precios_productos.xlsx")

precios_productos.info()

precios_productos=precios_productos.fillna({'NOMBRE_VENDEDOR':'--'})

print(precios_productos.isnull().sum())

#Convertir DataFrame a CSV
precios_productos.to_csv('precios_productos.csv')