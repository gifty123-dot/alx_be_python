shopping_list =[]
def add(shopping_list, item):
    shopping_list.append(item)
    print(shopping_list)
def remove_1(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' was removed")
    else:
        print(f"'{item}' not in list")
def display(shopping_list):
    if not shopping_list:
        print("Shopping List is empty")
    else:
        print("The Items in your shopping lists are:")
        for items in shopping_list:
            print("-", items)
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")