from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox

# main window ke liye
root = Tk()
root.title("Rock, Paper, Scissor Game")
root.iconbitmap('Games.ico')
root.configure(background="#56ACF1")
root.minsize(height=650,width=950)
root.maxsize(height=650,width=950)
# picture 
rock_img = ImageTk.PhotoImage(Image.open("img\\rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("img\\paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("img\\scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("img\\rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("img\\paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("img\\scissors.png"))

#picture insert
user_label = Label(root, image=scissor_img, bg="#56ACF1")
comp_label = Label(root, image=scissor_img_comp, bg="#56ACF1")

comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


# scores count karne liye 
playerScore = Label(root, text=0, font=100, bg="#56ACF1", fg="white")
computerScore = Label(root, text=0, font=100, bg="#56ACF1", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text= "PLAYER", bg="#56ACF1", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#56ACF1", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=60, bg="#56ACF1", fg="green")
msg.grid(row=3, column=2)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
    

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
    
  #----------------------------
def Exit():
		ans=messagebox.askyesnocancel("Confirmation","Are you sure want to exit?")
		if(ans==True):
             
			root.destroy()  
#final winner
def Endgame(a):
	
	#IF ANYONE(HUMAN OR COMPUTER) REACHES 3 WINS FIRST THEN GAME ENDS AND WINNER DECLARED
	if(a==3):
		b=messagebox.askyesnocancel("WIN","HURRAH YOU WON,Do you want to play again?")
		if(b):
			root.destroy()
			import game
		else:
			root.destroy()
			import index
	else:
		b=messagebox.askyesnocancel("LOOSE","OOPS YOU LOOSE,Do you want to play again?")
		if(b):
			root.destroy()
			import game
		else:
			root.destroy()
			import index
# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose!")
            updateCompScore()
        else:
            updateMessage("You Wins!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose!")
            updateCompScore()
        else:
            updateMessage("You Wins!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose!")
            updateCompScore()
        else:
            updateMessage("You Wins!!")
            updateUserScore()
if playerScore == 3 or computerScore==3:
    Endgame(playerScore)
    
    
# update choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)
# buttons
rock = Button(root, width=15, height=4, text="ROCK",
              bg="#FF3E4D",activebackground="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=15, height=4, text="PAPER",
               bg="#FAD02E",activebackground="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=15, height=4, text="SCISSOR",
                 bg="#0ABDE3",activebackground="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)
#exit button              
Exit_button=Button(root,width=15,height=2,text="EXIT",fg="blue",bg="gray",activebackground="GREEN",command=Exit)
Exit_button.grid(row=8,column=2) 
 
#back_button=Button(root,width=15,height=2,text="BACK",fg="red",#bg="gray",activebackground="GREEN",command=Back)
#back_button.grid(row=12,column=2) 
 
root.mainloop()