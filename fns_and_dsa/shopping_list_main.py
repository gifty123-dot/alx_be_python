from shopping_list_manager import display_menu, add, remove_1,display
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            Item = input("What Items Are You Adding To Your Shopping List Today?")
            add(shopping_list, Item)
        elif choice == '2':
            Item = input("So sad to see you won't be purchasing these items")
            remove_1(shopping_list, Item)
        elif choice == '3':
            print("I am glad to display your shopping list")
            display(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()