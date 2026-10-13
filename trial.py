# ============================================================
# EMPLOYEE LEAVE MANAGEMENT SYSTEM
# ============================================================

def displayMenu(menu):
    for ind, ele in enumerate(menu, start=1):
        print(ind, ele)


def employeeVerfication(Eid, employees):
    return Eid in employees


def askUserInteraction():
    again = input(" Do you wanna interact again say yes/ No : ").strip().lower()
    return True if again == "yes" else False


def displayLeaves(data):
    for ind, leave in enumerate(data, start=1):
        print(f"{ind} : {leave} ")


def validateLeave(Eid, choice, days, data, leaves, balance):

    if not 1 <= choice <= len(leaves):
        print("Dude you have choosen wrong option which is does not exist")
        return False

    # days check

    if not (1 <= days <= balance[Eid]):
        print("please enter a valid amount of days that you are eligible")
        return False

    return True


def create_record_dictFormat(**details): return details


def dynamicLeaveUpdate(history):

    for value in history:

        yield value['employee'], value['days']


def getLeaveBalanceData(Eid, balance, data, history):

    # here i need to print the number of leaves actually exists and used leaves and remaining leaves
    total = 0

    # this generator is for getting total number of leaves to get total leaves we have
    for key, value in dynamicLeaveUpdate(history):

        if key == Eid:

            total += value

    total += balance[Eid]

    print(f"Hey {data} here are the total leaves according to company rules {total} days . ")

    print(f" The leaves you used are {total - balance[Eid]} days. ")

    print(f" The remaining leaves you left are {balance[Eid]} days . ")


def getEmployeeName(data, Eid): return data[Eid]['name']


