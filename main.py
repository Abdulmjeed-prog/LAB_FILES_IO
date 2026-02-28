
def boolconv(user_input):
    if user_input.lower() == "y":
        user_input = True
    elif user_input.lower() == "n":
        user_input = False
    return user_input


while True:
    user_input = input("do you want to add a new To-Do item?(y or no or exit):  ")
    user_input = boolconv(user_input)
    if user_input == True:
        file = open("to-do.txt","a",encoding="utf-8")
        content = input("Write your txt: \n")
        file.write(f"{content}\n")
        file.close()
    elif user_input == False:
        while True:
            listitems = input("do you want to list your To-Do items: ")
            listitems = boolconv(listitems)
            if listitems == True:
                file = open("to_do.txt","r",encoding="utf-8")
                content = file.read()
                print(content)
                file.close()
            elif listitems == False:
                break
            else:
                print("Invalid choice")
    elif user_input.lower() == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    else:
        print("Invalid choice")
