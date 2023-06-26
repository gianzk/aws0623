# librerias
# ejecutar en terminal
# pip instal pandas 
# pip install sqlalchemy
# pip install mysql-connector-python
# pip install boto3
# print("esto es un comentario")
import urllib
import sqlalchemy as sq

import pandas as pd


import mysql.connector
engine = sq.create_engine("mysql+pymysql://admin:Admin2020*@localhost:3307/bdsample?charset=utf8mb4")


# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='Admin2020*',
    port=3307,
    database='bdsample'
)

# Crear un cursor para ejecutar las consultas
cursor = conexion.cursor()

# Obtener la lista de nombres de las tablas
consultaMapeo="select * from schema_mv1"
cursor.execute(consultaMapeo)
tablas = cursor.fetchall()

df=pd.read_sql("select * from schema_mv1",engine)
df.to_parquet("./parquets/demo1.parquet")

""" 
for row in tablas:
    consultaDeInfo=f"select * from {row[0]}"
    cursor.execute(consultaDeInfo)
    rows=cursor.fetchall()
    for rowI in rows:
        print(type(row))
        brea


 """