import mysql.connector

class Conexao():
    def banco_dados(self):
        conexao=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="estudo"
                )   
        return conexao
    