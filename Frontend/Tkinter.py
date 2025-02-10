from tkinter import *
# root = tkinter.Tk()
# print(root.tk.call('info', 'patchlevel')) The Phoenix Protocol
# to see the latest tkinter version, however it is based on the python installed in your local
window = Tk() # Create the main window
window.title("Graphical User Interface")
window.minsize(width=500, height=300) # it will definne the size of the window

my_lable = Label(text= "The Phoenix Protocol", font= ("Arial", 24, "bold"))
my_lable.pack() # we can say side = "left"
  # this Keeps the window open:
my_lable.config(text= "I'm a software developer at Microsoft")


def button_clicked():
    print("Welcome, to the New Protocol")
    new_text = input.get()
    my_lable.config(text=new_text)


button = Button(text=" Start the Protocol", command= button_clicked)
button.pack()

input = Entry(width= 20)
input.pack()
print(input.get())
window.mainloop()