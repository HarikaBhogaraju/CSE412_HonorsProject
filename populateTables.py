import csv

import psycopg2

#establishing the connection
#Change X and Y to appropriate username and password
conn = psycopg2.connect(
   database="cse412_honors", user='hbhogara', password='db123', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
data = []
with open('StudentMentalHealth_v2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        data_row = []
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #Timestamp, Gender, Age, Major, Year,
            #GPA, Marital_Status, Depression, Anxiety, Panic_Attack, Treatment
            if(row[1] == "Male"):
                data_row.append('M') #gender
            else:
                data_row.append('F') #gender

            data_row.append(row[3]) #major
            data_row.append(row[4])#year
            if(row[6] == "Yes" or row[6] == "yes"):
                data_row.append('Y')#marital status
            else:
                data_row.append('N')#marital status
            if(row[7] == "Yes" or row[7] == "yes"):
                data_row.append('Y')#depression
            else:
                data_row.append('N')#depression
            if(row[8] == "Yes" or row[8] == "yes"):
                data_row.append('Y')#panic attack
            else:
                data_row.append('N')#anxiety
            if(row[8] == "Yes" or row[9] == "yes"):
                data_row.append('Y')#panic attack
            else:
                data_row.append('N')#anxiety

            if(row[8] == "Yes" or row[10] == "yes"):
                data_row.append('Y')#treatment
            else:
                data_row.append('N')#treatment
            line_count += 1
            data.append(data_row)
    print("Line count: ",line_count)

for row in data:
    #insertProduct = "INSERT INTO Product (product_code,product_name,benefits,description,price) VALUES ("+ str(row[0]) + ","+ str(row[1]) + ","+ str(row[2]) + ","+ str(row[3]) + ","+ str(row[4]) + ")"
    insertEntry = ''' INSERT INTO
    MentalHealth(gender,major,year,marital_status,depression,anxiety,panic_attack,treatment)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s) '''
    cursor.execute(insertEntry,row)
    conn.commit()
