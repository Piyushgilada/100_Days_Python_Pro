from tkinter import *

window=Tk()
window.title('My First GUI Program')
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

# Label
my_label=Label(text="I am A Label",font=('arial',24,'italic'))
my_label['text']='new text'
my_label.config(text='new text')
my_label.pack(expand=True)

# my_label.place(x=100,y=100)
# my_label.pack()

# Button
def button_clicked():
    my_label['text']=input.get()
button=Button(text='click me',command=button_clicked)
button.pack(expand=True)


# Entry
input=Entry(width='10')
print(input.get())
input.pack(expand=True)
# input.grid(column=1,row=1)

# Text
text=Text(height=5, width=30)
text.focus()
text.insert(END, "Example of entry text ...")
text.pack(expand=True)


# spin box
# Scale
# CheckBox
# Radio Button
# List Box

window.mainloop()