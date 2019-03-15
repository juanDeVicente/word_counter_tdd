#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.word_counter_tdd.skeleton import word_count


def test_two_words():
    assert word_count("hola hola", "spanish") == [("hola", 2)]


def test_three_words():
    assert word_count("hola adios hola", "spanish") == [("hola", 2), ("adios", 1)]


def test_param_integer():
    with pytest.raises(ValueError):
        word_count(124)


def test_param_float():
    with pytest.raises(ValueError):
        word_count(1.12334)


def test_param_bool():
    with pytest.raises(ValueError):
        word_count(False)


def test_param_none():
    with pytest.raises(ValueError):
        word_count(None)


def test_words_upper_case_lower_case():
    assert word_count("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 5)]


def test_with_commas():
    assert word_count("Hola, me llamo Juan, encantado de conocerte soy Juan", "spanish") == [("juan", 2), ("hola", 1),
                                                                                             ("llamo", 1),
                                                                                             ("encantado", 1),
                                                                                             ("conocerte", 1)]


def test_use_stopwords():
    assert word_count("hola hola de hola la hola o hola y hola y y hola ante a el la los las", "spanish") == [
        ("hola", 7)]


def test_using_stop_words_english():
    assert word_count("hello hello hello shouldn't aren't hello ourselves a hello a a a a", "english") == [("hello", 5)]
