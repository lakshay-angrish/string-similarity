## string_similarity_lakshay_angrish

A library to calculate similarity between strings.

### Installation

Optional: [Create and activate a virtual environment](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments)

The library has been uploaded to `TestPyPI` and can be installed via:

```
pip install -i https://test.pypi.org/simple/ string-similarity-lakshay-angrish==0.0.2
```


### Usage

```python
>>> from string_similarity_lakshay_angrish import string_similarity
>>> string_similarity.calculate_string_similarity('abcd', 'abcde')
StringSimilarityResult(levenshtein=0.8, dice=0.8888888888888888)
>>> string_similarity.calculate_string_similarity('testing', 'bathing')
StringSimilarityResult(levenshtein=0.4285714285714286, dice=0.5714285714285714)
```
