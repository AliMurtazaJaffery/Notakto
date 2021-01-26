ali={'A':[[0,1,2],[3,4,5],[6,7,8]],'B':[[0,1,2],[3,4,5],[6,7,8]],'C':[[0,1,2],[3,4,5],[6,7,8]]}
def printboard(dictionary):
    for key in dictionary:
        if key==list(ali.keys())[-1]:
            print(key)
        else:
            print(f'{key:<7}',end='')
            
    counter1=0
    for e,f,g in dictionary.values():
        counter1+=1
        count=0
        for y in e:
            count+=1
            if counter1==len(dictionary) and count==3:
                print(y)
            else:
                
                if count%3==0:
                    print( y,end='  ')
                else:
                    print(y,end=' ')
    counter2=0
    for e,f,g in dictionary.values():
        count=0
        counter2+=1
        for y in f:
            count+=1
            if counter2==len(dictionary) and count==3:
                print(y)
            else:
                if count%3==0:
                    print( y,end='  ')
                else:
                    print(y,end=' ')
    counter3=0
    for e,f,g in dictionary.values():
        count=0
        counter3+=1
        for y in g:
            count+=1
            if counter3==len(dictionary) and count==3:
                print(y)
            else:    
                if count%3==0:
                    print( y,end='  ')
                else:
                    print(y,end=' ')
    return
def check_row(dictionary):
    for i in dictionary:
        for x in dictionary[i]:
            if x[0:2]==x[1:3]:
                del dictionary[i]
                return dictionary
    else:
        return 'None'
def check_column(dictionary):
    for i in dictionary:
        for x in range(3):
            if dictionary[i][0][x]==dictionary[i][1][x] and dictionary[i][1][x]==dictionary[i][2][x]:
                del dictionary[i]
                return dictionary
    else:
        return 'None'
def check_diagonal(dictionary):
    for i in dictionary:
        if dictionary[i][0][0]==dictionary[i][1][1] and dictionary[i][1][1]==dictionary[i][2][2]:
            del dictionary[i]
            return dictionary
        elif dictionary[i][0][2]==dictionary[i][1][1] and dictionary[i][1][1]==dictionary[i][2][0]:
            del dictionary[i]
            return dictionary
    else:
        return 'None'
def replace(dictionary,position,iteration):
    
    for i, x in enumerate(dictionary[iteration]):
        for j, a in enumerate(x):
            if a==position:
                dictionary[iteration][i][j] ='X'
                return dictionary
#functions specifically for AI
import copy
def check_row_AI(dictionary):#THIS DOESN'T DELETE DICTIONARY
    for i in dictionary:
        for x in dictionary[i]:
            if x[0:2]==x[1:3]:
                return dictionary
    return 'None'
def check_column_AI(dictionary):
    for i in dictionary:
        for x in range(3):
            if dictionary[i][0][x]==dictionary[i][1][x] and dictionary[i][1][x]==dictionary[i][2][x]:
                return dictionary
    else:
        return 'None'
def check_diagonal_AI(dictionary):
    for i in dictionary:
        if dictionary[i][0][0]==dictionary[i][1][1] and dictionary[i][1][1]==dictionary[i][2][2]:
            return dictionary
        elif dictionary[i][0][2]==dictionary[i][1][1] and dictionary[i][1][1]==dictionary[i][2][0]:
            return dictionary
    else:
        return 'None'
def search(dictionary):
    count=0
    for k in dictionary:
        for i, x in enumerate(dictionary[k]):
            for j, y in enumerate(x):
                if check_column_AI(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))!='None' or check_row_AI(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))!='None' or check_diagonal_AI(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))!='None':
                    count+=1
                    if count==1:
                        move=k+str(dictionary[k][i][j])
                        return move
    else:
        return 'None'
def new_search(dictionary,k):
    for i, x in enumerate(dictionary[k]):
            for j, y in enumerate(x):
                if check_column_AI(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))!='None' or check_row_AI(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))!='None' or check_diagonal_AI(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))!='None':
                    move=k+str(dictionary[k][i][j])
                    return move
    else:
        return 'None'
    
