import mysql.connector

def conectarBBDD(host, db, user, pwd):
    return mysql.connector.connect(host=host, database=db, user=user, password=pwd)
