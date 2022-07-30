import pytest

from string_similarity_lakshay_angrish import string_similarity


@pytest.mark.parametrize(
    "string1, string2, levenshtein_similarity",
    [
        ("kitten", "sitting", 1 - 3 / 7),
        ("equal", "equal", 1),
        ("equal", "equalize", 1 - 3 / 8),
        ("abcd", "efgh", 1 - 4 / 4),
        ("dome", "randomly", 1 - 5 / 8),
        ("comprehension", "incomprehensibilities", 1 - 10 / 21),
        (
            "comprehensioncomprehensioncomprehensioncomprehensioncomprehensioncomprehensioncomprehensioncomprehension",
            "incomprehensibilitiesincomprehensibilitiesincomprehensibilitiesincomprehensibilitiesincomprehensibilities",
            1 - 52 / 105,
        ),
    ],
)
def test_calculate_levenshtein_similarity(
    string1: str, string2: str, levenshtein_similarity: int
) -> None:
    assert (
        string_similarity.calculate_string_similarity(string1, string2).levenshtein
        == levenshtein_similarity
    )


@pytest.mark.parametrize(
    "string1, string2, dice_similarity",
    [
        ("kitten", "sitting", (2 * 4) / 13),
        ("equal", "equal", (2 * 5) / 10),
        ("equal", "equalize", (2 * 5) / 13),
        ("abcd", "efgh", (2 * 0) / 8),
        ("dome", "randomly", (2 * 3) / 12),
        ("comprehension", "incomprehensibilities", (2 * 12) / 34),
        (
            "comprehensioncomprehensioncomprehensioncomprehensioncomprehensioncomprehensioncomprehensioncomprehension",
            "incomprehensibilitiesincomprehensibilitiesincomprehensibilitiesincomprehensibilitiesincomprehensibilities",
            (2 * 71) / 209,
        ),
    ],
)
def test_calculate_dice_similarity(
    string1: str, string2: str, dice_similarity: float
) -> None:
    assert (
        string_similarity.calculate_string_similarity(string1, string2).dice
        == dice_similarity
    )
