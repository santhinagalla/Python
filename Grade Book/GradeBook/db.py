import pathlib
import os
import csv
import shutil
from tempfile import NamedTemporaryFile, TemporaryFile
from business import Semester, Student, Assessment

py_script_directory = pathlib.Path(__file__).parent.absolute()
working_directory = pathlib.Path().absolute()

db_folder = str(py_script_directory) + os.sep

class SemesterData:
    __db_file = db_folder + "policy.dat"
    def __initialize(self):
        if not os.path.exists(self.__db_file):
            with open(self.__db_file, "w+") as csv_file:
                csv_file.write("semester id,no_pas,w_pas,no_tests,w_tests,no_fe,w_fe")
                csv_file.write("\n")

    def readAllSemesters(self):
        self.__initialize()
        semesters = {}
        with open(self.__db_file, "r+") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass # ignore headers
                else:
                    semester = Semester(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                    semesters[row[0]] = semester
                line_count += 1
        return semesters
    
    def getSemester(self, semesterId):
        with open(self.__db_file, "r+") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0 and int(row[0])==semesterId:
                    semester = Semester(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                    return semester
                line_count += 1
        return None

    def write(self, semester):
        self.__initialize()
        with open(self.__db_file, "a+") as csv_file:
            csv_file.write("{0},{1},{2},{3},{4},{5},{6}".format(semester.semesterId, semester.numberOfAssignments, semester.assignmentsWeight, semester.numberOfTests, semester.testsWeight, semester.numberOfFinalExams, semester.examsWeight))
            csv_file.write("\n")



class StudentData:
    __db_file = db_folder + "students.dat"
    def __initialize(self):
        if not os.path.exists(self.__db_file):
            with open(self.__db_file, "w+") as csv_file:
                csv_file.write("student id,firstname,lastname,grade")
                csv_file.write("\n")

    def readAllStudents(self):
        self.__initialize()
        students = {}
        with open(self.__db_file, "r+") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass # ignore headers
                else:
                    student = Student(int(row[0]), row[1], row[2], row[3])
                    students[int(row[0])] = student
                line_count += 1
        return students # Dictionary with student id as key

    def readStudent(self, studentId):
        with open(self.__db_file, "r+") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0 and int(row[0]) == studentId:
                    student = Student(int(row[0]), row[1], row[2], row[3])
                    return student
                line_count += 1
        return None

    def writeAllStudents(self, students): # Students dictionary with studentId as keys
        self.__initialize()
        for studentId in students:
            student = students[studentId]
            with open(self.__db_file, "a+") as csv_file:
                csv_file.write("{0},{1},{2},{3}".format(student.studentId, student.firstName, student.lastName, student.grade))
                csv_file.write("\n")
    
    def write(self, student):
        writeAllStudents({student.studentId: student})
    
    def update(self, students): # students is dictionary with key as student id
        temporary_file = NamedTemporaryFile("w+t", newline="\n", delete=False)
        with open(self.__db_file, "r") as csv_file, temporary_file:
            reader = csv.reader(csv_file, delimiter=",")
            writer = csv.writer(temporary_file, delimiter=",")
            line_count=0
            for row in reader:
                if line_count > 0 and int(row[0]) in students.keys():
                    student = students[int(row[0])]
                    row[1], row[2], row[3] = student.firstName, student.lastName, student.grade
                writer.writerow(row)
                line_count += 1
        
        # move temporary file to db file
        shutil.move(temporary_file.name, self.__db_file)


class AssessmentData:
    __db_file = db_folder + "Grades.dat"
    def __initialize(self):
        if not os.path.exists(self.__db_file):
            with open(self.__db_file, "w+") as csv_file:
                csv_file.write("student id,semester id,assessment type,assessment id,score")
                csv_file.write("\n")
    
    def write(self, assessment):
        self.writeAll([assessment])
    
    def writeAll(self, assessments):
        self.__initialize()
        with open(self.__db_file, "a+") as csv_file:
            for assessment in assessments:
                csv_file.write("{0},{1},{2},{3},{4}".format(assessment.studentId, assessment.semesterId, assessment.assessmentType, assessment.assessmentId, assessment.score))
                csv_file.write("\n")
    
    def update(self, assessment):
        temporary_file = NamedTemporaryFile("w+t", newline="\n", delete=False)
        with open(self.__db_file, "r") as csv_file, temporary_file:
            reader = csv.reader(csv_file, delimiter=",")
            writer = csv.writer(temporary_file, delimiter=",")
            line_count=0
            for row in reader:
                if line_count > 0 and ( int(row[0])== assessment.studentId and int(row[1])== assessment.semesterId and row[2]== assessment.assessmentType and int(row[3])==assessment.assessmentId ):
                    row[4]=assessment.score
                writer.writerow(row)
                line_count += 1
        
        # move temporary file to db file
        shutil.move(temporary_file.name, self.__db_file)
    
    def getAllAssessments(self):
        assessments = []
        with open(self.__db_file, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            line_count=0
            for row in reader:
                if line_count > 0:
                    assessment = Assessment(int(row[0]), int(row[1]), row[2], int(row[3]), int(row[4]))
                    assessments.append(assessment)
                line_count += 1
        return assessments
    
    def getAssessments(self, studentId, semesterId):
        assessments = []
        with open(self.__db_file, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            line_count=0
            for row in reader:
                if line_count > 0 and (int(row[0])== studentId and int(row[1])== semesterId):
                    assessment = Assessment(int(row[0]), int(row[1]), row[2], int(row[3]), int(row[4]))
                    assessments.append(assessment)
                line_count += 1
        return assessments