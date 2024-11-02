gamesWonByA = int(input("What's the number of games won by player A?: "))
gamesWonByB = int(input("What's the number of games won by player B?: "))

if (gamesWonByA >= 6 and gamesWonByA - gamesWonByB >= 2) or (gamesWonByA == 7 and gamesWonByB == 6):
    print("A won.")
elif (gamesWonByB >= 6 and gamesWonByB - gamesWonByA >= 2) or (gamesWonByB == 7 and gamesWonByA == 6):
    print("B won.")
elif (gamesWonByA < 0 or gamesWonByB < 0 or
      (gamesWonByA > 7 and gamesWonByB < 5) or (gamesWonByB > 7 and gamesWonByA < 5) or 
      (gamesWonByA > 6 and gamesWonByB > 6)):
    print("Invalid.")
else:
    print("Still ongoing.")