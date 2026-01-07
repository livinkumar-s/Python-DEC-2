# mysql-connector-python 
# pip install package

import mysql.connector


conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="temp"
)

cursor=conn.cursor()
print("Connection Successfull!")

# SELECT
# cursor.execute("SELECT * FROM acrtess")
# output=cursor.fetchall()
# print(output)


# Insert
# cursor.execute("INSERT INTO acrtess (name,rating) VALUE (%s,%s)",("Anupama",8))
# conn.commit()

# update
# cursor.execute("UPDATE acrtess SET rating=%s WHERE id=%s",(10,2))
# conn.commit()

# Adding Contact

def addContact():
    name=input("Enter the name: ")
    phone=int(input("Enter the phone number: "))
    cursor.execute("INSERT INTO contacts (name, phone) VALUE (%s,%s)",(name,phone))
    conn.commit()

def delContact():
    phone=int(input("Enter the phone: "))

    cursor.execute("SELECT id FROM contacts WHERE phone=%s",[phone])
    id=cursor.fetchall()

    cursor.execute("DELETE FROM contacts WHERE id=%s",[id[0][0]])
    conn.commit()

while True:
    action=int(input("The actions You Wanna Perform:\n1-->Add Contact\n2-->Delete Contact\n\n===>"))

    if action==1:
        addContact()
    elif action==2:
        delContact()
    else:
        print("Please enter valid input...!")