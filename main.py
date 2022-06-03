from operator import index
import random

from matplotlib.cbook import index_of
def main():
    print("Rock Paper Scissors")
    mylist = ["rock", "paper", "scissors"]
    CPU_choice=random.choice(mylist)
    # print(CPU_choice)
    indexofcpu=mylist.index(CPU_choice)
    # print(indexofcpu)
    
    USER_choice=input("INPUT:\nR for rock,\nP for paper, \nS for scissors \n\n").lower()
    # print(USER_choice)
    if(USER_choice=="r" or USER_choice=="p" or USER_choice=="s"):
        if(USER_choice=="r"):
            print("CPU :"+mylist[indexofcpu].upper()+ " USER :"+mylist[0].upper())
            processing(mylist[indexofcpu],mylist[0])
        elif(USER_choice=="p"):
             print("CPU :"+mylist[indexofcpu].upper()+ " USER :"+mylist[1].upper())
             processing(mylist[indexofcpu],mylist[1])
        elif(USER_choice=="s"):
             print("CPU :"+mylist[indexofcpu].upper()+ " USER :"+mylist[2].upper())
             processing(mylist[indexofcpu],mylist[2])
    
    else:
        print("\n \n \n Invalid Input! \n Please try again")
        main()


def processing(cpu,user):
    if(cpu=="rock" and user=="scissors"):
        print("CPU WINS!")
    elif(cpu=="paper" and user=="rock"):
        print("CPU WINS!")
    elif(cpu=="scissors" and user=="paper"):
        print("CPU WINS!")
    elif(cpu==user):
        print("It's a Tie")
    if(user=="rock" and cpu=="scissors"):
        print("USER WINS!")
    elif(user=="paper" and cpu=="rock"):
        print("USER WINS!")
    elif(user=="scissors" and cpu=="paper"):
        print("USER WINS!")

if __name__=="__main__":
    main()