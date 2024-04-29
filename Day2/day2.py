import mysql.connector

my_db = mysql.connector.connect(
    host="localhost", user="root", password="", database="python_db"
)

cur = my_db.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS employee(
            id INT UNIQUE NOT NULL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INT NOT NULL,
            department CHAR(50),
            salary INT NOT NULL,
            managed_department CHAR(50) DEFAULT NULL
            );"""
)
my_db.commit()


class Employee:
    __employees = []

    def __init__(self, id, first_name, last_name, age, department, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        Employee.add_employee(self)
        cur.execute(
            """INSERT INTO employee(id, first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                self.id,
                self.first_name,
                self.last_name,
                self.age,
                self.department,
                self.salary,
            ),
        )
        my_db.commit()

    def transfer(self, department):
        self.department = department
        cur.execute(
            """UPDATE employee SET department = %s WHERE id = %s""",
            (self.department, self.id),
        )
        my_db.commit()

    def fire(self):
        Employee.get_employees().remove(self)
        cur.execute(
            """DELETE FROM employee WHERE id = %s""",
            (self.id,),
        )
        my_db.commit()

    def show(self):
        print(
            f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}"
        )

    @classmethod
    def list_employees(cls):
        cur.execute("SELECT * FROM employee")
        employees_data = cur.fetchall()
        for data in employees_data:
            print(
                f"ID: {data[0]}, Name: {data[1]} {data[2]}, Age: {data[3]}, Department: {data[4]}, Salary: {data[5]}"
            )

    @classmethod
    def add_employee(cls, employee):
        cls.__employees.append(employee)

    @classmethod
    def get_employees(cls):
        return cls.__employees

    @classmethod
    def get_employee_count(cls):
        return len(cls.__employees)

    @classmethod
    def get_employee_by_id(cls, emp_id):
        for emp in cls.__employees:
            if emp.id == emp_id:
                return emp
        return None


class Manager(Employee):
    def __init__(
        self, id, first_name, last_name, age, department, salary, managed_department
    ):
        super().__init__(id, first_name, last_name, age, department, salary)
        self.managed_department = managed_department

        cur.execute(
            """UPDATE employee SET managed_department = %s WHERE id = %s""",
            (self.managed_department, self.id),
        )
        my_db.commit()

    def show(self):
        print(
            f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: confidential, Managed Department: {self.managed_department}"
        )


def add_employee(role):
    id = get_last_id() + 1
    first_name = input("first Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))

    if role == "m":
        managed_department = input("Managed Department: ")
        Manager(id, first_name, last_name, age, department, salary, managed_department)
    else:
        Employee(id, first_name, last_name, age, department, salary)
    print("Employee Added successfully.")


def transfer(id):
    emp = Employee.get_employee_by_id(id)
    if emp:
        new_department = input("Enter the new department: ")
        emp.transfer(new_department)
        print("Employee transferred successfully.")
    else:
        print("Employee not found.")


def fire(id):
    emp = Employee.get_employee_by_id(id)
    if emp:
        emp.fire()
        print("Employee fired successfully.")
    else:
        print("Employee not found.")


def show(id):
    emp = Employee.get_employee_by_id(id)
    if emp:
        emp.show()
    else:
        print("Employee not found.")


def get_last_id():
    if Employee.get_employee_count() == 0:
        return 0
    else:
        last_employee = Employee.get_employees()[-1]
        return last_employee.id


def display_menu():
    print("\nEmployee Management System")
    print("Options:")
    print("  - Add Employee (Press 'e' for Employee, 'm' for Manager): 'add'")
    print("  - Transfer Employee: 'transfer'")
    print("  - Fire Employee: 'fire'")
    print("  - Show Employee: 'show'")
    print("  - List ALL Employees: 'list'")
    print("  - Exit Program: 'q'")
    print()


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "add":
            role = input("Are you adding an Employee ('e') or a Manager ('m')? ")
            add_employee(role)
        elif choice == "transfer":
            transfer(int(input("Enter the ID of the employee: ")))
        elif choice == "show":
            show(int(input("Enter the ID of the employee: ")))
        elif choice == "fire":
            fire(int(input("Enter the ID of the employee: ")))
        elif choice == "list":
            Employee.list_employees()
        elif choice == "q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
my_db.close()
