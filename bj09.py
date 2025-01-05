import sys, random

# select a card from the card list, add it to the deck, which is in place in main, thus no return is needed
def get_card(deck,num_cards):
    cards = [11,10,11,10,11,10,11,8,6,7,8,9,6,5,4,3,2]

    for i in range(num_cards):
        card = cards[random.choice(cards)]
        deck.append(card)
        if card == 11:
            cards.remove(11)
        else:
            cards.remove(card)

def check_score(deck):
    total = sum(deck)
    if sum(deck) == 21 and len(deck) == 2:
        return -1 #blackjack
    if 11 in deck and total > 21:
        index = deck.index(11)
        deck[index] = 1
    return sum(deck)  

def check_winner(computer_total, player_total,player_status,computer_status):
        if player_status == 'busted':  
            return 'computer'
        elif computer_status == 'busted':  
            return 'player'
        if (player_total > computer_total):
            return 'player'
        elif (computer_total > player_total):
            return 'computer'

        

def main():

    player_wins = 0
    computer_wins = 0
    game = True

    while game:
        player_cards=[]
        computer_cards=[]    
        player_status = 'clear'
        computer_status = 'clear'
        computer_current_score = 0
        current_score = 0
    
        if input('Would you like to play (y) or (n): ') == 'n':
            sys.exit()
        get_card(player_cards,2)
        get_card(computer_cards,1)

        while player_status == 'clear':
            current_score = check_score(player_cards)
            if current_score == -1:
                print('Blackjack! You win!')
                print('Your cards: ', player_cards)
                player_status = 'blackjack'
                current_score = 21
                break
            elif current_score > 21:
                print('Busted! Computer wins!')
                print('Your cards: ', player_cards)
                player_status = 'busted'
                break
            print(f'Computer has showing {computer_cards}')
            print(f'Player has in his hand {player_cards} for a total of {check_score(player_cards)}')
            print('------------------------------------------')
            if current_score == 21 or input('Do you want another card (y) or (n)):') == 'n':
                break
            else:
                get_card(player_cards,1)

        while computer_status == 'clear':
            if player_status == 'blackjack' or player_status == 'busted':
                break
            get_card(computer_cards,1)
            computer_current_score = check_score(computer_cards)
            if computer_current_score == -1:
                print('Computer has Blackjack! Computer wins!')
                print('Computer cards: ', computer_cards)
                computer_status = 'blackjack'
                computer_current_score = 21
                break   
            if computer_current_score and computer_current_score < 22:
                
                print(f'Computer has in his hand {computer_cards} for a total of {computer_current_score}')
                # get_card(computer_cards,1)
                computer_current_score = check_score(computer_cards)
            if computer_current_score > 21:
                print(f'Computer has in his hand {computer_cards} for a total of {computer_current_score}')
                print('COMPUTER BUSTED')
                computer_status = 'busted'
                break
            elif computer_current_score > 16:
                    break
        
        winner = check_winner(computer_current_score, current_score,player_status,computer_status)
        if winner == 'player':
            player_wins += 1
        elif winner == 'computer':
            computer_wins += 1

        print(f'Computer Player Total: {check_score(computer_cards)}')
        print(f'Human Player Total: {check_score(player_cards)}')
        print('------------------------------------------')
        print(f'Player Wins:  {player_wins}')
        print(f'Computer Wins:  {computer_wins}')
        print('------------------------------------------')
        





    
    




if __name__ == "__main__":
    main()