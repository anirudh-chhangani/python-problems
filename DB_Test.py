__author__ = 'dell'


import psycopg2
try:
    conn = psycopg2.connect("dbname='DB_test' user='postgres' host='localhost' password='1234567890'")
except:
    print "I am unable to connect to the database"
curr = conn.cursor()
field  = "datname"
curr.execute("SELECT "+field+" from pg_database")
print str(curr)
rows = curr.fetchall()
print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]