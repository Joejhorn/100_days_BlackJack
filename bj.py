import sys, random

computer_cards = []
player_cards = []
status = "no"

def get_card(deck,num_cards):
    cards = [1,2,3,4,5,6,7,8,9,11,11,11,11,11]
    for i in range(num_cards):
        deck.append(cards[random.choice(cards)])
        # deck.append(cards[random.randrange(0,14)])
    return deck

def check_score(deck):
    total = sum(deck)
    total_aces = deck.count(11)

    if total_aces == 1 and total < 21:
        return (total)
    if total_aces == 1 and total > 21:
        return (total - 10)
    if total_aces == 2:
        if (total - 10) < 21:
            return total - 10
        elif (total - 20 ) < 21:
            return total - 20
    if total_aces == 3:
        if (total - 10) < 21:
            return total - 10
        elif (total - 20 ) < 21:
            return total - 20
        elif (total - 30 ) < 21:
            return total - 30
    else:
        return total
    return sum(deck)

def main():
    global status
    if input('Would you like to play (y) or (n): ') == 'n':
        sys.exit()
    get_card(player_cards, 2)
    get_card(computer_cards, 1)


    while True:
        player_total = check_score(player_cards)

        if player_total > 21:
            print(f'Player has in his hand {player_cards} for a total of {check_score(player_cards)}')
            status = "busted"
            print('you busted')
            break

        print(f'Computer has showing {computer_cards}')
        print(f'Player has in his hand {player_cards} for a total of {check_score(player_cards)}')
        if input('Do you want another card (y) or (n)):') == 'n':
            break
        else:
            get_card(player_cards,1)

    while True and status != 'busted':
        computer_total = check_score(computer_cards)
        if computer_total < 17 and computer_total < 22:
            get_card(computer_cards,1)
            print(f'Computer has in his hand {computer_cards} for a total of {check_score(computer_cards)}')
            computer_total = check_score(computer_cards)
        if computer_total > 22:
            print('Computer Busted')
            break
        elif computer_total > 16:
                break
    print(f'Computer Player Total: {check_score(computer_cards)}')
    print(f'Human Player Total: {check_score(player_cards)}')



if __name__ == "__main__":
    main()
