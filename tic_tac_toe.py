import random
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
def checking(total_table):
    c = 0
    # print("checking")
    if (total_table[0][0] == total_table[0][1] == 'x'):
        if(total_table[0][2]!='o'):
            total_table[0][2] = 'o'
            c = 1
    if(total_table[0][1] == total_table[0][2] == 'x'):
        if(total_table[0][0]!='o'):
            total_table[0][0] = 'o'
            c = 1
    if (total_table[0][0] == total_table[0][2] == 'x'):
        if(total_table[0][1]!='o'):
            total_table[0][1] = 'o'
            c = 1
    if(total_table[1][0] == total_table[1][1] == 'x'):
        if(total_table[1][2]!='o'):
            total_table[1][2] = 'o'
            c = 1
    if (total_table[1][1] == total_table[1][2] == 'x'):
        if(total_table[1][0]!='o'):
            total_table[1][0] = 'o'
            c = 1
    if(total_table[1][0] == total_table[1][2] == 'x'):
        if(total_table[1][1]!='o'):
            total_table[1][1] = 'o'
            c = 1
    if (total_table[2][0] == total_table[2][1] == 'x'):
        if(total_table[2][2]!='o'):
            total_table[2][2] = 'o'
            c = 1
    if(total_table[2][1] == total_table[2][2] == 'x'):
        if(total_table[2][0]!='o'):
            total_table[2][0] = 'o'
            c = 1
    if (total_table[2][0] == total_table[2][2] == 'x'):
        if(total_table[2][1]!='o'):
            total_table[2][1] = 'o'
            c = 1

    #for columns
    if(total_table[0][0] == total_table[1][0] == 'x'):
        if(total_table[2][0]!='o'):
            total_table[2][0] = 'o'
            c = 1
    if (total_table[0][0] == total_table[2][0] == 'x'):
        if(total_table[1][0]!='o'):
            total_table[1][0] = 'o'
            c = 1
    if(total_table[1][0] == total_table[2][0] == 'x'):
        if(total_table[0][0]!='o'):
            total_table[0][0] = 'o'
            c = 1
    if(total_table[0][1] == total_table[1][1] == 'x'):
        if(total_table[2][1]!='o'):
            total_table[2][1] = 'o'
            c = 1
    if (total_table[0][1] == total_table[2][1] == 'x'):
        if(total_table[1][1]!='o'):
            total_table[1][1] = 'o'
            c = 1
    if(total_table[1][1] == total_table[2][1] == 'x'):
        if(total_table[0][1]!='o'):
            total_table[0][1] = 'o'
            c = 1
    if(total_table[0][2] == total_table[1][2] == 'x'):
        if(total_table[2][2]!='o'):
            total_table[2][2] = 'o'
            c = 1
    if (total_table[0][2] == total_table[2][2] == 'x'):
        if(total_table[1][2]!='o'):
            total_table[1][2] = 'o'
            c = 1
    if(total_table[1][2] == total_table[2][2] == 'x'):
        if(total_table[0][2]!='o'):
            total_table[0][2] = 'o'
            c = 1
    #for diagonals
    if(total_table[0][0] == total_table[1][1] == 'x'):
        if(total_table[2][2]!='o'):
            total_table[2][2] = 'o'
            c = 1
    if (total_table[0][0] == total_table[2][2] == 'x'):
        if(total_table[1][1]!='o'):
            total_table[1][1] = 'o'
            c = 1
    if(total_table[1][1] == total_table[2][2] == 'x'):
        if(total_table[0][0]!='o'):
            total_table[0][0] = 'o'
            c = 1
    if(total_table[0][2] == total_table[1][1] == 'x'):
        if(total_table[2][0]!='o'):
            total_table[2][0] = 'o'
            c = 1
    if (total_table[0][2] == total_table[2][0] == 'x'):
        if(total_table[1][1]!='o'):
            total_table[1][1] = 'o'
            c = 1
    if(total_table[1][1] == total_table[2][0] == 'x'):
        if(total_table[0][2]!='o'):
            total_table[0][2] = 'o'
            c = 1
    print_curr(total_table)
    return c
def complex_selection(total_table,p,q):
    # print("enters complex selection")
    if(total_table[p][q] != 'o'):
            total_table[p][q] = 'o'
            print_curr(total_table)
    else:
            c = checking(total_table)
            if(c!=1):
                # print("logical random")
                j = random.choice([0,1,2])
                k = random.choice([0,1,2])
                while total_table[j][k] == 'x' or total_table[j][k] == 'o':
                    j = random.choice([0,1,2])
                    k = random.choice([0,1,2])
                total_table[j][k] = 'o'
                print_curr(total_table)
