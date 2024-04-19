import pandas as pd
from pandas import Series, DataFrame

devoluciones = pd.read_excel("devoluciones.xlsx")

devoluciones.info()

devoluciones=devoluciones.fillna({'DOC_ANT':'--', 'CVE_PEDI':'--', 'FECHA_CANCELA':'--','CVE_VEND':'--'})
devoluciones.isnull().sum()

print(devoluciones.isnull().sum())

#Convertir DataFrame a CSV
devoluciones.to_csv('devoluciones.csv')