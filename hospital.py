def madlibs():
    number = input("time number: ")
    Measure_of_time = input("Measure of time: ")
    Mode_of_transportation = input("Mode of transportation: ")
    Adjective1 = input("Adjective: ")
    Adjective2 = input("Adjective: ")
    Noun = input("Noun: ")
    color= input("color: ")
    Part_of_body = input("Part of the body: ")
    verb = input("verb: ")


    madlib = f"It was about {number} {Measure_of_time} ago when I came to the hospital in a {Mode_of_transportation}.\nThe hospital is a/an {Adjective1}place, there are a lot of {Adjective2} {Noun}here.\nThere are nurses here who have {color} {Part_of_body} If someone wants to come into my room \nI told them that they have to {verb} first."
    print(madlib)

if __name__== '__main__':
    madlibs()