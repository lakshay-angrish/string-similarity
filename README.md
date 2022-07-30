## string_similarity_lakshay_angrish

A library to calculate similarity between strings.

### Installation

Optional: [Create and activate a virtual environment](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments)

The library has been uploaded to `TestPyPI` and can be installed via:

```bash
pip install -i https://test.pypi.org/simple/ string-similarity-lakshay-angrish==0.0.2
```


### Usage

```python
>>> from string_similarity_lakshay_angrish import string_similarity
>>> string_similarity.calculate_string_similarity('testing', 'bathing')
StringSimilarityResult(levenshtein=0.4285714285714286, dice=0.5714285714285714)
>>> result = string_similarity.calculate_string_similarity('incomprehensibility', 'comprehension')
>>> result.dice     # get the similarity based on dice coefficient
0.75
>>> result.levenshtein  # get the similarity based on levenshtein distance
0.5789473684210527
```

### Running Tests

  - Make sure that the package is installed as mentioned under the `Installation` section.

  - Clone the repository

  - `cd` to the repository root

 ```bash
 pip install pytest
 ```

 ```bash
pytest tests/
 ```