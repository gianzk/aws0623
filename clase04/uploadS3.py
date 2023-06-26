import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(response,"archivo subido")
    except ClientError as e:
        logging.error(e)
        return False
    return True




upload_file('./datacsv/offices01.csv',"democliv2","office01.csv") 
import pandas as pd
from getData import getConnLocal,getConectionLocalEngine

def getTableUplodas3():
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
        df.to_csv(f"./datacsv/{table_name}03.csv")
        #dfv2=pd.read_csv(f"./datacsv/{table_name}03.csv")
        upload_file(f"./datacsv/{table_name}03.csv","democliv2",f"{table_name}03.csv")


getTableUplodas3()