import random

#setting the difficulty of the games and its datas
difficulties = {"easy": 9, "normal": 16, "hard": 24}
difficulty = input("Choose the difficulty: easy or normal or hard. ").lower()
while difficulty not in difficulties:
    difficulty = input("Choose the difficulty: easy or normal or hard. ").lower()
difficulty_mines = {"easy": 10, "normal": 40, "hard": 99}
mine_count = difficulty_mines[difficulty]
length = difficulties[difficulty]
#making the lists
mines = list()
flags = list()
front_map = [["▫" for column in range(length)] for row in range(length)]
back_map = [["" for column in range(length)] for row in range(length)]
zero_map = [[False for column in range(length)] for row in range(length)]
was_number = [[False for column in range(length)] for row in range(length)]
#producing random positions in the map for mines
for _ in range(mine_count):
    new_mine = random.randint(1,length**2)
    while new_mine in mines:
        new_mine = random.randint(1,length**2)
    mines.append(new_mine)
mines.sort()

def draw(map):
    """This function makes a visual version of the map, either front or back"""
    print()
    for number in range(1,length+1):
        print(number,end=" ")
    print()
    i = 1
    for row in map:
        for column in row:
            print(column,end=" ")
        print(i)
        i += 1
    print()

def convert_to_position(row, column):
    """This function takes row and column and turn them into a position"""
    return row*length + column + 1

def convert_to_order(position):
    """This function takes position and turns it into a tuple of row and column"""
    row = 0
    while position not in range(1,length+1):
        position -= length
        row += 1
    column = position-1
    return row, column

def edit_sides(row,column):
    """This function takes row and column and corrects the positions around it in the map"""
    around_positions = [-length-1,-1,length-1,-length,length,-length+1,+1,length+1]
    row += 1
    column += 1
    #right and left sides
    if column == length:
        for around_position in [-length+1,1,length+1]:
            if around_position in around_positions:
                around_positions.remove(around_position)
    elif column == 1:
        for around_position in [-length-1,-1,length-1]:
            if around_position in around_positions:
                around_positions.remove(around_position)
    #up and bottom
    if row == length:
        for around_position in [length-1,length,length+1]:
            if around_position in around_positions:
                around_positions.remove(around_position)
    elif row == 1:
        for around_position in [-length-1,-length,-length+1]:
            if around_position in around_positions:
                around_positions.remove(around_position)
    return around_positions

def get_number(position):
    """This function takes position and returns the number and mines around it"""
    number = 0
    row, column = convert_to_order(position)
    around_positions = edit_sides(row, column)
    for around_position in around_positions:
        checking_position = position + around_position
        if checking_position in mines:
            number += 1
    return number

def zero(position,back_position):
    """this function runs when stepped position is 0 and reveals all numbers around it in the map"""
    main_row, main_column = convert_to_order(position)
    zero_map[main_row][main_column] = True
    around_positions = edit_sides(main_row,main_column)

    if -back_position in around_positions:
        around_positions.remove(-back_position)

    for around_position in around_positions:
        new_position = position + around_position
        row, column = convert_to_order(new_position)
        if front_map[row][column] != '!':
            front_map[row][column] = back_map[row][column]
            was_number[row][column] = True
        '''Also if any of the revealed numbers be 0, it occures again'''
        if (back_map[row][column] == 0) and zero_map[row][column] == False:
            zero(new_position,around_position)
            zero_map[row][column] = True
#inserting the mines from the list to the map
for mine in mines:
    row, column = convert_to_order(mine)
    back_map[row][column] = "*"
#revealing the number of all positions in the back_map
for position in range(length**2):
    position+=1
    row,column = convert_to_order(position)
    if back_map[row][column] != "*":
        back_map[row][column] = get_number(position)
#the main game starts here
while True:
    around_positions = [-length-1,-1,length-1,-length,length,-length+1,+1,length+1]
    draw(front_map)
    mode = input("Type 's' to step, or type 'f' to flag: ")
    while mode not in ['s','f']:
        mode = input("Type 's' to step, or type 'f' to flag: ")

    user_column = int(input("Column: "))-1
    while user_column not in range(length):
            user_column = int(input("Column: "))-1

    user_row = int(input("Row: "))-1
    while user_row not in range(length):
            user_row = int(input("Row: "))-1

    if mode == 'f':
        if front_map[user_row][user_column] == '!':
            flags.remove(convert_to_position(user_row,user_column))
            if was_number[user_row][user_column]:
                front_map[user_row][user_column] = back_map[user_row][user_column]
            else:
                front_map[user_row][user_column] = "▫"
        else:
            front_map[user_row][user_column] = '!'
            flags.append(convert_to_position(user_row,user_column))
    elif mode == 's':
        if back_map[user_row][user_column] == '*':
            print("Boom, roasted. you stepped on a mine!")
            draw(back_map)
            break
        else:
            if front_map[user_row][user_column] in range(9):
                print("choose again!")
                continue
            elif front_map[user_row][user_column] == '!':
                print("You have flagged here! choose somewhere else!")
                continue
            else:
                front_map[user_row][user_column] = back_map[user_row][user_column]
                if back_map[user_row][user_column] == 0:
                    around_positions = edit_sides(user_row,user_column)
                    zero(convert_to_position(user_row,user_column),0)
    flags.sort()
    if flags == mines:
        print("Congrats, you won the game =)")
        break
