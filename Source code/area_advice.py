
def provide_advice(area):
    if area == 'England':
        with open('EnglandAdvice.txt', 'r') as England:
            for i in England:
                print(i)
    elif area == 'Scotland':
        with open('ScotlandAdvice.txt', 'r') as Scotland:
            for i in Scotland:
                print(i)
    elif area == 'Wales':
        with open('WalesAdvice.txt', 'r') as Wales:
            for i in Wales:
                print(i)
    elif area == 'Northern Ireland':
        with open('NIAdvice.txt', 'r') as NI:
            for i in NI:
                print(i)

#provide_advice('Wales')




