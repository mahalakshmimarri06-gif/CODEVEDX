import csv
import os
from datetime import datetime # Make sure to add this import at the top of your file


def read_csv(file_path):
    """Reads data from a CSV file with error handling."""
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert salary to integer for calculations
                row['Salary'] = int(row['Salary'])
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except PermissionError:
        print(f"Error: Permission denied for file at {file_path}.")
    return None

def process_data(data, target_dept):
    """Filters data, sorts by name, and calculates average salary."""
    filtered = [emp for emp in data if emp['Department'].lower() == target_dept.lower()]
    if not filtered:
        return None, 0
    
    # Sort the filtered list by 'Name' alphabetically
    filtered.sort(key=lambda x: x['Name'])
    
    avg_salary = sum(emp['Salary'] for emp in filtered) / len(filtered)
    return filtered, avg_salary


def write_report(output_path, dept, employees, avg):
    """Exports results with a timestamp and process summary."""
    with open(output_path, 'w') as f:
        # Header Section
        f.write("=" * 45 + "\n")
        f.write(f"REPORT GENERATED ON: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"DEPARTMENT: {dept.upper()}\n")
        f.write("=" * 45 + "\n")
        
        # Summary Info
        f.write(f"Total Employees Processed: {len(employees)}\n")
        f.write("-" * 45 + "\n")
        
        # Table Headers
        f.write(f"{'Employee Name':<20} | {'Salary':>15}\n")
        f.write("-" * 45 + "\n")
        
        # Data Rows
        for emp in employees:
            f.write(f"{emp['Name']:<20} | ${emp['Salary']:>14,}\n")
            
        # Footer Section
        f.write("=" * 45 + "\n")
        f.write(f"{'Average Salary:':<20} | ${avg:>14,.2f}\n")
        f.write("=" * 45 + "\n")
        
    print(f"Report successfully saved to: {output_path}")

def main():
    input_file = 'data/employees.csv'
    
    
    # Load Data
    data = read_csv(input_file)
    
    if data:
        print("Available Departments: Engineering, Marketing, Sales")
        user_dept = input("Enter the department to generate a report for: ").strip()
        
        # Create a unique filename based on the department
        output_file = f'data/{user_dept}_report.txt'
        
        filtered_data, avg = process_data(data, user_dept)
        
        if filtered_data:
            write_report(output_file, user_dept, filtered_data, avg)
        else:
            print(f"No records found for department: {user_dept}")

if __name__ == "__main__":
    main()