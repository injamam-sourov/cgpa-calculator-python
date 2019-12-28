# create new class
class Course:
    def __init__(self, id, name, credit, grade):
        self.id= id
        self.name= name
        self.credit= credit
        self.grade= grade
        self.gradePoint= calcGradePoint(credit, grade)
# create empty course list
courses= []
# calculate grade point
def calcGradePoint(credit, grade):
    grade= grade.capitalize()
    if grade == 'A':
        gradePoint= credit*4.0
    elif grade == 'A-':
        gradePoint= credit*3.7
    elif grade == 'B+':
        gradePoint= credit*3.3
    elif grade == 'B':
        gradePoint= credit*3.0
    elif grade == 'B-':
        gradePoint= credit*2.7
    elif grade == 'C+':
        gradePoint= credit*2.3
    elif grade == 'C':
        gradePoint= credit*2.0
    elif grade == 'C-':
        gradePoint= credit*1.7
    elif grade == 'D+':
        gradePoint= credit*1.3
    elif grade == 'D':
        gradePoint= credit*1.0
    else:
        gradePoint= credit*0.0
    return gradePoint
# get course details, return course object
def getCourseDetails():
    print("Id: ", end= ' ')
    id= input()
    print("Name: ", end= ' ')
    name= input()
    print("Credit: ", end= ' ')
    credit= int(input())    # string to int
    print("Grade: ", end= ' ')
    grade= input()
    # create course object
    course = Course(id, name, credit, grade)
    return course
# program starts here
def main():
    # previous details
    print("Previous cgpa?", end=" ")
    cgpa0= float(input())  # string to float
    print("Credit(s) completed?", end=" ")
    credit0= int(input())  # string to int
    gradePoint0= cgpa0*credit0
    # current details
    print("Number of course(s) taken?", end=" ")
    numberOfCourses = int(input()) # string to int
    credit= 0
    gradePoint= 0
    # add courses to list
    for i in range(numberOfCourses):
        print("Course " + str(i+1))
        courses.append(getCourseDetails())
        # calculate current credit and grade point
        credit += courses[i].credit
        gradePoint += courses[i].gradePoint
    # calculate cgpa
    cgpa= (gradePoint+gradePoint0)/(credit+credit0)
    print(f"CGPA: {cgpa}")

    # print course table (use courses[]) * future

if __name__ == "__main__":
    main()
