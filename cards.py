from shovel_card import Shovel
from pickaxe_card import Pickaxe
from spelunk_card import Spelunk
from survey_card import Survey
from prospect_card import Prospect

def initialize_cards():
    shovel_cards = [Shovel() for _ in range(10)] 
    pickaxe_cards = [Pickaxe() for _ in range(5)]
    spelunk_cards = [Spelunk() for _ in range(3)]
    survey_cards = [Survey() for _ in range(2)]
    prospect_cards = [Prospect() for _ in range(1)]
    return shovel_cards + pickaxe_cards + spelunk_cards + survey_cards + prospect_cards