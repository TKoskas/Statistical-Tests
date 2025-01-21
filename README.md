# Statistical Tests
This repository contains implementations of common statistical tests, including equivalence tests, the Kolmogorov-Smirnov test, and Somers' D for ordinal variables. These functions are useful for data analysis in a variety of scenarios, especially when comparing the distributions or relationships between two datasets.

## Features
Somers' D: Measures the association between two ordinal variables.
Equivalence Test: Compares the means of two independent samples to determine if they are equivalent within a defined margin.
Kolmogorov-Smirnov Test: Compares two distributions to determine if they are significantly different.
## Requirements
To run the tests, you will need Python installed with the following libraries:

- `numpy`
- `scipy`

You can install the required libraries using pip:

```bash
pip install numpy scipy
```
## Functions
1. Somers' D
```python
def somers_d(x, y):
    """
    Calculates Somers' D for two ordinal variables.

    Parameters:
    - x: First ordinal variable (array-like)
    - y: Second ordinal variable (array-like)

    Returns:
    - Somers' D statistic (float)
    """
```

2. Equivalence Test
```python
def equivalence_test(x, y, alpha=0.05, equivalence_margin=0.2):
    """
    Performs an equivalence test between two independent samples.

    Parameters:
    - x: First sample (array-like)
    - y: Second sample (array-like)
    - alpha: Significance level (default 0.05)
    - equivalence_margin: Margin of equivalence (default 0.2)

    Returns:
    - Prints the equivalence test result
    """
```

3. Kolmogorov-Smirnov Test
```python
def ks_test(x, y, alpha=0.05):
    """
    Performs a Kolmogorov-Smirnov test to compare two distributions.

    Parameters:
    - x: First sample (array-like)
    - y: Second sample (array-like)
    - alpha: Significance level (default 0.05)

    Returns:
    - Prints the test result
    """
```

## Example Usage
Here is an example of how to use the functions in this repository:

```python
import numpy as np
from statistical_tests import somers_d, equivalence_test, ks_test

# Generate example data
x_ord = np.random.randint(0, 5, size=100)
y_ord = np.random.randint(0, 5, size=100)
x_norm = np.random.normal(loc=0, scale=1, size=100)
y_norm = np.random.normal(loc=0, scale=1, size=100)

# Calculate Somers' D
print("Somers' D (ordinal variables):", somers_d(x_ord, y_ord))

# Perform Equivalence Test
equivalence_test(x_norm, y_norm, equivalence_margin=0.1)


# Perform Kolmogorov-Smirnov Test
ks_test(x_norm, y_norm)
```
# License
This project is licensed under the MIT License
