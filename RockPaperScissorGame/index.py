from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#DEFINING GUI WINDOW
window=Tk()
window.title("ROCK PAPER SCISSOR GAME")
window.iconbitmap('Games.ico')
window.configure(background="#4A4A4A")

window.geometry("800x800")
filename=PhotoImage(file="img\\maxresdefault.png")
blabel=Label(window,image=filename)
blabel.place(x=0,y=0,relwidth=1,relheight=1)
#DEFINING FRAMES
frame1=Frame(window)
frame1.pack(side="top")
frame2=Frame(window)
frame2.pack(side="top")
def start():
	window.destroy()
	import game
	
def Exit():
		ans=messagebox.askyesnocancel("Confirmation","Are you sure want to exit?")
		if(ans==True):
            
			window.destroy()            
def rule():
    window.destroy()
    import RuleOfGame            
	
#LABELES AND BUTTONS
Label1=Label(frame1,bg="black",fg="white",text="ROCK PAPER SCISSOR GAME",font=('algerian',20,'bold'))
Label1.grid(row=1,column=1)
Start_button=Button(frame2,text="START",width=10,height=2,fg="Yellow",bg="green",activebackground="gray",command=start)
Start_button.grid(row=1,column=1)

Exit_button=Button(frame2,width=10,height=2,text="RULE",fg="YELLOW",bg="blue",activebackground="gray",command=rule)
Exit_button.grid(row=1,column=10)

rule_button=Button(frame2,width=10,height=2,text="EXIT",fg="yellow",bg="red",activebackground="gray", command=Exit)
rule_button.grid(row=1,column=20)
window.mainloop()