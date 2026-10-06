# Employee Leave Management System

employees = {
    101: {"name": "Rahul", "department": "CSE"},
    102: {"name": "Priya", "department": "ECE"},
    103: {"name": "Arjun", "department": "IT"},
    104: {"name": "Sneha", "department": "CSE"},
    105: {"name": "Kiran", "department": "EEE"},
    106: {"name": "Anjali", "department": "IT"},
    107: {"name": "Vijay", "department": "ECE"},
    108: {"name": "Meena", "department": "CSE"},
    109: {"name": "Ravi", "department": "MECH"},
    110: {"name": "Divya", "department": "IT"}
}

leave_types = ("Casual", "Sick", "Emergency")

menu = (
    "Display Employees",
    "Apply Leave",
    "Check Leave Balance",
    "Employee Details",
    "Leave History",
    "Employees Currently on Leave",
    "Available Leave Types",
    "Exit"
)

employees_on_leave = set()

leave_history = []

leave_balance = {
    101: 20,
    102: 20,
    103: 20,
    104: 20,
    105: 20,
    106: 20,
    107: 20,
    108: 20,
    109: 20,
    110: 20
}



while True:

    print("\n===== EMPLOYEE LEAVE MANAGEMENT =====")

    for ind,element in enumerate(menu, start = 1):

         print(ind, element)



    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\n===== EMPLOYEE LIST =====")

            for employee_id, details in employees.items():
                print(
                    employee_id,
                    "-",
                    details["name"],
                    "-",
                    details["department"]
                )

        case 2:
            print("\n===== APPLY LEAVE =====")

            employee_id = int(input("Enter Employee ID: "))

            if employee_id not in employees:
                print("Employee not found.")
                continue

            print("\nLeave Types:")

            for index, leave in enumerate(leave_types, start=1):
                print(index, leave)

            leave_choice = int(input("Select leave type: "))
            number_of_days = int(input("Enter number of days: "))

            if leave_choice < 1 or leave_choice > len(leave_types):
                print("Invalid leave type.")
                continue

            if number_of_days <= 0:
                print("Invalid number of days.")
                continue

            if number_of_days > leave_balance[employee_id]:
                print("Insufficient leave balance.")
                continue

            selected_leave = leave_types[leave_choice - 1]

            leave_balance[employee_id] -= number_of_days

            employees_on_leave.add(employee_id)

            leave_history.append({
                "employee_id": employee_id,
                "leave_type": selected_leave,
                "days": number_of_days
            })

            print("\nLeave approved.")
            print("Employee:", employees[employee_id]["name"])
            print("Leave Type:", selected_leave)
            print("Days:", number_of_days)
            print("Remaining Leaves:", leave_balance[employee_id])

        case 3:
            print("\n===== LEAVE BALANCE =====")

            employee_id = int(input("Enter Employee ID: "))

            if employee_id not in employees:
                print("Employee not found.")
                continue

            print("Employee:", employees[employee_id]["name"])
            print("Total Leaves: 20")
            print("Used Leaves:", 20 - leave_balance[employee_id])
            print("Remaining Leaves:", leave_balance[employee_id])

        case 4:
            print("\n===== EMPLOYEE DETAILS =====")

            employee_id = int(input("Enter Employee ID: "))

            if employee_id not in employees:
                print("Employee not found.")
                continue

            employee = employees[employee_id]

            print("Employee ID:", employee_id)
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Remaining Leaves:", leave_balance[employee_id])

        case 5:
            print("\n===== LEAVE HISTORY =====")

            if len(leave_history) == 0:
                print("No leave applications found.")

            else:
                for leave in leave_history:

                    employee_id = leave["employee_id"]

                    print("\nEmployee ID:", employee_id)
                    print("Name:", employees[employee_id]["name"])
                    print("Leave Type:", leave["leave_type"])
                    print("Days:", leave["days"])

        case 6:
            print("\n===== EMPLOYEES CURRENTLY ON LEAVE =====")

            if len(employees_on_leave) == 0:
                print("No employees are currently on leave.")

            else:
                for employee_id in employees_on_leave:
                    print(
                        employee_id,
                        "-",
                        employees[employee_id]["name"]
                    )

        case 7:
            print("\n===== AVAILABLE LEAVE TYPES =====")

            for leave in leave_types:
                print(leave)

        case 8:
            print("Thank you for using the system.")
            break

        case _:
            print("Invalid choice.")
