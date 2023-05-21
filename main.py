# created by: yashar zavary rezaie
# projectname: add one pass in one picture...

# we can write this username control part in mysql or mongo db...
# but because i can't send the database and it can be hard to build it in main source...
# i build this control with json files
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import re
from PIL import Image

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
root.title('coding in one picture')
root.iconbitmap('mainroot.ico')

coderFrame=Frame(master=root, bg="#707070",height=20,width=500)
coderFrame.pack(side='bottom')
coderFrame.pack_propagate(0)

# programmer stamp
stampLabel=Label(master=coderFrame, text='@Copyright-zavaryayshar2023', bg='#707070')
stampLabel.pack(side='right')

# url label place parts
urlLabel=Label(master=root,text='c:\\')
urlLabel.pack()


filename=''
# button and menu part
def browsefile(event):
    global filename
    filename=filedialog.askopenfilename(title='select your pic',filetypes=(("png files","*.png*"),("all files","*.*")))
    urlLabel.config(text=filename)

def comein(event):
    fileButton.config(bg='gray')

def comeout(event):
    fileButton.config(bg='#f8f8f9')

fileButton=Button(master=root,text="Browse Picture",bg='#f8f8f9')
fileButton.bind("<Button>",browsefile)
fileButton.bind('<Enter>',comein)
fileButton.bind('<Leave>',comeout)
fileButton.pack()

# progress start Button
# my main func for coding the picture
def progress(event):
    # my name part root 
    nameRoot=Tk()
    nw=500
    nh=250
    nx=(screenw/2 - nw/2)
    ny=(screenh/2 - nh/2)
    nameRoot.geometry('%dx%d+%d+%d'%(nw,nh,nx,ny))
    nameRoot.title('name select')
    nameRoot.iconbitmap('nameroot.ico')
        
    writeLabel=Label(master=nameRoot, text=f'write your sentence to code on the picture:\n{filename}')
    writeLabel.pack()
        
    nameEntry=Entry(master=nameRoot)
    nameEntry.pack()
        
    # my coding part
    def startProgress(event):
        def producecode(newName):
           for word in newName:
               yield bin(ord(word))[2:]
            
        im=Image.open(filename, 'r')
        copyIm=im.copy()
        w, h=copyIm.size
        pixelIm=list(copyIm.getdata())
        for i in range(w*h):
            pixelIm[i]=list(pixelIm[i])
        ytemp=0
        xtemp=0
        codename=nameEntry.get()
        for bincode in producecode(codename):
            for i in range(len(bincode)):
                if(xtemp%3==0):
                    ytemp+=1
                    xtemp=0
                if(bincode[i]=='1'):
                    if(pixelIm[ytemp][xtemp]%2==0):
                        pixelIm[ytemp][xtemp]+=1
                        xtemp+=1
                    else:
                        xtemp+=1
                else:
                    if(pixelIm[ytemp][xtemp]%2==1):
                        pixelIm[ytemp][xtemp]+=1
                        xtemp+=1
                    else:
                        xtemp+=1
            if(xtemp%3==0):
                    ytemp+=1
                    xtemp=0
            pixelIm[ytemp][xtemp]=255
            xtemp+=1
        if xtemp%3==0:
            ytemp+=1
            xtemp=0
        pixelIm[ytemp][xtemp]=254
        for i in range(w*h):
            pixelIm[i]=tuple(pixelIm[i])
        copyIm.putdata(pixelIm)
        
        copyIm.save(re.findall(r'(\w*).png', filename)[0]+'-encoded.png')
        copyIm.close()
        messagebox.showinfo('encoded result', 'picture successfully encoded')
                
        
        
        
        
    def comein(event):
        okButton.config(bg='gray')
            
    def comeout(event):
        okButton.config(bg='#f8f8f9')
        
    okButton=Button(master=nameRoot, text='start progress')
    okButton.bind('<Enter>',comein)
    okButton.bind('<Leave>',comeout)
    okButton.bind('<Button>',startProgress)
    okButton.pack()
        
    nameRoot.mainloop()

def dprogress(event):
    dfile=Image.open(filename, 'r')
    rgbfile=list(dfile.getdata())
    xtemp=0
    ytemp=0
    secData=''
    bindata='0b'
    while True:
        if xtemp%3==0:
            ytemp+=1
            xtemp=0
        if rgbfile[ytemp][xtemp]==254:
            break
        if(rgbfile[ytemp][xtemp]==255):
            bindata=int(bindata, 2)
            secData+=chr(bindata)
            bindata='0b'
            xtemp+=1
            if xtemp%3==0:
                ytemp+=1
                xtemp=0
        bindata+=str(rgbfile[ytemp][xtemp]%2)
        if rgbfile[ytemp][xtemp]==254:
            break
        xtemp+=1
    messagebox.showinfo('decode result', f'secret code:\n{secData}')
            
    


onetimeclick=True
def select(event):
    global onetimeclick
    if filename=='':
        messagebox.showerror('picture Error', 'you don\'t select a picture')
        return
    elif re.search(r'.+png', filename):
        if onetimeclick:
            onetimeclick=False
            
            def comein(event):
                encodeButton.config(bg='red')

            def comeout(event):
                encodeButton.config(bg='#f8f8f9')
            
            encodeButton=Button(master=root, text='encode', bg='#f8f8f9')
            encodeButton.bind('<Button>',progress)
            encodeButton.bind('<Enter>',comein)
            encodeButton.bind('<Leave>',comeout)
            encodeButton.pack(side='right')
            
            def comein(event):
                decodeButton.config(bg='green')

            def comeout(event):
                decodeButton.config(bg='#f8f8f9')
            
            decodeButton=Button(master=root, text='decode')
            decodeButton.bind('<Button>',dprogress)
            decodeButton.bind('<Enter>',comein)
            decodeButton.bind('<Leave>',comeout)
            decodeButton.pack(side='left')
        else:
            return
    else:
        messagebox.showerror('picture Error', 'this url is isn\'t a picture')
        return

def comein(event):
    startButton.config(bg='gray')

def comeout(event):
    startButton.config(bg='#f8f8f9')
    
startButton=Button(master=root,text='select',bg='#f8f8f9')
startButton.bind('<Button>',select)
startButton.bind('<Enter>',comein)
startButton.bind('<Leave>',comeout)
startButton.pack()


# exit button
def exittime(event):
    root.destroy()

def comein(event):
    exButton.config(bg='gray')

def comeout(event):
    exButton.config(bg='#f8f8f9')

exButton=Button(master=root, text='exit',bg='#f8f8f9')
exButton.bind('<Button>',exittime)
exButton.bind('<Enter>',comein)
exButton.bind('<Leave>',comeout)
exButton.pack()


root.mainloop()

