
class Semester(object):
    def __init__(self, semesterId, numberOfAssignments, assignmentsWeight, numberOfTests, testsWeight, numberOfFinalExams, examsWeight):
        self.semesterId = semesterId
        self.numberOfAssignments=numberOfAssignments
        self.assignmentsWeight=assignmentsWeight
        self.numberOfTests=numberOfTests
        self.testsWeight=testsWeight
        self.numberOfFinalExams=numberOfFinalExams
        self.examsWeight=examsWeight

    @property
    def semesterId(self):
        return self.__semesterId
    @semesterId.setter
    def semesterId(self, semesterId):
        self.__semesterId = semesterId

    @property
    def numberOfAssignments(self):
        return self.__numberOfAssignments
    @numberOfAssignments.setter
    def numberOfAssignments(self, numberOfAssignments):
        self.__numberOfAssignments = numberOfAssignments
    
    @property
    def assignmentsWeight(self):
        return self.__assignmentsWeight
    @assignmentsWeight.setter
    def assignmentsWeight(self, assignmentsWeight):
        self.__assignmentsWeight = assignmentsWeight
    
    @property
    def numberOfTests(self):
        return self.__numberOfTests
    @numberOfTests.setter
    def numberOfTests(self, numberOfTests):
        self.__numberOfTests = numberOfTests
    
    @property
    def testsWeight(self):
        return self.__testsWeight
    @testsWeight.setter
    def testsWeight(self, testsWeight):
        self.__testsWeight = testsWeight
    
    @property
    def numberOfFinalExams(self):
        return self.__numberOfFinalExams
    @numberOfFinalExams.setter
    def numberOfFinalExams(self, numberOfFinalExams):
        self.__numberOfFinalExams = numberOfFinalExams
    
    @property
    def examsWeight(self):
        return self.__examsWeight
    @examsWeight.setter
    def examsWeight(self, examsWeight):
        self.__examsWeight = examsWeight

class Student(object):
    def __init__(self, studentId, firstName, lastName, grade=""):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade

    @property
    def studentId(self):
        return self.__studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.__studentId = studentId
    
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    
    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        self.__grade = grade



class Assessment(object):
    def __init__(self, studentId, semesterId, assessmentType, assessmentId, score):
        self.studentId = studentId
        self.semesterId = semesterId
        self.assessmentType = assessmentType
        self.assessmentId = assessmentId
        self.score = score
    
    @property
    def studentId(self):
        return self.__studentId
    @studentId.setter
    def studentId(self, studentId):
        self.__studentId = studentId
    
    @property
    def semesterId(self):
        return self.__semesterId
    @semesterId.setter
    def semesterId(self, semesterId):
        self.__semesterId = semesterId
    
    @property
    def assessmentType(self):
        return self.__assessmentType
    @assessmentType.setter
    def assessmentType(self, assessmentType):
        self.__assessmentType = assessmentType
    
    @property
    def assessmentId(self):
        return self.__assessmentId
    @assessmentId.setter
    def assessmentId(self, assessmentId):
        self.__assessmentId = assessmentId
    
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score
    