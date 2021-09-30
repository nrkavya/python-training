class Employee:
    def __init__(self,name,id,sal,dept):
        self.name = name
        self.id = id
        self.sal = sal
        self.dept = dept

    def displayEmployee(self):
        print ("Name : ",self.name, "id :",self.id, "sal :",self.sal, "dept :", self.dept)



class TimeSheet(Employee):
    def __init__(self, date, no_of_hours, activity, description, status, name, id, sal, dept):
        Employee.__init__(self, name, id, sal, dept)
        self.date = date
        self.no_of_hours = no_of_hours
        self.activity = activity
        self.description = description
        self.status = status


    def createTimeSheet(self):
        print ("date :", self.date, "Num of hours :", self.no_of_hours, "activity :", self.activity, "description :", self.description, "status :", self.status, "name :", self.name, "id :", self.id, "salary :", self.sal, "dept :",self.dept)


e1=Employee('kavya','1345','5000','do')
e1.displayEmployee()
e1=TimeSheet('28/09/2021','8','python training','basics','completed','kavya','1345','25000','do')
e1.displayEmployee()
e1.createTimeSheet()






