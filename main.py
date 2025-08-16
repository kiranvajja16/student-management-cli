from services.manager import (
    add_student, view_students, search_student, delete_student,
    update_student, student_stats,
    import_from_csv, export_to_csv, load_data, save_data, clear_all_students
)


def menu():
    load_data()  # ✅ load data from file when program starts
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Statistics")
        print("9. Clear All Students")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
            save_data()  # ✅ save whenever data changes
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
            save_data()
        elif choice == "5":
            update_student()
            save_data()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            import_from_csv()
            save_data()
        elif choice == "8":
            student_stats()
        elif choice == "9":
            clear_all_students()
            save_data()
        elif choice == "10":
            save_data()  # ✅ final save before exit
            print("Goodbye 👋")
            break
        else:
            print("⚠️ Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