def computer_selection_for_winning(total_table):
    count = 0
    if (total_table[0][0] == total_table[0][1] == 'o'):
        if(total_table[0][2] !='x'):
            total_table[0][2] = 'o'
            count = 1
    elif(total_table[0][1] == total_table[0][2] == 'o'):
        if(total_table[0][0] !='x'):
            total_table[0][0] = 'o'
            count = 1
    elif (total_table[0][0] == total_table[0][2] == 'o'):
        if(total_table[0][1] !='x'):
            total_table[0][1] = 'o'
            count = 1
    elif(total_table[1][0] == total_table[1][1] == 'o'):
        if(total_table[1][2] !='x'):
            total_table[1][2] = 'o'
            count = 1
    elif (total_table[1][1] == total_table[1][2] == 'o'):
        if(total_table[1][0] !='x'):
            total_table[1][0] = 'o'
            count = 1
    elif(total_table[1][0] == total_table[1][2] == 'o'):
        if(total_table[1][1] !='x'):
            total_table[1][1] = 'o'
            count = 1
    elif (total_table[2][0] == total_table[2][1] == 'o'):
        if(total_table[2][2] !='x'):
            total_table[2][2] = 'o'
            count = 1
    elif(total_table[2][1] == total_table[2][2] == 'o'):
        if(total_table[2][0] !='x'):
            total_table[2][0] = 'o'
            count = 1
    elif (total_table[2][0] == total_table[2][2] == 'o'):
        if(total_table[2][1] !='x'):
            total_table[2][1] = 'o'
            count = 1

    #for columns
    elif(total_table[0][0] == total_table[1][0] == 'o'):
        if(total_table[2][0] !='x'):
            total_table[2][0] = 'o'
            count = 1
    elif (total_table[0][0] == total_table[2][0] == 'o'):
        if(total_table[1][0] !='x'):
            total_table[1][0] = 'o'
            count = 1
    elif(total_table[1][0] == total_table[2][0] == 'o'):
        if(total_table[0][0] !='x'):
            total_table[0][0] = 'o'
            count = 1
    elif(total_table[0][1] == total_table[1][1] == 'o'):
        if(total_table[2][1] !='x'):
            total_table[2][1] = 'o'
            count = 1
    elif (total_table[0][1] == total_table[2][1] == 'o'):
        if(total_table[1][1] !='x'):
            total_table[1][1] = 'o'
            count = 1
    elif(total_table[1][1] == total_table[2][1] == 'o'):
        if(total_table[0][1] !='x'):
            total_table[0][1] = 'o'
            count = 1
    elif(total_table[0][2] == total_table[1][2] == 'o'):
        if(total_table[2][2] !='x'):
            total_table[2][2] = 'o'
            count = 1
    elif (total_table[0][2] == total_table[2][2] == 'o'):
        if(total_table[1][2] !='x'):
            total_table[1][2] = 'o'
            count = 1
    elif(total_table[1][2] == total_table[2][2] == 'o'):
        if(total_table[0][2] !='x'):
            total_table[0][2] = 'o'
            count = 1
    #for diagonals
    elif(total_table[0][0] == total_table[1][1] == 'o'):
        if(total_table[2][2] !='x'):
            total_table[2][2] = 'o'
            count = 1
    elif (total_table[0][0] == total_table[2][2] == 'o'):
        if(total_table[1][1] !='x'):
            total_table[1][1] = 'o'
            count = 1
    elif(total_table[1][1] == total_table[2][2] == 'o'):
        if(total_table[0][0] !='x'):
            total_table[0][0] = 'o'
            count = 1
    elif(total_table[0][2] == total_table[1][1] == 'o'):
        if(total_table[2][0] !='x'):
            total_table[2][0] = 'o'
            count = 1
    elif (total_table[0][2] == total_table[2][0] == 'o'):
        if(total_table[1][1] !='x'):
            total_table[1][1] = 'o'
            count = 1
    elif(total_table[1][1] == total_table[2][0] == 'o'):
        if(total_table[0][2] !='x'):
            total_table[0][2] = 'o'
            count = 1
    if count == 1:
        print_curr(total_table)
    return count

