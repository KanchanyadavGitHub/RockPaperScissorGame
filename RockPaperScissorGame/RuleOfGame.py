from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
window=Tk()
window.title("ROCK PAPER SCISSOR GAME")
window.iconbitmap('Games.ico')
window.configure(background="white")
window.minsize(height=800,width=800)
window.maxsize(height=800,width=800) 
filename=PhotoImage(file="img\\bbb.png")
blabel=Label(window,image=filename)
blabel.place(x=0,y=0,relheight=1,relwidth=1)
frame1=Frame(window)
frame1.pack(side="top")
Label1=Label(frame1,bg="black",fg="white",text="RULE OF ROCK PAPER SCISSOR GAME",font=('algerian',20,'bold'))
Label1.grid(row=1,column=1)
image=Image.open("img\\rules.jpg")
photo= ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
def back():
        ans=messagebox.askyesnocancel("Confirmation","ARE YOU WANT TO GO HOME PAGE?")
        if(ans==True):
            
            window.destroy()    
            import index
back_button=Button(window,width=20,height=2,text="BACK",fg="yellow",bg="black",activebackground="red",command=back)
back_button.place(x=320,y=330)
#back_button.pack()
window.mainloop()