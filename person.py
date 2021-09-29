class Employee:
    def __init__(self,name,id,sal,dept):
        self.name = name
        self.id = id
        self.sal = sal
        self.dept = dept

    def displayEmployee(self):
        print ("Name : ",self.name, "id :",self.id, "sal :",self.sal, "dept :", self.dept)



class TimeSheet(Employee):
    def __init__(self,date,no_of_hours,activity,description,status):
        self.date = date
        self.no_of_hours = no_of_hours
        self.activity = activity
        self.description = description
        self.status = status


    def createTimeSheet(self):
        print ("date :", self.date, "Num of hours :", self.no_of_hours, "activity :", self.activity, "description :", self.description, "status :", self.status)


emp1 = Employee("kavya","3245","350000","hr")
emp2 = Employee("varshitha","5674","500000","accounting")
emp1.displayEmployee()
emp2.displayEmployee()

p = TimeSheet("22/1/21","40","none","filled","ok")
p.createTimeSheet()







