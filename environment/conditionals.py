# userReply = input("do you need a ship package ? (Enter yes or no) ")

# if userReply == "yes" :
   
#     print ("we can help you ship that package!")
    
# else:
#     print("please come back when you need to ship a package. thank you !")
    
    
userReply = input("would you like to buy stamps, buy an envelope, or make a copy (Enter stamps, envelope or copy) ")

if userReply == "stamps" :
    print("we have many stamp designs to choose from")

elif userReply == "envelope" :
    print("we have many envelope sizes to choose from")
    
elif userReply == "copy" :
    copies = input("how many copies would you like ? (enter a number)") 
    print("here are {} copies" .format(copies)) 
    
else :
    print("thank you! please come again.")
    

print("Welcome to guess the number!")

print("The rules are simple. i will think of a number, and you will try to guess it.")

#if the user has not guessed the correct answer, enter the loop.
import random

number = random.randint(1,10)
#Ask the user for a guess


isGuessRight = False

while isGuessRight != True:
    
    guess = input("guess a number between 1 and 10 : ")
    
    #Is the guess the correct number?
    
    if int(guess) == number:
        print("you guessed {}. That is correct ! you win !" .format(guess))
        
        isGuessRight == True
        
    #If the correct guess, tell the user it was the correct guess and exit the loop.
        
    else:
        print("you guessed {}. sorry, that isnt it try again." .format(guess))
        
    #If the wrong guess, tell the user it was the wrong guess and continue the loop.
    
    

        
        
    
    
    
    
    
    
    
    
    
    
    
    


