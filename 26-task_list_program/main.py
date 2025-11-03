"""with open(file="tasks.txt", mode="w") as data_task:
    data_task.write("test")"""

# ADD TASK
def add_task(user_task):
    # Open the file in append mode and add the new task with a newline
    with open(file="tasks.txt", mode="a") as data_task:
        data_task.write(f"{user_task}\n")

# LIST TASKS
def list_task():
    # Print an empty line before listing
    print("\n")
    # Open the file in read mode and enumerate the tasks
    with open(file="tasks.txt", mode="r") as data_task:
        for index, task in enumerate(data_task):
            # Print the task with numbering, stripping the newline character
            print(f"{index+1} - {task.strip()}")
    # Print an empty line after listing
    print("\n")

# REMOVE TASK
def remove(index_to_remove):
    # Load the file into a list of lines
    with open(file="tasks.txt", mode="r") as data_task:
        linhas = data_task.readlines()
        # Check if the task number is valid
        if 1 <= index_to_remove <= len(linhas):
            # Remove the task from the list
            del linhas[index_to_remove-1]
            print(f"Task '{index_to_remove}' removed successfully!")
        else:
            print("Invalid task number")

    # Overwrite the file with the updated list of tasks
    with open(file="tasks.txt", mode="w") as data_task:
        for updated_tasks in linhas:
            data_task.write(updated_tasks)

# Welcome message
def print_header():
    print(r"""
 ____            _        _     _     _     
|  _ \ ___  __ _| |_ __ _| |__ | |__ (_)___ 
| |_) / _ \/ _` | __/ _` | '_ \| '_ \| / __|
|  _ <  __/ (_| | || (_| | | | | | | | \__ \
|_| \_\___|\__,_|\__\__,_|_| |_|_| |_|_|___/

     Welcome to Your Task Manager!
""")


print_header()

# MAIN LOOP
game_on = True
while game_on:
    # Ask user for option
    print("\nOptions:")
    user_option = input("Type 'a' to ADD\n"
                        "Type 'l' to LIST\n"
                        "Type 'r' to REMOVE\n"
                        "Type 's' to Exit\n"
                        "Your choice: ").lower()

    if user_option == "a":
        user_task = str(input("Write down your new task: "))
        add_task(user_task)
    elif user_option == "l":
        list_task()
    elif user_option == "r":
        user_task = int(input("Type the task number to remove: "))
        remove(user_task)
