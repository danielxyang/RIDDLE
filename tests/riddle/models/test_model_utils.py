"""
test_model_utils.py

Unit test(s) for the `model_utils.py` module.

Requires:   pytest, NumPy, RIDDLE (and their dependencies)

Author:     Ji-Sung Kim, Rzhetsky Lab
Copyright:  2016, all rights reserved
"""

import pytest

import sys; sys.dont_write_bytecode = True
import os
from math import fabs
from itertools import izip

import numpy as np

from riddle.models.model_utils import (chunks, probas_to_preds)

class TestModelUtils():
    def test_chunks(self):
        list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list_B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        for i, (a, b) in enumerate(izip(chunks(list_A, 4), chunks(list_B, 4))): 
            if (i == 0):
                assert a == [1, 2, 3, 4]
                assert b == [10, 9, 8, 7]
            if (i == 1):
                assert a == [5, 6, 7, 8]
                assert b == [6, 5, 4, 3]
            if (i == 2):
                assert a == [9, 10]
                assert b == [2, 1]

    def test_probas_to_preds(self):
        probas = np.asarray([[0.5, 0.3, 0.1, 0.1], [0.1, 0.1, 0.1, 0.99], 
            [0.3, 0.3, 15, 3]])
        assert np.all(np.equal(probas_to_preds(probas), np.asarray([0, 3, 2])))
    