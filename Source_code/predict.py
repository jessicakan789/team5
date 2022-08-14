import Levenshtein  # This package can measure the similarity between strings
from yes_no_input import get_yes_no_input


def get_similar_word(list_of_words, input_word, threshold):
    """
    Compares a string to a list of other strings, and returns any that are 'closest' in terms of Levenshtein distance.
    The Levenshtein distance is the number of single character changes to get from one word to another. The match rating
    must be above a certain threshold, otherwise they are disregarded.

    :param list_of_words: (type: list)
    A list of strings to compare against.
    :param input_word: (type: string)
    The string for which we are trying to find similar matches from the above list_of_words.
    :param threshold: (type: float)
    A value between 0 and 1.0 signifying how 'good' the match must be to be returned. 1.0 = full match.
    This can be chosen via trial-and-error, or otherwise a 0.7 threshold works well.

    # NOTE: Makesure all strings are lowercase, with white space removed, before passing values into this function.

    :return:
    If a match can be found, returns a tuple. Tuple contains the probability of the match found (type: float) in its
    first index, and the list of 'closest' words identified from the list_of_words parameter. Usually this list will
    contain just one element, but the code is able to deal with multiple values also.

    Otherwise, if no match can be found, returns None.
    """

    similarities = [Levenshtein.ratio(x,input_word) for x in list_of_words]

    if max(similarities) >= threshold:
        max_idx_list = [idx for idx, val in enumerate(similarities) if val == max(similarities)]
        return max(similarities), [list_of_words[x] for x in max_idx_list]

    return None


def check_similar(prob, list_of_words):
    """
    Provides a "Did you mean..." functionality. Iterates through a list of similar words and prompts the user to either
    accept or reject.

    :param prob: (type: float)
    The probability or 'closeness' of the match, as given by the Levenshtein module in the get_similar_word function.
    :param list_of_words: (type: list)
    List of strings containing all 'similar' words as identified by the Levenshtein module in the get_similar_word
    function. This list will usually contain just 1 element, but the code is able to handle more.

    :return:
    If the user approves one of the similar words, then this word is returned as a string type.

    If not, the function returns a None type.
    """

    for word in list_of_words:

            is_similar = get_yes_no_input("Did you mean '{}'? y/n  (Probability of match: {:.2f})".format(word.title(), prob))

            if is_similar:
                return word
    return None


def get_user_input(given_options, level):
    """
    This function provides the main body of code for requesting the user location input. This calls upon the functions
    get_similar_word and check_similar. The user is given 3 attempts at typing in their location. If the location is not
    recognised (and all similar words are rejected) more than 3 times, the program should exit prematurely.

    :param given_options: (type: list)
    A predefined list of possible inputs. For the COVID calculator app, this will be the locations as fetched from the
    database.
    :param level:
    The location level that the user has chosen. This is either UTLA (upper-tier local authority) or Nation.

    :return:
    If the user input is instantly recognised, this is returned. (type: str)
    Otherwise, if the user approves one of the simialr words, this is returned. (type: str)
    If the number of attempts has been exceeded, there is no return value specified, and so returns a None type.
    """
    attempts = 0

    while attempts < 3:
        user_input = input("Please enter the name of a {}: ".format(level.title())).lower().strip()

        if user_input in given_options:
            return user_input
        else:
            print("Location {} not found!".format(user_input))
            similar = get_similar_word(given_options,user_input,0.7)

            if similar is None:  # no matches ..
                attempts += 1
                print("No similar locations found. Please try again. ({} attempts left) ".format(3-attempts))
                continue
            else:  # matches were found ..
                chosen_word = check_similar(similar[0], similar[1])

                if chosen_word is None:
                    attempts += 1
                    print("You have declined all possible matches. Please try again. ({} attempts left) ".format(3-attempts))
                    continue
                else:
                    return chosen_word




