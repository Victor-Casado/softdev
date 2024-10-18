#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
def idFinder(a):
    return int(a['id'])
studentlist = []
gradelist = []
# Open the CSV file for reading
with open('students.csv', mode='r') as file:
    # Create a CSV reader with DictReader
    csv_reader = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each row (as a dictionary) to the list
        studentlist.append(row)

with open('courses.csv', mode='r') as file:
    # Create a CSV reader with DictReader
    csv_reader = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each row (as a dictionary) to the list
        gradelist.append(row)
#print(gradelist)
#print('\n')
studentlist.sort(key=idFinder)
#print(studentlist)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
for i in gradelist:
    code = i['code']
    mark = int(i['mark'])
    id = int(i['id'])
    c.execute(f"INSERT INTO courses VALUES ({code}, {mark}, {id})")

c.execute("CREATE TABLE students (code TEXT, mark INTEGER, id INTEGER PRIMARY KEY)")
for i in gradelist:
    name = i['name']
    age = int(i['age'])
    id = int(i['id'])
    c.execute(f"INSERT INTO students VALUES ({name}, {age}, {id})")

#==========================================================

db.commit() #save changes
db.close()  #close database
