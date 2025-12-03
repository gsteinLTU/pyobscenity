from dataclasses import dataclass
from typing import Optional

from pyobscenity.util import compare_intervals

@dataclass
class MatchPayload:
    startIndex: int
    endIndex: int
    matchLength: int
    termId: int

@dataclass
class BlacklistedTerm:
    id: int
    term: str

def compare_matches(a: MatchPayload, b: MatchPayload) -> int:
    '''
    Compares two MatchPayload objects for sorting.
    :param a: The first MatchPayload object.
    :param b: The second MatchPayload object.
    :return: Negative if a < b, positive if a > b, zero if equal.
    '''
    result = compare_intervals(a.startIndex, a.endIndex, b.startIndex, b.endIndex)
    if result != 0:
        return result
    return 0 if a.termId == b.termId else -1 if a.termId < b.termId else 1

class Matcher:
    '''
    Base class for matchers.
    '''
    def get_all_matches(self, input: str, sorted: Optional[bool] = False) -> list[MatchPayload]:
        '''
        Gets all matches in the input text.
        :param input: The input text to be matched against.
        :return: A list of MatchPayload objects representing the matches.
        '''
        pass

    def has_match(self, input: str) -> bool:
        '''
        Checks if there is at least one match in the input text.
        :param input: The input text to be checked.
        :return: True if there is at least one match, False otherwise.
        '''
        pass