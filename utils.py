import random

def get_cards(n=5):
    concepts = [
        "Name Screening", "Beneficial Owner", "PEP", "Sanctioned Entity",
        "Shell Company", "Smurfing", "Wire Transfer", "FATF",
        "Suspicious Activity Report", "KYC", "CDD", "MLRO"
    ]
    return random.sample(concepts, n)

def validate_guess(card, guess):
    return card.strip().lower() == guess.strip().lower()
