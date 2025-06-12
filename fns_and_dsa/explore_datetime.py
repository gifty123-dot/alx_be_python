from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    future_date = datetime.now().date() + timedelta(days=days)
    print(f"Future date after {days} days: {future_date}")
    return future_date
