from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters =  [random.choice(letters) for _ in range(nr_letters)]
    password_symbols =  [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =  [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not email or not password or not website:
        messagebox.showinfo(title="WARNING", message="Don't Leave The Fields Empty")
    else:
        try:
            with open("/Users/SAMEH/Desktop/web/python/password-manager/data.json", mode="r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            data = {}

        data.update(new_data)

        with open("/Users/SAMEH/Desktop/web/python/password-manager/data.json", mode="w") as file:
            json.dump(data, file, indent=4)

        password_entry.delete(0, 'end')
        website_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30) 

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="/Users/SAMEH/Desktop/web/python/password-manager/logo.png")
canvas.create_image(100 ,112, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", padx= 50)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jsameh16@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1 )

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
