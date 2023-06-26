import requests
import pandas as pd
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat

# https://apis.net.pe/api-tipo-cambio.html

# 1. conectarme al sitio
response = requests.get(url)

re=response.json() # nos brinda la información en formato JSON

print(re["compra"])

""" df=pd.DataFrame.from_dict(re) """
df=pd.DataFrame({'compra':[ 3.631], 'venta': [3.645], 'origen': ['SUNAT'], 'moneda': ['USD'], 'fecha': ['2023-06-17']})
""" print(df) """

columnas=list(re.keys())
valores=list(re.values())

print(columnas,valores)

schema={}
for i,j in enumerate(columnas):
    schema[j]=[valores[i]]

print(schema)

""" df.to_csv("api.csv")


"estructura de dictionary"
dict={
    "key":"value",
    "key2":"value2"
} """