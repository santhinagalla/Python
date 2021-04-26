import pathlib, os
from db import StudentData, SemesterData, AssessmentData
from business import Semester, Student, Assessment


py_script_directory = pathlib.Path(__file__).parent.absolute()
db_folder = str(py_script_directory) + os.sep

class StudentAssessment:

    def __init__(self):
        """
        # Read last semester from saved data
        self.__allSemesters = SemesterData().readAllSemesters()
        self.__semester = self.__allSemesters[list(self.__allSemesters)[-1]]
        """
        self.__semester=None
        self.__students= StudentData().readAllStudents()
        self.__assessments=[] # AssessmentData().getAllAssessments()
    
    def __getSemester(self):
        return self.__semester
    
    def __getStudents(self):
        return self.__students
    
    def __getAssessments(self):
        return self.__assessments
    
    def __getAssessmentsFor(self, studentId, semesterId):
        temp_list=[]
        for assessment in self.__getAssessments():
            if assessment.studentId==studentId and assessment.semesterId==semesterId:
                temp_list.append(assessment)
        return temp_list

    def setupNewSemester(self):
        semesterId = input("Enter Semester Id: ")
        
        numberOfAssignments=int(input("Enter number of Assignments: "))
        if numberOfAssignments not in range(0,7):
            raise ValueError("Number of Assignments should be between 0 to 6.")
        assignmentsWeight=int(input("Enter each Assignments Weight: ")) if numberOfAssignments > 0 else 0
        
        numberOfTests=int(input("Enter number of Tests: "))
        if numberOfTests not in range(0,5):
            raise ValueError("Number of Tests should be between 0 to 4.")
        testsWeight=int(input("Enter each Tests Weight: ")) if numberOfTests > 0 else 0
        
        numberOfFinalExams=int(input("Enter number of Final Exams: "))
        if numberOfFinalExams not in range(0,2):
            raise ValueError("Number of Final Exams should be between 0 to 1.")    
        examsWeight=int(input("Enter Final Exams Weight: ")) if numberOfFinalExams > 0 else 0
        
        totalWeight = (assignmentsWeight if numberOfAssignments >= 1 else 0) + \
            (testsWeight if numberOfTests >= 1 else 0)  + \
            (examsWeight if numberOfFinalExams >= 1 else 0)
        
        if totalWeight != 100:
            raise ValueError("Relative Weights should be between 1 to 100, " + str(totalWeight))

        semester = Semester(semesterId, numberOfAssignments, assignmentsWeight, numberOfTests, testsWeight, numberOfFinalExams, examsWeight)
        self.__semester = semester
        SemesterData().write(semester)
        # initialize grades data
        self.__assessments=[]

    def addStudent(self):
        studentId = int(input("Enter Student ID: "))
        if studentId not in range(0, 10000):
            raise ValueError("Student Id should be between 0 to 9999.")

        firstName = input("Enter Student first name: ")
        if len(firstName) > 20:
            raise ValueError("First Name cannot exceed 20 characters.")

        lastName = input("Enter Student last name: ")
        if len(lastName) > 20:
            raise ValueError("Last Name cannot exceed 20 characters.")

        student = Student(studentId, firstName, lastName)
        self.__students[student.studentId] = student
        # StudentData().write(student)
    
    def __recordAssessment(self, type):
        dict = {"P": "Programming Assignment", "T": "Test", "F": "Final Exam"}
        
        assessmentId = -1

        allStudents = self.__getStudents()
        semester = self.__getSemester()
        
        if type=="P":
            assessmentId = int(input("Enter "+ dict[type] +" id: "))
            if semester.numberOfAssignments <1 or assessmentId not in range(1, semester.numberOfAssignments+1):
                raise ValueError("Programming Assignment id is not valid")
        elif type=="T":
            assessmentId = int(input("Enter "+ dict[type] +" id: "))
            if semester.numberOfTests <1 or assessmentId not in range(1, semester.numberOfTests+1):
                raise ValueError("Test id is not valid")
        elif type=="F":
            assessmentId = 1
            if semester.numberOfFinalExams < 1:
                raise ValueError("Final Exam not allowed")

        for studentId in allStudents:
            student = allStudents[studentId]
            score = int(input("Enter score for '" + student.lastName + "' with id '" + str(student.studentId) + "': "))
            assessment = Assessment(student.studentId, semester.semesterId, type, assessmentId, score)
            self.__assessments.append(assessment)
    
    def recordProgrammingAssignments(self):
        self.__recordAssessment("P")
    
    def recordTestScores(self):
        self.__recordAssessment("T")
    
    def recordFinalExams(self):
        self.__recordAssessment("F")
    
    def changeGradeForStudent(self):
        dict = {"P": "Programming Assignment", "T": "Test", "F": "Final Exam"}

        studentId = int(input("Enter student id to change grade: "))

        allStudents = self.__getStudents()
        if studentId not in allStudents.keys():
            raise ValueError("Student id not found")

        typeOfAssessment = input("Please enter type of score to change (P - Programming Assignment, T - Test, F - Final Score): ").strip().upper()[0]
        if typeOfAssessment not in dict.keys():
            raise ValueError("Please enter valid type of score to change")

        semester = self.__getSemester()
        semesterId = semester.semesterId

        assessmentId = -1
        assessmentId = int(input("Enter "+ dict[typeOfAssessment] +" id: "))
        
        newScore = int(input("Enter new score: "))

        isUpdated = False
        for assessment in self.__getAssessments():
            if assessment.studentId==studentId and assessment.semesterId==semesterId and \
                assessment.assessmentType == typeOfAssessment and assessment.assessmentId==assessmentId:
                assessment.score=newScore
                isUpdated = True
        if not isUpdated:
            print(dict[typeOfAssessment] + " with id " + str(assessmentId) + " is not found to update. You can record new one.")
    
    def __getAllStudentsFinalScores(self):
        semester = self.__getSemester()
        semesterId = semester.semesterId
        
        allStudents = self.__getStudents()
        for studentId in allStudents:
            student = allStudents[studentId]
            allAssessments = self.__getAssessmentsFor(studentId, semesterId)
            if len(allStudents) < 1:
                print("No grades recorded for Student '" + student.lastName +"' with id '" + str(student.studentId) + "'")
                continue

            programmingAssignmentsConducted = 0
            programmingTotal = 0
            programmingScores=""

            testsConducted = 0
            testsTotal = 0
            testsScores=""

            finalExamsConducted = 0
            finalExamTotal = 0
            finalExamScores=""
            
            for assessment in allAssessments:
                if assessment.assessmentType == "P":
                    programmingTotal += assessment.score
                    programmingAssignmentsConducted += 1
                    programmingScores += str(assessment.score)+","
                elif assessment.assessmentType == "T":
                    testsTotal += assessment.score
                    testsConducted += 1
                    testsScores += str(assessment.score)+","
                elif assessment.assessmentType == "F":
                    finalExamTotal += assessment.score
                    finalExamsConducted += 1
                    finalExamScores += str(assessment.score)+","
            gradeScore = (programmingTotal * semester.assignmentsWeight / (programmingAssignmentsConducted * 100) if semester.assignmentsWeight > 0 else 0) +\
                        (testsTotal * semester.testsWeight / (testsConducted * 100) if semester.testsWeight > 0 else 0) +\
                            (finalExamTotal * semester.examsWeight / (finalExamsConducted * 100 ) if finalExamsConducted > 0 and semester.examsWeight > 0 else 0)
            student.grade = gradeScore

            student.programmingTotal = programmingTotal
            student.testsTotal = testsTotal
            student.finalExamTotal = finalExamTotal

            student.programmingScores = programmingScores[:-1] if len(programmingScores) > 1 else ""
            student.testsScores = testsScores[:-1] if len(testsScores) > 1 else ""
            student.finalExamScores = finalExamScores[:-1] if len(finalExamScores) > 1 else ""
        return allStudents
    
    def calculateFinalScoresForAllStudents(self):
        allStudents = self.__getAllStudentsFinalScores()
    
    def outputGradeData(self):
        # Write students to CSV file
        StudentData().writeAllStudents(self.__getStudents())

        # Write assessment data to CSV file
        AssessmentData().writeAll(self.__getAssessments())

        allStudents = list(self.__getAllStudentsFinalScores().values())

        # Sort by student id
        sorted(allStudents, key= lambda student: student.studentId)
        
        # Sort by student last name
        # sorted(allStudents, key= lambda student: student.lastName)

        db_file = db_folder + "Grades.out"
        with open(db_file, "w+") as csv_file:
            for student in allStudents:
                formatString = "Name={}, Id={}, Assignment Score(s)=[{}], Test Score(s)=[{}], Final Exam Score(s)=[{}], Final Score={}"
                row = formatString.format(student.firstName+" "+student.lastName, student.studentId, student.programmingScores, student.testsScores, student.finalExamScores, student.grade)
                csv_file.write(row)
                csv_file.write("\n")
        