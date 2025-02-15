from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
	
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example whole numbers

	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	symbols = ["+", "-", "*", "/", "=", "<", ">", "(", ")", "[", "]", "{", "}", "$", "%", "@", "#", "&", "*", "_",  "!", "?", ".", ",", ":", ";", "'", "\""]

	password_letter = [choice(letters) for _ in range(randint(8, 10))]
	password_number = [choice(numbers) for _ in range(randint(2, 4))]
	password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

	password_list = password_letter + password_number + password_symbol
	shuffle(password_list)
	new_password = "".join(map(str, password_list))
	# for char in password_list:
	#     new_password += str(char)
	password_entry.delete(0, 'end') 
	password_entry.insert(0, new_password)
	pyperclip.copy(text=new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	
	if len(website) ==0 or len(password) ==0:
		messagebox.showinfo(title="Oops", message= "you've forgot something, Please check")
	else:
		is_okay = messagebox.askokcancel(title= website, message= f"These are the details entered: /nEmail: {email} " f"/n password: {password} /n Is it okay to save?")
		if is_okay:
			with open("data.txt", "a") as file:
				file.write(f"{website} | {email} | {password}\n")
				website_entry.delete(0, END)
				password_entry.delete(0, END)

	
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password-Manager-Tool")
window.config(padx=50, pady=20)

password = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
password.create_image(100, 100, image=logo_img)
password.image = logo_img
password.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/User_name:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.focus()
email_entry.insert(0, "praveen@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_entry.focus()

# generate password button
generate_password_button = Button(text="Generate Password", command= password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command= save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()