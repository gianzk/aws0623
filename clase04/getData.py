import sqlalchemy as sq
import mysql.connector
import pandas as pd

def getConectionLocalEngine():
   return sq.create_engine("mysql+pymysql://admin:Admin2020*@localhost:3307/bdsample?charset=utf8mb4")
def getConnLocal():
    return mysql.connector.connect(
    host='localhost',
    user='admin',
    password='Admin2020*', 
    port=3307,
    database='bdsample'
    )

def getTablesToCsv():
   sqlSentence="select * from schema_mv1"
   conn=getConnLocal()
   cursor=conn.cursor()
   cursor.execute(sqlSentence)
   rows=cursor.fetchall()

    #warning de pandas
   connv2=getConectionLocalEngine()
   for row in rows:
        table_name=row[0]
        df=pd.read_sql(f"select * from {table_name}",connv2)
        df.to_csv(f"./datacsv/{table_name}02.csv")

getTablesToCsv()