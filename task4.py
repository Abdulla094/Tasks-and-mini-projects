# WAP to accept admission of 5 students by taking the input from the user 
# store it in a dictionary 
# later one of the students cancels the addmission so print the complete name of the student

admission_detail = {}
for i in range(0,5):
    print("Enter the details of students : ",i+1)
    name = str(input("Enter the name od student :"))
    fathers_name = str(input("Enter the name of father :"))
    roll_no = int(input("Enter the roll no. of the student :"))
    mothers_name = str(input("Enter the name of mother : "))
    s_age = int(input("Enter the age :"))

print(admission_detail)
