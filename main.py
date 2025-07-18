print("Welcome to treasure island. \nYour mission is to find the treasure.")
question_1 = str(input("Choose a direction, type 'left' or 'right'---> ")).lower()
if question_1 == "left":
    print("Game Over")
elif question_1 == "right":
    question_2 = str(input("Will you swim or wait? Type 'swim' or 'wait'---> ")).lower()
    if question_2 == "swim":
        print("Game Over")
    elif question_2 == "wait":
        last_question = str(input("Their are three doors, you are to pick one out of it. \nType one of this colours to choose, \n'red', 'blue', 'yellow'. ---> ")).lower()
        if last_question == "red":
            print("Game Over")
        elif last_question == "yellow":
            print("Game Over")
        elif last_question == "blue":
            print("You Win!")
        else:
            print("You typed the wrong input, please re-run the code")
    else:
        print("You typed the wrong input, please re-run the code")
else:
    print("You typed the wrong input, please re-run the code")

