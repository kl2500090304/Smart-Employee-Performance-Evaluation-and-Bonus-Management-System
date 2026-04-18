import csv
import matplotlib.pyplot as plt
import os

# File paths
EMP_FILE = "employees.csv"
PERF_FILE = "performance.csv"
BONUS_FILE = "bonus_report.csv"


# ================= INITIAL SETUP =================
def initialize_files():
    # Create files with headers if not exist
    if not os.path.exists(EMP_FILE):
        with open(EMP_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Role", "Salary"])

    if not os.path.exists(PERF_FILE):
        with open(PERF_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Attendance", "Task", "Project", "Feedback", "Score"])

    if not os.path.exists(BONUS_FILE):
        with open(BONUS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Score", "Bonus"])


# ================= EMPLOYEE MODULE =================
def add_employee():
    try:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        role = input("Enter Role: ")
        salary = float(input("Enter Salary: "))

        with open(EMP_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([emp_id, name, dept, role, salary])

        print("✅ Employee added successfully!")

    except:
        print("❌ Invalid input!")


def view_employees():
    try:
        with open(EMP_FILE, "r") as f:
            reader = csv.reader(f)
            print("\n--- Employee List ---")
            for row in reader:
                print(row)
    except:
        print("❌ Error reading file!")


# ================= PERFORMANCE MODULE =================
def add_performance():
    try:
        emp_id = input("Enter Employee ID: ")

        attendance = int(input("Attendance (0-100): "))
        task = int(input("Task (0-100): "))
        project = int(input("Project (0-100): "))
        feedback = int(input("Feedback (0-100): "))

        if not all(0 <= x <= 100 for x in [attendance, task, project, feedback]):
            print("❌ Scores must be between 0 and 100!")
            return

        score = round((attendance * 0.2 +
                       task * 0.3 +
                       project * 0.3 +
                       feedback * 0.2), 2)

        with open(PERF_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([emp_id, attendance, task, project, feedback, score])

        print(f"✅ Performance added! Score = {score}")

    except:
        print("❌ Invalid input!")


# ================= BONUS MODULE =================
def calculate_bonus():
    try:
        with open(EMP_FILE, "r") as ef, open(PERF_FILE, "r") as pf:
            emp_data = list(csv.reader(ef))[1:]  # skip header
            perf_data = list(csv.reader(pf))[1:]

        with open(BONUS_FILE, "w", newline="") as bf:
            writer = csv.writer(bf)
            writer.writerow(["ID", "Name", "Score", "Bonus"])

            for p in perf_data:
                emp_id = p[0]
                score = float(p[5])

                for e in emp_data:
                    if e[0] == emp_id:
                        salary = float(e[4])

                        if score >= 85:
                            bonus = salary * 0.2
                        elif score >= 70:
                            bonus = salary * 0.1
                        elif score >= 50:
                            bonus = salary * 0.05
                        else:
                            bonus = 0

                        writer.writerow([emp_id, e[1], score, round(bonus, 2)])

        print("✅ Bonus calculated successfully!")

    except:
        print("❌ Error calculating bonus!")


# ================= ANALYTICS MODULE =================
def show_analytics():
    scores = []

    try:
        with open(PERF_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                scores.append(float(row[5]))

        if len(scores) == 0:
            print("❌ No performance data!")
            return

        plt.figure()
        plt.bar(range(len(scores)), scores)
        plt.title("Employee Performance Scores")
        plt.xlabel("Employees")
        plt.ylabel("Score")
        plt.show()

    except:
        print("❌ Error generating graph!")


# ================= MAIN MENU =================
def menu():
    while True:
        print("\n===== SMART EMPLOYEE SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Add Performance")
        print("4. Calculate Bonus")
        print("5. Show Analytics")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            add_performance()
        elif choice == '4':
            calculate_bonus()
        elif choice == '5':
            show_analytics()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


# ================= RUN =================
initialize_files()
menu()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
