from enum import Enum
from collections import Counter


def _calculate_dice_coefficient(string1: str, string2: str) -> float:
    counter1 = Counter(string1)
    counter2 = Counter(string2)

    total = sum(counter1.values()) + sum(counter2.values())
    intersection = counter1 & counter2
    intersection = sum(intersection.values())

    return (2 * intersection) / total


def _calculate_levenshtein_distance(string1: str, string2: str) -> int:
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


class SimilarityCalculationMethod(Enum):
    LEVENSHTEIN_DISTANCE = 0
    DICE_COEFFICIENT = 1


def calculate_string_similarity(
    string1: str,
    string2: str,
    method: SimilarityCalculationMethod = SimilarityCalculationMethod.LEVENSHTEIN_DISTANCE,
) -> float:
    if method == SimilarityCalculationMethod.LEVENSHTEIN_DISTANCE:
        levenshtein_distance = _calculate_levenshtein_distance(string1, string2)
        max_len = max(len(string1), len(string2))
        if max_len == 0:
            return 0
        return 1 - levenshtein_distance / max_len

    elif method == SimilarityCalculationMethod.DICE_COEFFICIENT:
        return _calculate_dice_coefficient(string1, string2)

    else:
        raise ValueError(f"Invalid method")
