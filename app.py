from datetime import datetime

def calculate_age():
    try:
        # Get user input for date of birth
        dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
        
        # Convert input to a date object
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        
        # Get today's date
        today = datetime.today()
        
        # Calculate age
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day
        
        # Adjust if the current date is before the birth date in the year
        if age_months < 0 or (age_months == 0 and age_days < 0):
            age_years -= 1
            age_months += 12
        
        if age_days < 0:
            # Get the number of days in the previous month
            previous_month = (today.month - 1) if today.month > 1 else 12
            previous_month_year = today.year if today.month > 1 else today.year - 1
            days_in_prev_month = (datetime(previous_month_year, previous_month + 1, 1) - 
                                  datetime(previous_month_year, previous_month, 1)).days
            age_days += days_in_prev_month
        
        print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Run the function
calculate_age()
