from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    with open("/Users/SAMEH/Desktop/web/python/password-manager/data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password}\n")

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

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()