import random

count = 0 
dictionary = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
list = [1,2,3,4,5,6,7,8,9]
win = False
start = True

def make_board():
    global dictionary,list,win,count,start
    for n in dictionary:
        if count%3 == 0:
            print()
        count = count + 1
        if start:
            print(str(n)+"|",end = "|")
        else:
            print("| "+str(dictionary[n]),end = " |")

def game():
    global dictionary,list,win,count,start
    start = True
    while not x_win_check() or o_win_check():
        make_board()
        print()
        ask = int(input("enter a number between 1 and 9: "))

        if dictionary[ask] == "X" or dictionary[ask] == "O":
            print("you already put that there")

        elif ask in dictionary:
            dictionary[ask] = "X"
            list.remove(ask)
            computer_decision()
            start = False

    make_board()
    if o_win_check():
        print("\n"+"\n"+"CPU WIN")
    elif x_win_check():
        print("\n"+"\n"+"YOU WIN")

def computer_decision():
    global dictionary,list,win,count,start
    if len(list) > 1:
        a = random.choice(list)
        dictionary[a] = "O"
        list.remove(a)

def ai_decision():
    global dictionary,list,win,count,start
    pass

def x_win_check():   
    global dictionary,list,win,count  
    if dictionary[1] == dictionary[2] == dictionary[3] == "X" or dictionary[4] == dictionary[5] == dictionary[6]== "X" or dictionary[7] == dictionary[8] == dictionary[9] == "X":
        return True
    elif dictionary[1] == dictionary[4] == dictionary[7]=="X" or dictionary[2] == dictionary[5] == dictionary[8]=="X" or dictionary[3] == dictionary[6] == dictionary[9] == "X":
        return True
    elif dictionary[1] == dictionary[5] == dictionary[9]=="X" or dictionary[3] == dictionary[5] == dictionary[7]=="X":
        return True
    if len(list) == 0:
        print("DRAW")

def o_win_check():
    if dictionary[1] == dictionary[2] == dictionary[3] == "O" or dictionary[4] == dictionary[5] == dictionary[6]== "O" or dictionary[7] == dictionary[8] == dictionary[9] == "O":
        return True
    elif dictionary[1] == dictionary[4] == dictionary[7]=="O" or dictionary[2] == dictionary[5] == dictionary[8]=="O" or dictionary[3] == dictionary[6] == dictionary[9] == "O":
        return True
    elif dictionary[1] == dictionary[5] == dictionary[9]=="O" or dictionary[3] == dictionary[5] == dictionary[7]=="O":
        return True
    if len(list) == 0:
        print("DRAW")

game()