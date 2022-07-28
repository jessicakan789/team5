import Levenshtein


# This package can measure the similarity between strings

# # These locations would be fetched from the database of upper-tier local authorities
# locations = ['salford','barnet','barnsley', 'bath', 'bolton', 'blackpool','camden','dorset', 'sefton', 'sandwell']


# Make sure strings are all lowercase, remove white space etc., before using this function
def get_similar_word(list_of_words, input_word, threshold):
    # returns a tuple - (probability, [list of similar words])
    # list contains words, from given set, which are 'closest' to the input word
    # if no words are close enough (decided by threshold parameter) returns None
    similarities = [Levenshtein.ratio(x,input_word) for x in list_of_words]

    if max(similarities) >= threshold:
        max_idx_list = [idx for idx, val in enumerate(similarities) if val == max(similarities)]
        return max(similarities),[list_of_words[x] for x in max_idx_list]

    return None


# Can add exit functionality here if required ...
def check_similar(prob, list_of_words):
    # Iterates through each item in the list to provide a "Did you mean..." functionality to the user
    # The parameters prob and list_of_words should be fetched from the get_similar_word function
    for word in list_of_words:
        while True:
            is_similar = input("Did you mean '{}'? y/n  (Probability of match: {:.2f})".format(word, prob))
            if is_similar.lower().strip() == "y":
                return word
            elif is_similar.lower().strip() == "n":
                break
            else:
                print("Invalid input. Please type 'y' for yes or 'n' for no.")
                continue
    return None


def get_user_input(given_options):
    while True:
        user_input = input("Please enter the name of a UTLA: ").lower().strip()
        # match format to however locations are in database... or make everything lower for ease

        if user_input in given_options:
            print("Location {} found!".format(user_input))
            return user_input
        else:
            print("Location {} not found!".format(user_input))
            similar = get_similar_word(given_options,user_input,0.7)

            if similar is None:  # no matches ..
                print("No similar locations found. Please try again.")
                continue
            else:  # matches were found ..
                chosen_word = check_similar(similar[0], similar[1])

                if chosen_word is None:
                    print("You have declined all possible matches. Please try again.")
                    continue
                else:
                    return chosen_word


# print("Chosen location is : " + get_user_input(locations))  # RETURNS MATCHED WORD



