import datetime
import json

to_do_list = []

def load_list():
    try:
        with open("to_do_list.json", "r") as file:
            data = json.load(file)
            for item in data:
                due_datetime = datetime.datetime.strptime(item["due_datetime"], "%Y-%m-%d %H:%M:%S.%f")
                to_do_list.append({"task": item["task"], "due_datetime": due_datetime})
    except:
        print("No previous list found.")

def save_list():
    data = []
    for item in to_do_list:
        data.append({"task": item["task"], "due_datetime": item["due_datetime"].strftime("%Y-%m-%d %H:%M:%S.%f")})
    with open("to_do_list.json", "w") as file:
        json.dump(data, file)

def add_to_list():
    todo = input("Input new task: ")
    due_date = input("Input due date (MM-DD): ")
    due_time = input("Input due time (HH:MM): ")
    current_year = datetime.datetime.now().year
    due_datetime = datetime.datetime.strptime(str(current_year) + '-' + due_date + ' ' + due_time, "%Y-%m-%d %H:%M")
    to_do_list.append({"task": todo, "due_datetime": due_datetime})

def display_items(todo_list):
    if todo_list == []:
        print("\n\nThere are currently no tasks.\n\n")
    todo_list.sort(key=lambda x: x["due_datetime"])
    for i, item in enumerate(todo_list):
        print(f"{i+1}. {item['task']} - Due: {item['due_datetime'].strftime('%Y-%m-%d %H:%M')}")

def edit_item(todo_list):
    item_num = int(input("Input the number of the item you would like to change: "))
    change = input("Input new task: ")
    due_date = input("Input new due date (MM-DD): ")
    due_time = input("Input new due time (HH:MM): ")
    current_year = datetime.datetime.now().year
    due_datetime = datetime.datetime.strptime(str(current_year) + '-' + due_date + ' ' + due_time, "%Y-%m-%d %H:%M")
    todo_list[item_num-1]['task'] = change
    todo_list[item_num-1]['due_datetime'] = due_datetime

def delete_item(todo_list):
    item_num = int(input("Input the number of the item you would like to delete: "))
    todo_list.pop(item_num-1)
    display_items(to_do_list)


def mark_as_complete(todo_list):
    item_num = int(input("Input the number of the item you would like to mark as complete: "))
    todo_list[item_num-1] += ' |0|'
    display_items(to_do_list)

# load the to-do list when the program starts
load_list()
print("\nWelcome to your To-Do List!")
while True:

    print("Select an option:")
    print("1. Display items in the list")
    print("2. Add an item to the list")
    print("3. Edit an item in the list")
    print("4. Delete an item from the list")
    print("5. Mark items as complete")
    print("6. Exit the program")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        display_items(to_do_list)
    elif choice == 2:
        add_to_list()
    elif choice == 3:
        edit_item(to_do_list)
    elif choice == 4:
        delete_item(to_do_list)
    elif choice == 5:
        mark_as_complete(to_do_list)
    elif choice == 6:
        print("Exiting program...")
        save_list()
        import time
        time.sleep(2)
        print("\n"*4)
        break
    else:
        print("Invalid choice. Please try again.")

