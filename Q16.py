# Q16. A student will not be allowed to sit in exam if his/her attendence is less than 80%.Take following input from userTotal Number of classes heldTotal Number of classes attended. And print percentage of class attended. Is student is allowed to sit in exam or not.

a=int(input("Number of classes held:"))
b=int(input("Number of classes attended:"))

percentage=b/a*100

if percentage>=80:
    print("The student is allowed to sit in the exam hall")
else:
    print("The student is not allowed to sit in the exam hall")

# Output :

# Number of classes held:50
# Number of classes attended:40
# The student is allowed to sit in the exam hall