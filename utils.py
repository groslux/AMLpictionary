import random
import unicodedata

# Liste des cartes AML par défaut
DEFAULT_CARDS = [
    "Beneficial Owner",
    "Shell Company",
    "Name Screening",
    "PEP",
    "Strawman"
]

def get_cards(n=5):
    """Retourne une sélection aléatoire de cartes AML."""
    return random.sample(DEFAULT_CARDS, k=n)

def normalize(text):
    """Supprime les accents et met en minuscule sans unidecode."""
    if not isinstance(text, str):
        return ""
    text = unicodedata.normalize('NFD', text)
    text = ''.join(char for char in text if unicodedata.category(char) != 'Mn')
    return text.strip().lower()

def validate_guess(answer, guess):
    """Compare guess et réponse en normalisant le texte."""
    return normalize(answer) == normalize(guess)
