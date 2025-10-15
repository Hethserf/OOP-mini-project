class Students:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def calculate_average(self):
        if len(self.grade) == 0:
            return 0
        return sum(self.grade) / len(self.grade)

student1 = Students("Ali",[18,17,16,15])
student2 = Students("Sarah",[20,18,16,19])
student3 = Students("Mohammad",[])

print(f'Average : {student1.calculate_average()}')
print(f'Average : {student2.calculate_average()}')
print(f'Average : {student3.calculate_average()}')
