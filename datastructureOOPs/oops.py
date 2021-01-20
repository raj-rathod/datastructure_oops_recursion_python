class Organization:
    def __init__(self , name, founder, since, type):
        self.name = name
        self.founder = founder
        self.since = since
        self.type = type

    def show_organization(self):
        print("                  Organization                          ")
        print(f"Name : {self.name}  Founded By : {self.founder} Since : {self.since} Type of Organization : {self.type}")

class Department:
    x =1
    def __init__(self , data):
        self.D_id = Department.x
        Department.x+=1
        self.department_name = data[0]
        self.manager_name = data[1]
        self.number_of_emp = data[2]

    def show_department(self):
        print(f"Department_ID : {self.D_id}   Department : {self.department_name}   Manager : {self.manager_name}  Number Of employee : {self.number_of_emp}")


class Project:
    pid = 1
    def __init__(self,data):
        self.projectID = Project.pid
        Project.pid += 1
        self.project_name = data[0]
        self.department_name = data[1]
        self.number_of_emp = data[2]
        self.working_hrs = data[3]
        self.deadline = data[4]

    def show_project(self):
        print(f"Project ID : {self.projectID}  Project Name : {self.project_name}  Department Name : {self.department_name} Number Of Emp : {self.number_of_emp}  Working Hours : {self.working_hrs} Finishing Date : {self.deadline}")


class Employee():
    eid = 1
    def __init__(self,data):
      self.eid = Employee.eid
      Employee.eid += 1
      self.name = data[0]
      self.age = data[1]
      self.gender = data[2]
      self.department_name = data[3]
      self.salary = data[4]


    def show_employee(self):
        print(f"Emp Id : {self.eid}  Emp Name : {self.name}  Emp Age : {self.age} Gender : {self.gender} Salary : {self.salary} Department : {self.department_name}")

