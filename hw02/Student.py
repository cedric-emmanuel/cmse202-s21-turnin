class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0,year=0):
        self.name = name
        self.gpa = gpa
        self.year=year
        self.courses=[]
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def enrol(self,course_list):
        self.courses.append(course_list)

    def display_courses(self):
        print("I am enroled in ",self.courses)
    def years_until_graduation(self):
        return 4-self.year

    
class Spartan(Student):
    def __init__(self,name):
        super().__init__(self,name)
        self.motto=[]
    def set_motto(self,m):
        self.motto=m
    def school_spirit(self):
        print("My name is:",self.name)
        print("I am a Spartan. My motto is",self.motto)