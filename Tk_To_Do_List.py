import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_task():
    task = entry_task.get()
    time = entry_time.get()
    if task:
        if time:
            task_with_time = f"{time} - {task}"
        else:
            task_with_time = task
        listbox_pending.insert(tk.END, task_with_time)
        entry_task.delete(0, tk.END)
        entry_time.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task(listbox):
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_completed_tasks():
    listbox_completed.delete(0, tk.END)

def toggle_completed_task():
    try:
        selected_task_index = listbox_pending.curselection()[0]
        task_text = listbox_pending.get(selected_task_index)
        listbox_pending.delete(selected_task_index)
        listbox_completed.insert(tk.END, f"✓ {task_text}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def main():
    global entry_task, entry_time, listbox_pending, listbox_completed

    root = tk.Tk()
    root.title("task1 TO-DO List")


    root.tk_setPalette(background='#e6e6e6', foreground='#333333')


    entry_task = tk.Entry(root, width=40, font=('Helvetica', 12), bd=5)
    entry_task.insert(0, "Add task")
    entry_task.bind("<FocusIn>", lambda event: entry_task.delete(0, tk.END)) 
    entry_task.bind("<FocusOut>", lambda event: entry_task.insert(0, "Add task") if not entry_task.get() else None) 
    entry_task.pack(pady=10)

    
    entry_time = tk.Entry(root, width=40, font=('Helvetica', 12), bd=5)
    entry_time.insert(0, "Add time")
    entry_time.bind("<FocusIn>", lambda event: entry_time.delete(0, tk.END)) 
    entry_time.bind("<FocusOut>", lambda event: entry_time.insert(0, "Add time") if not entry_time.get() else None)  
    entry_time.pack(pady=5)

    btn_add = tk.Button(root, text="ADD TASK", width=20, command=add_task, bg='#262626', fg='white')
    btn_add.pack(pady=5)
    middle_label = tk.Label(root, text="Pending Tasks", font=('Times', 14, 'bold underline'), fg='#000000')
    middle_label.pack(pady=0)

    listbox_pending = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=5, font=('Helvetica', 12), bd=5, bg='#d9d9d9')
    listbox_pending.pack(pady=10)

    btn_delete_pending = tk.Button(root, text="DELETE PENDING TASK", width=20, command=lambda: delete_task(listbox_pending), bg='#262626', fg='white')
    btn_delete_pending.pack(pady=5)

    btn_toggle_completed = tk.Button(root, text="MARK COMPLETED", width=20, command=toggle_completed_task, bg='#262626', fg='white')
    btn_toggle_completed.pack(pady=3)

    middle_label = tk.Label(root, text="Completed Tasks", font=('Times', 14, 'bold underline'), fg='#000000')
    middle_label.pack(pady=0)
    
    listbox_completed = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=5, font=('Helvetica', 12), bd=5, bg='#a9a9a9')
    listbox_completed.pack(pady=10)


    btn_delete_completed = tk.Button(root, text="DELETE COMPLETED TASK", width=20, command=lambda: delete_task(listbox_completed), bg='#262626', fg='white')
    btn_delete_completed.pack(pady=3)

    
    # Clear Completed Tasks button
    # btn_clear_completed = tk.Button(root, text="Clear Completed", width=20, command=clear_completed_tasks, bg='#262626', fg='white')
    # btn_clear_completed.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()





