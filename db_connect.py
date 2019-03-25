
import pymysql

from tabulate import tabulate

# Open database connection
db = pymysql.connect("localhost", "root", "laxmi0217", "mysql")

# prepare a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("SELECT * FROM car.cars")
rows = cursor.fetchall()

print(tabulate(rows, headers=['ID', 'Make','Model', 'Year', 'Color', 'vin'], tablefmt='psql'))


# disconnect from server
db.close()
