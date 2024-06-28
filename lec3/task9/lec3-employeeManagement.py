import csv
import os

class EmployeeDatabase:
    def __init__(self, file_name='employees.csv'):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Job', 'Salary'])

    def _read_employees(self):
        with open(self.file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
        
    def _write_employees(self, employees):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Job', 'Salary'])
            writer.writeheader()
            writer.writerows(employees)

    def add_employee(self, name, job, salary):
        employees = self._read_employees()
        new_id = int(employees[-1]['ID']) + 1 if employees else 1
        employees.append({'ID': str(new_id), 'Name': name, 'Job': job, 'Salary': str(salary)})
        self._write_employees(employees)
        print(f'Added employee {name}')

    def print_employee(self, emp_id):
        employees = self._read_employees()
        employee = next((emp for emp in employees if emp['ID'] == str(emp_id)), None)
        if employee:
            print(f"ID: {employee['ID']}, Name: {employee['Name']}, Job: {employee['Job']}, Salary: {employee['Salary']}")
        else:
            print(f'Employee with ID {emp_id} not found')

    def remove_employee(self, emp_id):
        employees = self._read_employees()
        employees = [emp for emp in employees if emp['ID'] != str(emp_id)]
        self._write_employees(employees)
        print(f'Removed employee with ID {emp_id}')

if __name__ == '__main__':
    db = EmployeeDatabase()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add new employee")
        print("2. Print employee data")
        print("3. Remove employee from the system")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            job = input("Enter employee job: ")
            salary = float(input("Enter employee salary: "))
            db.add_employee(name, job, salary)
        elif choice == '2':
            emp_id = int(input("Enter ID: "))
            db.print_employee(emp_id)
        elif choice == '3':
            emp_id = int(input("Enter ID: "))
            db.remove_employee(emp_id)
        elif choice == '4':
            break
        else:
            print("Wrong selection, try again.")
