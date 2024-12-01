# Sergei Chaparin

yourRating = input("Please enter your rating of Intouchables (1-5): ")
myRating = input("I will enter mine: ")
print("Your rating is", yourRating, "and my rating is", myRating)
ratingDifference = int(myRating) - int(yourRating)
if myRating > yourRating:
    print(ratingDifference)
    print("You liked the movie less than I did by", abs(ratingDifference), "points.")
elif myRating < yourRating:
    print(ratingDifference)
    print("You liked the movie more than I did by", abs(ratingDifference), "points.")
else:
    print("We like the movie the same!")
