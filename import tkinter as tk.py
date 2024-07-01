import tkinter as tk
import tkinter.messagebox
import pickle

root = tk.Tk()
root.title("TO DO LIST")
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tk.END,task)
        entry_task.delete(0,tk.END)
    else:
        tkinter.messagebox.showwarning(title="OOPS",message="You must enter a task")
def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showerror(title="OOPS", message="Nothing seclected to delete")


def load_task():
    task = pickle.load(open("task.dat","rb"))
    for task in task:
        listbox_task.insert(tk.END,task)
        
    
def save_task():
    task = listbox_task.get(0,listbox_task.size())
    pickle.dump(task,open("task.dat","wb"))
    
frame_task = tk.Frame(root)
frame_task.pack()

listbox_task = tk.Listbox(frame_task, height=10,width=50)
listbox_task.pack(side='left')

scrollbar = tk.Scrollbar(frame_task)
scrollbar.pack(side= "right",fill="y" )
listbox_task.config(yscrollcommand= scrollbar.set)
scrollbar.config(command=listbox_task.yview)
entry_task = tk.Entry(root,width=50)
entry_task.pack()

button_add_task = tk.Button(root,text="Add task",width=48,command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root,text="Delete task",width=48,command=delete_task)
button_delete_task.pack()


button_load_task = tk.Button(root,text="Load task",width=48,command=load_task)
button_load_task.pack()

button_save_task = tk.Button(root,text="Save task",width=48,command=save_task)
button_save_task.pack()


root.mainloop()