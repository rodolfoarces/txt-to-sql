#!/usr/bin/python

import sys, getopt
import os
import psycopg2
import playsound

def main (argv):
	# Default values
	conn_host = '127.0.01'
	conn_port = 5432
	conn_user = 'postgres'
	conn_password = ''
	conn_database = ''
	conn_table = ''
	conn_column = ''
	# Parameters
	txt_file = ''
	snd_file = ''
	
	# Debigging what arguments were passed
	#print('ARGV      :', argv)
	
	try:
		opts, args = getopt.getopt(argv,'hH:p:u:P:t:c:d:f:s:', ["help", "host=", "port=", "user=", "password=", "table=", "column=", "database=", "file=", "sound="])
	except getopt.GetoptError:
		print_help()
		sys.exit(1)
	
	# Debugging what options were passed	
	#print('OPTIONS   :', opts)
	
	# Quit when asking for help
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			print_help()
			sys.exit(1)
		elif opt in ("-t", "--table"):
			conn_table = arg
		elif opt in ("-c", "--column"):
			conn_column = arg
		elif opt in ("-H", "--host"):
			conn_host = arg
		elif opt in ("-p", "--port"):
			conn_host = arg
		elif opt in ("-u", "--user"):
			conn_user = arg
		elif opt in ("-P", "--password"):
			conn_password = arg
		elif opt in ("-d", "--database"):
			conn_database = arg
		elif opt in ("-f", "--file"):
			txt_file = arg
		elif opt in ("-s", "--sound"):
			snd_file = arg

	# Check if column, table and database are set
	if conn_column == '' or conn_table == '' or conn_database == '' or txt_file == '':
		print_help()
		sys.exit(1)
	
	if not os.path.exists(txt_file) and not os.path.isfile(txt_file):
		print("The text file you referenced doesn't exists or is not a file")
		sys.exit(2)
		
	 
	# Debugging - Show connection parameters
	# print ("Table: ", conn_table, " Column: ", conn_column, " Database: ", conn_database)
	
	try:
		connection = psycopg2.connect(user = conn_user,
                                  password = conn_password,
                                  host = conn_host,
                                  port = conn_port,
                                  database = conn_database)
		cursor = connection.cursor()

		# Debugging - Print PostgreSQL Connection properties
		# print ( connection.get_dsn_parameters(),"\n")

		# Load the file
		f = open(txt_file, "r")
		
		# Read the first line
		txt_line = f.readline()
		#Iterate over lines
		while txt_line:
			#Create sentence command
			sentence = "INSERT INTO " + conn_table + " (" + conn_column + ") VALUES ('" + txt_line.rstrip('\n') + "');"
			#print(sentence)
			cursor.execute(sentence)
			connection.commit()
			txt_line = f.readline()
		
		# Closing file
		f.close()

	except (Exception, psycopg2.Error) as error :
		print ("Error while connecting to PostgreSQL", error)

	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			# Debugging - Print connection closed message
			# print("PostgreSQL connection is closed")
	
	if snd_file != '':
		if os.path.exists(snd_file) and os.path.isfile(snd_file):
			playsound(snd_file)
		else:
			playsound(/usr/share/sounds/alsa/Noise.wav)
	else:
		playsound(/usr/share/sounds/alsa/Noise.wav)
		
	
def print_help():
	print("txt2sql.py -t <table> -c <column> [ -H <host> | -p <port> | -u <user> | -P <password> ]\nParameters -t (--table),  -c (--column), -f (--file) and -d (--database) are REQUIRED")

if __name__ == "__main__":
   main(sys.argv[1:])
