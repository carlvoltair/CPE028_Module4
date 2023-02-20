class Grades:
    def __init__ (self,Course_code, Units, Grade):
          self.Course_code = Course_code
          self.Units = Units
          self.Grade = Grade
    def __str__(self):

        return f'Course code: {self.Course_code}\nNo. of units: {self.Units}\ngrade:{self.Grade}'
      

          


   