def main():

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
        emp_id: 20 for emp_id in employees
    }

    print("================ Employee Leave Management ================")

    while True:
        displayMenu(menu)

        try:
            choice = int(input("Please enter a number: "))

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if not 1 <= choice <= len(menu):
            print("Please enter a number between 1 and 8.")
            continue

        chosen = menu[choice - 1]
        print(f"You have chosen: {chosen}")

        match choice:

            case 1:
                '''
                Here we have to display employees to display
                the data and for that we have to use concepts:
                for loop on dictionary and ask still wanna
                interact
                '''

                for employee, data in employees.items():
                    print(
                        f"{employee} : {data['name']} "
                        f"and {data['department']} department."
                    )

                    print(
                        " ==============================================================="
                    )

                if askUserInteraction():
                    continue
                else:
                    break

            case 2:
                '''
                Here user chose Apply Leave.
                First, we have to verify the employee.
                Then display the types of leave available.
                Get the user's selected leave_type.
                Similarly, get the number_of_days he/she needs.
                Validate both inputs and validate the leave and
                update the employees_on_leave, leave_history ,
                employee_balance
                '''

                try:

                    # ask the user for employee_id

                    employee_id = int(input("please enter your employee_id :  "))

                    if not employeeVerfication(employee_id, employees):
                        print("Invalid employee ID. Please try again.")
                        continue

                    # here we need to display types of leaves we have

                    displayLeaves(leave_types)

                    leave_choice = int(
                        input("please enter your leave_choice as displayed: ")
                    )

                    number_of_days = int(
                        input("please enter number of days you need:  ")
                    )

                except ValueError:
                    print("Please enter valid numeric values.")
                    continue

                # here we need to display types of leaves we have

                # check the user is eligible for leave

                if not validateLeave(
                    employee_id,
                    leave_choice,
                    number_of_days,
                    employees,
                    leave_types,
                    leave_balance
                ):
                    print("buddy please make sure you are eligible for leaves")
                    continue

                leave = leave_types[leave_choice - 1]

                print(f"yeah dude you have choose {leave}")

                # Dynamically updating the all details related to leaves :)

                leave_balance[employee_id] -= number_of_days

                # here we have create a record of the employee why he/she taken leave and how many days for future verification

                employee_leave_data = create_record_dictFormat(
                    employee=employee_id, leave_type=leave, days=number_of_days
                )

                # stroing the created a leave_history in a list

                leave_history.append(employee_leave_data)

                # adding the employee_id in database to get the better clarity who was on leave

                employees_on_leave.add(employee_id)

                print("ok well leave_approved")

                print(
                    f" Hello {employees[employee_id]['name']}  , belongs to' {employees[employee_id]['department']} ' & type of leave you have choosen is {leave} "
                    f"and you have taken {number_of_days} leave and you are "
                    f"left with {leave_balance[employee_id]}"
                )

                if askUserInteraction():
                    continue
                else:
                    break

            case 3:

                # check the leave balance
                '''
                here i just need to print the leave balance
                so what we need the data which contains the leave count
                for that we have leave_balance so for that we have to pass employee_id to check
                so ask for the employee_id and validate the employee then get the details
                of the employee
                '''

                try:

                    employee_id = int(input("please enter your employee_id : "))

                    if not employeeVerfication(employee_id, employees):

                        print("hey you have entered wrong id please check your id properly")

                        continue

                    name = getEmployeeName(employees, employee_id)

                    getLeaveBalanceData(
                        employee_id, leave_balance, name, leave_history
                    )

                except Exception as e:

                    print(str(e) + "  it is an error")

                if askUserInteraction():
                    continue

                else:
                    break

            case 4:
                '''
                Here we have to display the details of a particular employee.
                First, ask the user for the employee_id.
                Then validate the employee_id using employeeVerfication().
                If the employee exists, get the employee details from
                the employees dictionary and display the name, department,
                remaining leaves, and total leaves used.
                '''

                try:

                    # asking the user to enter the employee_id whose details are required

                    employee_id = int(input("Please enter your employee_id: "))

                    # checking whether the entered employee_id exists in the employees dictionary

                    if not employeeVerfication(employee_id, employees):
                        print("Invalid employee ID. Please check your ID.")
                        continue

                    # getting the employee details from the nested dictionary

                    employee_data = employees[employee_id]

                    # displaying the basic employee information

                    print("\n========== EMPLOYEE DETAILS ==========")
                    print(f"Employee ID: {employee_id}")
                    print(f"Employee Name: {employee_data['name']}")
                    print(f"Department: {employee_data['department']}")

                    # displaying the employee's current leave balance

                    print(f"Remaining Leaves: {leave_balance[employee_id]} days")

                    # calculating the total leaves used by this employee from leave_history

                    total_used = sum(
                        record['days']
                        for record in leave_history
                        if record['employee'] == employee_id
                    )

                    # displaying the total number of leaves used

                    print(f"Total Leaves Used: {total_used} days")
                    print("======================================")

                except ValueError:
                    print("Please enter a valid numeric employee ID.")
                    continue

                # asking whether the user wants to continue using the system

                if askUserInteraction():
                    continue
                else:
                    break

            case 5:
                '''
                Here we have to display the leave history of employees.
                The leave_history list contains dictionaries, and each
                dictionary stores the employee_id, leave_type, and days.

                We need to iterate through leave_history using a loop.
                For each record, retrieve the employee_id and use it to
                get the employee's name from the employees dictionary.

                Finally, display the employee name, employee_id,
                leave type, and number of leave days.
                '''

                # checking whether any leave records exist in the list

                if not leave_history:
                    print("No leave history is available.")
                else:

                    # displaying the heading for leave history

                    print("\n========== EMPLOYEE LEAVE HISTORY ==========")

                    # iterating through every leave record stored in leave_history

                    for ind, record in enumerate(leave_history, start=1):

                        # retrieving the employee_id from the current leave record

                        employee_id = record['employee']

                        # retrieving the employee's name using the employee_id

                        employee_name = employees[employee_id]['name']

                        # displaying all details related to this leave record

                        print(f"\nLeave Record: {ind}")
                        print(f"Employee ID: {employee_id}")
                        print(f"Employee Name: {employee_name}")
                        print(f"Leave Type: {record['leave_type']}")
                        print(f"Number of Days: {record['days']}")

                        print("--------------------------------------------")

                # asking whether the user wants to continue using the system

                if askUserInteraction():
                    continue
                else:
                    break

            case 6:
                '''
                Here we have to display the employees currently on leave.

                We are using employees_on_leave, which is a set containing
                employee IDs of employees who have applied for leave.

                We iterate through the set and retrieve the employee's
                name and department from the employees dictionary.

                Note: This set records employees who have applied for leave.
                It does not track whether their leave is active today or
                whether their approved leave period has ended.
                '''

                # checking whether the set contains any employee IDs

                if not employees_on_leave:
                    print("Currently, no employees have applied for leave.")
                else:

                    # displaying the heading for employees on leave

                    print("\n========== EMPLOYEES CURRENTLY ON LEAVE ==========")

                    # iterating through the employee IDs stored in the set

                    for employee_id in employees_on_leave:

                        # retrieving the employee's name and department

                        employee_name = employees[employee_id]['name']
                        department = employees[employee_id]['department']

                        # calculating the total leave days recorded for this employee

                        total_days = sum(
                            record['days']
                            for record in leave_history
                            if record['employee'] == employee_id
                        )

                        # displaying the employee's details

                        print(f"Employee ID: {employee_id}")
                        print(f"Employee Name: {employee_name}")
                        print(f"Department: {department}")
                        print(f"Total Leave Days Recorded: {total_days}")

                        print("--------------------------------------------")

                # asking whether the user wants to continue using the system

                if askUserInteraction():
                    continue
                else:
                    break

            case 7:
                '''
                Here we have to display all the leave types available
                in the company.

                The leave_types variable is a tuple containing fixed
                leave types: Casual, Sick, and Emergency.

                Since the tuple is iterable, we can pass it to
                displayLeaves(), which uses enumerate() to display
                each leave type with its corresponding number.
                '''

                # displaying all the leave types with their numbers

                print("\n========== AVAILABLE LEAVE TYPES ==========")

                displayLeaves(leave_types)

                print("============================================")

                # asking whether the user wants to continue using the system

                if askUserInteraction():
                    continue
                else:
                    break

            case 8:
                print("=================Thanks for the interaction==============")
                break


if __name__ == "__main__":
    main()
