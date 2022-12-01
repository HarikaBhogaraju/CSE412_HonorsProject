import csv

import psycopg2

#establishing the connection
#Change X and Y to appropriate username and password
conn = psycopg2.connect(
   database="cse412_honors", user='hbhogara', password='db123', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Feedback
createMentalHealth = '''CREATE TABLE MentalHealth(
mh_id SERIAL PRIMARY KEY,
gender CHAR(1) NOT NULL,
major VARCHAR(200) NOT NULL,
year VARCHAR(200) NOT NULL,
marital_status CHAR(1) NOT NULL,
depression CHAR(1) NOT NULL,
anxiety CHAR(1) NOT NULL,
panic_attack CHAR(1) NOT NULL,
treatment CHAR(1) NOT NULL
)'''

cursor.execute(createMentalHealth)
print("Student Mental Health Table created successfully")

conn.commit()
