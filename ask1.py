import random


Empty="E1 E2 E3"
rings=["L","M","S"]
row1=[]
row2=[]
row3=[]
moves_sum =0

for metritis in range(100):

    Large= 9
    Medium= Large
    Small= Large
    moves=0
    for i in range(3):
        row1.append(Empty)
        row2.append(Empty)
        row3.append(Empty)
    table=[row1,row2,row3]
    cell=5
    row=5
    win = False
    while win == False:



        def pick_ring():
            ring=random.choice(rings)
            return ring

        def pick_place(place):
            place=random.randrange(3)
            return place

        def make_move(table,row,cell,seat,ring):
            if (ring == 'L' and Large > 0) or (ring == 'M' and Medium > 0) or (ring == 'S' and Small > 0):
                if table[row][cell] == Empty or table[row][cell][0] != ring or table[row][cell][2] != ring or table[row][cell][4] != ring:
                    table[row][cell] = table[row][cell].replace(seat,ring)
            return table


        def checkwin(win,table):
            for r in range(2):
                if table[r][0][0] == 'L' and table[r][1][0] == 'L' and table[r][2][0] == 'L':
                    win = True
                    break
                elif table[r][0][2] == 'M' and table[r][1][2] == 'M' and table[r][2][2] == 'M':
                    win = True
                    break
                elif table[r][0][4] == 'S' and table[r][1][4] == 'S' and table[r][2][4] == 'S':
                    win = True
                    break
            if win != True :
                for c in range(2):
                    if table[0][c][0] == 'L' and table[1][c][0] == 'L' and table[2][c][0] == 'L':
                        win = True
                        break
                    elif table[0][c][2] == 'M' and table[1][c][2] == 'M' and table[2][c][2] == 'M':
                        win = True
                        break
                    elif table[0][c][4] == 'S' and table[1][c][4] == 'S' and table[2][c][4] == 'S':
                        win = True
                        break
            if win != True:
                if table[0][0][0] == 'L' and table[1][1][0] == 'L' and table[2][2][0] == 'L':
                    win = True
                elif table[0][0][2] == 'M' and table[1][1][2] == 'M' and table[2][2][2] == 'M':
                    win = True
                elif table[0][0][4] == 'S' and table[1][1][4] == 'S' and table[2][2][4] == 'S':
                    win = True
            if win != True:
                if table[0][2][0] == 'L' and table[1][1][0] == 'L' and table[2][0][0] == 'L':
                    win = True
                elif table[0][2][2] == 'M' and table[1][1][2] == 'M' and table[2][0][2] == 'M':
                    win = True
                if table[0][2][4] == 'S' and table[1][1][4] == 'S' and table[2][0][4] == 'S':
                    win = True
            if win != True :
                for c in range(2):
                    if table[0][c][0] == 'L' and table[1][c][2] == 'M' and table[2][c][4] == 'S':
                        win = True
                        break
                    elif table[0][c][4] == 'S' and table[1][c][2] == 'M' and table[2][c][0] == 'L':
                        win = True
                        break
            if win != True :
                for r in range(2):
                    if table[r][0][0] == 'L' and table[r][1][2] == 'M' and table[r][2][4] == 'S':
                        win = True
                        break
                    elif table[r][0][4] == 'S' and table[r][1][2] == 'M' and table[r][2][0] == 'L':
                        win = True
                        break
            if win != True:
                if table[0][0][0] == 'L' and table[1][1][2] == 'M' and table[2][2][4] == 'S':
                    win = True
                elif table[0][0][4] == 'S' and table[1][1][2] == 'M' and table[2][2][0] == 'L':
                    win = True
            if win != True:
                if table[0][2][0] == 'L' and table[1][1][2] == 'M'  and table[2][0][4] == 'S':
                    win = True
            elif table[0][2][4] == 'S' and table[1][1][2] == 'M'  and table[2][0][0] == 'L':
                win = True
            return win




        ring=pick_ring()
        row=pick_place(row)
        cell=pick_place(cell)
        prin= table[row][cell]

        if ring == "L":
            seat='E1'
        elif ring == "M":
            seat='E2'
        elif ring == "S":
            seat ='E3'
        make_move(table,row,cell,seat,ring)
        meta=table[row][cell]

        if prin == meta:
            while prin == meta:
                    ring=pick_ring()
                    row=pick_place(row)
                    cell=pick_place(cell)
                    prin= table[row][cell]

                    if ring == "L":
                        seat='E1'
                    elif ring == "M":
                        seat='E2'
                    elif ring == "S":
                        seat ='E3'
                    make_move(table,row,cell,seat,ring)
                    meta=table[row][cell]
        moves = moves +1
        if ring == 'L':
            Large = Large - 1
        elif ring == 'M':
            Medium = Medium - 1
        elif ring == 'S':
            Small = Small - 1
        win=checkwin(win,table)
    moves_sum = moves_sum + moves
print("Μεσος ορος κινησεων:", moves_sum / 100)
