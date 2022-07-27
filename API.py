import requests
import json
import Levenshtein  # This package can measure the similarity between strings


# These locations would be fetched from the database of upper-tier local authorities
locations = ['salford','barnet','barnsley', 'bath', 'bolton', 'blackpool','camden','dorset', 'sefton', 'sandwell']


# Make sure strings are all lowercase, remove white space etc., before using this function
def get_similar_word(list_of_words, input_word, threshold):
    # returns a tuple - (probability, [list of similar words])
    # list contains words, from given set, which are 'closest' to the input word
    # if no words are close enough (decided by threshold parameter) returns None
    similarities = [Levenshtein.ratio(x,input_word) for x in locations]

    if max(similarities) >= threshold:
        max_idx_list = [idx for idx, val in enumerate(similarities) if val == max(similarities)]
        return max(similarities), [locations[x] for x in max_idx_list]

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
            similar = get_similar_word(locations, user_input, 0.7)

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


def get_rate_by_location(location):
    structure = {
        "date": "date",
        "name": "areaName",
        "code": "areaCode",
        "dailyCases": "newCasesByPublishDate",
        "cumulativeCases": "cumCasesByPublishDate",
        "dailyDeaths": "newDeaths28DaysByPublishDate",
        "cumulativeDeaths": "cumDeaths28DaysByPublishDate"
    }

    structure_params = {
        "structure": json.dumps(structure, separators=(",", ":"))
    }

    result = requests.get(
        'https://api.coronavirus.data.gov.uk/v1/data?filters=areaName={};areaType=utla&structure='
        .format(location),
        params=structure_params
    )

    latest = 0

    for i in range(0, 7):
        latest += int(result.json()['data'][i]['dailyCases'])

    print('weeklyCases:', latest)

    if latest <= 100:
        print("Your risk of getting COVID is LOW")
        print("We recommend you wash your hands frequently")
    if 100 < latest <= 400:
        print("Your risk of getting COVID is MEDIUM")
        print("We recommend you wear a mask")
    if latest > 400:
        print("Your risk of getting COVID is HIGH")
        print("We recommend you take a LFD")


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('############################')
    print()

    try:
        location = get_user_input(locations)  # RETURNS MATCHED WORD
        if location.isnumeric():
            raise ValueError

    except ValueError:
        print("Sorry wrong input format. Please try again")
        exit()

    print()

    get_rate_by_location(location.title())

    print()
    print('Keep smiling and carry on!')


if __name__ == '__main__':
    run()

# Example
# black pool
