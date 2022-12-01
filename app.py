from flask import Flask, render_template, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import jinja2
import csv
import os
import psycopg2
import matplotlib
matplotlib.use('agg')

#establishing the connection
#Change X and Y to appropriate username and password
conn = psycopg2.connect(
   database="cse412_honors", user='hbhogara', password='db123', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

from io import BytesIO
app = Flask(__name__)

def data_vis_depression():
    if os.path.exists('depression.png'):
        os.remove('depression.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth'''
    cursor.execute(getTotalPeople)
    numberofPeople = cursor.fetchall()

    getNumberofDepressed = '''SELECT COUNT(*) FROM MentalHealth WHERE depression=%s'''
    cursor.execute(getNumberofDepressed,['Y'])
    numberofDepressed = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    depression_labels = ["Depression", "No Depression"]

    total = int(numberofPeople[0][0])
    totalDepressed = int(numberofDepressed[0][0])
    totalNotDepressed = total - totalDepressed


    percentageDepressed = round((totalDepressed*100)/total)
    percentageNotDepressed = round((totalNotDepressed*100)/total)
    print(percentageDepressed)
    print(percentageNotDepressed)

    values = [percentageDepressed, percentageNotDepressed]

    y = np.array(values)
    plt.clf()
    plt.pie(y, labels = depression_labels)
    plt.savefig("depression.png")

def data_vis_anxiety():
    if os.path.exists('anxiety.png'):
        os.remove('anxiety.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth'''
    cursor.execute(getTotalPeople)
    numberofPeople = cursor.fetchall()

    getNumberofAnxious = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s'''
    cursor.execute(getNumberofAnxious,['Y'])
    numberofAnxious = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    anxiety_labels = ["Anxiety", "No Anxiety"]

    total = int(numberofPeople[0][0])
    totalAnxious = int(numberofAnxious[0][0])
    totalNotAnxious = total - totalAnxious


    percentageAnxious = round((totalAnxious*100)/total)
    percentageNotAnxious = round((totalNotAnxious*100)/total)
    print(percentageAnxious)
    print(percentageNotAnxious)

    values_1 = [percentageAnxious, percentageNotAnxious]

    y_1 = np.array(values_1)
    plt.clf()
    plt.pie(y_1, labels = anxiety_labels)

    plt.savefig("anxiety.png")

def data_vis_anxiety_gender():
    if os.path.exists('anxiety_gender.png'):
        os.remove('anxiety_gender.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s'''

    cursor.execute(getTotalPeople,['Y'])
    numberofPeople = cursor.fetchall()

    getMale = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s AND gender=%s'''
    cursor.execute(getMale,['Y','M'])
    men = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    anxiety_labels = ["Male", "Female"]

    total = int(numberofPeople[0][0])
    totalMen = int(men[0][0])
    totalWomen = total - totalMen


    percentageMen = round((totalMen*100)/total)
    percentageWomen = round((totalWomen*100)/total)
    print(percentageMen)
    print(percentageWomen)

    values_1 = [percentageMen, percentageWomen]

    y_1 = np.array(values_1)
    plt.clf()
    plt.pie(y_1, labels = anxiety_labels)

    plt.savefig("anxiety_gender.png")

def data_vis_depression_gender():
    if os.path.exists('depression_gender.png'):
        os.remove('depression_gender.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth WHERE depression=%s'''

    cursor.execute(getTotalPeople,['Y'])
    numberofPeople = cursor.fetchall()

    getMale = '''SELECT COUNT(*) FROM MentalHealth WHERE depression=%s AND gender=%s'''
    cursor.execute(getMale,['Y','M'])
    men = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    depression_labels = ["Male", "Female"]

    total = int(numberofPeople[0][0])
    totalMen = int(men[0][0])
    totalWomen = total - totalMen


    percentageMen = round((totalMen*100)/total)
    percentageWomen = round((totalWomen*100)/total)
    print(percentageMen)
    print(percentageWomen)

    values_1 = [percentageMen, percentageWomen]

    y_1 = np.array(values_1)
    plt.clf()
    plt.pie(y_1, labels = depression_labels)

    plt.savefig("depression_gender.png")

def data_vis_anxiety_gender():
    if os.path.exists('anxiety_gender.png'):
        os.remove('anxiety_gender.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s'''

    cursor.execute(getTotalPeople,['Y'])
    numberofPeople = cursor.fetchall()

    getMale = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s AND gender=%s'''
    cursor.execute(getMale,['Y','M'])
    men = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    anxiety_labels = ["Male", "Female"]

    total = int(numberofPeople[0][0])
    totalMen = int(men[0][0])
    totalWomen = total - totalMen


    percentageMen = round((totalMen*100)/total)
    percentageWomen = round((totalWomen*100)/total)
    print(percentageMen)
    print(percentageWomen)

    values_1 = [percentageMen, percentageWomen]

    y_1 = np.array(values_1)
    plt.clf()
    plt.pie(y_1, labels = anxiety_labels)

    plt.savefig("anxiety_gender.png")

def data_vis_depression_status():
    if os.path.exists('depression_status.png'):
        os.remove('depression_status.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth WHERE depression=%s'''

    cursor.execute(getTotalPeople,['Y'])
    numberofPeople = cursor.fetchall()

    getMarried = '''SELECT COUNT(*) FROM MentalHealth WHERE depression=%s AND marital_status=%s'''
    cursor.execute(getMarried,['Y','Y'])
    married = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    status_labels = ["Married", "Single"]

    total = int(numberofPeople[0][0])
    totalMarried = int(married[0][0])
    totalSingle = total - totalMarried


    percentagemarried = round((totalMarried*100)/total)
    percentageSingle = round((totalSingle*100)/total)
    print(percentagemarried)
    print(percentageSingle)

    values_1 = [percentagemarried, percentageSingle]

    y_1 = np.array(values_1)
    plt.clf()
    plt.pie(y_1, labels = status_labels)

    plt.savefig("depression_status.png")

def data_vis_anxiety_status():
    if os.path.exists('anxiety_status.png'):
        os.remove('anxiety_status.png')

    getTotalPeople = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s'''

    cursor.execute(getTotalPeople,['Y'])
    numberofPeople = cursor.fetchall()

    getMarried = '''SELECT COUNT(*) FROM MentalHealth WHERE anxiety=%s AND marital_status=%s'''
    cursor.execute(getMarried,['Y','Y'])
    married = cursor.fetchall()

    #numberofDepressedWomen = int(numberofPeople[0][0])-int(numberofDepressedMen[0][0])
    #values = [numberofDepressedMen,numberofDepressedWomen]

    status_labels = ["Married", "Single"]

    total = int(numberofPeople[0][0])
    totalMarried = int(married[0][0])
    totalSingle = total - totalMarried


    percentagemarried = round((totalMarried*100)/total)
    percentageSingle = round((totalSingle*100)/total)
    print(percentagemarried)
    print(percentageSingle)

    values_1 = [percentagemarried, percentageSingle]

    y_1 = np.array(values_1)
    plt.clf()
    plt.pie(y_1, labels = status_labels)

    plt.savefig("anxiety_status.png")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/depression')
def run_depressed():
    if os.path.exists('depression.png'):
        os.remove('depression.png')
    data_vis_depression()
    filename = 'depression.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/anxiety')
def run_anxiety():
    if os.path.exists('anxiety.png'):
        os.remove('anxiety.png')
    data_vis_anxiety()
    filename = 'anxiety.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/anxiety_gender')
def run_anxiety_gender():
    if os.path.exists('anxiety_gender.png'):
        os.remove('anxiety_gender.png')
    data_vis_anxiety_gender()
    filename = 'anxiety_gender.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/depression_gender')
def run_depression_gender():
    if os.path.exists('depression_gender.png'):
        os.remove('depression_gender.png')
    data_vis_depression_gender()
    filename = 'depression_gender.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/depression_status')
def run_depression_status():
    if os.path.exists('depression_status.png'):
        os.remove('depression_status.png')
    data_vis_depression_status()
    filename = 'depression_status.png'
    return send_file(filename, mimetype='image/gif')

@app.route('/anxiety_status')
def run_anxiety_status():
    if os.path.exists('anxiety_status.png'):
        os.remove('anxiety_status.png')
    data_vis_anxiety_status()
    filename = 'anxiety_status.png'
    return send_file(filename, mimetype='image/gif')
