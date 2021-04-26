from StudentAssessment import StudentAssessment
import sys
import traceback

def quit():
    sys.exit(0)

def displayChoices():
    print("Your choices are:")
    print("\t1. S - Set up for new semester")
    print("\t2. A - Add Student")
    print("\t3. P - Record programming assignment score for all students")
    print("\t4. T - Record test score for all students")
    print("\t5. F - Record Final exam score for all students")
    print("\t6. C - Change a grade for a particular student.")
    print("\t7. G - Calculate final score for all students")
    print("\t8. O - Output the grade data")
    print("\t9. Q - Quit")

def main():
    studentAssessment = StudentAssessment()
    
    while True:
        displayChoices()
        try:
            command = input("Enter your command: ").strip().upper()[0]
            if command == "S":
                studentAssessment.setupNewSemester()
            elif command == "A":
                studentAssessment.addStudent()
            elif command == "P":
                studentAssessment.recordProgrammingAssignments()
            elif command == "T":
                studentAssessment.recordTestScores()
            elif command == "F":
                studentAssessment.recordFinalExams()
            elif command == "C":
                studentAssessment.changeGradeForStudent()
            elif command == "G":
                studentAssessment.calculateFinalScoresForAllStudents()
            elif command == "O":
                studentAssessment.outputGradeData()
            elif command == "Q":
                quit()
        except Exception as e:
            print("** Exception occured")
            print(e)
            traceback.print_tb(e.__traceback__)
        finally:
            print("\n\n")

if __name__ == "__main__":
    main()