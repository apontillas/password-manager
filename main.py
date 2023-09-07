from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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
    password_entry.insert(0, f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Ooops', message="Please don't leave fiels empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\n Password: {password} \nIs it ok to save?")
        if is_ok:
            with open('password.txt', 'a') as file:
                file.write(f"{website} | {email} |  {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


new_window = Tk()
new_window.config(pady=50, padx=50)
new_window.title('Keep it as a Secret')

new_canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
new_canvas.create_image(100, 100, image=lock_image)
new_canvas.grid(row=0, column=1)


# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

generate_pass_btn = Button(text='Generate Password', width=10, command=generate_password)
generate_pass_btn.grid(row=3, column=2)

# Button
add_btn = Button(text='Add', command=save_password)
add_btn.config(width=33)
add_btn.grid(row=4, column=1, columnspan=2)


# Entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, 'angely.tukivakala@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21, show='*')
password_entry.grid(row=3, column=1)


new_window.mainloop()