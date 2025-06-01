task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

priority = priority.lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task but not time-bound.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print("Priority not recognized.")