import mysql.connector
from mysql.connector import Error
from arrangeTable import *
from written_exam import *

def get_courses():
    print("Getting courses")
    db = mysql.connector.connect(host='127.0.0.1', 
    username='root', 
    password='', 
    database='timetable_funaab')
    cursor = db.cursor()
    courses_query = "SELECT * FROM courses_cbt"
    cursor.execute(courses_query)
    rows = cursor.fetchall()
    print("Total rows : ", cursor.rowcount)
    output = dict({})
    for row in rows:
        #output = output + str(row[0])+ "\t" + str(row[1]) + "\t" + str(row[2]) + "\n"
        output.update({str(row[1]):row[3]});
    return(output)

def send_eTimetable(data):
    schedule = Arr();
    print(schedule.arrange(data,0,{'compb':500, 'AST':250},0,0,set([])))
def send_writtenTable(data):
    schedule = written_exams(data);
    print(schedule.arrange());
# send_eTimetable(get_courses())
send_writtenTable(get_courses());
