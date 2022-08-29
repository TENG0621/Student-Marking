



from cmath import sqrt
import statistics
import math 

i = 1
b = []
mark_list=[]
while True:   
    a = []

    student_number = i
    i += 1
    a.append(student_number)

    student_name = input("\nPlease enter name : ")
    a.append(student_name)
    
    student_id = int(input("Enter student's ID :"))
    a.append(student_id)

    student_mark = int(input("Enter student's mark : "))
    mark_list.append(student_mark) #make a list for student mark 
    a.append(student_mark)

    if student_mark <= 100 and student_mark >= 80:
        student_grade = "A"
        a.append(student_grade)

    elif student_mark <= 79 and student_mark >=60:
        student_grade = "B"
        a.append(student_grade)
    
    elif student_mark <= 59 and student_mark >= 50:
        student_grade = "C"
        a.append(student_grade)

    elif student_mark <= 49 and student_mark >= 0:
        student_grade = 'D'
        a.append(student_grade)

    print(a)
    b.append(a)

    again = input("\nDo you want to make a another record ? [y/n] :")
    if again == "y":
        continue
    else:
        break 


# #for the calculation purpose 
# x = len(b)
# total = sum(mark_list)
# average = float(total/x)
# standard_deviation = float(statistics.pstdev(mark_list))
# variance = sqrt(float(standard_deviation))

# print("The average marks is : " + str(average))
# print("The standard deviation is : " + str(standard_deviation))
# print("The variance is : " + str(variance))

#for the deleting of the student info 
while True: 
    for x in b: #making it like vertical list 
        print(x)

    delete_student = int(input("\nPlease Choose the number of student that you wish to delete : "))
    while True:
        if student_number >= delete_student:
            index = delete_student - 1
            b.pop(index) 
#             for y in b:
#                 student_name = y
            
            # x = len(b)
            # if delete_student < x:
            #     student_number[b] = student_number[b] - 1
            break

        else:
            delete_student = int(input("Invalid number. Please enter again : "))
            continue
    
    q = input("\nDo you want to delete another student information ? [y/n] : ")
    if q == "y":
        print(x)
        delete_student = int(input("Please Choose the number of student that you wish to delete : "))

    elif q == "n":
        print("Thank you")
        break 



        










        


