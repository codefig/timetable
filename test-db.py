import mysql.connector
from mysql.connector import Error
from arrangeTable_updarted import *
from written_exam_updated import *

def get_courses(string):
    db = mysql.connector.connect(host='127.0.0.1', 
    username='root', 
    password='', 
    database='timetable_funaab')
    cursor = db.cursor()
    if(string is "cbt"):
        courses_query = "SELECT * FROM courses_cbt";
        cursor.execute(courses_query)
        rows = cursor.fetchall()
        output = dict({})
        for row in rows:
        #output = output + str(row[0])+ "\t" + str(row[1]) + "\t" + str(row[2]) + "\n"
            output.update({str(row[1]):row[3]});
        return (output)
    else:
        courses_query = "SELECT * FROM courses_written"
        cursor.execute(courses_query)
        rows = cursor.fetchall()
        output = dict({})
        for row in rows:
            #output = output + str(row[0])+ "\t" + str(row[1]) + "\t" + str(row[2]) + "\n"
            output.update({str(row[1]):row[2 ]});
        return(output)

def get_halls_cbt():
    db = mysql.connector.connect(host='127.0.0.1', 
    username='root', 
    password='', 
    database='timetable_funaab')
    cursor = db.cursor()
    lecture_query = "SELECT * FROM halls_cbt"
    cursor.execute(lecture_query)
    rows = cursor.fetchall()
    output = dict({})
    for row in rows:
        #output = output + str(row[0])+ "\t" + str(row[1]) + "\t" + str(row[2]) + "\n"
        output.update({str(row[1]):int(row[2])});
    return(output)

def get_halls_written():
    db = mysql.connector.connect(host='127.0.0.1', 
    username='root', 
    password='', 
    database='timetable_funaab')
    cursor = db.cursor()
    lecture_query = "SELECT * FROM halls_written"
    cursor.execute(lecture_query)
    rows = cursor.fetchall()
    lecture_t = dict({})
    lecture_turbo = dict({})
    for row in rows:
        lecture_t.update({str(row[1]):int(row[2])});
        lecture_turbo.update({str(row[1]):int(row[3])});
    return([lecture_t,lecture_turbo])

# def send_eTimetable(data,halls):
#     # print (data)
#     # print(halls);
#     print data;
#     print halls;
#     schedule = Arr(halls,data,0,set([]));
#     print(schedule.arrange()[1]);

def send_writtenTable(data,halls,halls_t,which):
  
    schedule = written_exams(data,halls,halls_t,which);
    result = schedule.arrange();
    # print(result[0]);
    return(result[1]);

# send_eTimetable(get_courses(),get_halls_cbt())

# halls = get_halls_cbt();
# table = send_writtenTable(get_courses("cbt"),halls,halls,"cbt");

halls = get_halls_written();
table = send_writtenTable(get_courses("cbt"),halls[0],halls[1],"cbt");

# print(table)

output = ""
for i in table:
    for (days, values) in i.items():
       for(time, arrangement) in values.items():
           for(venue, course) in arrangement.items():
               courselist = " ".join(course)
               output  = output + days + "\t" + courselist +"\t" + time + "\t" + venue +"\n"
print(output)
# send_eTimetable(get_courses("written"),halls);

