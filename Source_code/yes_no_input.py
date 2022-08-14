def get_yes_no_input(question):
    """
    This function is used to request a yes/no input in a robust way. Any invalid inputs are not accepted, and the
    user will be prompted to try again.

    :param question: (type: str) This is the question that will be displayed to the user as a prompt for the yes/no
    input.

    :return: True/False (type: bool) This signifies how the user answered the question. A YES input will return a TRUE
    value, whereas a NO input will return FALSE.

    """
    while True:
        answer = input("{}".format(question)).strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Sorry, invalid input. Please try again")
            continue
