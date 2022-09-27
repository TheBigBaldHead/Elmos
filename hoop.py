import time
print("Let's play hoop\nYou have 5 seconds for each turn! - Type * instead of hoop!")
hoop = int(input("\nPlease insert hoop cycle length (a number): "))

def is_computer():
    if number%2 == 1:
        return True
    else:
        return False

def is_hoop():
    if number%hoop == 0:
        return True
    else:
        return False

def True_answer(answer):
    try:
        if is_hoop():
            if answer == "*":
                return True
            else:
                return False
        else:
            if int(answer) == number:
                return True
            else:
                return False
    except ValueError:
        answer = input("Wrong! try again: ")

def check_time(current_time):
    if current_time - start_time > 5:
        return False
    else:
        return True

number = 1
while True:
    if is_computer():
        if is_hoop():
            print("*")
        else:
            print(number)
    else:
        start_time = time.time()
        answer = input("")
        while not True_answer(answer) and check_time(time.time()):
            answer = input("Wrong! try again: ")
        if check_time(time.time()) == False:
            print("Time is over. you lost!")
            break
    number += 1
