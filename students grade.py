def get_letter_grade(average):
    """Determine the letter grade based on average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(average):
    """Calculate GPA based on average score."""
    return round(average / 20, 2)  # Simple conversion for demonstration

def main():
    print("Welcome to the Student Grade Tracker!")
    
    grades = {}
    
    while True:
        subject = input("Enter the subject (or 'exit' to finish): ").strip()
        if subject.lower() == 'exit':
            break
        
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if 0 <= grade <= 100:
                grades[subject] = grade
            else:
                print("Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if grades:
        average = sum(grades.values()) / len(grades)
        letter_grade = get_letter_grade(average)
        gpa = calculate_gpa(average)

        print("\n--- Grade Summary ---")
        print(f"Subjects and Grades: {grades}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa}")

    else:
        print("No grades were entered.")

    print("Thank you for using the Student Grade Tracker!")

if __name__ == "__main__":
    main()
