from collections import Counter
from enum import (
    auto,
    IntEnum,
)
from typing import (
    List,
    Optional,
    Tuple,
)

import attr
import operator

class PokerHandRank(IntEnum):
    '''Poker hands ranked in ascending order'''
    HighCard        = auto()
    OnePair         = auto()
    TwoPairs        = auto()
    ThreeOfAKind    = auto()
    Straight        = auto()
    Flush           = auto()
    FullHouse       = auto()
    FourOfAKind     = auto()
    StraightFlush   = auto()
    RoyalFlush      = auto()

@attr.s
class Card:
    SPECIAL_NUMBERS: str = 'TJQKA'

    number: int = attr.ib(converter=int)    # converter handles cards numbered 2-9
    suit: str = attr.ib(validator=attr.validators.instance_of(str), eq=False)

    @number.validator
    def valid_card_number(self, attribute, value):
        if not 2 <= value <= 14: # Ace is 14
            raise ValueError(f"invalid card {attribute} '{value}'")
    @suit.validator
    def valid_suit(self, attribute, value):
        if len(value) != 1 or value not in {'H','C','S','D'}:
            raise ValueError(f"invalid card {attribute} '{value}'")

    @classmethod
    def from_str(cls, s):
        if len(s) != 2:
            raise ValueError(f"invalid {cls.__name__} string '{s}'")
        number, suit = s
        if number in cls.SPECIAL_NUMBERS:
            number = 10 + cls.SPECIAL_NUMBERS.find(number)
        return cls(number, suit)

    def __str__(self):
        return f'{self.number}{self.suit}'

@attr.s
class PokerHand:
    cards: Tuple[Card, Card, Card, Card, Card] = attr.ib(
        factory=tuple,
        validator=attr.validators.instance_of(tuple),
        eq=False,
    )
    rank: Tuple[PokerHandRank, Optional[int]] = attr.ib(init=False)

    @cards.validator
    def valid_hand(self, attribute, value):
        if len(value) != 5:
            raise ValueError(f'a poker hand has 5 {attribute}, not {len(value)}')
        for t in map(type, value):
            if t is not Card:
                raise ValueError(f"cannot have type '{t}' in poker hand")

    @classmethod
    def from_str(cls, s: str, split_by: str=None):
        '''Creates Card objects from the string representation'''
        return cls(tuple(map(Card.from_str, s.split(split_by))))

    def __str__(self):
        return f"{' '.join(map(str, self.cards))} | {self.rank}"

    @property
    def suits(self):
        return Counter(map(operator.attrgetter('suit'), self.cards)).keys()

    def __attrs_post_init__(self):
        '''Compute the poker hand's rank'''
        # Note that self.cards isn't sorted.
        # Start by sorting them in descending order of their number.
        self.cards = sorted(self.cards, reverse=True)
        # Now the logic to identify the hand's best possible rank.
        # Let's compute some useful hand stats.
        same_suit = all(x == self.cards[0].suit for x in map(operator.attrgetter('suit'), self.cards))
        hand_numbers = list(map(operator.attrgetter('number'), self.cards))
        all_consecutive = all(map(lambda tup: tup[0] - 1 == tup[1], zip(hand_numbers[:-1], hand_numbers[1:])))

        if same_suit and all_consecutive:
            # First: Royal Flush
            if hand_numbers[0] == 14:
                self.rank = (PokerHandRank.RoyalFlush,)
            # Second: StraightFlush
            else:
                self.rank = (PokerHandRank.StraightFlush, hand_numbers[0])
        else:
            commonality: List[Tuple[int, int, Optional[int]]] = Counter(hand_numbers).most_common()
            # Third: Four of a Kind
            if commonality[0][1] == 4:
                self.rank = (
                    PokerHandRank.FourOfAKind,
                    commonality[0][0],
                    commonality[1][0]
                )
            # Fourth: Full House
            elif commonality[0][1] == 3 and commonality[1][1] == 2:
                self.rank = (
                    PokerHandRank.FullHouse,
                    commonality[0][0],
                    commonality[1][0]
                )
            # Fifth: Flush
            elif same_suit:
                self.rank = (
                    PokerHandRank.Flush,
                    *hand_numbers
                )
            # Sixth: Straight
            elif all_consecutive:
                self.rank = (
                    PokerHandRank.Straight,
                    *hand_numbers
                )
            # Seventh: Three of a Kind
            elif commonality[0][1] == 3:
                rest = map(
                    operator.itemgetter(0),
                    commonality[1:]
                )
                self.rank = (
                    PokerHandRank.ThreeOfAKind,
                    commonality[0][0],
                    *sorted(rest, reverse=True)
                )
            elif commonality[0][1] == 2:
                # Eigth: Two Pairs
                if commonality[1][1] == 2:
                    pairs = commonality[0][0], commonality[1][0]
                    self.rank = (
                        PokerHandRank.TwoPairs,
                        *sorted(pairs, reverse=True),
                        commonality[2][0]
                    )
                # Ninth: One Pair
                else:
                    rest = map(
                        operator.itemgetter(0),
                        commonality[1:]
                    )
                    self.rank = (
                        PokerHandRank.OnePair,
                        commonality[0][0],
                        *sorted(rest, reverse=True)
                    )
            # Tenth: High Card
            else:
                self.rank = (
                    PokerHandRank.HighCard,
                    *hand_numbers
                )

def parse_poker_file(name: str) -> List[Tuple[PokerHand, PokerHand]]:
    middle: int = 2 * 5 + 4 # five cards per hand, 2 characters, 4 spaces
    poker_hands: List[Tuple[PokerHand, PokerHand]] = []
    with open(name, 'r') as f:
        poker_hands = [
            tuple(
                map(PokerHand.from_str, (line[:middle], line[middle:]))
            ) for line in f.readlines()
        ]
    return poker_hands

if __name__ == '__main__':
    poker_file: str = 'p054_poker.txt'
    poker_hands: List[Tuple[PokerHand, PokerHand]] = parse_poker_file(poker_file)
    player_1_wins: int = sum(a.rank > b.rank for a,b in poker_hands)
    print(f'Player 1 wins {player_1_wins} hands out of {len(poker_hands)}.')