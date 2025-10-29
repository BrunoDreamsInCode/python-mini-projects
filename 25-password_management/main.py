from tkinter import *
from tkinter import messagebox
from random import random, choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_gen():
    password_entry.delete(0, END)  # clear previous password

    # generate random letters, numbers, symbols
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    # combine and shuffle
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # convert list to string and insert into entry
    final_password = "".join(password_list)
    password_entry.insert(index=END, string=f"{final_password}")

    # copy password to clipboard
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    web_site = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(web_site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        # confirm before saving
        is_ok = messagebox.askokcancel(title=web_site, message=f"These are the details:\nWebSite:{web_site}\n"
                                                       f"E-mail:{email}\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            # append data to file
            with open("Passwords.txt", "a") as data:
                data.write(f"WebSite:{web_site} | E-mail:{email} | Password:{password}\n")

            # clear website and password entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# canvas for logo
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

# labels
website_label = Label(text="Website:")
email_username_label = Label(text="E-mail/Username:")
password_label = Label(text="Password: ")

# buttons
button_generate = Button(text="Generate Password", command=password_gen)
button_add = Button(text="Add", width=36, command=get_data)

# position labels and buttons
website_label.grid(row=1,column=0)
email_username_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
button_generate.grid(row=3,column=2)
button_add.grid(row=4,column=1,columnspan=2, sticky="ew")

# entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_username_entry = Entry(width=35)
email_username_entry.insert(index=END,string="youremail@gmail.com")
email_username_entry.grid(row=2, column=1,columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1, sticky="ew")

canvas.mainloop()
