def print_curr(total_table):
    p = 0
    for i in range(3):
        print(" ___",end="")
    print()
    for i in range(3):
        for j in range(3):
            
            if j == 0 :
               print("| ",end = "")
            print(total_table[i][j] , end = " | ")
        
        print()
        print("|",end= "")
        for i in range(3):
            print("___|",end ="")
        print()
k = 1
total_table = []
for i in range(3):
    original_table = []
    for j in range(3):
        original_table.append(k)
        k+=1
    total_table.append(original_table)
player1 = 0
player2 = 0
i = 0
p1w = 0
p2w = 0
while i<9:
    print_curr(total_table)
    print("enter number to choose your place")
    select1 = int(input())
    if(select1>=1 and select1<=9): 
        if (select1 == 1 and (total_table[0][0] != 'x' and total_table[0][0] != 'o')) or (select1 == 2 and (total_table[0][1] != 'x' and total_table[0][1] != 'o')) or (select1 == 3 and (total_table[0][2] != 'x' and total_table[0][2] != 'o')) or (select1 == 4 and (total_table[1][0] != 'x' and total_table[1][0] != 'o')) or (select1 == 5 and (total_table[1][1] != 'x' and total_table[1][1] != 'o')) or (select1 == 6 and (total_table[1][2] != 'x' and total_table[1][2] != 'o')) or (select1 == 7 and (total_table[2][0] != 'x' and total_table[2][0] != 'o')) or (select1 == 8 and (total_table[2][1] != 'x' and total_table[2][1] != 'o')) or (select1 == 9 and (total_table[2][2] != 'x' and total_table[2][2] != 'o')):         
            if(i%2 == 0):
                for j in range(3):
                    for k in range(3):
                        if total_table[j][k] == select1:
                            total_table[j][k] = 'X'
            else:
                for j in range(3):
                    for k in range(3):
                        if total_table[j][k] == select1:
                            total_table[j][k] = 'O'
        
            if(total_table[0][0]==total_table[0][1]==total_table[0][2]=='x' or total_table[1][0]==total_table[1][1]==total_table[1][2]=='x' or total_table[2][0]==total_table[2][1]==total_table[2][2]=='x'):
                p1w = 1
                break
            elif(total_table[0][0]==total_table[0][1]==total_table[0][2]=='o' or total_table[1][0]==total_table[1][1]==total_table[1][2]=='o' or total_table[2][0]==total_table[2][1]==total_table[2][2]=='o'):
                p2w = 1
                break
            elif(total_table[0][0]==total_table[1][0]==total_table[2][0]=='x' or total_table[0][1]==total_table[1][1]==total_table[2][1]=='x' or total_table[0][2]==total_table[1][2]==total_table[2][2]=='x') :
                p1w = 1
                break
            elif(total_table[0][0]==total_table[1][0]==total_table[2][0]=='o' or total_table[0][1]==total_table[1][1]==total_table[2][1]=='o' or total_table[0][2]==total_table[1][2]==total_table[2][2]=='o') :
                p2w = 1
                break
            elif total_table[0][0]==total_table[1][1]==total_table[2][2]=='x':
                p1w = 1
                break
            elif total_table[0][0]==total_table[1][1]==total_table[2][2]=='o':
                p2w = 1
                break
            elif total_table[0][2]==total_table[1][1]==total_table[2][0]=='x':
                p1w = 1
                break
            elif total_table[0][2]==total_table[1][1]==total_table[2][0]=='o':
                p2w = 1
                break
            elif i == 8:
                print_curr(total_table)
                print("Draw Match !!")
                print("G A M E O V E R")
                break
            i+=1
        else:
            print_curr(total_table)
            print("number ",end = "")
            print(select1 ,end = " ")
            print("is already choosen"+"\n"+"enter another number")
    else:
        print("please enter valid number")
if p1w == 1:
    print_curr(total_table)
    print("player 1 wins")
    print("G A M E O V E R")
elif p2w == 1 :
    print_curr(total_table)
    print("player 2 wins")
    print("G A M E O V E R")                