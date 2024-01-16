# function to check if a users response was Yes or No. Only accepts 'y' or 'n'.
def descision(response: str):
    if response == "y":
        return "y"
    elif response == "n":
        return "n"
    # traps user in a loop until there response is valid.
    cont = True
    while cont:
        value = input("Re-enter a valid value: ")
        if value == "y":
            cont = False 
            return "y"
        elif value == "n":
            cont = False 
            return "n"