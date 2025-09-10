"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    """Return the value of a single card."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Return the card with the higher value, or both if equal."""
    v1, v2 = value_of_card(card_one), value_of_card(card_two)
    if v1 > v2:
        return card_one
    elif v2 > v1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Return the most advantageous value (1 or 11) for an upcoming Ace."""
    v1, v2 = value_of_card(card_one), value_of_card(card_two)

    # If there’s already an Ace in hand, upcoming Ace = 1
    if card_one == 'A' or card_two == 'A':
        return 1

    # If treating Ace as 11 doesn't bust (<= 21), return 11
    if v1 + v2 + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Return True if hand is a blackjack (Ace + 10-value card)."""
    cards = {card_one, card_two}
    return ('A' in cards) and (
        card_one in ['10', 'J', 'Q', 'K'] or card_two in ['10', 'J', 'Q', 'K']
    )


def can_split_pairs(card_one, card_two):
    """Return True if cards are a pair (same value)."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Return True if total is 9, 10, or 11 (eligible for double down)."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
