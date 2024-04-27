 # Defines a Student class with attributes name, rollno, m1 (marks1), and m2 (marks2).

class Student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.m1 = marks1
        self.m2 = marks2

       
# Includes a method calculate_result() to determine if a student passed or failed based on their marks.

    def calculate_result(self):
        total_marks = self.m1 + self.m2
        if total_marks >= 40:
            return "Pass"
        else:
            return "Fail"
        

ls = []

# Adds a new student object to the ls (list of students) list

def accept(name, rollno, marks1, marks2):
    ob = Student(name, rollno, marks1, marks2)
    ls.append(ob)


# Displays details of a student.

def display(ob):
    print("Name   : ", ob.name)
    print("RollNo : ", ob.rollno)
    print("Marks1 : ", ob.m1)
    print("Marks2 : ", ob.m2)
    print("Result : ", ob.calculate_result())
    print("-----------------------------------------")
    print("\n")
    

# Searches for a student object by roll number

def search(rn):
    for i in range(len(ls)):
        if ls[i].rollno == rn:
            return ls[i]
    return None

# Deletes a student object from the list by roll number.

def delete(rn):
    i = search(rn)
    if i is not None:
        ls.remove(i)
    else:
        print("Student not found")

# Updates the roll number of a student object.

def update(rn, new_rollno):
    i = search(rn)
    if i is not None:
        i.rollno = new_rollno
    else:
        print("Student not found")

# Defines a Teacher class with attributes name, emp_id (employee ID), and subject.

class Teacher:
    def __init__(self, name, emp_id, subject):
        self.name = name
        self.emp_id = emp_id
        self.subject = subject

teacher_list = []

# Adds a new teacher object to the teacher_list

def accept_teacher(name, emp_id, subject):
    ob = Teacher(name, emp_id, subject)
    teacher_list.append(ob)

# Displays details of a teacher object passed as an argument

def display_teacher(ob):
    print("Name     : ", ob.name)
    print("Emp ID   : ", ob.emp_id)
    print("Subject  : ", ob.subject)
    print("\n")


# Searches for a teacher object by employee ID

def search_teacher(emp_id):
    for i in range(len(teacher_list)):
        if teacher_list[i].emp_id == emp_id:
            return teacher_list[i]
    return None


# Deletes a teacher object from the list by employee ID

def delete_teacher(emp_id):
    teacher = search_teacher(emp_id)
    if teacher is not None:
        teacher_list.remove(teacher)
    else:
        print("Teacher not found")


# Updates the employee ID of a teacher object.

def update_teacher(emp_id, new_emp_id):
    teacher = search_teacher(emp_id)
    if teacher is not None:
        teacher.emp_id = new_emp_id
    else:
        print("Teacher not found")


while True:
    try:
        print(""" 
                __________________________________________________________________________________________
                |                                          ABC PUBLIC SCHOOL                             |
                |                    1. ADD STUDENT                       2. DISPLAY STUDENT             |
                |                    3. SEARCH STUDENT                    4. DELETE STUDENT              |
                |                    5. UPDATE STUDENT                    6. ADD TEACHER                 |
                |                    7. DISPLAY TEACHER                   8. SEARCH TEACHER              |
                |                    9 DELETE TEACHER                     10. UPDATE TEACHER              |
                |                                          11.EXIT                                       |
                |________________________________________________________________________________________|
                
              
              """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = str(input("Enter name: "))
            rollno = int(input("Enter roll number: "))
            marks1 = int(input("Enter marks1: "))
            marks2 = int(input("Enter marks2: "))
            accept(name, rollno, marks1, marks2)
        elif choice == 2:
            for ob in ls:
                display(ob)
        elif choice == 3:
            rollno = int(input("Enter roll number: "))
            ob = search(rollno)
            if ob is not None:
                display(ob)
            else:
                print("Student not found")
        elif choice == 4:
            rollno = int(input("Enter roll number: "))
            delete(rollno)
        elif choice == 5:
            rollno = int(input("Enter roll number: "))
            new_rollno = int(input("Enter new roll number: "))
            update(rollno, new_rollno)
        elif choice == 6:
            name = input("Enter name: ")
            emp_id = int(input("Enter employee ID: "))
            subject = input("Enter subject: ")
            accept_teacher(name, emp_id, subject)
        elif choice == 7:
            for ob in teacher_list:
                display_teacher(ob)
        elif choice == 8:
            emp_id = int(input("Enter employee ID: "))
            teacher = search_teacher(emp_id)
            if teacher is not None:
                display_teacher(teacher)
            else:
                print("Teacher not found")
        elif choice == 9:
            emp_id = int(input("Enter employee ID: "))
            delete_teacher(emp_id)
        elif choice == 10:
            emp_id = int(input("Enter employee ID: "))
            new_emp_id = int(input("Enter new employee ID: "))
            update_teacher(emp_id, new_emp_id)
        elif choice == 11:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number for choice.")
    except Exception as e:
        print("An error occurred:", e)
