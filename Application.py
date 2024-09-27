# import req lib
import tkinter as tk
from tkinter import ttk #importing ttk module fom tkinter library
from tkinter import messagebox
import sqlite3 as sql #for db operations

# defining the functions for application

# functions to add tasks to the list
def insert_task():
    # fetching the task from entry field
    task_entry = task_input.get()
    if not task_entry :
        messagebox.showinfo("Error","Field is Empty!!")
    else:
        task.append(task_entry)
        # using execute() methdo to execute a sql statement
        db_cursor.execute("INSERT INTO todo (task_name) VALUES (?)",(task_entry,))
        update_list()
        task_input.delete(0,'end') 

# updating the task in the listbox
def update_list():
    clear_task_list()
    for task_item in task:
        # using the insert cmmmd to insert task in the list
        task_box.insert('end',task_item)

# deleting task vfrom lst
def remove_task():
    try:
        # getting the selected entry from the list box
        val = task_box.get(task_box.curselection())
        if val in task:
            task.remove(val)
            update_list()
            # using execute for delete query
            db_cursor.execute('DELETE FROM todo WHERE task_name = ?',(val,))
            db_connection.commit()
    except:
        messagebox.showinfo("ERROR","N0 Task Selected for deletion !!")

# function for deleting all tasks
def del_all_tsk():
    msg_box = messagebox.askyesno('Confirm','Delete all tasks?')
    if msg_box:
        while task:
            task.pop()
        db_cursor.execute('DELETE FROM todo')
        update_list()

# Clearing the list
def clear_task_list():
    task_box.delete(0,'end')


# closing the application
def exit_app():
    print(task)
    # uisng the destroy method to close the application
    guiWindow.destroy()


# retrive data from database
def load_task_DB():
    while task:
        task.pop()
    # iterating through the rows in the db table
    for row in db_cursor.execute('SELECT task_name FROM todo'):
        task.append(row[0])



# MAIN GUI WINDOW 
if __name__ =="__main__":
    # Intialization main window
    guiWindow = tk.Tk()
    guiWindow.title("TO-DO List")
    guiWindow.geometry("500x500+700+200")
    guiWindow.resizable(0,0)
    guiWindow.config(bg = "#E6E6FA") #light lavender bg


    # Adding DATABASE
    db_connection = sql.connect('Task_Manager.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS todo (task_name TEXT)")

    # defining empty list
    task = []  


    # adding necessary widgets to the application and applying trigerrs

    # Adding FRAMES
    top_frame = tk.Frame(guiWindow,bg = "#E6E6FA")
    mid_frame = tk.Frame(guiWindow,bg = "#E6E6FA")
    bottom_frame = tk.Frame(guiWindow,bg = "#E6E6FA")

    # using pack() method to place the frames in the application
    top_frame.pack(fill="both")
    mid_frame.pack(side="left",expand=True,fill="both")
    bottom_frame.pack(side="right",expand=True,fill="both")


    # header LABELS
    header_label = ttk.Label(top_frame, text= "My To-Do List",font=("Helvetica", 24), background="#E6E6FA",foreground="#4B0082")
    header_label.pack(pady=20)

    input_label = ttk.Label(mid_frame, text="Add Task: ",font=("Verdana","11","bold"), background="#E6E6FA", foreground="#000000")
    input_label.place(x=20, y=30)

    task_input = ttk.Entry(mid_frame,font=("Verdana","12"),width=18, background="#E6E6FA",foreground="#A52A2A")
    task_input.place(x=20,y=60)

    # ADDING BUTTONS
    add_button = ttk.Button(mid_frame,text="Add Task", width=24, command=insert_task)
    del_button = ttk.Button(mid_frame,text="Delete Task", width=24,command=remove_task)
    del_all_button = ttk.Button(mid_frame,text="Delete All Task", width=24, command=del_all_tsk)
    quite_button = ttk.Button(mid_frame,text="Exit",width=24,command=exit_app)
    # using place method to set the pos of the buttons in the app
    add_button.place(x=20,y=100)
    del_button.place(x=20,y=140)
    del_all_button.place(x=20,y=180)
    quite_button.place(x=20,y=220)

    # LIST BOX to display task
    
    task_box = tk.Listbox(bottom_frame,width=30,height=15,selectmode='single',
                              background="#FFFACD",foreground="#000000",
                              selectbackground="#8B0000",selectforeground="#FFFFFF")
    
    task_box.place(x=20,y=20)


    # loading tasks from db and displaying them
    load_task_DB()
    update_list()

    # Running the GUI loop
    guiWindow.mainloop()

    # establishing the connection with the DB
    db_connection.commit()
    db_cursor.close()


