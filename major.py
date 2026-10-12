# ============================================================
# EMPLOYEE LEAVE MANAGEMENT SYSTEM USING OOPS
# ============================================================


class Employee:

    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.total_leaves = 20
        self.remaining_leaves = 20

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Total Leaves: {self.total_leaves}")
        print(f"Remaining Leaves: {self.remaining_leaves}")

    @property
    def used_leaves(self):
        return self.total_leaves - self.remaining_leaves


class LeaveRecord:

    def __init__(self, employee_id, leave_type, days):
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.days = days

    def display_record(self, employee):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {employee.name}")
        print(f"Leave Type: {self.leave_type}")
        print(f"Number of Days: {self.days}")


class LeaveManagementSystem:

    def __init__(self):

        self.employees = {
            101: Employee(101, "Rahul", "CSE"),
            102: Employee(102, "Priya", "ECE"),
            103: Employee(103, "Arjun", "IT"),
            104: Employee(104, "Sneha", "CSE"),
            105: Employee(105, "Kiran", "EEE"),
            106: Employee(106, "Anjali", "IT"),
            107: Employee(107, "Vijay", "ECE"),
            108: Employee(108, "Meena", "CSE"),
            109: Employee(109, "Ravi", "MECH"),
            110: Employee(110, "Divya", "IT")
        }

        self.leave_types = ("Casual", "Sick", "Emergency")

        self.menu = (
            "Display Employees",
            "Apply Leave",
            "Check Leave Balance",
            "Employee Details",
            "Leave History",
            "Employees Currently on Leave",
            "Available Leave Types",
            "Exit"
        )

        self.leave_history = []
        self.employees_on_leave = set()

    def display_menu(self):
        for index, option in enumerate(self.menu, start=1):
            print(f"{index}. {option}")

    def verify_employee(self, employee_id):
        return employee_id in self.employees

    def ask_user_interaction(self):
        answer = input(
            "Do you want to interact again? (yes/no): "
        ).strip().lower()

        return answer == "yes"

    def display_leaves(self):
        for index, leave in enumerate(self.leave_types, start=1):
            print(f"{index}. {leave}")

    def dynamic_leave_update(self):
        for record in self.leave_history:
            yield record.employee_id, record.days

    def validate_leave(self, employee_id, choice, days):

        employee = self.employees[employee_id]

        if not 1 <= choice <= len(self.leave_types):
            print("Invalid leave type.")
            return False

        if not 1 <= days <= employee.remaining_leaves:
            print("Please enter a valid number of leave days.")
            return False

        return True

    def display_employees(self):
        for employee in self.employees.values():
            print(
                f"{employee.employee_id}: {employee.name} "
                f"- {employee.department}"
            )

    def apply_leave(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            if not self.verify_employee(employee_id):
                print("Invalid employee ID.")
                return

            self.display_leaves()

            choice = int(input("Choose leave type: "))
            days = int(input("Enter number of leave days: "))

        except ValueError:
            print("Please enter valid numeric values.")
            return

        if not self.validate_leave(employee_id, choice, days):
            return

        employee = self.employees[employee_id]
        leave_type = self.leave_types[choice - 1]

        employee.remaining_leaves -= days

        record = LeaveRecord(employee_id, leave_type, days)

        self.leave_history.append(record)
        self.employees_on_leave.add(employee_id)

        print("\nLeave approved successfully!")

        print(f"Employee: {employee.name}")
        print(f"Department: {employee.department}")
        print(f"Leave Type: {leave_type}")
        print(f"Days Taken: {days}")
        print(f"Remaining Leaves: {employee.remaining_leaves}")

    def check_leave_balance(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            if not self.verify_employee(employee_id):
                print("Invalid employee ID.")
                return

            employee = self.employees[employee_id]

            print("\n========== LEAVE BALANCE ==========")
            print(f"Employee: {employee.name}")
            print(f"Total Leaves: {employee.total_leaves}")
            print(f"Used Leaves: {employee.used_leaves}")
            print(f"Remaining Leaves: {employee.remaining_leaves}")

        except ValueError:
            print("Please enter a valid employee ID.")

    def employee_details(self):

        try:
            employee_id = int(input("Enter employee ID: "))

            if not self.verify_employee(employee_id):
                print("Invalid employee ID.")
                return

            print("\n========== EMPLOYEE DETAILS ==========")

            # self.employees[employee_id] is aobject which stores the data like behind process each user has each object so we are particular while calling
            self.employees[employee_id].display_details()

        except ValueError:
            print("Please enter a valid employee ID.")

    def leave_history_report(self):

        if not self.leave_history:
            print("No leave history available.")
            return

        print("\n========== LEAVE HISTORY ==========")

        for index, record in enumerate(self.leave_history, start=1):
            print(f"\nLeave Record: {index}")

            employee = self.employees[record.employee_id]
            record.display_record(employee)

            print("-----------------------------------")

    def employees_currently_on_leave(self):

        if not self.employees_on_leave:
            print("No employees have applied for leave.")
            return

        print("\n========== EMPLOYEES ON LEAVE ==========")

        for employee_id in sorted(self.employees_on_leave):

            employee = self.employees[employee_id]

            total_days = sum(
                days
                for emp_id, days in self.dynamic_leave_update()
                if emp_id == employee_id
            )

            print(f"Employee ID: {employee.employee_id}")
            print(f"Employee Name: {employee.name}")
            print(f"Department: {employee.department}")
            print(f"Total Leave Days Recorded: {total_days}")
            print("---------------------------------------")

    def available_leave_types(self):

        print("\n========== AVAILABLE LEAVE TYPES ==========")
        self.display_leaves()

    def run(self):

        print("========== EMPLOYEE LEAVE MANAGEMENT ==========")

        while True:

            self.display_menu()

            try:
                choice = int(input("Please enter a number: "))

            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if not 1 <= choice <= len(self.menu):
                print("Please enter a number between 1 and 8.")
                continue

            print(f"You have chosen: {self.menu[choice - 1]}")

            match choice:

                case 1:
                    self.display_employees()

                case 2:
                    self.apply_leave()

                case 3:
                    self.check_leave_balance()

                case 4:
                    self.employee_details()

                case 5:
                    self.leave_history_report()

                case 6:
                    self.employees_currently_on_leave()

                case 7:
                    self.available_leave_types()

                case 8:
                    print("Thanks for using the system!")
                    break

            if choice != 8 and not self.ask_user_interaction():
                print("Thanks for the interaction!")
                break


if __name__ == "__main__":
    system = LeaveManagementSystem()
    system.run()

    '''

    for i, v in system.employees.items():

        print(v.employee_id)

        print(v.name)

        print(v.department)
    '''
