import mysql.connector

conexion = mysql.connector.connect(user='root', password='', host='localhost', database='sistema_reconocimiento_uni', port='3306')

print(conexion)