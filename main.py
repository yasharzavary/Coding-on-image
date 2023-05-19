# created by: yashar zavary rezaie
# projectname: add one pass in one picture...

# we can write this username control part in mysql or mongo db...
# but because i can't send the database and it can be hard to build it in main source...
# i build this control with json files
from tkinter import *


# main gui part
root=Tk()

w=500
h=500
screenh=root.winfo_screenheight()
screenw=root.winfo_screenwidth()

x=(screenw/2 - w/2)
y=(screenh/2 - h/2)

root.geometry("%dx%d+%d+%d"%(w,h,x,y))
root.resizable(width=False,height=False)

coderFrame=Frame(master=root, bg="#707070",height=20,width=500)
coderFrame.pack(side='bottom')
coderFrame.pack_propagate(0)

# programmer stamp
stampLabel=Label(master=coderFrame, text='@zavaryayshar2023', bg='#707070')
stampLabel.pack(side='right')





root.mainloop()










