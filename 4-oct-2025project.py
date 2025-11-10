#project 5
#OOP Wrapper
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name,"Age",self.age)
class employee(person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.__emp_id=emp_id
        self.__salary=salary
    @property
    def emp_id(self):
        return self.__emp_id 
    @emp_id.setter
    def emp_id(self,eid):
        self.__emp_id=eid
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,sal):
        self.__salary=sal
    def display(self):
        super().display()
        print("ID:", self.emp_id,"Salary:",self.salary)
class manager(employee):
    def __init__(self,name,age,emp_id,salary,department):
        super().__init__(name,age,emp_id,salary)
        self.department=department
    def display(self):
        super().display()
        print("Departmemt:",self.department)
people=[]
while True:
    print()
    print("Python OOP project:Employee management system")
    print()
    print("Choose an operation")
    print("1. Create a person")
    print("2. Create a employee")
    print("3. Create a manager")
    print("4. Show details")
    print("5. Exit")
    choice=input("Enter your choice:").strip()
    match choice:
        case "1":
            n=input("Name:")
            a=int(input("Age:"))
            people.append(person(n,a))
            print("Person created")
        case "2":
            n=input("Name: ")
            a=int(input("Age: "))
            eid=input("ID: ")
            s=float(input("Salary: "))
            people.append(employee(n,a,eid,s))
            print("Employee created")
        case "3":
            n=input("Name: ")
            a=int(input("Age: "))
            eid=input("ID: ")
            s=float(input("Salary: "))
            d=input("Departmemnt: ")
            people.append(manager(n,a,eid,s,d))
            print("Manager created")
        case "4":
            print("Choose detail to show")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            choice2 = input("Enter your choice: ").strip()

            match choice2:
                case "1":
                    print("Person details:")
                    for p in people:
                        if isinstance(p, person) and not isinstance(p, employee):
                            p.display()
                case "2":
                    print("Employee details:")
                    for e in people:
                        if isinstance(e, employee) and not isinstance(e, manager):
                            e.display()
                case "3":
                    print("Manager details:")
                    for m in people:
                        if isinstance(m, manager):
                            m.display()
                case _:
                    print("Invalid choice")
        case "5":
            print("Exiting the system. All resources have been freed.")
            print()
            print("Goodbye")
        case _:
            print("Invalid choice")


        

