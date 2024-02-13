import random

class Deck:
    def __init__(self):
        self.Cards = []
        Ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        Suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

        Ranks = [ 
                {"x_in_rank": "1", "matched_value": 1},
                {"x_in_rank": "2", "matched_value": 2},
                {"x_in_rank": "3", "matched_value": 3},
                {"x_in_rank": "4", "matched_value": 4},
                {"x_in_rank": "5", "matched_value": 5},
                {"x_in_rank": "6", "matched_value": 6},
                {"x_in_rank": "7", "matched_value": 7},
                {"x_in_rank": "8", "matched_value": 8},
                {"x_in_rank": "9", "matched_value": 9},
                {"x_in_rank": "10", "matched_value": 10},
                {"x_in_rank": "J", "matched_value": 10},
                {"x_in_rank": "Q", "matched_value": 10},
                {"x_in_rank": "K", "matched_value": 10},
                {"x_in_rank": "A", "matched_value": 11}
        ]

        for x_in_suit in Suits:
            for x_in_ranks in Ranks:
                self.Cards.append([x_in_suit, x_in_ranks])
            
    def shuffle(self):
        if len(self.Cards) > 1:
            random.shuffle(self.Cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.Cards) > 0:
                card = self.Cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Card:
    def __init__(self, Suits, Ranks):
        self.suit = Suits
        self.rank = Ranks
    def __str__(self):
        return self.Ranks["rank"] + " of " + self.Suits 
    

card1 = Card("Hearts", {"x_in_rank": "J", "matched_value": 10})
print (card1)

#def card_values():
    

#def calculate_score():
    #if sum.User_c



#BlackjackGame = input("Hello welcome to the game of Blackjack, would you like me to explain the rules? Please type either Yes or No: ")
#if  BlackjackGame == "Yes":
        #print("The rules of Blackjack is simple in summary when all cards are drawn, whoever has a total closer to 21 than the dealer wins. If player's hand and dealer's hand have an equal value, it's a tie. ")
        #ans1 = input("Are you ready to begin? (Yes or No): ")
#if ans1 == "Yes":
        #print("Okay lets start!")
        #carddeal1 = input("You have a " + deal_shuffled_card + " would you like to hit or stay?")
#else:
        #print("Please let me know when your ready. For now the game will terminate")
#else:
    #input("Lets begin the games? (Yes or No): ")
    #if input == "Yes":
        #print("Okay")



