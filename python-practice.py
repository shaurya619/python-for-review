import operator
import random


#########################################PLEASE READ THE CONTENT GIVEN BELOW############################################################
#I used this code in a task in GCI 2018, but now since I havent done advanced python since a long time so i have forgotten a bit but I will recall it after some practice
#########################################################################################################################################

def readStudentDetails():
    print()
    # { 'John': 600, 'Ben': 800, 'David': 950, 'Mark': 980}
    print("Enter the number of students: ")
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the marks of students: ")
        marks = int(input())
        studentRecord[name] = marks
    print()
    return studentRecord


def rankStudents(studentRecord):
    try:
        print()
        # [('Mark', 980), ('David', 950), ('Ben', 800), ('John', 600)]
        sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
        print(sortedStudentRecord)
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()


def rewardStudents(sortedStudentRecord, reward):
    print()
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print()


def appreciateStudents(sortedStudentRecord):
    print()
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break
    print()


studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)



import operator
import random

def readStudentDetails():
    print()
    # { 'John': 600, 'Ben': 800, 'David': 950, 'Mark': 980}
    print("Enter the number of students: ")
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the marks of students: ")
        marks = int(input())
        studentRecord[name] = marks
    print()
    return studentRecord


def rankStudents(studentRecord):
    try:
        print()
        # [('Mark', 980), ('David', 950), ('Ben', 800), ('John', 600)]
        sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
        print(sortedStudentRecord)
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()


def rewardStudents(sortedStudentRecord, reward):
    print()
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print()


def appreciateStudents(sortedStudentRecord):
    print()
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break
    print()


studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)




############################################################################






def lottery():
    d = ["John", "Dan", "David", "Simon", "Benedict"]
    abc = random.choice(d)
    print("Conratulation", abc, "on winning the lottery" )

lottery()
############################################################################






def lottery():
    d = ["John", "Dan", "David", "Simon", "Benedict"]
    abc = random.choice(d)
    print("Conratulation", abc, "on winning the lottery" )

lottery()
