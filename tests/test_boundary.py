import numpy as np
from unittest import TestCase
from cmaes import CMA


class TestCMABoundary(TestCase):
    def test_valid_dimension(self):
        CMA(mean=np.zeros(2), sigma=1.3, bounds=np.array([[-10, 10], [-10, 10]]))

    def test_invalid_dimension(self):
        with self.assertRaises(AssertionError):
            CMA(mean=np.zeros(2), sigma=1.3, bounds=np.array([-10, 10]))

    def test_set_valid_bounds(self):
        optimizer = CMA(mean=np.zeros(2), sigma=1.3)
        optimizer.set_bounds(bounds=np.array([[-10, 10], [-10, 10]]))

    def test_set_invalid_bounds(self):
        optimizer = CMA(mean=np.zeros(2), sigma=1.3)
        with self.assertRaises(AssertionError):
            optimizer.set_bounds(bounds=np.array([-10, 10]))
