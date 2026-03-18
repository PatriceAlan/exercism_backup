"""
Implementation of the school class with its functions
"""

class School:
    """
    Class for the grade school problem
    """
    def __init__(self):
        """
        Initialization of the class
        """
        self.students = {}
        self._added = []

    def add_student(self, name, grade):
        """
        Function to add a student if he doesn't exist
        """
        if name not in self.students:
            self.students[name] = grade
            self._added.append(True)
        else:
            self._added.append(False)

    def roster(self):
        """
        Function to list all the students of the school roster sorted by grade and by name
        """
        return [name for name, grade in sorted(self.students.items(), key=lambda item: (item[1], item[0]))]
        

    def grade(self, grade_number):
        """
        Function to filter grade of students and sort alphabetically
        """
        return sorted([name for name, grade in self.students.items() if grade == grade_number])

    def added(self):
        """
        Function to verify if students have been added"""
        return self._added
