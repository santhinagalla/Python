import copy,os
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, homeworkList, examList):
        pass

class StrategyMethod1(Strategy):
    def do_algorithm(self, homeworkScoresList, examScoresList):
        homeworkAvg = sum(homeworkScoresList) /len(homeworkScoresList) if len(homeworkScoresList) > 0 else 0
        examAvg = sum(examScoresList) /len(examScoresList) if len(examScoresList) > 0 else 0
        return round((homeworkAvg * 40 / 100) + (examAvg * 60 /100),2)

class StrategyMethod2(Strategy):
    def do_algorithm(self, homeworkScoresList, examScoresList):
        if len(homeworkScoresList) > 5:
            homeworkScoresList.remove(min(homeworkScoresList))
        homeworkAvg = sum(homeworkScoresList) /len(homeworkScoresList)  if len(homeworkScoresList) > 0 else 0
        examAvg = sum(examScoresList) /len(examScoresList) if len(examScoresList) > 0 else 0
        return round((homeworkAvg * 40 / 100) + (examAvg * 60 /100),2)

class Subject(ABC):
    @abstractmethod
    def attachObserver(self, observer):
        pass
    @abstractmethod
    def notifyObservers(self, observer):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Student(Subject):
    def __init__(self, student_name):
        self.__name = student_name
        self.__hw_scores = []
        self.__ex_scores = []
        self.__observers = []
    
    @property
    def name(self):
        return self.__name

    def attachObserver(self, observer):
        self.__observers.append(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update()
    
    def addHWScore(self, score):
        self.__hw_scores.append(score)
        self.notifyObservers()
    
    def addExamScore(self, score):
        self.__ex_scores.append(score)
        self.notifyObservers()
    
    def getAverage(self, strategy=StrategyMethod1()):
        # Send copies of list to make sure Algorithms do not change
        return strategy.do_algorithm(copy.deepcopy(self.__hw_scores), copy.deepcopy(self.__ex_scores))
            

class Course(Subject):
    def __init__(self, courseTitle, courseNo):
        self.__courseTitle = courseTitle
        self.__courseNo = courseNo
        self.__students = []
        self.__observers = []

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update()

    def attachObserver(self, observer):
        self.__observers.append(observer)
    
    @property
    def courseNo(self):
        return self.__courseNo
    
    @property
    def courseTitle(self):
        return self.__courseTitle

    def addStudent(self, student):
        self.__students.append(student)
    
    def getStudentAverages(self):
        studentAverages = {}
        for student in self.__students:
            studentAverages[student.name] = student.getAverage()
        return studentAverages


class RecordOffice(Observer):
    def __init__(self):
        self.__courses = []
        self.__studentRecords = {}

    def addCourse(self, course):
        self.__courses.append(course)

    def getStudentRecords(self):
        self.__updateStudentGrades()
        return self.__studentRecords

    def __getGrade(self, average):
        # (>=90=> A, >= 80=> B, >= 70=> C, >=60=>D, <=59=>F)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else: 
            return 'F'
    def __updateStudentGrades(self):
        for course in self.__courses:
            studentGrades = self.__studentRecords.get(course.courseNo, {})
            studentAveragesDict = course.getStudentAverages()
            for student_name in studentAveragesDict:
                studentGrades[student_name] = self.__getGrade(studentAveragesDict[student_name])
            self.__studentRecords[course.courseNo] = studentGrades

    def update(self):
        print("\nAn update to student record is notified")
        self.__updateStudentGrades()
    
    def __str__(self):
        strf = "\n"
        for courseNo in self.__studentRecords:
            strf += f"Course={courseNo}" + os.linesep
            studentGrades = self.__studentRecords[courseNo]
            for student_name in studentGrades:
                strf += f"\t{student_name:<20} : {studentGrades[student_name]}" + os.linesep
        return strf
