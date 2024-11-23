# 1. Name:
#      \Michael Johnson
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program calculates the number of days between two valid dates using the provided start and end dates.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was ensuring the iterative logic properly handled transitions between months and years, 
#      particularly accounting for leap years and February's varying number of days. Debugging edge cases 
#      (e.g., start and end dates within the same month or year) was also challenging.
# 5. How long did it take for you to complete the assignment?
#      Approximately 5 hours, including debugging, validation, and testing edge cases, along with recording/editing video.


def is_leap_year(year):
    """Determine if a year is a leap year."""
    assert year >= 1753, "Year must be 1753 or later."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    """Return the number of days in a given month of a given year."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]

def validate_date(year, month, day):
    """Validate if the given year, month, and day form a valid date."""
    if year < 1753:
        raise ValueError("Year must be 1753 or later.")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1 <= day <= get_days_in_month(month, year)):
        raise ValueError(f"Day must be between 1 and {get_days_in_month(month, year)}.")

def calculate_days(start_year, start_month, start_day, end_year, end_month, end_day):
    """Calculate the total number of days between two valid dates."""
    total_days = 0
    current_day = start_day
    current_month = start_month
    current_year = start_year

    while (current_year < end_year or
           current_month < end_month or
           (current_month == end_month and current_day < end_day)):
        days_in_current_month = get_days_in_month(current_month, current_year)
        
        if current_year == end_year and current_month == end_month:
            total_days += end_day - current_day
            break
        else:
            total_days += days_in_current_month - current_day
            current_day = 0
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1

    return total_days

def get_input(prompt):
    """Prompt the user for an integer input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Enter the start date:")
    while True:
        try:
            start_year = get_input("Start year (YYYY): ")
            start_month = get_input("Start month (MM): ")
            start_day = get_input("Start day (DD): ")
            validate_date(start_year, start_month, start_day)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    print("\nEnter the end date:")
    while True:
        try:
            end_year = get_input("End year (YYYY): ")
            end_month = get_input("End month (MM): ")
            end_day = get_input("End day (DD): ")
            validate_date(end_year, end_month, end_day)
            if (end_year, end_month, end_day) < (start_year, start_month, start_day):
                raise ValueError("End date must be after start date.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    total_days = calculate_days(start_year, start_month, start_day, end_year, end_month, end_day)
    print(f"\nThe number of days between the dates is: {total_days}")

if __name__ == "__main__":
    main()