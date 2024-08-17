class Task: 
    def __init__(self, name, description, category, priority, status=None):
        self.name = name 
        self.description = description 
        self.category = category 
        self.priority = priority 
        self.status = status
        
    def __str__(self): 
        return (f"Name: {self.name} \n"
                f"Description: {self.description} \n"
                f"Category: {self.category} \n"
                f"Priority: {self.priority} \n" 
                f"Status: {self.status}") 
           
    def update_status(self, new_status): 
        if new_status in ["to-do", "done", "canceled"]: 
            self.status = new_status
        else: 
            print("Invalid status. Only choose from 'to-do', 'done', or 'canceled'.")

class ToDoList: 
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        name = input("Add task name: ")
        description = input("Add task description: ")
        category = input("Add task category: ")
        priority = input("Add task priority: ")
        status = input("Add task status: ") or None
        task = Task(name, description, category, priority, status)
        self.tasks.append(task) 
        print(f"The task '{name}' has been added successfully.")    

    def view_tasks(self):
        if not self.tasks: 
            print("There's no tasks to display.") 
        else:
            for i, task in enumerate(self.tasks): 
                print(f"\nTask {i+1}:")
                print(task)

    def edit_task(self): 
        self.view_tasks()
        index = int(input("Enter the number of the task you want to edit: ")) - 1 
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            new_name = input("Enter the new name: ") or task.name
            new_description = input("Enter the new description: ") or task.description
            new_category = input("Enter the new category: ") or task.category
            new_priority = input("Enter the new priority: ") or task.priority
            new_status = input("Enter the new status: ") or task.status
        
            task.name = new_name
            task.description = new_description
            task.category = new_category
            task.priority = new_priority
            task.status = new_status
        
            print("Task has been updated successfully.")
        else:
            print("Task doesn't exist.")
    
    def move_task(self):
        self.view_tasks()
        index = int(input("Enter the number of the task you want to update: ")) - 1
        if 0 <= index < len(self.tasks):
            new_status = input("Enter the new status (to-do, done, canceled): ")
            self.tasks[index].update_status(new_status)
        else:
            print("Task doesn't exist.")

    def delete_task(self): 
        self.view_tasks()  
        index = int(input("Enter the number of the task you want to delete: ")) - 1
        if 0 <= index < len(self.tasks): 
            deleted_task = self.tasks.pop(index)
            print(f"The task '{deleted_task.name}' has been deleted successfully.")   
    
    def print_tasks(self, filter_by=None): 
        found = False
        if filter_by:
            print(f"Tasks with '{filter_by}' status or category:")
        else:
            print("All tasks:")
            
        for i, task in enumerate(self.tasks):
            if filter_by and (filter_by == task.status or filter_by == task.category):
                print(f"Task {i+1}: {task.name}")
                found = True 
            elif not filter_by: 
                print(f"Task {i+1}: {task.name}")
                found = True 
            
        if not found: 
            print(f"There are no tasks with the specified status or category.")     

    def sort_tasks(self, by=None, descending=False):
        if by is None:
            by = input("Enter the attribute to sort by (e.g., name, category, priority): ")
        
        if not all(hasattr(task, by) for task in self.tasks):
            print("Invalid attribute for sorting.")    
            return
        
        self.tasks.sort(key=lambda task: getattr(task, by), reverse=descending)

# Main function with a menu-driven interface
def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Move Task")
        print("5. Delete Task")
        print("6. Print Tasks")
        print("7. Print 'Done' Tasks")
        print("8. Print 'Canceled' Tasks")
        print("9. Print Tasks by Category")
        print("10. Sort Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.edit_task()
        elif choice == '4':
            todo_list.move_task()
        elif choice == '5':
            todo_list.delete_task()
        elif choice == '6':
            todo_list.print_tasks()
        elif choice == '7':
            todo_list.print_tasks(filter_by='done')
        elif choice == '8':
            todo_list.print_tasks(filter_by='canceled')
        elif choice == '9':
            category = input("Enter category to filter by: ")
            todo_list.print_tasks(filter_by=category)
        elif choice == '10':
            by = input("Sort by (name, category, priority, status): ")
            order = input("Descending order? (yes/no): ").lower() == 'yes'
            todo_list.sort_tasks(by, order)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