def boot_trap(dictionary,input_player2):
    boottrap_dic={0:[5,7],1:[6,8],2:[3,7],3:[2,8],5:[0,6],6:[1,5],7:[0,2],8:[1,3]}
    board_position=int(input_player2[1])
    board=input_player2[0]
    for i in boottrap_dic:
        if board_position==i:
            if any(boottrap_dic[i][0] in x for x in dictionary[board]):
            #print(check_row_AI(replace(copy.deepcopy(dictionary),boottrap_dic[i][0],input_player2[0])))
                if check_row_AI(replace(copy.deepcopy(dictionary),boottrap_dic[i][0],input_player2[0]))=='None' and check_column_AI(replace(copy.deepcopy(dictionary),boottrap_dic[i][0],input_player2[0]))=='None' and check_diagonal_AI(replace(copy.deepcopy(dictionary),boottrap_dic[i][0],input_player2[0]))=='None':
                    return input_player2[0]+str(boottrap_dic[i][0])
            else:
                return input_player2[0]+str(boottrap_dic[i][1])
def double_x_trap(dictionary):
    list=[[0,5,7],[0,7,5],[5,0,7],[5,7,0],[7,0,5],[7,5,0],[2,3,7],[2,7,3],[3,2,7],[3,7,2],[7,2,3],[7,3,2],[6,1,5],[6,5,1],[1,6,5],[1,5,6],[5,6,1],[5,1,6],[8,1,3],[8,3,1],[1,8,3],[1,3,8],[3,8,1],[3,1,8]]
    for k in dictionary:
        for a,b,c in list:
            if not any(a in x for x in dictionary[k]):
                if not any(b in y for y in dictionary[k]):
                    return k+str(c)
    else:
        return 'None'
def new_double_x_trap(dictionary,k):
    list=[[0,5,7],[0,7,5],[5,0,7],[5,7,0],[7,0,5],[7,5,0],[2,3,7],[2,7,3],[3,2,7],[3,7,2],[7,2,3],[7,3,2],[6,1,5],[6,5,1],[1,6,5],[1,5,6],[5,6,1],[5,1,6],[8,1,3],[8,3,1],[1,8,3],[1,3,8],[3,8,1],[3,1,8]]
    for a,b,c in list:
        if not any(a in x for x in dictionary[k]):
            if not any(b in y for y in dictionary[k]):
                return k+str(c)
    else:
        return 'None'
    
def attack_1(dictionary):
    count=0
    list=[[0,5,7],[2,3,7],[6,1,5],[8,1,3]]
    for i in dictionary:
        for a,b,c in list:
            count+=1
            if not any(a in x for x in dictionary[i]):
                if not any(b in y for y in dictionary[i]):
                    if not any(c in z for z in dictionary[i]):
                        if count==1:
                            return i+str(8)
                        if count==2:
                            return i+str(6)
                        if count==3:
                            return i+str(2)
                        if count==4:
                            return i+str(0)
    else:
        return 'None'
#2nd move is safety search
def safety_search(dictionary):
    for k in dictionary:
        for i, x in enumerate(dictionary[k]):
            for j, y in enumerate(x):
                if dictionary[k][i][j]!='X':
                    if check_column(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))=='None' and check_row(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))=='None' and check_diagonal(replace(copy.deepcopy(dictionary),dictionary[k][i][j],k))=='None':
                        
                        move=k+str(dictionary[k][i][j])
                        return move
    else:
        return 'None'
def count_x(dictionary):
    count=0
    for k in dictionary:
        for i, x in enumerate(dictionary[k]):
            for j, y in enumerate(x):            
                if dictionary[k][i][j]=='X':                
                    count+=1
    return count
def new_count_x(dictionary,k):
    count=0
    for i, x in enumerate(dictionary[k]):
        for j, y in enumerate(x):            
            if dictionary[k][i][j]=='X':                
                count+=1
    return count
    
def early_sacrifice(dictionary,previous_turn):  
    count=0
    for k in dictionary:
        for i, x in enumerate(dictionary[k]):
            for j, y in enumerate(x):            
                if dictionary[k][i][j]=='X':                
                    count+=1
    if count==1:
        for k in dictionary:
            for i in range (9):
                if not any(i in x for x in dictionary[k]):
                    if i==0:
                        return k+str(8)
                    if i==1:
                        return k+str(7)
                    if i==2:
                        return k+str(6)
                    if i==3:
                        return k+str(5)
                    if i==5:
                        return k+str(3)
                    if i==6:
                        return k+str(2)
                    if i==7:
                        return k+str(1)
                    if i==8:
                        return k+str(0)
    if count>1:
        i=int(previous_turn[1])
        if i==0:
            return k+str(8)
        if i==1:
            return k+str(7)
        if i==2:
            return k+str(6)
        if i==3:
            return k+str(5)
        if i==5:
            return k+str(3)
        if i==6:
            return k+str(2)
        if i==7:
            return k+str(1)
        if i==8:
            return k+str(0)
