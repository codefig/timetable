# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface-cbt.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QPushButton, QMainWindow
import mysql.connector
from mysql.connector import Error
from courseDialog import Ui_Dialog
from venueDialog import Venue_Dialog
from WrittenHallDialog import Ui_writtenHallDialog

from arrangeTable_updarted import *
from written_exam_updated import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") 
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 831, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 831, 561))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuCourses = QtWidgets.QMenu(self.menubar)
        self.menuCourses.setObjectName("menuCourses")
        self.menuTimetable = QtWidgets.QMenu(self.menubar)
        self.menuTimetable.setObjectName("menuTimetable")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHalls = QtWidgets.QMenu(self.menubar)
        self.menuHalls.setObjectName("menuHalls")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Course = QtWidgets.QAction(MainWindow)
        self.actionAdd_Course.setObjectName("actionAdd_Course")
        self.actionView_Courses = QtWidgets.QAction(MainWindow)
        self.actionView_Courses.setObjectName("actionView_Courses")
        self.actionEdit_Course = QtWidgets.QAction(MainWindow)
        self.actionEdit_Course.setObjectName("actionEdit_Course")
        self.actionGenerate_E_Exam_Timetable = QtWidgets.QAction(MainWindow)
        self.actionGenerate_E_Exam_Timetable.setObjectName("actionGenerate_E_Exam_Timetable")
        self.actionPrint_Timetable = QtWidgets.QAction(MainWindow)
        self.actionPrint_Timetable.setObjectName("actionPrint_Timetable")
        self.actionCheck_Connection = QtWidgets.QAction(MainWindow)
        self.actionCheck_Connection.setObjectName("actionCheck_Connection")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_Hall = QtWidgets.QAction(MainWindow)
        self.actionAdd_Hall.setObjectName("actionAdd_Hall")
        self.actionView_Halls = QtWidgets.QAction(MainWindow)
        self.actionView_Halls.setObjectName("actionView_Halls")
        self.actionEdit_Hall = QtWidgets.QAction(MainWindow)
        self.actionEdit_Hall.setObjectName("actionEdit_Hall")
        self.actionDelete_All = QtWidgets.QAction(MainWindow)
        self.actionDelete_All.setObjectName("actionDelete_All")
        self.actionDelete_All_Halls = QtWidgets.QAction(MainWindow)
        self.actionDelete_All_Halls.setObjectName("actionDelete_All_Halls")
        self.menuCourses.addAction(self.actionAdd_Course)
        self.menuCourses.addAction(self.actionView_Courses)
        self.menuCourses.addAction(self.actionEdit_Course)
        self.menuCourses.addSeparator()
        self.menuTimetable.addAction(self.actionGenerate_E_Exam_Timetable)
        self.menuTimetable.addAction(self.actionPrint_Timetable)
        self.menuDatabase.addAction(self.actionCheck_Connection)
        self.menuDatabase.addAction(self.actionConnect)
        self.menuDatabase.addAction(self.actionDisconnect)
        self.menuAbout.addAction(self.actionAbout)
        self.menuHalls.addAction(self.actionAdd_Hall)
        self.menuHalls.addAction(self.actionView_Halls)
        self.menuHalls.addAction(self.actionEdit_Hall)
        self.menuHalls.addAction(self.actionDelete_All)
        self.menuHalls.addSeparator()
        self.menuHalls.addAction(self.actionDelete_All_Halls)
        self.menubar.addAction(self.menuCourses.menuAction())
        self.menubar.addAction(self.menuHalls.menuAction())
        self.menubar.addAction(self.menuTimetable.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #declare personal variables 
        self.databaseName = "timetable_funaab"
        self.alertMessageBox = QMessageBox()
        self.db = None

        self.courseCode = ""
        self.courseTitle = ""
        self.courseNumberofStudent = 0

        self.hallName = ""
        self.hallCapacity = 0

        self.newMainWindow = QMainWindow()
        self.courseDialog = QtWidgets.QDialog()
        self.hallDialog = QtWidgets.QDialog()
        self.hallHidden = False

        #perform connection of various buttons to slot and signals 
        self.actionAdd_Course.triggered.connect(self.add_course)
        self.actionView_Courses.triggered.connect(self.view_courses)
        self.actionEdit_Course.triggered.connect(self.edit_course)

        self.actionAdd_Hall.triggered.connect(self.add_hall)
        self.actionEdit_Hall.triggered.connect(self.edit_hall)
        self.actionView_Halls.triggered.connect(self.view_halls)
        self.actionDelete_All_Halls.triggered.connect(self.delete_halls)

        self.actionGenerate_E_Exam_Timetable.triggered.connect(self.generate_timetable)
        self.actionPrint_Timetable.triggered.connect(self.print_timetable)

        self.actionConnect.triggered.connect(self.connect_database)
        self.actionDisconnect.triggered.connect(self.disconnect_database)
        self.actionCheck_Connection.triggered.connect(self.check_connection)

        self.actionAbout.triggered.connect(self.print_about)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Written-Exam Timetable Generator"))
        self.menuCourses.setTitle(_translate("MainWindow", "Courses"))
        self.menuTimetable.setTitle(_translate("MainWindow", "Timetable"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.menuHalls.setTitle(_translate("MainWindow", "Halls"))
        self.actionAdd_Course.setText(_translate("MainWindow", "Add Course"))
        self.actionView_Courses.setText(_translate("MainWindow", "View Courses"))
        self.actionEdit_Course.setText(_translate("MainWindow", "Edit Course"))
        self.actionGenerate_E_Exam_Timetable.setText(_translate("MainWindow", "Generate Exam Timetable"))
        self.actionPrint_Timetable.setText(_translate("MainWindow", "Print Timetable"))
        self.actionCheck_Connection.setText(_translate("MainWindow", "Check Connection"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAdd_Hall.setText(_translate("MainWindow", "Add Hall"))
        self.actionView_Halls.setText(_translate("MainWindow", "View Halls"))
        self.actionEdit_Hall.setText(_translate("MainWindow", "Edit Hall"))
        self.actionDelete_All.setText(_translate("MainWindow", "Delete HAll"))
        self.actionDelete_All_Halls.setText(_translate("MainWindow", "Delete All Halls"))
    
    def add_course(self):
        
        self.courseui = Ui_Dialog()
        self.courseui.setupUi(self.courseDialog)
        # self.courseDialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.courseui.courseDialog.accepted.connect(self.add_new_course)
        self.courseui.courseDialog.rejected.connect(self.courseDialog.reject)

        self.courseDialog.exec_()
       

        
    def add_new_course(self):
        self.courseCode = self.courseui.codeInput.text()
        self.courseNumberofStudent = self.courseui.registeredStudentsInput.text()
        self.courseTitle =  self.courseui.titleInput.text()
        
        if self.db == None:
            QMessageBox.warning(self.newMainWindow, "Error ", "Please Connect to Database first")
        elif(self.courseCode == '' or self.courseNumberofStudent == ''):
            QMessageBox.about(self.newMainWindow, "Error", "Please Ensure Course Code and Number of Students are supplied")
        else:
            insert_query = "INSERT INTO courses_written(code,no_of_students, title) VALUES(%s, %s, %s)"
            cursor = self.db.cursor()
            insert_tuple = (self.courseCode,self.courseNumberofStudent, self.courseTitle)
            result = cursor.execute(insert_query, insert_tuple)
            print("result is : ", result)
            if(cursor.lastrowid):
                QMessageBox.information(self.newMainWindow, "Course ", "Course Added Successfully!")
                self.courseui.codeInput.setText("")
                self.courseui.registeredStudentsInput.setText("")
                self.courseui.titleInput.setText("")
            self.db.commit()

    def view_courses(self):
        if self.db == None:
            QMessageBox.warning(self.newMainWindow, "Error ", "Please Connect to Database first")
        else:
            cursor = self.db.cursor()
            courses_query = "SELECT * FROM courses_written"
            cursor.execute(courses_query)
            rows = cursor.fetchall()
            print("Total rows : ", cursor.rowcount)
            output = ""
            counter =1
            for row in rows:
                output = output + str(counter) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) +"\n"
                counter = counter +1
            self.textEdit.setText(output)
       
    
    def edit_course(self):
        if(self.db == None):
            QMessageBox.warning(self.newMainWindow, "Error ", "Please connect to database first")

        title, ok = QtWidgets.QInputDialog.getText(self.newMainWindow, 'Edit Course', 
            'Enter the course CODE:')
        if ok: 
            if(title == ''):
                QMessageBox.warning(self.newMainWindow, "Error ", "Course Title should not be empty")
            else:
                search_query = 'SELECT * FROM courses_written WHERE code = ' + "'"+str(title) + "'"
                print(search_query)
                cursor = self.db.cursor()
                cursor.execute(search_query)
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.information(self.newMainWindow, "Error ", "Course Not Found with that Code")
                else:
                    #create dialog and insert all course data
                    self.courseDialog = QtWidgets.QDialog()
                    self.courseui = Ui_Dialog()
                    self.courseui.setupUi(self.courseDialog)
                    self.courseDialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                    self.courseId = row[0]
                    self.courseui.codeInput.setText(str(row[1]))
                    self.courseui.registeredStudentsInput.setText(str(row[2]))
                    self.courseui.titleInput.setText(str(row[3]))
                  
            
                    self.courseui.courseDialog.accepted.connect(lambda: self.update_course(
                        self.courseId, 
                        self.courseui.codeInput.text(), 
                        self.courseui.registeredStudentsInput.text(), 
                        self.courseui.titleInput.text()))
                    self.courseui.courseDialog.rejected.connect(self.courseDialog.reject)
            
                    self.courseDialog.exec_()

    def update_course(self, course_id, course_code, reg_students, course_title):
        update_query = "UPDATE courses_written SET code=%s, no_of_students=%s, title=%s WHERE id=%s" 
        data =  (course_code, reg_students, course_title,  course_id)
        cursor = self.db.cursor()
        cursor.execute(update_query,data)
        self.db.commit()
        QMessageBox.information(self.newMainWindow, "Updated ", "Course Updated successfully !")
        self.courseDialog.hide()

    def add_hall(self):
        self.hallui = Ui_writtenHallDialog()
        self.hallui.setupUi(self.hallDialog)
    
        self.hallui.buttonBox.accepted.connect(self.add_new_hall)
        self.hallui.buttonBox.rejected.connect(self.close_hall_dialog)
        
        self.hallDialog.exec_()


    def add_new_hall(self):
    
        self.hallName = self.hallui.nameInput.text()
        self.capacityOne = self.hallui.capOneInput.text()
        self.capacityTwo = self.hallui.capTwoInput.text()
    

        if self.db == None:
            QMessageBox.warning(self.newMainWindow, "Error ", "Please Connect to Database first")
        elif(self.hallName == '' or self.hallCapacity == ''):
            QMessageBox.about(self.newMainWindow, "Error", "Please Ensure Hall Name and both capacities  are supplied")
        else:
            insert_query = "INSERT INTO halls_written(name, capOne, capTwo) VALUES(%s, %s, %s)"
            cursor = self.db.cursor()
            insert_tuple = (self.hallName, self.capacityOne, self.capacityTwo)
            result = cursor.execute(insert_query, insert_tuple)
            print("result is : ", result)
            if(cursor.lastrowid):
                QMessageBox.information(self.newMainWindow, "Hall ", "Written Exam Hall Added Successfully!")
                self.hallui.nameInput.setText("")
                self.hallui.capOneInput.setText("")
                self.hallui.capTwoInput.setText("")
            self.db.commit()

    def close_hall_dialog(self):
        self.hallDialog.hide()
    
    def edit_hall(self):
        print("THis is the edit hall function")
        if(self.db == None):
            QMessageBox.warning(self.newMainWindow, "Error ", "Please connect to database first")
        else:
            hallName, ok = QtWidgets.QInputDialog.getText(self.newMainWindow, 'Edit Hall', 
                'Enter Hall Name:')
            if ok: 
                print("The username is : ", hallName)
                if(hallName == ''):
                    QMessageBox.warning(self.newMainWindow, "Error ", "Hall Name should not be empty")
                else:
                    search_query = 'SELECT * FROM halls_written WHERE name = ' + "'"+str(hallName) + "'"
                    print(search_query)
                    cursor = self.db.cursor()
                    cursor.execute(search_query)
                    row = cursor.fetchone()
                    if row is None:
                        QMessageBox.information(self.newMainWindow, "Error ", "Hall  Not Found with that Name")
                    else:
                        #create dialog and insert hall data
                        self.hallDialog = QtWidgets.QDialog()
                        self.hallui = Ui_writtenHallDialog()
                        self.hallui.setupUi(self.hallDialog)
            
                        self.hallId = row[0]
                        self.hallui.nameInput.setText(str(row[1]))
                        self.hallui.capOneInput.setText(str(row[2]))
                        self.hallui.capTwoInput.setText(str(row[3]))
                    
                
                        self.hallui.buttonBox.accepted.connect(lambda: self.update_hall(
                            self.hallId, 
                            self.hallui.nameInput.text(), 
                            self.hallui.capOneInput.text(), 
                            self.hallui.capTwoInput.text()))
                        self.hallui.buttonBox.rejected.connect(self.hallDialog.reject)
                        self.hallDialog.exec_()
    
    def update_hall(self, id, name, capacityOne, capacityTwo):
        print("this is the update hall funciton")
        update_query = "UPDATE halls_written SET name=%s,capOne=%s, capTwo=%s WHERE id=%s" 
        data =  (name, capacityOne, capacityTwo, id)
        cursor = self.db.cursor()
        cursor.execute(update_query,data)
        self.db.commit()
        QMessageBox.information(self.newMainWindow, "Updated ", "Hall Information Updated successfully !")
        self.hallDialog.hide()

    def view_halls(self):
        
        if self.db == None:
            QMessageBox.warning(self.newMainWindow, "Error ", "Please Connect to Database first")
        else:
            cursor = self.db.cursor()
            courses_query = "SELECT * FROM halls_written"
            cursor.execute(courses_query)
            rows = cursor.fetchall()
            print("Total rows : ", cursor.rowcount)
            output = ""
            counter = 1
            for row in rows:
                output = output + str(counter) +"\t" + str(row[1]) + "\t" + str(row[2]) + '\t' + str(row[3]) + "\n"
                counter = counter + 1
            self.textEdit.setText(output)
    
    def delete_halls(self):
        print("This is the delete halls function")
    
    def generate_timetable(self):
        if self.db == None:
            QMessageBox.warning(self.newMainWindow, "Error ", "Please Connect to Database first")
        else:
            halls = self.get_halls_written();
            table = self.send_writtenTable(self.get_courses("written"),halls[0],halls[1],"written")
            output = ""
            for i in table:
                for (days, values) in i.items():
                    for(time, arrangement) in values.items():
                        for(venue, course) in arrangement.items():
                            courselist = ", ".join(course)
                            output  = output + days + "\t" + courselist +"\t" + time + "\t\t" + venue +"\n"
            self.textEdit.setText(output)
    
    def print_timetable(self):
        print("This is the print timetable function")

    def get_courses(self,string):
        
        cursor = self.db.cursor()
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
    def get_halls_written(self):
        
        cursor = self.db.cursor()
        lecture_query = "SELECT * FROM halls_written"
        cursor.execute(lecture_query)
        rows = cursor.fetchall()
        lecture_t = dict({})
        lecture_turbo = dict({})
        for row in rows:
            lecture_t.update({str(row[1]):int(row[2])});
            lecture_turbo.update({str(row[1]):int(row[3])});
        return([lecture_t,lecture_turbo])

    def send_writtenTable(self,data,halls,halls_t,which):
    
        schedule = written_exams(data,halls,halls_t,which);
        result = schedule.arrange();
        # print(result[0]);
        return(result[1]);
    
    def connect_database(self):
        try:
            self.db = mysql.connector.connect(host='127.0.0.1', 
            username='root', 
            password='', 
            database=self.databaseName)
            if(self.db.is_connected()):
                QMessageBox.about(self.newMainWindow, "DB connection", "Connected to database Successfully !")
        except Exception as err:
            QMessageBox.critical(self.newMainWindow, "DB Connection", str(err))

            
    
    def disconnect_database(self):
        if(self.db):
            self.db.close()
            QMessageBox.information(self.newMainWindow, "DB connection", "Database connection closed successfully!")
            self.db = None
        else:
            QMessageBox.critical(self.newMainWindow, "DB Connection", "Please Ensure Database is connected first")
    
    def check_connection(self):
        if self.db == None:
            QMessageBox.warning(self.newMainWindow, "Check connection", "Application Not connected to database")
        else:
            QMessageBox.information(self.newMainWindow, "Check connection", "Application is connected to database")
            


    def print_about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(" WRITTEN EXAM TIMETABLE GENERATOR")
        msg.setInformativeText("This Application generates the WRITTEN Exam Timetable")
        msg.setWindowTitle("About Application")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
