from typing import List, Dict, Union

Card = str
Hand = List[Card]
PlayerInfo = Dict[str, Union[str, int, Hand]]
GameState = Dict[str, Union[PlayerInfo, Hand, int, bool]]