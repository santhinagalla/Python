
from entities import Student, Course, StrategyMethod1, StrategyMethod2, RecordOffice


def main():
    # Create student and add homework scores and exam scores
    std1 = Student("Robert")
    std1.addHWScore(60)
    std1.addHWScore(70)
    std1.addHWScore(65)
    std1.addHWScore(75)
    std1.addHWScore(80)
    std1.addHWScore(90)
    std1.addExamScore(90)
    std1.addExamScore(95)
    print(f"{std1.name} average using Strategy 1: {std1.getAverage(StrategyMethod1())}")
    print(f"{std1.name} average using Strategy 2: {std1.getAverage(StrategyMethod2())}")
    print(f"{std1.name} average using Strategy 1: {std1.getAverage()}") # By default it takes Strategy 1, if we don not pass any Strategy


    # Create second student
    std2 = Student("John")

    # Create Course object and add students to Course
    course1 = Course("Computer Science", "CS")
    course1.addStudent(std1)
    course1.addStudent(std2)

    std2.addHWScore(50)
    std2.addHWScore(60)
    std2.addHWScore(55)
    std2.addHWScore(65)
    std2.addHWScore(70)
    std2.addHWScore(80)
    std2.addExamScore(75)
    std2.addExamScore(80)

    # Create second course and add students to course
    course2 = Course("Machine Learning", "ML")
    std3 = Student("Mark")
    std4 = Student("Paul")
    course2.addStudent(std3)
    course2.addStudent(std4)

    std3.addHWScore(60)
    std3.addHWScore(70)
    std3.addHWScore(65)
    std3.addHWScore(75)
    std3.addHWScore(80)
    std3.addHWScore(90)
    std3.addExamScore(80)
    std3.addExamScore(85)

    # Create record office
    recordOffice = RecordOffice()
    recordOffice.addCourse(course1)
    recordOffice.addCourse(course2)

    # Attach record office as observer for students
    std1.attachObserver(recordOffice)
    std2.attachObserver(recordOffice)
    std3.attachObserver(recordOffice)
    std4.attachObserver(recordOffice)

    print("Before Update: ", recordOffice.getStudentRecords())
    std4.addHWScore(50)
    print("After first homework: ", recordOffice.getStudentRecords())
    std4.addHWScore(60)
    print("After second homework: ", recordOffice.getStudentRecords())
    std4.addHWScore(55)
    print("After third homework: ", recordOffice.getStudentRecords())
    std4.addHWScore(65)
    print("After fourth homework: ", recordOffice.getStudentRecords())
    std4.addHWScore(70)
    print("After fifth homework: ", recordOffice.getStudentRecords())
    std4.addHWScore(80)
    print("After sixth homework: ", recordOffice.getStudentRecords())
    std4.addExamScore(75)
    print("After first exam: ", recordOffice.getStudentRecords())
    std4.addExamScore(80)
    print("After second exam: ", recordOffice.getStudentRecords())
    print()

    # Print student averages for course
    print(f"Student averages for course '{course1.courseTitle}' = {course1.getStudentAverages()}")
    print(f"Student averages for course '{course2.courseTitle}' = {course2.getStudentAverages()}")
    print(f"Grades from Record office: {recordOffice}")

main()