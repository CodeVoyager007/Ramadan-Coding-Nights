import json
import os
from datetime import datetime
import colorama
from colorama import Fore, Style

# Initialize colorama for Windows compatibility
colorama.init()

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{Fore.CYAN}╔══════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║      📝 Todo List Manager        ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════╝{Style.RESET_ALL}")

def display_menu():
    print("\n📋 Main Menu:")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Add Task")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} View Tasks")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Complete Task")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Remove Task")
    print(f"{Fore.GREEN}5.{Style.RESET_ALL} Exit")

def add_task():
    print_header()
    print(f"\n{Fore.YELLOW}=== Add New Task ==={Style.RESET_ALL}")
    
    # Get task description
    task = input(f"\n📌 Enter task description: ").strip()
    if not task:
        print(f"{Fore.RED}Task cannot be empty!{Style.RESET_ALL}")
        input("\nPress Enter to continue...")
        return

    # Get priority
    print(f"\n{Fore.CYAN}Priority Levels:{Style.RESET_ALL}")
    print("1. High 🔴")
    print("2. Medium 🟡")
    print("3. Low 🟢")
    
    while True:
        try:
            priority_choice = int(input("\nSelect priority (1-3): "))
            if 1 <= priority_choice <= 3:
                priority = ["High", "Medium", "Low"][priority_choice - 1]
                break
        except ValueError:
            pass
        print(f"{Fore.RED}Please enter a valid number (1-3){Style.RESET_ALL}")

    # Get due date
    due_date = ""
    if input("\nAdd due date? (y/n): ").lower().startswith('y'):
        while True:
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                break
            except ValueError:
                print(f"{Fore.RED}Please enter a valid date format (YYYY-MM-DD){Style.RESET_ALL}")

    tasks = load_tasks()
    new_task = {
        "task": task,
        "done": False,
        "priority": priority,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    
    print(f"\n{Fore.GREEN}✨ Task added successfully!{Style.RESET_ALL}")
    input("\nPress Enter to continue...")

def view_tasks():
    print_header()
    tasks = load_tasks()
    
    if not tasks:
        print(f"\n{Fore.YELLOW}No tasks found! Add some tasks to get started.{Style.RESET_ALL}")
        input("\nPress Enter to continue...")
        return

    pending = [t for t in tasks if not t.get('done', False)]
    completed = [t for t in tasks if t.get('done', False)]

    if pending:
        print(f"\n{Fore.YELLOW}📋 Pending Tasks:{Style.RESET_ALL}")
        for idx, task in enumerate(pending, 1):
            priority_colors = {
                'High': Fore.RED,
                'Medium': Fore.YELLOW,
                'Low': Fore.GREEN
            }
            priority_icons = {
                'High': '🔴',
                'Medium': '🟡',
                'Low': '🟢'
            }
            
            print(f"\n{idx}. {task['task']}")
            # Only show priority if it exists
            if 'priority' in task:
                priority = task['priority']
                print(f"   {priority_colors.get(priority, Fore.WHITE)}"
                      f"{priority_icons.get(priority, '⚪')} "
                      f"Priority: {priority}{Style.RESET_ALL}")
            if task.get('due_date'):
                print(f"   📅 Due: {task['due_date']}")

    if completed:
        print(f"\n{Fore.GREEN}✅ Completed Tasks:{Style.RESET_ALL}")
        for idx, task in enumerate(completed, 1):
            print(f"{idx}. {task['task']}")

    input("\nPress Enter to continue...")

def complete_task():
    print_header()
    tasks = load_tasks()
    pending = [t for t in tasks if not t['done']]

    if not pending:
        print(f"\n{Fore.YELLOW}No pending tasks!{Style.RESET_ALL}")
        input("\nPress Enter to continue...")
        return

    print(f"\n{Fore.YELLOW}Select task to complete:{Style.RESET_ALL}")
    for idx, task in enumerate(pending, 1):
        print(f"{idx}. {task['task']}")

    try:
        choice = int(input("\nEnter task number: "))
        if 1 <= choice <= len(pending):
            task_idx = tasks.index(pending[choice - 1])
            tasks[task_idx]['done'] = True
        else:
            print(f"{Fore.RED}Invalid task number!{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
    
    save_tasks(tasks)
    print(f"\n{Fore.GREEN}✓ Task marked as complete!{Style.RESET_ALL}")
    input("\nPress Enter to continue...")

def remove_task():
    print_header()
    tasks = load_tasks()

    if not tasks:
        print(f"\n{Fore.YELLOW}No tasks to remove!{Style.RESET_ALL}")
        input("\nPress Enter to continue...")
        return

    print(f"\n{Fore.YELLOW}Select task to remove:{Style.RESET_ALL}")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task.get('done', False) else "⏳"
        print(f"{idx}. {status} {task['task']}")

    try:
        choice = int(input("\nEnter task number: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"\n{Fore.GREEN}🗑️ Task removed: {removed['task']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid task number!{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
    
    input("\nPress Enter to continue...")

def main():
    while True:
        print_header()
        display_menu()
        
        choice = input(f"\n{Fore.CYAN}Enter your choice (1-5): {Style.RESET_ALL}")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print(f"\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()