import random
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
        
    def get_avg_grade(self, list_of_grades):
        grade = 0;
        count = 0;
        for g in list_of_grades:
            grade+=int(g)
            count+=1
        return grade/count

    def get_progression(self, ects):
        return int(ects)/150*100;
class Datasheet:
    def __init__(self, courses=[]):
        self.courses = courses
    
    def get_grades_as_list():
        yield 1+1
        
class Course:
    def __init__(self, name, classroom, teacher, etcs, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade
        
class studentGenerator:
     def create_students_csv(self, nr_of_students):
        courses = ["science", "math", "geo", "english"]
        url = "www.schoolfoto/"
        genders = ["male", "female"]
        names = ["Jamie", "kim", "unisexName", "Pixi"]
        names_teachers = ["JamieT", "kimT", "unisexNameT", "PixiT"]
        list_of_students = []
        for x in range(nr_of_students):
            list_of_students.append(""+ random.choice(names) + "," + random.choice(courses) + "," + random.choice(names_teachers) + "," + random.choice(genders) + "," + str(random.randrange(140)) +"," + str(random.randrange(7)) + "," + str(random.randrange(12)) + "," + url+str(random.randrange(9999))) 
        print(list_of_students)
        of = open("students_week3.csv", 'w')
        for stud in list_of_students:
            of.write(stud + "\n")
        of.close()
        
class read_from_csv:
    def read(self, csv):
        student_list = []
        with open(csv, newline='') as csv:
            lines = csv.readlines()
        rows = lines[:]
        new_list = []
        for r in rows:
            new_list.append(r)
        for n in new_list:
            arr = n.split(",")
            name = arr[0]
            course_name = arr[1]
            teacher = arr[2]
            gender = arr[3]
            ects = arr[4]
            classroom = arr[5]
            grade = arr[6]
            img_url = arr[7]
            c = Course(course_name, classroom, teacher, ects, grade)
            d = Datasheet(c)
            s = Student(name, gender, d, img_url)
            student_list.append(s)
            
        student_list.sort(key=lambda x:s.data_sheet.courses.grade, reverse=True)
        for s in student_list:
            print(s.name + " " + s.image_url + " " + str(s.get_avg_grade(s.data_sheet.courses.grade)))
        students = []
        grades = []
        for s in student_list:
            students.append(s.name)
            grades.append(int(s.data_sheet.courses.grade))

        plt.bar(students, grades)
        plt.title('grades pr student')
        plt.xlabel('student')
        plt.ylabel('grade')
        plt.show()
        
        for s in student_list:
            print("etcs progression for " + s.name + " : " + str(s.get_progression(s.data_sheet.courses.etcs)))
        
        progression_categories = ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]
        a,b,c,d,e = 0,0,0,0,0
        
        for s in student_list:
            if s.get_progression(s.data_sheet.courses.etcs) in range(0,21):
                a +=1
            if s.get_progression(s.data_sheet.courses.etcs) in range(21,41):
                b +=1
            if s.get_progression(s.data_sheet.courses.etcs) in range(41,61):
                c +=1
            if s.get_progression(s.data_sheet.courses.etcs) in range(61,81):
                d +=1
            if s.get_progression(s.data_sheet.courses.etcs) in range(81,101):
                e +=1
        number_of_students = [a, b, c, d, e]
        plt.bar(progression_categories, number_of_students)
        plt.title('ects pr student')
        plt.xlabel('ects')
        plt.ylabel('nrOfStudents')
        plt.show()
        
        