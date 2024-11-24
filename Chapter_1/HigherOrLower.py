import random

# card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8


# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()  # pop one off the top of the deck and return
    return thisCard


# Pass in a deck and this function return a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # Make a copy of starting deck
    random.shuffle(deckListOut)
    return deckListOut


# Main Code
print("Welcome to Higher or Lower.")
print("You have to choose whether the next card will be higher or lower than the current card")
print("If you get it right you get 20 points, if you get it wrong you lose 15 points")
print("You have 50 points to start")
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # play multiple times
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is: ', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Will the next card be higher or lower than ' + currentCardRank + ' of ' + currentCardSuit + '? enter h or l: ')
        answer = answer.casefold()  # force lower case
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')