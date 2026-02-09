a = int(input("ENter the marks obtained:    "))

if (a>=90 and a<=100):
    print("Grade: A")
elif (a>=80 and a<90):
    print("Grade: B")
elif (a>=70 and a<80):
    print("Grade: C")
elif (a>=60 and a<70):
    print("Grade: D")
elif (a>=50 and a<60):
    print("Grade: E")
elif (a>=0 and a<50):
    print("Grade: F")
else:
    print("Invalid marks entered")
    