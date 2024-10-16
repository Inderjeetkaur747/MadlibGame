def madlibs():
    noun1 = input("noun: ")
    noun2 = input("noun: ")
    adjective1 = input("adjective(feeling): ")
    verb1 = input("verb: ")
    adjective2 = input("adjective(feeling): ")
    animal1 = input("animal: ")
    verb2 = input("verb: ")
    color = input("color: ")
    verb3 = input("verb(ending in ing): ")


    madlib = f'This weekend I am going camping with {noun1} \n I packed my lantern, sleeping bag, and{noun2}.\
    I am so {adjective1} to {verb1} in a tent.\n I am {adjective2} we might see a {animal1}, they are kind of dangerous.\n We are going to hike, fish, and {verb2}.\n I have heard that the {color} lake is great for {verb3}.'

    print(madlib)
# madlibs()