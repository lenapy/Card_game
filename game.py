import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def count_points(self):
        """Return number of points that card gives"""
        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Hand:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card_on_hand(self, card):
        self.hand.append(card)

    def count_points_on_hand(self):
        """Count card points that u have on your hand"""
        points = 0
        number_of_aces_on_hand = 0
        for card in self.hand:
            points += card.count_points()
            if card.get_rank() == "A":
                number_of_aces_on_hand += 1
        if points + number_of_aces_on_hand * 10 <= 21:
            points += number_of_aces_on_hand * 10
        return points

    def __str__(self):
        text = "%s's contains:\n" % self.name
        for card in self.hand:
            text += (str(card) + " ")
        text += ("\nHand value: " + str(self.count_points_on_hand()))
        return text


class Deck:
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        # generate a deck of 52 cards
        self.cards = [Card(r, s) for r in ranks for s in suits]
        # shuffle the cards
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal cards"""
        return self.cards.pop()


def game_21():
    bid = input("Your bid ?")
    deck = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card_on_hand(deck.deal_card())
    player_hand.add_card_on_hand(deck.deal_card())
    dealer_hand.add_card_on_hand(deck.deal_card())
    print(dealer_hand)
    print("*"*20)
    print(player_hand)
    continue_game = True
    if player_hand.count_points_on_hand() == 21:
        print("You win,", 3*int(bid))
    while player_hand.count_points_on_hand() < 21:
        answer = input("Hit or stand (h/s) ?")
        if answer == "h":
            player_hand.add_card_on_hand(deck.deal_card())
            print(player_hand)
            if player_hand.count_points_on_hand() > 21:
                print("You lose,", bid)
                continue_game = False
        else:
            print("You stand")
            exit()

    if continue_game:
        while dealer_hand.count_points_on_hand() < 17:
            dealer_hand.add_card_on_hand(deck.deal_card())
            print(dealer_hand)
            if dealer_hand.count_points_on_hand() > 21:
                print("Dealer lose")
                continue_game = False

        if continue_game:
            if player_hand.count_points_on_hand() > dealer_hand.count_points_on_hand():
                print("Player win,", bid)
            else:
                print("Dealer win,", bid)

if __name__ == "__main__":
    game_21()

