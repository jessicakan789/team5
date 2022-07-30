import Levenshtein  # This package can measure the similarity between strings


# Make sure strings are all lowercase, remove white space etc., before using this function
def get_similar_word(list_of_words, input_word, threshold):
    # returns a tuple - (probability, [list of similar words])
    # list contains words, from given set, which are 'closest' to the input word
    # if no words are close enough (decided by threshold parameter) returns None
    similarities = [Levenshtein.ratio(x, input_word) for x in list_of_words]

    if max(similarities) >= threshold:
        max_idx_list = [idx for idx, val in enumerate(similarities) if val == max(similarities)]
        return max(similarities), [list_of_words[x] for x in max_idx_list]

    return None


def get_user_input(given_options):
    while True:
        user_input = input("Please enter area name: ").lower().strip()
        # match format to however locations are in database... or make everything lower for ease

        if user_input in given_options:
            print("Location {} found!".format(user_input))
            return user_input
        else:
            print("Location {} not found!".format(user_input))
            similar = get_similar_word(given_options, user_input, 0.7)

            if similar is None:  # no matches ..
                print("No similar locations found. Please try again.")
                continue
            else:  # matches were found ..

                for word in similar[1]:
                    is_similar = input("Did you mean '{}'? y/n  (Probability of match: {:.2f})".format(word, similar[0]))
                    if is_similar.lower().strip() == "y":
                        return word
                    elif is_similar.lower().strip() == "n":
                        pass

                    # TO DO: deal with invalid inputs here !!!

                print("You have declined all possible matches. Please try again.")
                continue

