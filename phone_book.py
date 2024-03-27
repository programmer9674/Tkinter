from tkinter import *
from tkinter import messagebox
import sqlite3


def create_table_if_not_exists(table_name):
    connection = sqlite3.connect('contactList.db')
    cursor = connection.cursor()
    sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
            name varchar (30),
            phone_number varchar (20)
        );
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()


def check_contact(name):
    connection = sqlite3.connect('contactList.db')
    cursor = connection.cursor()
    sql = """
       SELECT * FROM CONTACT WHERE name = ?
    """, (name,)
    cursor.execute(*sql)
    result = [c for c in cursor]  # [(Alex, 928349), (Alex, 273984234)]
    connection.commit()
    connection.close()
    return result


def add_contact():
    name = eName.get()
    number = eNumber.get()
    if name and number:
        eName.delete(0, END)
        eNumber.delete(0, END)
        create_table_if_not_exists("CONTACT")
        if len(check_contact(name)) <= 0:
            connection = sqlite3.connect('contactList.db')
            cursor = connection.cursor()
            sql = """
                INSERT INTO CONTACT (name, phone_number) VALUES (?, ?)
            """, (name, number)
            cursor.execute(*sql)
            connection.commit()
            connection.close()
            messagebox.showinfo("SUCCES", "New Contact added.")
            show_all_contact()
        else:
            messagebox.showinfo("INFO", "Contact Already Exists.")


def delete_contact():
    selected_row = contactList.curselection()  # [1]
    if selected_row:
        name = contactList.get(selected_row[0]).split(":")[0]  # (Alex, 928349)
        connection = sqlite3.connect('contactList.db')
        cursor = connection.cursor()
        sql = """
            DELETE FROM CONTACT WHERE name = ?
        """, (name, )
        cursor.execute(*sql)
        connection.commit()
        connection.close()
        messagebox.showinfo("SUCCES", f"{name} deleted.")
        show_all_contact()


def search_contact():
    name = eName.get()
    if name:
        res = check_contact(name)
        if len(res) > 0:
            messagebox.showinfo("SUCCESS", f'{res[0][0]} : {res[0][1]}')
        else:
            messagebox.showinfo("SUCCESS", 'Not Found :(')


def update_contact():
    name = eName.get()
    number = eNumber.get()
    if name and number:
        eName.delete(0, END)
        eNumber.delete(0, END)
        create_table_if_not_exists("CONTACT")
        if len(check_contact(name)) > 0:
            connection = sqlite3.connect('contactList.db')
            cursor = connection.cursor()
            sql = """
                UPDATE CONTACT SET phone_number=? WHERE name = ?
            """, (number, name)
            cursor.execute(*sql)
            connection.commit()
            connection.close()
            messagebox.showinfo("SUCCES", "contact updated")
            show_all_contact()
        else:
            messagebox.showinfo("INFO", "Contact does not Exist.")


def show_all_contact():
    contactList.delete(0, END)
    connection = sqlite3.connect('contactList.db')
    cursor = connection.cursor()
    sql = """
        SELECT * FROM CONTACT order by name
    """
    cursor.execute(sql)
    [contactList.insert(END, f"{c[0]}:{c[1]}") for c in cursor]
    connection.commit()
    connection.close()


root = Tk()
root.geometry('500x500')
root.title('PhoneBook')
root.resizable(width=False, height=False)

frame1 = Frame(root, width=250, height=500, bg='tomato')
frame1.pack_propagate(0)
frame1.pack(side=LEFT)

frame2 = Frame(root, width=250, height=500, bg='beige')
frame2.grid_propagate(False)
frame2.pack(side=LEFT)

bAdd = Button(frame1, text='Add New Contact', command=add_contact)
bAdd.pack(padx=10, pady=30, expand=True, fill=BOTH)

bDel = Button(frame1, text='Delete Contact', command=delete_contact)
bDel.pack(padx=10, pady=30, expand=True, fill='both')

bSearch = Button(frame1, text='Search Contact', command=search_contact)
bSearch.pack(padx=10, pady=30, expand=True, fill='both')

bUpdate = Button(frame1, text='Update Contact', command=update_contact)
bUpdate.pack(padx=10, pady=30, expand=True, fill='both')

Label(frame2, text="Name: ").grid(row=0, column=0, sticky='w')
eName = Entry(frame2)
eName.grid(row=0, column=1, pady=20)

Label(frame2, text="Number: ").grid(row=1, column=0, sticky='w')
eNumber = Entry(frame2)
eNumber.grid(row=1, column=1, pady=20)

contactList = Listbox(frame2, bg='lightgreen')
contactList.grid(row=2, column=0, columnspan=2,
                 pady=50, padx=10, sticky='nsew')
show_all_contact()
root.mainloop()
