print("Welcome to the Hogwarts Sorting Hat")

trait = input("What trait best describes you? ").lower()

if trait == "brave":
    print("You belong in Gryffindor!")
elif trait == "intelligent":
    print("You belong in Ravenclaw!")
elif trait == "loyal":
    print("You belong in Hufflepuff!")
elif trait == "ambitious":
    print("You belong in Slytherin!")
else:
    print("The sorting hat is confused.")    
