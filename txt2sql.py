#!/usr/bin/python

import sys, getopt
import psycopg2

def main (argv):
	# Default values
	conn_host = 'localhost'
	conn_port = 5432
	conn_user = 'postgres'
	conn_password = ''
	conn_database = ''
	conn_table = ''
	conn_column = ''
	
	# Debigging what arguments were passed
	#print('ARGV      :', argv)
	
	try:
		opts, args = getopt.getopt(argv,'hH:p:u:P:t:c:d:', ["help", "host=", "port=", "user=", "password=", "table=", "column=", "database="])
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

	# Check if column, table and database are set
	if conn_column == '' or conn_table == '' or conn_database == '':
		print_help()
		sys.exit(1)
		
	print ("Table: ", conn_table, " Column: ", conn_column, " Database: ", conn_database)
	
	try:
		connection = psycopg2.connect(user = conn_user,
                                  password = conn_password,
                                  host = conn_host,
                                  port = conn_port,
                                  database = conn_database)
		cursor = connection.cursor()

		# Print PostgreSQL Connection properties
		print ( connection.get_dsn_parameters(),"\n")

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

	except (Exception, psycopg2.Error) as error :
		print ("Error while connecting to PostgreSQL", error)

	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
	
def print_help():
	print("txt2sql.py -t <table> -c <column> [ -H <host> | -p <port> | -u <user> | -P <password> ]\nParameters -t (--table) and -c (--column) are REQUIRED")

if __name__ == "__main__":
   main(sys.argv[1:])
