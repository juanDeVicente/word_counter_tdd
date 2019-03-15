#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from word_counter_tdd.skeleton import fib

__author__ = "Juan de Vicente Tortosa"
__copyright__ = "Juan de Vicente Tortosa"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