def count_centre_x(dictionary):
    count_x=0
    for k in dictionary:
        if dictionary[k][1][1]=='X':
                board_1=k
                count_x+=1                
    if count_x==2:
        return 2,'lol'
    else:
        return count_x,board_1
def AI(dictionary,memory):
    global board
    global board_2
    
    counter=0
    while len(dictionary)==3:
        if count_x(ali)==0:
            return 'C'+str(4),memory
        if count_x(ali)==2:
            if search(dictionary)!='None':
                return search(dictionary) ,memory
            else:    
                if not any ('X' in i for i in dictionary['A']):
                    return 'A'+str(4),memory
                else:
                    return 'B'+str(4),memory
        if count_x(ali)==4:
            if search(dictionary)!='None':
                return search(dictionary),memory
            else:
                return double_x_trap(dictionary),memory
        if count_x(ali)==6:
            return search(dictionary),memory
    while len(dictionary)==2:
        if count_x(dictionary)==1:
            for k in dictionary:
                if dictionary[k][1][1]!='X':
                    if not any ('X' in i for i in dictionary[k]):
                        return k+str(4),'None'
        if count_x(dictionary)==3:
            centre_x,board=count_centre_x(dictionary)
            if centre_x==2:
                return search(dictionary),'None'
            else:
                for i in dictionary:
                    if i!=board:
                        board_2=i
                if move[0]==board:
                    return boot_trap(ali,move),'None'
                else:
                    if search(ali)!='None':
                        return search(ali),'None'
                    else:
                        return double_x_trap(ali),'trap'
        if count_x(dictionary)==5:
            if move[0]==board:
                return boot_trap(ali,move),'None'
            else:
                if new_search(dictionary,board_2)!='None':                    
                    return new_search(dictionary,board_2),'None'
                if new_count_x(dictionary,board_2)==2 and new_double_x_trap(dictionary,board_2)!='None':
                    return new_double_x_trap(dictionary,board_2),'None'
        if count_x(dictionary)==7:
            if move[0]==board:
                return boot_trap(ali,move),'None'
            else:
                if new_search(dictionary,board_2)!='None':
                    return new_search(dictionary,board_2),'None'
    while len(dictionary)==1:
        print(memory)
        if count_x(ali)==1:
            return early_sacrifice(ali,move),'early_sacrifice'
        if memory=='early_sacrifice':
            return early_sacrifice(ali,move),'early_sacrifice'
        if count_x(ali)==2:
            for i in dictionary:
                if dictionary[i][1][1]=='X':
                    return boot_trap(ali,move),'boot_trap'            
        if memory=='boot_trap':
            return boot_trap(ali,move),'boot_trap'
        if count_x(ali)==3:
            if attack_1(ali)!='None':
                return attack_1(ali),'final_step'
        if memory=='final_step':
            return safety_search(ali),'None'        
def get_turn_player(dictionary):
    spot=input('Player 2: ')
    Board=spot[0]
    location=int(spot[1])
    for i in dictionary:
        if i==Board:
            replace(dictionary,location,i)
            return dictionary,spot
def get_turn_AI(dictionary,memory,opponents_move):
    spot,ai_memory=AI(ali,memory)
    print('Player 1:', spot)
    Board=spot[0]
    location=int(spot[1])
    for i in dictionary:
        if i==Board:
            replace(dictionary,location,i)
            return dictionary,ai_memory  
ai_memory=None
move=None
turn='Player 1'
while len(ali)!=0:
    printboard(ali)
    if turn=='Player 1':
        ali,ai_memory=get_turn_AI(ali,ai_memory,move)
    else:
        ali,move=get_turn_player(ali)
    check_row(ali)
    check_column(ali)
    check_diagonal(ali)
    if turn=='Player 1':
        turn='Player 2'
    else:
        turn='Player 1'
if turn=='Player 1':
    print('Player 1 wins game')
if turn=='Player 2':
    print('Player 2 wins game')

