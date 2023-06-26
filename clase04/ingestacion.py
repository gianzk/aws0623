"""
    bd local o remota => mapeamos tablas 
"""
import sqlalchemy as sq
import mysql.connector
import pandas as pd

def getbdInit():
    engineLocal = sq.create_engine("mysql+pymysql://admin:Admin2020*@localhost:3307/bdsample?charset=utf8mb4")
    return engineLocal


def getbdInitAws():
    engineAWS = sq.create_engine("mysql+pymysql://adminDemov1:Basedatos2023.@db-demo-v1.c6efsfp6ae0y.us-east-1.rds.amazonaws.com:3306/dbDemov1?charset=utf8mb4")
    connect=engineAWS.connect()
    return connect




def getAwsbd():
    region = 'us-east-1'

    # Configurar los parámetros de conexión a la base de datos RDS
    db_endpoint = 'db-demo-v1.c6efsfp6ae0y.us-east-1.rds.amazonaws.com'
    db_name = 'dbDemov1'
    db_user = 'adminDemov1'
    db_password = 'Basedatos2023.'

    # Crear una nueva conexión a la base de datos
    try:
        conn = mysql.connector.connect(
            host=db_endpoint,
            port=3306,
            database=db_name,
            user=db_user,
            password=db_password
        )
        print('Conexión exitosa a la base de datos')

        # Aquí puedes ejecutar consultas o realizar operaciones en la base de datos
        # ...
        return conn
    except Exception as e:
        print('Error al conectar a la base de datos:', e)
        return 0
    
conAws=getAwsbd()
conAwsv2=getbdInitAws()
conbd=getbdInit()

mapeodetablas="select * from schema_mv1"


with conbd.connect() as connection:
    rows=connection.execute(sq.text(mapeodetablas))
    for row in rows:
        try:
            table_name=row[0]
            print(table_name)
            df=pd.read_sql(table_name,connection)
            df.to_sql(name=table_name,con=conAwsv2,index=False,if_exists='replace')
        except Exception as e:
            print("error",e)


