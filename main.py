from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for i in range(nr_letters)]
    password_list += [choice(symbols) for i in range(nr_symbols)]
    password_list += [choice(numbers) for i in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Ooops', message="Please don't leave fields empty!")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_input = website_entry.get().lower()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        messagebox.showerror(title="Opps", message=f"We don't have an {website_input}'s password saved.")
    else:
        if website_input in data:
            email_saved = data[website_input]['email']
            password_saved = data[website_input]['password']
            messagebox.showinfo(title=website_input, message=f"Your email/username is: {email_saved} \n"
                                                                 f"\n Your password is: {password_saved}")
        else:
            messagebox.showinfo(title="Opps", message=f"We don't have an {website_input}'s password saved.")




# ---------------------------- UI SETUP ------------------------------- #


new_window = Tk()
new_window.config(pady=50, padx=50)
new_window.title('Keep it as a Secret')

new_canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="rabbit.png")
new_canvas.create_image(100, 100, image=lock_image)
new_canvas.grid(row=0, column=1)


# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Button
generate_pass_btn = Button(text='Generate Password', width=10, command=generate_password)
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text='Add', command=save_password)
add_btn.config(width=33)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text='Search', command=find_password)
search_btn.config(width=10)
search_btn.grid(row=1, column=2)


# Entry
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(0, 'angely@email.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21, show='*')
password_entry.grid(row=3, column=1)


new_window.mainloop()