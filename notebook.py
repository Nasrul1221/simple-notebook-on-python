import tkinter as tk
from tkinter import ttk

def create_file(filename):
    with open(filename, 'w') as f:
        f.write('')
    label0.grid(row=0, column=0, columnspan=2)
    label0.config(text='File created!')

def open_file(filename):
    """Main function for notebook creation, this function does something that depends on that you click"""
    try:
        with open(filename, 'r+') as f:
            pass
    except FileNotFoundError:
        label0.grid(row=0, column=0, columnspan=2)
        label0.config(text='File is not exists!')
    else:
        entry0.grid_forget()

        entry0.grid(row=2, column=0, columnspan=2)
        label0.grid(row=0, column=0, columnspan=2)

        btn_enter1.grid_forget()
        btn_enter2.grid(row=3, column=0, columnspan=2)

        label0.config(text='File was opened! \nEnter you want and choose(add or remove).')
        btn_enter2.grid_forget()

        #Button add
        entry0.grid(row=2, column=0, columnspan=2)
        btn_add = tk.ttk.Button(frm, text='Add', command=lambda: adding_to(filename, entry0.get()))
        btn_add.grid(row=3, column=0)

        #Button remove
        entry0.grid_forget()
        entry0.grid(row=2, column=0, columnspan=2)
        btn_remove = tk.ttk.Button(frm, text='Remove', command=lambda: remove_from(filename, entry0.get()))
        btn_remove.grid(row=3, column=1)


#Function for adding to notebook
def adding_to(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')
# Function for removing from notebook
def remove_from(filename, text):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(text, '')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    label0.config(text='I was deleted!')

#
def entry_creating0():
    btn_enter1.grid_forget()
    entry0.grid_forget()

    entry0.grid(row=2, column=0, columnspan=2)
    btn_enter0.grid(row=3, column=0, columnspan=2)

def entry_creating1():
    btn_enter0.grid_forget()
    entry0.grid_forget()

    entry0.grid(row=2, column=0, columnspan=2)
    btn_enter1.grid(row=3, column=0, columnspan=2)

#Window
window = tk.Tk()
window.title("Your magic notebook")

#Frame
frm = tk.Frame()
frm.grid()

#Style
style = tk.ttk.Style()
style.configure('Custom.TButton', font='Georgia 12')


#Buttons
btn0 = tk.ttk.Button(frm, text='Create files', command=entry_creating0, style='Custom.TButton').grid(row=1, column=0)
btn1 = tk.ttk.Button(frm, text='Open files', command=entry_creating1, style='Custom.TButton').grid(row=1, column=1)
btn_enter0 = tk.ttk.Button(frm, text='Enter', command=lambda: create_file(entry0.get()), style='Custom.TButton')
btn_enter1 = tk.ttk.Button(frm, text='Enter', command=lambda: open_file(entry0.get()), style='Custom.TButton')
btn_enter2 = tk.ttk.Button(frm, text='Enter', command=None, style='Custom.TButton')

#Entry strings
entry0 = tk.Entry(frm, width=34, highlightthickness='2', highlightcolor='gray')

#Label
label0 = tk.Label(frm)
label1 = tk.Label(frm)

window.mainloop()