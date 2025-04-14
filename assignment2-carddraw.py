import requests

def get_new_deck():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url).json()
    return response["deck_id"]

def draw_cards(deck_id, count=5):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(url).json()
    return response["cards"]

def print_cards(cards):
    for card in cards:
        print(f"{card['value']} of {card['suit']}")

def main():
    deck_id = get_new_deck()
    cards = draw_cards(deck_id)
    print("Drawn cards:")
    print_cards(cards)

if __name__ == "__main__":
    main()

