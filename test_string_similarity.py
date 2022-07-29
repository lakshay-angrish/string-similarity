import pytest

from string_similarity import calculate_string_similarity, SimilarityCalculationMethod


@pytest.mark.parametrize(
    "string1, string2, levenshtein_distance",
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
def test_calculate_levenshtein_distance(
    string1: str, string2: str, levenshtein_distance: int
) -> None:
    assert (
        calculate_string_similarity(
            string1, string2, SimilarityCalculationMethod.LEVENSHTEIN_DISTANCE
        )
        == levenshtein_distance
    )


@pytest.mark.parametrize(
    "string1, string2, dice_coefficient",
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
def test_calculate_dice_coefficient(
    string1: str, string2: str, dice_coefficient: float
) -> None:
    assert (
        calculate_string_similarity(
            string1, string2, SimilarityCalculationMethod.DICE_COEFFICIENT
        )
        == dice_coefficient
    )
