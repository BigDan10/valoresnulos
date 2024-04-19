import pandas as pd
from pandas import Series, DataFrame

notas_credito = pd.read_excel("notas_credito.xlsx")

notas_credito.info()

notas_credito=notas_credito.fillna({'CVE_PEDI':'--','FECHA_CANCELA':'--','CVE_VEND':'--'})
notas_credito.isnull().sum()

print(notas_credito.isnull().sum())

#Convertir DataFrame a CSV
notas_credito.to_csv('notas_credito.csv')