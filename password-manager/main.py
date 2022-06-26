from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
from os.path import exists as file_exists

# attribute for logo <a href="https://www.flaticon.com/free-icons/password" title="password icons">Password icons created by Freepik - Flaticon</a>""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_list+=[choice(letters) for x in range(randint(8, 10))]

    password_list+=[choice(numbers) for x in range(randint(2, 4))]

    password_list+=[choice(symbols) for x in range(randint(2, 4))]


    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def password_save():
    #1 get website email and password entries
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()

    # Message prompts
    ## check for empty fields
    if website=="" or email=="" or password=="":
        messagebox.showerror(title = "OOps", message="Please don\'t leave any fields empty!")
    else:
        data_dict = {website:{
            'email':email,
            'password':password
        }}
        ## confirmation before adding data
        is_ok = messagebox.askokcancel(title=website, message=f"The data you have entered is: \nwebsite: {website}\npassword: {password}\nAre you sure you want to save?")

        if is_ok and not file_exists("passwords.json"): # checking if file exists
        #2 write the data in password.json
            with open("passwords.json", "w") as pfile:
                json.dump(data_dict,pfile,indent=4) # indent helpful in reading json file
        else:
            with open("passwords.json", "r") as pfile:
                data = json.load(pfile) #read json file
                data.update(data_dict)
            with open("passwords.json", "w") as pfile:
                json.dump(data,pfile,indent=4) # indent helpful in reading json file

        #3 clear entries
        website_entry.delete(0,'end')
        password_entry.delete(0,'end')

# ---------------------------- SEARCH DATA ------------------------------- #
def find_password():
    try:
        with open("passwords.json", "r") as pfile:
            data = json.load(pfile)

    except FileNotFoundError:
        messagebox.showinfo(title="No file", message="No Data File Found, Please add the data")
        website_entry.delete(0,END)
    else:

        search = website_entry.get().lower()
        searchkey = data[search]
        if search not in data.keys():
            messagebox.showerror(title="No details",message="No details for the website exists\nTry and check the spelling")
        else:
            messagebox.showinfo(title="info", message=f"email: {searchkey['email']}\npassword: {searchkey['password']}")
            website_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

#initial setup
window = Tk() # create a window
window.title("Password Manager")
window.minsize(height=200,width=200)
window.config(padx=20, pady=20,bg="lightblue")

#Canvas
canvas = Canvas(height=200,width=200,bg ="lightblue",highlightbackground="lightblue")
logo_img = PhotoImage(file="logo.png") # read png
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text="Website:",bg ="lightblue")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:",bg ="lightblue")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:",bg ="lightblue")
password_label.grid(column=0,row=3)

# entries:
website_entry = Entry(width = 35)
website_entry.grid(column=1,row=1)
website_entry.focus() # to put cursor on the the entry field when we launch

email_entry = Entry(width=53)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"henloyalmeida@gmail.com") # prepopulate a text
# insert(index, text)

password_entry = Entry(width=36)
password_entry.grid(column=1,row=3)

#buttons

generate_button = Button(text="Generate Password",command=gen_password,bg ="lightblue")
generate_button.grid(column=2,row=3)

add_button = Button(text="Add", width=52, command=password_save,bg ="lightblue")
add_button.grid(column=1,row=4, columnspan=2)

search_button = Button(text="Search",width = 13, command=find_password,bg ="lightblue")
search_button.grid(column=2,row=1)

window.mainloop() # create a continous loop
