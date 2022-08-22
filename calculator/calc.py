import sqlite3

db = sqlite3.connect('calculator.db')

cursor = db.cursor()

cursor.execute("""
       SELECT name FROM sqlite_master WHERE type='table' AND name='calculator';
        """)

if cursor.fetchone() is not None:
    print("table exist")
else:
    cursor.execute("""CREATE TABLE calculator (process)""")

print("""

CALCULATOR

PRESS 1 TO ADD.
PRESS 2 TO SUBTRACT.
PRESS 3 TO MULTIPLY.
PRESS 4 TO DIVIDE.

""")

operation = str(input("Select transaction: "))

if operation == "1":
    number1 = int(input("enter number1: "))
    number2 = int(input("enter number2: "))
    command = """INSERT INTO calculator VALUES ('Output-> """+str(number1)+"""+"""+str(number2)+""" = """+str(number1+number2)+"""')"""
    cursor.execute(command)
    print("Result:", "number1 + number2: ", number1 + number2)
elif operation == "2":
    number1 = int(input("enter number1: "))
    number2 = int(input("enter number2: "))
    command = """INSERT INTO calculator VALUES ('Output-> """+str(number1)+"""-"""+str(number2)+""" = """+str(number1-number2)+"""')"""
    cursor.execute(command)
    print("Result:", "number1 - number2): ",number1 - number2)
elif operation == "3":
    number1 = int(input("enter number1: "))
    number2 = int(input("enter number2: "))
    command = """INSERT INTO calculator VALUES ('Output-> """+str(number1)+"""*"""+str(number2)+""" = """+str(number1*number2)+"""')"""
    cursor.execute(command)
    print("Result:", "number1 * number2: ", number1 * number2)
elif operation == "4":
    number1 = int(input("enter number1: "))
    number2= int(input("enter number1: "))
    command = """INSERT INTO calculator VALUES ('Output-> """+str(number1)+"""/"""+str(number2)+""" = """+str(number1/number2)+"""')"""
    cursor.execute(command)
    print("Result:", "number1/number2: ", number1/number2)
else:
    print("you entered an invalid transaction...")

    
db.commit()

command = """SELECT * FROM calculator"""

cursor.execute(command)

data = cursor.fetchall()

print(data) 