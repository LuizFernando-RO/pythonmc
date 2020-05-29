import mysql.connector

user = "ardit700_student"
password = "ardit700_student"
host = "108.167.140.122"
database = "ardit700_pm1database"

con = mysql.connector.connect(user=user, password=password, host=host, database=database)

word = input("Enter word: ")

cursor = con.cursor()
query = cursor.execute(" SELECT * FROM Dictionary WHERE Expression = '{}' ".format(word))
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("Word not found")