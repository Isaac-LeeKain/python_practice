import random

def create_deck():
    suits = ['♠', '♡', '♢', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_score(cards):
    score = sum([int(card[0]) if card[0].isdigit() else 10 if card[0] != 'A' else 11 for card in cards])
    if score > 21 and 'A' in [card[0] for card in cards]:
        score -= 10
    return score

def compare_scores(player_score, dealer_score):
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack():
    deck = create_deck()
    player_cards = [deal_card(deck), deal_card(deck)]
    dealer_cards = [deal_card(deck), deal_card(deck)]
    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass, or 'd' to double down: ")
            if should_continue == 'y':
                player_cards.append(deal_card(deck))
            elif should_continue == 'd':
                player_cards.append(deal_card(deck))
                game_over = True
            else:
                game_over = True

    while dealer_score < 17 and dealer_score != 21:
        dealer_cards.append(deal_card(deck))
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

play_blackjack()
