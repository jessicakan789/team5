def get_yes_no_input(question):
    while True:
        answer = input("{}".format(question)).strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Sorry, invalid input. Please try again")
            continue
