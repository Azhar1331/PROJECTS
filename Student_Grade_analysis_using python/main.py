import csv
import numpy as np
import os
import sys

# Set a high recursion limit if needed for deep operations, though not critical here
# sys.setrecursionlimit(2000) 

class GradeBook:
    """
    Manages student records, allows for adding students, calculating averages
    using NumPy, and saving/loading data via CSV.
    """
    def __init__(self, filename='grades_data.csv'):
        self.filename = filename
        self.students = [] # List of dictionaries: [{'id': 1, 'name': 'Alice', 'scores': [88.0, 92.0]}, ...]
        self._load_data()

    def _load_data(self):
        """Loads student data from the CSV file on initialization."""
        if not os.path.exists(self.filename):
            print("INFO: Data file not found. Starting with an empty GradeBook.")
            return

        with open(self.filename, mode='r', newline='') as file:
            # Use DictReader to read rows as dictionaries with header names as keys
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    # Scores are saved as a string (e.g., '[88.0, 92.0]'); we need to parse it back into a list of floats.
                    # We strip the brackets and split by comma.
                    scores_str = row['scores'].strip("[]")
                    # Use a generator expression/list comprehension to convert each score element to a float
                    scores = [float(s.strip()) for s in scores_str.split(',') if s.strip()]

                    # Convert ID back to an integer
                    student_id = int(row['id'])

                    # Reconstruct the student dictionary
                    self.students.append({
                        'id': student_id,
                        'name': row['name'],
                        'scores': scores
                    })
                except Exception as e:
                    print(f"WARNING: Could not process row: {row}. Error: {e}")

        print(f"INFO: Loaded {len(self.students)} student records.")

    def add_student(self, name, student_id, scores_list):
        """Adds a new student record to the in-memory list."""
        
        # 1. Input validation for scores
        try:
            # Attempt to convert all input scores to floats
            valid_scores = [float(s) for s in scores_list]
        except ValueError:
            print("ERROR: Scores must be numerical values (e.g., '88, 92.5').")
            return
        
        # 2. Check for duplicate ID
        if any(s['id'] == student_id for s in self.students):
            print(f"ERROR: Student with ID {student_id} already exists. Cannot add.")
            return

        # 3. Add to the list
        self.students.append({
            'id': student_id,
            'name': name,
            'scores': valid_scores
        })
        print(f"SUCCESS: Student {name} added.")

    def _calculate_average(self, scores_list):
        """Private helper to calculate average using NumPy."""
        if not scores_list:
            return 0.0
        
        # Convert Python list to NumPy array for calculation
        scores_array = np.array(scores_list)
        return np.mean(scores_array)

    def display_summary(self):
        """Displays a formatted summary table of all students, including NumPy-calculated average and min."""
        print("\n--- Student Grade Summary ---")
        if not self.students:
            print("No students found.")
            return

        # Prepare formatted header
        col_names = ["ID", "Name", "Average", "Min Score"]
        print(f"{col_names[0]:<5} | {col_names[1]:<20} | {col_names[2]:<10} | {col_names[3]:<10}")
        print("-" * 50)
        
        for student in self.students:
            avg = self._calculate_average(student['scores'])
            
            # Use NumPy's min function for minimum score (handle no scores case)
            if student['scores']:
                min_score = np.min(np.array(student['scores']))
            else:
                min_score = 0.0
            
            # Print row with string formatting (f-string)
            print(f"{student['id']:<5} | {student['name']:<20} | {avg:<10.2f} | {min_score:<10.2f}")

    def find_top_student(self):
        """Finds the student with the highest average score."""
        if not self.students:
            print("No students to analyze.")
            return
            
        highest_avg = -1.0
        top_student = None

        for student in self.students:
            current_avg = self._calculate_average(student['scores'])
            
            if current_avg > highest_avg:
                highest_avg = current_avg
                top_student = student['name']

        if top_student:
            print(f"\n🥇 Top Student: {top_student} with an average of {highest_avg:.2f}")
        else:
            print("Could not determine top student.")

    def save_data(self):
        """Saves all current student records to the CSV file."""
        # Define fieldnames to match the dictionary keys
        fieldnames = ['id', 'name', 'scores']
        
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in self.students:
                # Prepare row for CSV: convert the list of scores back to a string for saving
                row_to_write = {
                    'id': student['id'],
                    'name': student['name'],
                    # Use str() to save the list [88.0, 92.0] as a parsable string
                    'scores': str(student['scores'])
                }
                writer.writerow(row_to_write)
                
        print(f"SUCCESS: All {len(self.students)} records saved to {self.filename}.")

def print_menu():
    """Displays the main CLI menu options."""
    print("\n--- Grade Book Menu ---")
    print("1. Add Student")
    print("2. Display Summary")
    print("3. Find Top Student")
    print("4. Save and Exit")
    print("------------------------")

def main():
    """The main application loop."""
    # Initialize the GradeBook, which automatically attempts to load existing data
    book = GradeBook()

    while True:
        print_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            name = input("Enter student name: ").strip()
            
            # Get Student ID input with error handling
            try:
                student_id = int(input("Enter student ID (e.g., 101): ").strip())
            except ValueError:
                print("ERROR: Invalid ID. ID must be an integer.")
                continue

            # Get scores input
            scores_input = input("Enter scores (e.g., 88, 92.5, 78): ").strip()
            # Convert input string into a list of score strings
            scores_list = [s.strip() for s in scores_input.split(',')]
            
            book.add_student(name, student_id, scores_list)

        elif choice == '2':
            book.display_summary()

        elif choice == '3':
            book.find_top_student()
            
        elif choice == '4':
            book.save_data()
            print("Exiting GradeBook. Goodbye! 👋")
            break
            
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()