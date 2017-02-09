print("\nHello and welcome to Manmeet Singh's Grader\nPlease only enter POSITIVE NUMBERS")

E1=float(input("\nPlease type Exam 1's Grade: "))#all of this is just
E1Out=float(input("\nWhat was Exam 1 out of? "))#collecting the information
E2=float(input("\nPlease type Exam 2's Grade: "))#needed to calculate
E2Out=float(input("\nWhat was Exam 2 out of? "))#the grades and is casted as float
E3=float(input("\nPlease type your Final Exam Grade: "))
E3Out=float(input("\nWhat was your Final Exam out of? "))
Q1=float(input("\nPlease type Quiz 1's Grade: "))
Q1Out=float(input("\nWhat was Quiz 1 out of? "))
Q2=float(input("\nPlease type Quiz 2's Grade: "))
Q2Out=float(input("\nWhat was Quiz 2 out of? "))
Q3=float(input("\nPlease type Quiz 3's Grade: "))
Q3Out=float(input("\nWhat was Quiz 3 out of? "))
P1=float(input("\nPlease type Project 1's Grade: "))
P1Out=float(input("\nWhat was Project 1 out of? "))
P2=float(input("\nPlease type Project 2's Grade: "))
P2Out=float(input("\nWhat was Project 2 out of? "))
P3=float(input("\nPlease type Project 3's Grade: "))
P3Out=float(input("\nWhat was Project 3 out of? "))
P4=float(input("\nPlease type Project 4's Grade: "))
P4Out=float(input("\nWhat was Project 4 out of? "))
P5=float(input("\nPlease type Project 5's Grade: "))
P5Out=float(input("\nWhat was Project 5 out of? "))
P6=float(input("\nPlease type Project 6's Grade: "))
P6Out=float(input("\nWhat was Project 6 out of? "))

print("\nThanks for inputing your grades\nI'll calculate everything now\n...CALCULATING...")

E1percent=((E1/E1Out)*100)#Figures out the percent grade from the info above
E2percent=((E2/E2Out)*100)
E3percent=((E3/E3Out)*100)
Q1percent=((Q1/Q1Out)*100)
Q2percent=((Q2/Q2Out)*100)
Q3percent=((Q3/Q3Out)*100)
P1percent=((P1/P1Out)*100)
P2percent=((P2/P2Out)*100)
P3percent=((P3/P3Out)*100)
P4percent=((P4/P4Out)*100)
P5percent=((P5/P5Out)*100)
P6percent=((P6/P6Out)*100)

print("\nYou got %s out of %s on Exam 1" )% (E1, E1Out)#shows user what they entered
print("Meaning you got a %s percent on Exam 1" )% (E1percent)#shows user the percent grade using info above

print("\nYou got %s out of %s on Exam 2" )% (E2, E2Out)
print("Meaning you got a %s percent on Exam 2" )% (E2percent)

print("\nYou got %s out of %s on your Final Exam" )% (E3, E3Out)
print("Meaning you got a %s percent on your Final Exam" )% (E3percent)

print("\nYou got %s out of %s on Quiz 1" )% (Q1, Q1Out)
print("Meaning you got a %s percent on Quiz 1" )% (Q1percent)

print("\nYou got %s out of %s on Quiz 2" )% (Q2, Q2Out)
print("Meaning you got a %s percent on Quiz 2" )% (Q2percent)

print("\nYou got %s out of %s on Quiz 3" )% (Q3, Q3Out)
print("Meaning you got a %s percent on Quiz 3" )% (Q3percent)

print("\nYou got %s out of %s on Project 1" )% (P1, P1Out)
print("Meaning you got a %s percent on Project 1" )% (P1percent)

print("\nYou got %s out of %s on Project 2" )% (P2, P2Out)
print("Meaning you got a %s percent on Project 2" )% (P2percent)

print("\nYou got %s out of %s on Project 3" )% (P3, P3Out)
print("Meaning you got a %s percent on Project 3" )% (P3percent)

print("\nYou got %s out of %s on Project 4" )% (P4, P4Out)
print("Meaning you got a %s percent on Project 4" )% (P4percent)

print("\nYou got %s out of %s on Project 5" )% (P5, P5Out)
print("Meaning you got a %s percent on Project 5" )% (P5percent)

print("\nYou got %s out of %s on Project 6" )% (P6, P6Out)
print("Meaning you got a %s percent on Project 6" )% (P6percent)

QAve=((Q1percent+Q2percent+Q3percent)/3)#calculates the quiz average
PAve=((P1percent+P2percent+P3percent+P4percent+P5percent+P6percent)/6)#calculates the Project average
Etot=E1percent+E2percent+E3percent#adds all exams up
LGrade=((QAve+PAve+Etot)/5)#figures out the total average to use for the letter grade
print("\nYour average for the course is %s")% (LGrade) #Prints the number average of the course

if (LGrade >= 93.333):#using the LGrade variable, I can figure out the letter grade
        Grade=("A")#sets the grade variable to a string that we can print later
elif (LGrade >= 90):
        Grade=("A-")
elif (LGrade >= 86.667):
        Grade=("B+")
elif (LGrade >= 83.333):
        Grade=("B")
elif (LGrade >= 80):
        Grade=("B-")
elif (LGrade >= 76.667):
        Grade=("C+")
elif (LGrade >= 73.333):
        Grade=("C")
elif (LGrade >= 70):
        Grade=("C-")
elif (LGrade >= 66.667):
        Grade=("D+")
elif (LGrade >= 65):
        Grade=("D")
else:
        Grade=("F")



if (Grade == "F"):
        print("\nYour Letter grade for the course is F\nYou are Failing\n")#Another if statement that prints out if you are failing when you get a F
else:
        print("\nYour Letter grade for the course is %s\nYou are Passing\n")% (Grade)#Prints out you are passing if string variable Grade is not a F
