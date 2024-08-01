from shovel_card import Shovel
from pickaxe_card import Pickaxe
from spelunk_card import Spelunk
from survey_card import Survey
from prospect_card import Prospect
from investment_card import Investment
from treasure_cards import *
from bedrock_card import Bedrock
from deep_exploration_card import Deep_Exploration
from back_to_basics import Back_To_Basics
from trade_secrets import Trade_Secrets
from tunnel_collapse import Tunnel_Collapse
from pilfer_card import Pilfer
from hard_hat_card import Hard_Hat
from earthquake_card import Earthquake
from taxes_card import Taxes

def initialize_cards():
    shovel_cards = [Shovel() for _ in range(10)] 
    pickaxe_cards = [Pickaxe() for _ in range(5)]
    spelunk_cards = [Spelunk() for _ in range(3)]
    survey_cards = [Survey() for _ in range(2)]
    prospect_cards = [Prospect() for _ in range(1)]
    ruby_cards = [Ruby() for _ in range(10)]
    sapphire_cards = [Sapphire() for _ in range(3)]
    emerald_cards = [Emerald() for _ in range(2)]
    diamond_cards = [Diamond() for _ in range(1)]
    investment_cards = [Investment()]
    bedrock_cards = [Bedrock()]
    deep_exploration_card = [Deep_Exploration()]
    back_to_basics = [Back_To_Basics() for _ in range(2)]
    trade_secrets = [Trade_Secrets() for _ in range(2)]
    tunnel_collapse = [Tunnel_Collapse() for _ in range(2)]
    pilfer_cards = [Pilfer() for _ in range(2)]
    hard_hat_cards = [Hard_Hat() for _ in range(2)]
    earthquake_card = [Earthquake()]
    taxes_cards = [Taxes() for _ in range(2)]



    return shovel_cards + pickaxe_cards + spelunk_cards + survey_cards + prospect_cards + ruby_cards + sapphire_cards + emerald_cards + diamond_cards + investment_cards + bedrock_cards + deep_exploration_card + back_to_basics + trade_secrets + tunnel_collapse + pilfer_cards + hard_hat_cards + earthquake_card + taxes_cards