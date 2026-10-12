class Employee:

     def __init__(self,employee_id, name, department):

          self.employee_id = employee_id

          self.name = name

          self.department = department

          self.total_leaves = 20

          self.used_leaves = 0

     @property
     def usedLeaves(self):

          return self.total_leaves - self.used_leaves
class LeaveRecord:

     def __init__(self,employee_id, leave_type, days):

          self.employee_id = employee_id

          self.leave_type  = leave_type

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

