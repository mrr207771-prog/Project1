print("STUDENT MARK MANAGEMENT")
name=input("ENTER STUDENT NAME:")
mark1=int(input("ENTER LINUX MARK:"))
mark2=int(input("ENTER AWS MARK:"))
mark3=int(input("ENTER GIT MARK:"))
total=mark1+mark2+mark3
average=total/3
print("-------STUDENT RESULT------------")
print("STUDENT NAME:",name)
print("LINX MARK:",mark1)
print("AWS MARK:",mark2)
print("GIT MARK:",mark3)
print("TOTAL:",total)
print("AVERAGE:",average)
if mark1>=35 and mark2>=35 and mark3>=35:
    print("RESUT:PASS")
else:
    print("RESULT:FAIL")
