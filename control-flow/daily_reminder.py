Task = input("Enter your task")
Time_Bound = input("Is it time-bound? (yes/no) ")
Priority = input("Priority (high/medium/low)")

match Priority.lower():
    case "high":
        if time.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Reminder: High priority task but not time bound")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print("Priority not recognized.")
