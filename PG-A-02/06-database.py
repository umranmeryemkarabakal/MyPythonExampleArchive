import sqlite3

connection = sqlite3.connect("chinook.db")
print("veri tabani baglantisi hazir")

cursor = connection.cursor()

cursor.execute("select * from customers") 
# customer tablosunun tüm sütunları *, *>name : name 
result = cursor.fetchall()

for customer in result:
    print(customer[1] + " " + customer[2])

connection.close()



connection = sqlite3.connect("chinook.db")
print("veri tabani baglantisi hazir")

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers WHERE city='Oslo'")
result= cursor.fetchone()

connection.close()




connection = sqlite3.connect("chinook.db")
print("veri tabani baglantisi hazir")

cursor = connection.cursor()

sql = "INSERT INTO  genres(name) VALUES('MACERA')"

cursor.execute(sql)
connection.commit()

connection.close()
