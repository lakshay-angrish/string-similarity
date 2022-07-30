from dataclasses import dataclass
from collections import Counter


def _calculate_dice_coefficient(string1: str, string2: str) -> float:
    """Calculates the Dice Coefficient of 2 strings

    Args:
        string1 (str): String argument 1
        string2 (str): String argument 2

    Returns:
        float: the dice coefficient of `string1` and `string2`
    """
    counter1 = Counter(string1)
    counter2 = Counter(string2)

    total = sum(counter1.values()) + sum(counter2.values())
    intersection = counter1 & counter2
    intersection = sum(intersection.values())

    return (2 * intersection) / total


def _calculate_levenshtein_distance(string1: str, string2: str) -> int:
    """Calculates the levenshtein distance between 2 strings

    Args:
        string1 (str): String argument 1
        string2 (str): String argument 2

    Returns:
        int: levenshtein distance between `string1` and `string2`
    """
    len1 = len(string1)
    len2 = len(string2)

    table = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                table[i][j] = j

            elif j == 0:
                table[i][j] = i

            elif string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1]

            else:
                table[i][j] = (
                    min(
                        table[i][j - 1],
                        table[i - 1][j],
                        table[i - 1][j - 1],
                    )
                    + 1
                )

    return table[i][j]


@dataclass
class StringSimilarityResult:
    levenshtein: float = 0.0
    dice: float = 0.0


def calculate_string_similarity(
    string1: str,
    string2: str,
) -> StringSimilarityResult:
    """Returns a value between 0 and 1 to denote how similar 2 strings are.
    1 being exactly equal and 0 being not similar at all.

    Args:
        string1 (str): String argument 1
        string2 (str): String argument 2

    Returns:
        StringSimilarityResult: An object which contains the string similarity of `string1`
        and `string2` calculated using various methods.
    """

    result = StringSimilarityResult()
    levenshtein_distance = _calculate_levenshtein_distance(string1, string2)
    max_len = max(len(string1), len(string2))
    if max_len == 0:
        result.levenshtein = 0.0
    else:
        result.levenshtein = 1 - levenshtein_distance / max_len

    result.dice = _calculate_dice_coefficient(string1, string2)

    return result
