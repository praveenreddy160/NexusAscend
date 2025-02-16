from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
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
# ---------------------------- Search-PASSWORD ------------------------------- #
def email_search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            try:
                data = json.load(data_file)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON file.")
                return
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")
        return
    else:
        if website in data:  # Directly check if the website exists as a key
            email_data = data[website].get("email", "Email not found") #using .get to avoid key error if email is not found
            password_data = data[website].get("password", "Password not found") #using .get to avoid key error if it is not found
            messagebox.showinfo(title=website, message=f"Email: {email_data}\nPassword: {password_data}")
        else:
            messagebox.showinfo("Not Found", f"No data found for {website}.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	website_data = {
		website: {
		"email": email,
		"password": password,
		}
	}
	if len(website) ==0 or len(password) ==0:
		messagebox.showinfo(title="Oops", message= "you've forgot something, Please check")
	else:
			try:
				with open("data.json", "r") as file:
					new_data = json.load(file)
			except FileNotFoundError:
				with open("data.json", "r") as file:
					new_data = json.load(file)
			else:
				new_data.update(website_data)

				with open("data.json", "w") as file:	
					json.dump(new_data, file, indent=4)
			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)
	
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password-Manager-Tool")
window.config(padx=50, pady=20)

password = Canvas(height=200, width=200)
logo_img = PhotoImage(file="C:/Users/prave/nexusascend/src/Authenticator_app/logo.png")
password.create_image(100, 100, image=logo_img)
password.image = logo_img
password.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, columnspan= 1)
search_entry_label = Label(text="Search")
search_entry_label.grid(row=2, column=1)
email_label = Label(text="Email/User_name:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Search button
search_button = Button(text="Search", width=15, command= email_search)
search_button.grid(row=1, column=2)


#Entries

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=30)
email_entry.grid(row=2, column=1)
email_entry.focus()
email_entry.insert(0, "praveen@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)
password_entry.focus()

# generate password button
generate_password_button = Button(text="Generate Password", command= password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=10, command= save)
add_button.grid(row=4, column=0, columnspan=2)

window.mainloop()