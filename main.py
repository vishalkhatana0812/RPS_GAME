import random
from PIL import Image

#read the image
rock = Image.open("rock.jpg")
paper = Image.open("paper.jpg")
scissor = Image.open("scissor.jpg")

rock.thumbnail((400, 400))
paper.thumbnail((400,400))
scissor.thumbnail((400,400))

user_rps=int(input("enter 0 for rock , 1 for paper, 2 for scissor"))
print("User Chose : ")
if user_rps==0:
  rock.show()
elif user_rps==1:
  paper.show()  
elif user_rps==2:
  scissor.show()  
else:
  print("Invalid Input")  
computer_rps=random.randint(0,2)
print("Computer Chose : ")
if computer_rps==0:
  rock.show()
elif computer_rps==1:
  paper.show()  
elif computer_rps==2:
  scissor.show()  
flag=0
while flag==0 :
  
  if user_rps==computer_rps:
    print("it's a draw")
    user_rps=int(input("enter 0 for rock , 1 for paper, 2 for scissor"))
    computer_rps=random.randint(0,2)
   
  elif(user_rps==0 and computer_rps==2) or (user_rps==1 and computer_rps==0 ) or(user_rps==2 and computer_rps==1) :
    flag=1 
    print("YOU WIN")
  
  else:
    flag=1
    print("YOU LOSE")