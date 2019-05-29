#working on tic tac toe

#initial step


board=[]

def display_board(board):
    i=0
    for temp in board:
        if i==3 :
            print("\n")
            print(temp,"\t",end="")
            i=1
        else:
            print(temp,"\t",end="")
            i+=1


list_input=["-","-","-","-","-","-","-","-","-"]

#taking input


display_board(list_input)

def wincheck():
    if(list_input[0]==list_input[3]==list_input[6]=="X" or list_input[1]==list_input[4]==list_input[7]=="X" or list_input[2]==list_input[5]==list_input[8]=="X" or list_input[2]==list_input[5]==list_input[8]=="X" or  list_input[0]==list_input[4]==list_input[8]=="X" or  list_input[2]==list_input[4]==list_input[6]=="X" or  list_input[0]==list_input[1]==list_input[2]=="X" or  list_input[3]==list_input[4]==list_input[5]=="X" or  list_input[6]==list_input[7]==list_input[8]=="X" ):
        print("X wins")
    elif(list_input[0]==list_input[3]==list_input[6]=="O" or list_input[1]==list_input[4]==list_input[7]=="O" or list_input[2]==list_input[5]==list_input[8]=="O" or list_input[2]==list_input[5]==list_input[8]=="O" or  list_input[0]==list_input[4]==list_input[8]=="O" or  list_input[2]==list_input[4]==list_input[6]=="O" or  list_input[0]==list_input[1]==list_input[2]=="O" or  list_input[3]==list_input[4]==list_input[5]=="O" or  list_input[6]==list_input[7]==list_input[8]=="O" ):
        print("o wins")
    else:
        print("draw")


c=0
while c<=8:
  marker=input("enter X or O")
  pos=int(input("enter 1 to 9"))
  list_input[pos]=marker
  c=c+1
  wincheck()
