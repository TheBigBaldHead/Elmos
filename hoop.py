import time
print("Let's play hoop\nYou have 5 seconds for each turn! - Type * instead of hoop!")
hoop = int(input("\nPlease insert hoop cycle length (a number): "))

def computer():
    if number%2 == 1:
        return True
    else:
        return False

def is_hoop():
    if number%hoop == 0:
        return True
    else:
        return False

def True_answer():
    if not is_hoop():
        if int(answer) == number:
            return True
        else:
            return False
    elif is_hoop():
        if answer == "*":
            return True
        else:
            return False
number = 1
while True:
    if computer():
        if is_hoop():
            print("*")
        else:
            print(number)
    else:
        start_time = time.time()
        answer = input("")
        while not True_answer():
            answer = input("Wrong! try again: ")
        if time.time() - start_time > 5:
            print("Time is over. you lost!")
            break
    number += 1
