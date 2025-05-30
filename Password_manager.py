from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    if len(p_entry.get()) > 0:
        p_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_syms = [choice(symbols) for _ in range(randint(2, 4))]
    password_nums = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_syms + password_nums

    shuffle(password_list)

    password = "".join(password_list)

    p_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- Search Credentials ------------------------------- #

def search_credentials():
    try:
        with open("data.json",mode="r") as file:
            user_data = json.load(file)
            website_name = w_entry.get()
            is_found = False
            for data in user_data:
                try:
                    if str(data).lower() == website_name.lower():
                        messagebox.showinfo(title=website_name,message=f"Email : {user_data[data]["Email"]}\nPassword : {user_data[data]["Password"]}")
                        is_found=True
                        break
                except KeyError:
                    messagebox.showerror(title="Error",message=f"{website_name} not found!")
            if not is_found:
                messagebox.showerror(title="Error",message=f"No data found for \"{website_name}\" website in the file")
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="Data file does not found.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():
    if len(w_entry.get()) == 0 or len(e_entry.get())==0 or len(p_entry.get())==0:
        messagebox.showwarning(title="page says",message="Please don't leave any of fields empty.")
        return

    new_data = {
        w_entry.get() :{
        "Email":e_entry.get(),
        "Password":p_entry.get()
        }
    }
    is_ok = messagebox.askokcancel(title="page says",message=f"Details :\nEmail : {e_entry.get()}\n"
                                                             f"Password : {p_entry.get()}\n"         
                                                        f"Are you sure you want to save it ? ")
    if is_ok:
        try:
            with open("data.json",mode="r") as file:
                data = json.load(file)
                data.update(new_data)
                with open("data.json", "w") as file2:
                    json.dump(data, file2, indent=4)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data,file,indent=4)

        w_entry.delete(0,END)
        e_entry.delete(0,END)
        p_entry.delete(0,END)
        w_entry.focus()
        
# ---------------------------- UI SETUP ------------------------------- #

FONT = ("Arial",10,"bold")

window = Tk()
window.title("Password Manager")
window.minsize(460,400)
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

# Website label
website = Label(text="Website : ",font=FONT)
website.grid(column=0,row=1)
# text field for website
w_entry = Entry(width=25)
w_entry.place(x=125,y=200)
w_entry.focus()

#search button
search = Button(text="Search",width=7,command=search_credentials)
search.place(x=283,y=198)

# Email username label
email_username = Label(text="Email/Username : ",font=FONT)
email_username.grid(column=0,row=2)
# text field for email username
e_entry = Entry(width=36)
e_entry.grid(column=1,row=2,columnspan=2)

# password
passwd = Label(text="Password : ",font=FONT)
passwd.grid(column=0,row=3)
# text field
p_entry = Entry(width=25)
# p_entry.grid(column=1,row=3)
p_entry.place(x=125,y=250)

# Generate button
generate_passwd = Button(text="Generate",width=7,command=generate_password)
generate_passwd.place(x=283,y=248)
# Add button
add = Button(text="Add",width=30,command=add_to_file)
add.place(x=125,y=275)


window.mainloop()
