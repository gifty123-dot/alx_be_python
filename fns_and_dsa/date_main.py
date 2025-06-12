from explore_datetime import display_current_datetime, calculate_future_date

def main():
    display_current_datetime()
    userDate=int(input("Enter The future Days you want calculated:"))
    calculate_future_date(userDate)

if __name__ == "__main__":
    main()
