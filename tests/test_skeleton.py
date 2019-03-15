#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.word_counter_tdd.skeleton import word_count


def test_two_words():
    assert word_count('hola hola', 'spanish') == [('hola', 2)]


def test_three_words():
    assert word_count('hola adios hola', 'spanish') == [('hola', 2), ('adios', 1)]


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


def test_wikipedia_definition_of_test_spanish():
    assert word_count(
        'Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de ' \
        'sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo ' \
        'de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su ' \
        'destinatario original. En otras palabras, un texto es un entramado de signos con una intención ' \
        'comunicativa que adquiere sentido en determinado contexto. Las ideas esenciales que comunica un texto ' \
        'están contenidas en lo que se suele denominar «macroproposiciones», unidades estructurales de nivel ' \
        'superior o global, que otorgan coherencia al texto constituyendo su hilo central, el esqueleto ' \
        'estructural que cohesiona elementos lingüísticos formales de alto nivel, como los títulos y subtítulos, ' \
        'la secuencia de párrafos, etc. En contraste, las «microproposiciones» son los elementos coadyuvantes de ' \
        'la cohesión de un texto, pero a nivel más particular o local. Esta distinción fue realizada por Teun van' \
        ' Dijk en 1980. El nivel microestructural o local está asociado con el concepto de cohesión. Se refiere a ' \
        'uno de los fenómenos propios de la coherencia, el de las relaciones particulares y locales que se dan ' \
        'entre elementos lingüísticos, tanto los que remiten unos a otros como los que tienen la función de ' \
        'conectar y organizar. También es un conjunto de oraciones agrupadas en párrafos que habla de un tema ' \
        'determinado.', 'spanish') == [('texto', 5), ('nivel', 4), ('elementos', 3), ('composición', 2), ('signos', 2),
                                       ('determinado', 2), ('coherencia', 2), ('lingüísticos', 2), ('párrafos', 2),
                                       ('cohesión', 2), ('local', 2), ('codificados', 1), ('sistema', 1),
                                       ('escritura', 1), ('forma', 1), ('unidad', 1), ('caracteres', 1),
                                       ('imprimibles', 1), ('grafema', 1), ('generados', 1), ('algoritmo', 1),
                                       ('cifrado', 1), ('aunque', 1), ('cualquier', 1), ('persona', 1), ('puede', 1),
                                       ('ser', 1), ('descifrado', 1), ('destinatario', 1), ('original', 1),
                                       ('palabras', 1), ('entramado', 1), ('intención', 1), ('comunicativa', 1),
                                       ('adquiere', 1), ('contexto', 1), ('ideas', 1), ('esenciales', 1),
                                       ('comunica', 1), ('contenidas', 1), ('suele', 1), ('denominar', 1),
                                       ('macroproposiciones', 1), ('unidades', 1), ('estructurales', 1),
                                       ('superior', 1), ('global', 1), ('otorgan', 1), ('constituyendo', 1),
                                       ('hilo', 1), ('central', 1), ('esqueleto', 1), ('estructural', 1),
                                       ('cohesiona', 1), ('formales', 1), ('alto', 1), ('títulos', 1),
                                       ('subtítulos', 1), ('secuencia', 1), ('etc', 1), ('contraste', 1),
                                       ('microproposiciones', 1), ('coadyuvantes', 1), ('particular', 1),
                                       ('distinción', 1), ('realizada', 1), ('teun', 1), ('van', 1), ('dijk', 1),
                                       ('1980', 1), ('microestructural', 1), ('asociado', 1), ('concepto', 1),
                                       ('refiere', 1), ('fenómenos', 1), ('propios', 1), ('relaciones', 1),
                                       ('particulares', 1), ('locales', 1), ('dan', 1), ('remiten', 1), ('función', 1),
                                       ('conectar', 1), ('organizar', 1), ('conjunto', 1), ('oraciones', 1),
                                       ('agrupadas', 1), ('habla', 1), ('tema', 1)]


def test_words_upper_case_lower_case():
    assert word_count('hOla HOLA hoLa HOla holA', 'spanish') == [('hola', 5)]


def test_with_commas():
    assert word_count('Hola, me llamo Juan, encantado de conocerte soy Juan', 'spanish') == [('juan', 2), ('hola', 1),
                                                                                             ('llamo', 1),
                                                                                             ('encantado', 1),
                                                                                             ('conocerte', 1)]


def test_use_stopwords():
    assert word_count('hola hola de hola la hola o hola y hola y y hola ante a el la los las', 'spanish') == [
        ('hola', 7)]