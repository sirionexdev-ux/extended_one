employee_name = "Siva"
employee_id = 101
employee_type = "Permanent"
department = "CSE"

basic_salary = 30000
bonus = 5000
deduction = 2000

total_leaves = 20
used_leaves = 0
remaining_leaves = total_leaves

working_days = 22
present_days = 20
absent_days = working_days - present_days

employee_status = "Active"


while True:

    print("\n")
    print("=" * 55)
    print("             EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 55)

    print("1. Employee Details")
    print("2. Apply Leave")
    print("3. Check Leave Balance")
    print("4. Cancel Leave")
    print("5. Attendance Details")
    print("6. Salary Details")
    print("7. Employee Status")
    print("8. Employee Report")
    print("9. Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:

        case 1:

            print("\n---------- EMPLOYEE DETAILS ----------")

            print(f"Employee Name   : {employee_name}")
            print(f"Employee ID     : {employee_id}")
            print(f"Employee Type   : {employee_type}")
            print(f"Department      : {department}")

        case 2:

            print("\n---------- APPLY LEAVE ----------")

            print("1. Sick Leave")
            print("2. Casual Leave")
            print("3. Emergency Leave")

            leave_choice = int(input("Select leave type: "))
            number_of_days = int(input("Enter number of days: "))

            if number_of_days <= 0:

                print("\nNumber of days must be greater than 0.")
                continue

            if number_of_days > remaining_leaves:

                print("\nLeave Rejected!")
                print(f"Only {remaining_leaves} days are available.")
                continue

            match leave_choice:

                case 1:
                    leave_type = "Sick Leave"

                case 2:
                    leave_type = "Casual Leave"

                case 3:
                    leave_type = "Emergency Leave"

                case _:
                    print("\nInvalid leave type.")
                    continue

            used_leaves += number_of_days
            remaining_leaves = total_leaves - used_leaves

            print("\nLeave Applied Successfully!")
            print(f"Leave Type       : {leave_type}")
            print(f"Days Applied     : {number_of_days}")
            print(f"Used Leaves      : {used_leaves}")
            print(f"Remaining Leaves : {remaining_leaves}")

        case 3:

            print("\n---------- LEAVE BALANCE ----------")

            print(f"Total Leaves     : {total_leaves}")
            print(f"Used Leaves      : {used_leaves}")
            print(f"Remaining Leaves : {remaining_leaves}")

            if remaining_leaves == 0:
                print("You have no leaves remaining.")

            elif remaining_leaves <= 5:
                print("Your leave balance is low.")

            else:
                print("You have sufficient leave balance.")

        case 4:

            print("\n---------- CANCEL LEAVE ----------")

            if used_leaves == 0:

                print("No leaves available to cancel.")
                continue

            cancel_days = int(input("Enter number of days to cancel: "))

            if cancel_days <= 0:

                print("Invalid number of days.")
                continue

            if cancel_days > used_leaves:

                print("You cannot cancel more than used leaves.")
                continue

            used_leaves -= cancel_days
            remaining_leaves = total_leaves - used_leaves

            print("\nLeave Cancelled Successfully!")
            print(f"Cancelled Days  : {cancel_days}")
            print(f"Used Leaves     : {used_leaves}")
            print(f"Remaining Leaves: {remaining_leaves}")

        case 5:

            print("\n---------- ATTENDANCE DETAILS ----------")

            print(f"Working Days : {working_days}")
            print(f"Present Days : {present_days}")
            print(f"Absent Days  : {absent_days}")

            attendance_percentage = (
                present_days / working_days
            ) * 100

            print(f"Attendance % : {attendance_percentage:.2f}%")

            if attendance_percentage >= 90:
                print("Excellent Attendance")

            elif attendance_percentage >= 75:
                print("Good Attendance")

            else:
                print("Attendance is low.")

        case 6:

            print("\n---------- SALARY DETAILS ----------")

            gross_salary = basic_salary + bonus
            net_salary = gross_salary - deduction

            print(f"Basic Salary : ₹{basic_salary}")
            print(f"Bonus        : ₹{bonus}")
            print(f"Gross Salary : ₹{gross_salary}")
            print(f"Deduction    : ₹{deduction}")
            print(f"Net Salary   : ₹{net_salary}")

            if net_salary >= 40000:
                print("Salary Grade : A")

            elif net_salary >= 30000:
                print("Salary Grade : B")

            else:
                print("Salary Grade : C")

        case 7:

            print("\n---------- EMPLOYEE STATUS ----------")

            print(f"Current Status : {employee_status}")

            change_status = input(
                "Do you want to change status? (yes/no): "
            ).lower()

            if change_status == "yes":

                print("\n1. Active")
                print("2. On Leave")
                print("3. Resigned")

                status_choice = int(input("Select status: "))

                match status_choice:

                    case 1:
                        employee_status = "Active"

                    case 2:
                        employee_status = "On Leave"

                    case 3:
                        employee_status = "Resigned"

                    case _:
                        print("Invalid status.")
                        continue

                print(
                    f"Employee status changed to: "
                    f"{employee_status}"
                )

        case 8:

            print("\n")
            print("=" * 55)
            print("                 EMPLOYEE REPORT")
            print("=" * 55)

            print(f"Name             : {employee_name}")
            print(f"Employee ID      : {employee_id}")
            print(f"Department       : {department}")
            print(f"Employee Type    : {employee_type}")
            print(f"Status           : {employee_status}")

            print("-" * 55)

            print(f"Total Leaves     : {total_leaves}")
            print(f"Used Leaves      : {used_leaves}")
            print(f"Remaining Leaves : {remaining_leaves}")

            print("-" * 55)

            print(f"Working Days     : {working_days}")
            print(f"Present Days     : {present_days}")
            print(f"Absent Days      : {absent_days}")

            print("-" * 55)

            print(f"Basic Salary     : ₹{basic_salary}")
            print(f"Bonus            : ₹{bonus}")
            print(f"Deduction        : ₹{deduction}")
            print(f"Net Salary       : ₹{net_salary}")

            print("=" * 55)

        case 9:

            print("\nThank you for using")
            print("Employee Management System!")

            break

        case _:

            print("\nInvalid choice!")
            print("Please select an option from 1 to 9.")
