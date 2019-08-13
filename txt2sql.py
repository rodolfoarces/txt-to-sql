#!/usr/bin/python

import sys, getopt

def main (argv):
	# Default values
	host = 'localhost'
	port = 5432
	user = 'postgres'
	password = ''
	table = ''
	column = ''
	
	# Debigging what arguments were passed
	#print('ARGV      :', argv)
	
	try:
		opts, args = getopt.getopt(argv,'hH:p:u:P:t:c:', ["help", "host=", "port=", "user=", "password=", "table=", "column="])
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
			table = arg
		elif opt in ("-c", "--column"):
			column = arg
		elif opt in ("-H", "--host"):
			host = arg
		elif opt in ("-p", "--port"):
			host = arg
		elif opt in ("-u", "--user"):
			user = arg
		elif opt in ("-P", "--password"):
			password = arg

	# Check if column and table are set
	if column == '' or table == '':
		print_help()
		sys.exit(1)
		
	print ("Table: ", table, " Column: ", column)

def print_help():
	print("txt2sql.py -t <table> -c <column> [ -H <host> | -p <port> | -u <user> | -P <password> ]\nParameters -t (--table) and -c (--column) are REQUIRED")

if __name__ == "__main__":
   main(sys.argv[1:])
