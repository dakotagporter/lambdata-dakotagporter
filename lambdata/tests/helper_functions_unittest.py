"""Basic unittest for Lambdata package."""

import numpy as np
import pandas as pd
import unittest
import helper_functions


class ExampleTests(unittest.TestCase):
    def test_nullcount(self):
        """
        Testing that null_count function works as expected
        """
        df = pd.DataFrame({"A": [1, np.NaN, 3],
                           "B": ['a', 'b', np.NaN],
                           "C": [4, 5, 6]})
        self.assertEqual(helper_functions.null_count(df).dtype, 'int64')


if __name__ == '__main__':
    unittest.main()
