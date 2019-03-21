#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:
    console_scripts =
         fibonacci = word_counter_tdd.skeleton:run
Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.
Note: This skeleton file can be safely removed if not needed!
"""

from nltk.corpus import stopwords
import sys


def word_count(text, stopwords_language='english'):
    if not isinstance(text, str) or not isinstance(stopwords_language, str):
        raise ValueError

    text = ' '.join(text.split())  # Quitamos todos los espacios extra entre palabras
    words = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "") \
        .replace("¿", "").replace("¡", "")
    # Los apostrofes son un problema, asi que hay que cambiar los signos de puntuacion a mano

    words = words.split(' ')  # Separamos por palabras

    words = [word.lower() for word in words if word.lower() not in stopwords.words(stopwords_language)]

    words_count = {}

    for key in words:
        words_count[key] = words_count.get(key, 0) + 1
        # get funciona tal que si existe la clave devuelve el valor, si no devuelve el segundo parametro

    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)  # Ordenamos las palabras segun lo pedido


def main(args):
    """Main entry point allowing external calls
    Args:
      args ([str]): command line parameter list
    """


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    word_count("hello   buddy")
    run()
