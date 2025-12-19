from tkinter import *
win=Tk()

win.title("Game")
win.minsize(width=500,height=300)



#Entry
entry1=Entry(width=10)
entry1.grid(row=0,column=1)


#label
my_label=Label(text="Miles",font=("Arial",24,"bold"),fg="black")
my_label.grid(row=0,column=2)

my_label2=Label(text="is equal to",font=("Arial",24,"bold"),fg="black")
my_label2.grid(row=1,column=0)


my_label3=Label(text="is equal to",font=("Arial",24,"bold"),fg="black")
my_label3.grid(row=1,column=3)

my_km=Label(text="",font=("Arial",24,"bold"),fg="green",bg="sky blue",width=10)
my_km.grid(row=1,column=1)

#Button

def button_cliceked():
    
    kilometers = float(entry1.get()) * 1.60934
    my_km.config(text=kilometers)
    

but1=Button(text="Calculate",command=button_cliceked)
but1.grid(row=2,column=1,)

#Entry
entry1=Entry(width=10)
entry1.grid(row=0,column=1)






win.mainloop()
