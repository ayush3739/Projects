from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols=[random.choice(symbols) for char in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for char in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_fill.insert(0,password)
    pyperclip.copy(pass_fill.get())




# ---------------------------- SAVE PASSWORD ------------------------------- #
def addpass():
    if len(website_fill.get())<1 or len(pass_fill.get())<1:
        messagebox.showerror(title="Empty spaces",message="You have left some fields empty ")
    else:
        is_ok=messagebox.askokcancel(title=website_fill.get(),message=f"These are the details entered: \nEmail: {email_fill.get()}"
                                f"\nPassword: {pass_fill.get()} \n Is it ok to save?")
        if is_ok:
            with open("demo.txt","a") as file:
                file.write(f"{website_fill.get()} | {email_fill.get()} | {pass_fill.get()}\n")
                
                website_fill.delete(0,END)
                email_fill.delete(0,END)
                email_fill.insert(0,"ayushmaurya@gmail.com")
                pass_fill.delete(0,END)
            
# ---------------------------- UI SETUP ------------------------------- #
win =Tk()
win.title("Password Manager")
win.config(padx=10,pady=20)

can = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
can.create_image(100, 100, image=pass_img)
can.grid(row=0,column=1  )

website=Label(text="Website:")
website.grid(row=1,column=0)

website_fill=Entry(width=35)
website_fill.grid(row=1,column=1,columnspan=2)
website_fill.focus()

email=Label(text="Email/Username:")
email.grid(row=2,column=0)

email_fill=Entry(width=35)
email_fill.grid(row=2,column=1,columnspan=2)
email_fill.insert(0,"ayushmaurya@gmail.com")

password=Label(text="Password:")
password.grid(row=3,column=0,padx=0)

pass_fill=Entry(width=25)
pass_fill.grid(row=3,column=1,padx=0)

button1=Button(text="Generate Password",command=generate_pass)
button1.grid(row=3,column=2,padx=0)

add_button=Button(text="Add",width=35,command=addpass)
add_button.grid(row=4,column=1,columnspan=2,pady=10)


win.mainloop()

