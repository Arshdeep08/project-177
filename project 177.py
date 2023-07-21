from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Enscapsualtion")

label_name = Label(root, text = "Name : ")
label_name.place(relx = 0.4,rely=0.1,anchor=CENTER)

label_entry_name = Entry(root)
label_entry_name.place(relx = 0.6,rely=0.1,anchor=CENTER)

label_password = Label(root, text = "Password : ")
label_password.place(relx = 0.4,rely=0.2,anchor=CENTER)

label_entry_password = Entry(root)
label_entry_password.place(relx = 0.6,rely=0.2,anchor=CENTER)

label_captcha = Label(root, text = "Captcha : ")
label_captcha.place(relx = 0.4,rely=0.3,anchor=CENTER)

label_entry_captcha = Entry(root)
label_entry_captcha.place(relx = 0.6,rely=0.3,anchor=CENTER)

root.mainloop()