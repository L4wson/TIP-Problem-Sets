# Write a function called blackjack() that takes an integer score as a parameter.
# If score equals 21, print "Blackjack!".
# If score is greater than 21, print "Bust!".
# If score is greater than or equal to 17 and less than 21, print "Nice hand!".
# If score is less than 17, print "Hit me!". 

def blackjack(score):
    if  score > 21:
        print("Bust!")
    elif score < 17:
        print("Hit me!")
    elif score >= 17 and score < 21:
        print("Nice Hand!")
    else:
        print("Blackjack!")

blackjack(24)
blackjack(17)
blackjack(21)
blackjack(10)