def computer_selection(total_table):
    #for rows
    count = computer_selection_for_winning(total_table)
    if(count == 0):
        if (total_table[0][0] == total_table[0][1] == 'x'):
            p = 0
            q = 2
            complex_selection(total_table,p,q)
        elif(total_table[0][1] == total_table[0][2] == 'x'):
            p = 0
            q = 0
            complex_selection(total_table,p,q)

        elif (total_table[0][0] == total_table[0][2] == 'x'):
            p = 0
            q = 1
            complex_selection(total_table,p,q)
        elif(total_table[1][0] == total_table[1][1] == 'x'):
            p = 1
            q = 2
            complex_selection(total_table,p,q)
        elif (total_table[1][1] == total_table[1][2] == 'x'):
            p = 1
            q = 0
            complex_selection(total_table,p,q)
        elif(total_table[1][0] == total_table[1][2] == 'x'):
            p = 1
            q = 1
            complex_selection(total_table,p,q)
        elif (total_table[2][0] == total_table[2][1] == 'x'):
            p = 2
            q = 2
            complex_selection(total_table,p,q)
        elif(total_table[2][1] == total_table[2][2] == 'x'):
            p = 2
            q = 0
            complex_selection(total_table,p,q)
        elif (total_table[2][0] == total_table[2][2] == 'x'):
            p = 2
            q = 1
            complex_selection(total_table,p,q)

        #for columns
        elif(total_table[0][0] == total_table[1][0] == 'x'):
            p = 2
            q = 0
            complex_selection(total_table,p,q)
        elif (total_table[0][0] == total_table[2][0] == 'x'):
            p = 1
            q = 0
            complex_selection(total_table,p,q)
        elif(total_table[1][0] == total_table[2][0] == 'x'):
            p = 0
            q = 0
            complex_selection(total_table,p,q)
        elif(total_table[0][1] == total_table[1][1] == 'x'):
            p = 2
            q = 1
            complex_selection(total_table,p,q)
        elif (total_table[0][1] == total_table[2][1] == 'x'):
            p = 1
            q = 1
            complex_selection(total_table,p,q)
        elif(total_table[1][1] == total_table[2][1] == 'x'):
            p = 0
            q = 1
            complex_selection(total_table,p,q)
        elif(total_table[0][2] == total_table[1][2] == 'x'):
            p = 2
            q = 2
            complex_selection(total_table,p,q)
        elif (total_table[0][2] == total_table[2][2] == 'x'):
            p = 1
            q = 2
            complex_selection(total_table,p,q)
        elif(total_table[1][2] == total_table[2][2] == 'x'):
            p = 0
            q = 2
            complex_selection(total_table,p,q)
        #for diagonals
        elif(total_table[0][0] == total_table[1][1] == 'x'):
            p = 2
            q = 2
            complex_selection(total_table,p,q)
        elif (total_table[0][0] == total_table[2][2] == 'x'):
            p = 1
            q = 1
            complex_selection(total_table,p,q)
        elif(total_table[1][1] == total_table[2][2] == 'x'):
            p = 0
            q = 0
            complex_selection(total_table,p,q)
        elif(total_table[0][2] == total_table[1][1] == 'x'):
            p = 2
            q = 0
            complex_selection(total_table,p,q)
        elif (total_table[0][2] == total_table[2][0] == 'x'):
            p = 1
            q = 1
            complex_selection(total_table,p,q)
        elif(total_table[1][1] == total_table[2][0] == 'x'):
            p = 0
            q = 2
            complex_selection(total_table,p,q)

k = 1
total_table = []
for i in range(3):
    original_table = []
    for j in range(3):
        original_table.append(k)
        k+=1
    total_table.append(original_table)
i = 0
cpu_count = 0
p1w = 0
p2w = 0
print("please enter no of players want to play")
no_of_players = int(input())
if no_of_players == 1:
    print_curr(total_table)
    while i<9:
                pp = 0 
                
                if(i%2 == 0):
                    print("enter number to choose your place")
                    print("YOUR TURN...")
                    select1 = int(input())
                    if(select1>=1 and select1<=9): 
                        if (select1 == 1 and (total_table[0][0] != 'x' and total_table[0][0] != 'o')) or (select1 == 2 and (total_table[0][1] != 'x' and total_table[0][1] != 'o')) or (select1 == 3 and (total_table[0][2] != 'x' and total_table[0][2] != 'o')) or (select1 == 4 and (total_table[1][0] != 'x' and total_table[1][0] != 'o')) or (select1 == 5 and (total_table[1][1] != 'x' and total_table[1][1] != 'o')) or (select1 == 6 and (total_table[1][2] != 'x' and total_table[1][2] != 'o')) or (select1 == 7 and (total_table[2][0] != 'x' and total_table[2][0] != 'o')) or (select1 == 8 and (total_table[2][1] != 'x' and total_table[2][1] != 'o')) or (select1 == 9 and (total_table[2][2] != 'x' and total_table[2][2] != 'o')):         
                               
                            for j in range(3):
                                for k in range(3):
                                    if total_table[j][k] == select1:
                                        total_table[j][k] = 'x'
                            print_curr(total_table)
                        else:
                            pp = 1
                            print_curr(total_table)
                            print("number ",end = "")
                            print(select1 ,end = " ")
                            print("is already choosen"+"\n"+"enter another number")
                    else:
                        pp = 1
                        print("enter valid number")
                        print_curr(total_table)
                else:
                    print("CPU TURN...")
                    if(cpu_count == 0):
                        # print("random")
                        j = random.choice([0,1,2])
                        k = random.choice([0,1,2])
                        while total_table[j][k] == 'x':
                            j = random.choice([0,1,2])
                            k = random.choice([0,1,2])
                        total_table[j][k] = 'o'
                        cpu_count = 1
                        print_curr(total_table)
                    else:
                        # print("logical")
                        computer_selection(total_table)
                        
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
                if pp == 0:
                    i+=1
    if p1w == 1:
        print_curr(total_table)
        print("YOU WIN")
        print("G A M E O V E R")
    elif p2w == 1 :
        print_curr(total_table)
        print("CPU WIN")
        print("G A M E O V E R")   
elif no_of_players == 2:
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
                                total_table[j][k] = 'x'
                else:
                    for j in range(3):
                        for k in range(3):
                            if total_table[j][k] == select1:
                                total_table[j][k] = 'o'
            
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
else:
    print("please enter valid no of players")             