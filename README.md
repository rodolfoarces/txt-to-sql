# TXT-to-SQL

TXT-to-SQL is a python script that inserts lines of a Text file into an PostgreSQL Database.

--host Set database host to connect, default value is **localhost**

--port Set port to connect, default value is **5432**

--user Set user to connect, default value is **postgres**

--password Set password to connect, default value is **No password**

--table Set table to connect, is **required value**

--column Set column to insert text, is a **required value**, must be a TEXT column

Example:

```
txt2sql.py -t <table> -c <column> [ -H <host> | -p <port> | -u <user> | -P <password> ] 
```

## Requierements

Python module: psycopg2
