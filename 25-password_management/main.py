from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        web_site:   {
        "e-mail": email,
        "password": password,
        }
    }

    if len(web_site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("password.json", "r") as data_file:
                #Reagind old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            messagebox.showinfo(title="Success", message=f"Data for '{web_site}' saved successfully ✅")
            website_entry.delete(0, END)
            password_entry.delete(0, END)



def search_function():
    account_search = website_entry.get().strip().lower()
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Oops", message="Account not found!")
        return

    data_lower = {key.lower(): value for key, value in data.items()}

    if account_search in data_lower:
        info = data_lower[account_search]
        print(f"Info = {info}")
        messagebox.showinfo(title="Account founded!", message=f"E-mail: {info["e-mail"]}\n"
                                                              f"Password: {info["password"]}")
    else:
        if account_search == "":
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
        else:
            messagebox.showinfo(title="Oops", message=f"The account: '{account_search}' wasn't founded!")



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
button_generate = Button(text="Generate Password", width=15, command=password_gen)
button_add = Button(text="Add", width=36, command=get_data)
button_search = Button(text="Search", width=15, command=search_function)





# position labels and buttons
website_label.grid(row=1,column=0)
email_username_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
button_generate.grid(row=3,column=2)
button_add.grid(row=4,column=1,columnspan=2, sticky="ew")
button_search.grid(row=1, column=2)




# entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="ew")

email_username_entry = Entry(width=35)
email_username_entry.insert(index=END,string="youremail@gmail.com")
email_username_entry.grid(row=2, column=1,columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1, sticky="ew")




canvas.mainloop()
