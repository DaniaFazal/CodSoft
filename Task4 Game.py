import random
def userchoice():
    while True:
        user_choice = input("Choose rock, paper or scissor: ").lower()
        if user_choice in ['rock' , 'paper' , 'scissor']:
            return user_choice
        else:
            print("Invalid choose.Please choose valid options")
def computerchoice():
    return random.choice(['rock','paper','scissor'])

def findwinner(user_choice, computer_choice):
    if(user_choice==computer_choice):
        print("IT'S TIE")
    elif(user_choice=='rock'and computer_choice=='scissor')or \
    (user_choice=='paper' and computer_choice=='rock') or \
    (user_choice=='scissor' and computer_choice=='paper'):
        return "User Wins"
    else:
        return "Computer Wins"

def main():
    user_score =0
    computer_score =0
    
    print("Welcome to the game")
    while True:
        user_choice = userchoice()
        computer_choice = computerchoice()

        print(f"You choose: {user_choice}")
        print(f"Computer choose: {computer_choice}")
        result = findwinner(user_choice,computer_choice)
        print(result)

        if (result=="User Wins"):
            user_score +=1
        elif (result=="Computer Wins"):
            computer_score +=1
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play this game again?(yes/no): ").lower()
        if play_again!="yes":
            print("Hope you enjoy this game")
            break
if __name__ == "__main__":
    main()