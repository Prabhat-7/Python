class Student:
    def __init__(self,name,mks):
        self.name=name
        self.mks=mks
    def get_average(self):
        sum=0
        for val in self.mks:
            sum+=val
        print("the average score is",sum/3)

s1=Student("Prabhat",[98,99,100])
s1.get_average()