from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Arial", 20,)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project from Day 005
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    generated_password = [choice(letters) for _ in range(randint(8, 10))]
    generated_password += [choice(numbers) for _ in range(randint(2, 4))]
    generated_password += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(generated_password)
    string_password = "".join(generated_password)

    password_text_box.insert(0, string_password)
    pyperclip.copy(string_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    website = website_text_box.get()
    email = email_text_box.get()
    password = password_text_box.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Save updated data
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Save updated data
                json.dump(data, file, indent=4)
        finally:
            website_text_box.delete(0, END)
            password_text_box.delete(0, END)

# ------------------ SEARCH FOR EXISTING PASSWORD --------------------- #


def find_password():
    website = website_text_box.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Login details for {website} not found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_pic)
canvas.grid(column=1, row=0)

# Website label and text box

website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

website_text_box = Entry(width=21, font=FONT)
website_text_box.grid(column=1, row=1)
website_text_box.focus()

# Email label and text box

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)

email_text_box = Entry(width=35, font=FONT)
email_text_box.grid(column=1, row=2, columnspan=2)
email_text_box.insert(0, "default@email.com")

# Password label and text box

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

password_text_box = Entry(width=21, font=FONT)
password_text_box.grid(column=1, row=3)

# Generate password button

generate_password_button = Button(text="Generate Password", width=14, font=("Arial", 16), command=password_generator)
generate_password_button.grid(column=2, row=3)

# Add password to text file button

add_button = Button(text="Add", width=36, font=("Arial", 18), command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Search button

search_button = Button(text="Search", width=14, font=("Arial", 16), command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
