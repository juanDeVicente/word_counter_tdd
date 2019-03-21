#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.word_counter_tdd.skeleton import word_count



import pytest
from src.word_counter_tdd.skeleton import word_count


def test_two_same_words():
    assert word_count("hola hola", "spanish") == [("hola", 2)]


def test_three_same_words():
    assert word_count("hola hola hola", "spanish") == [("hola", 3)]


def test_two_different_words():
    assert word_count("hola adios", "spanish") == [("hola", 1), ("adios", 1)]


def test_three_different_words():
    assert word_count("hola adios perejil", "spanish") == [("hola", 1), ("adios", 1), ("perejil", 1)]


def test_two_same_words_one_word_different():

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

def test_param_list():
    with pytest.raises(ValueError):
        word_count(['hola', 'adios', 'hola'])


def test_param_dict():
    with pytest.raises(ValueError):
        word_count({'hola': 2, 'adios': 5, '123': 25})


def test_words_upper_case_lower_case_same_words():
    assert word_count("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 5)]


def test_words_upper_case_lower_case_different_words():
    assert word_count("hOla hoLa adios Adios adiOS HOLA") == [("hola", 3), ("adios", 3)]

def test_words_upper_case_lower_case():
    assert word_count("hOla HOLA hoLa HOla holA", "spanish") == [("hola", 5)]


def test_with_commas():

    assert word_count("Hola, me llamo Juan, encantado de conocerte soy Juan", "spanish") == [("juan", 2), ("hola", 1),
                                                                                             ("llamo", 1),
                                                                                             ("encantado", 1),
                                                                                             ("conocerte", 1)]

def test_using_stopwords_spanish():
    assert word_count("hola hola de hola la hola o hola y hola y y hola ante a el la los las", "spanish") == [
        ("hola", 7)]

def test_using_stop_words_english():
    assert word_count("hello hello hello shouldn't aren't hello ourselves a hello a a a a", "english") == [("hello", 5)]

def test_example_english():
    assert word_count("Hello, my name is Juan. Nice to meet you. i'm juan", "english") == [("juan", 2), ("hello", 1), ("name", 1), ("nice", 1), ("meet",1), ("i'm",1)]

def test_stop_words_apostophe_english():
    assert word_count("You're amazing", "english") == [("amazing", 1)]

def test_stop_words_apostophe_and_puntuation_english():
    assert word_count("you're,,,,,,, amazing.....", "english") == [("amazing", 1)]

def test_text_with_more_than_one_space_english():
    assert word_count("hello   buddy") == [("hello", 1), ("buddy", 1)]
    # MIRAR PORQUE NO SE WHY CON ESPACIOS PARES NO FUNCIONA PERO CON ESPACIOS PARES, SI

def test_with_exclamations_and_interrogations_english():
    assert word_count("today!!!!! is a great day???????") == [("today", 1), ("great", 1), ("day",1)]

def test_only_stop_words_english():
    assert word_count("how are you", "english") == []
