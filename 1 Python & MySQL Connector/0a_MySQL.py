# pip install MySQL-connector-python
# python -m pip install MySQL-connector-python
# pip3 install MySQL-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port = 3306,  # not necessary
  user="lintang",
  passwd="12345",
  auth_plugin = 'mysql_native_password' # if authentication plugin 'caching_sha2_password' is not supported
)
print(mydb)
