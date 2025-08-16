import csv
import json
import os


students = []
DATA_FILE = os.path.join(os.path.dirname(__file__), "../data.json")

def load_data():
    global students
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                students = json.load(f)
            except json.JSONDecodeError:
                students = []
    else:
        students = []

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# simple in-memory storage


def export_to_csv(filename="students.csv"):
    if not students:
        print("⚠️ No students available to export.")
        return

    fieldnames = ["id", "roll", "name", "age", "course", "year", "email", "phone"]

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print(f"✅ Data exported successfully to {filename}")

def add_student():
    student = {
        "id": input("Enter the id:"),
        "roll": input("Enter roll number: "),
        "name": input("Enter student name: "),
        "age": input("Enter student age: "),
        "course": input("Enter student course: "),
        "year": input("Enter student year: "),
        "email": input("Enter student email: "),
        "phone": input("Enter student phone: ")
    }
    students.append(student)
    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("⚠️ No students available.")
        return

    print("\n===== Student List =====")
    print("{:<5} {:<15} {:<5} {:<10} {:<6} {:<20} {:<12}".format(
        "ID", "Name", "Age", "Course", "Year", "Email", "Phone"
    ))
    print("-" * 90)
    for s in students:
        print("{:<5} {:<15} {:<5} {:<10} {:<6} {:<20} {:<12}".format(
            s.get("id", "-"),
            s.get("name", "-"),
            s.get("age", "-"),
            s.get("course", "-"),
            s.get("year", "-"),
            s.get("email", "-"),
            s.get("phone", "-")
        ))

def clear_all_students():
    global students
    students = []  # clear in memory
    save_data()    # also clear file
    print("✅ All student records have been cleared!")
def search_student():
    roll = input("🔍 Enter student ID to search: ")
    found = False
    for s in students:
        if s["id"] == roll:
            print("\n✅ Student Found:")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Course: {s['course']}")
            print(f"Year: {s['year']}")
            print(f"Email: {s['email']}")
            print(f"Phone: {s['phone']}")
            found = True
            break
    if not found:
        print("❌ Student not found!")

def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print(f"🗑️ Student {s['name']} deleted.")
            return
    print("⚠️ Student not found.")

def update_student():
    roll = input("Enter roll number to update: ").strip()
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ").strip() or s["name"]
            s["age"] = input("Enter new age: ").strip() or s["age"]
            s["course"] = input("Enter new course: ").strip() or s["course"]
            s["year"] = input("Enter new year: ").strip() or s["year"]
            s["email"] = input("Enter new email: ").strip() or s["email"]
            s["phone"] = input("Enter new phone: ").strip() or s["phone"]
            print(f"✅ Student with roll {roll} updated.")
            return
    print("⚠️ Student not found.")



def import_from_csv(filename="students.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            
            # check if required columns exist
            required_fields = {"id", "roll", "name", "age", "course", "year", "email", "phone"}
            if not required_fields.issubset(reader.fieldnames):
                print(f"⚠️ CSV file missing required fields! Found: {reader.fieldnames}")
                return

            students.clear()
            for row in reader:
                try:
                    students.append({
                        "id": int(row.get("id", 0)),
                        "roll": row.get("roll", ""),
                        "name": row.get("name", ""),
                        "age": int(row.get("age", 0)),
                        "course": row.get("course", ""),
                        "year": int(row.get("year", 0)),
                        "email": row.get("email", ""),
                        "phone": row.get("phone", "")
                    })
                except ValueError:
                    print(f"⚠️ Skipping bad row: {row}")
            
        print(f"✅ Data imported successfully from {filename}")

    except FileNotFoundError:
        print("⚠️ File not found.")


def student_stats():
    total_students = len(students)
    print(f"\n📊 Total Students: {total_students}")

    # Count by course
    course_counts = {}
    for s in students:
        course_counts[s["course"]] = course_counts.get(s["course"], 0) + 1

    print("\n📚 Students by Course:")
    for course, count in course_counts.items():
        print(f"   {course}: {count}")

    # Count by year
    year_counts = {}
    for s in students:
        year_counts[s["year"]] = year_counts.get(s["year"], 0) + 1

    print("\n🎓 Students by Year:")
    for year, count in year_counts.items():
        print(f"   Year {year}: {count}")
