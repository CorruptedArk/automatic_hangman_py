#!/usr/bin/env python3

# automatic_hangman_py is a program designed to play hangman better than any human and allow a human to play as well
#   Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

#   automatic_hangman_py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   automatic_hangman_py is distributed in the hope that it will be interesting and fun,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""This module contains the OptimalMachine class"""

import random
from typing import List

class OptimalMachine:
    """This class handles the logic of the hangman solver"""
    def __init__(self, dictionary: List[str]):
        """Constructor takes dictionary as a list of words"""
        self.dictionary = dictionary.copy()
        self.subdictionary = []
        self.guess_count = 0
        self.guess_list = []
        self.probabilities = {"a":0.0, "b":0.0, "c":0.0, "d":0.0, "e":0.0, "f":0.0, "g":0.0, "h":0.0, "i":0.0, "j":0.0, "k":0.0, "l":0.0, "m":0.0, "n":0.0, "o":0.0, "p":0.0, "q":0.0, "r":0.0, "s":0.0, "t":0.0, "u":0.0, "v":0.0, "w":0.0, "x":0.0, "y":0.0, "z":0.0}
    
    def _filter_dictionary(self, letter: str, revealed_text: str, include:bool) -> None:
        """Filters the current subdictionary based on revealed text and if a letter is a correct guess"""
        temp_dict = self.subdictionary.copy()

        if include:
            for word in temp_dict:
                if not letter in word:
                    self.subdictionary.remove(word)
        else:
            for word in temp_dict:
                if letter in word:
                    self.subdictionary.remove(word)
        
        temp_dict = self.subdictionary.copy()
         
        for word in temp_dict:
            for index in range(len(revealed_text)):
                if revealed_text[index] != "_" and revealed_text[index] != word[index]:
                    self.subdictionary.remove(word)
                    break

    def _set_probabilities_from_dictionary(self) -> None: 
        """Sets letter probabilities by frequency in the current list of possible words"""
        total = 0.0

        for letter, probability in self.probabilities.items():
            self.probabilities[letter] = 0.0

        for letter, probability in self.probabilities.items():
            if letter not in self.guess_list:
                for word in self.subdictionary:
                    for word_letter in word:
                        if letter == word_letter:
                            self.probabilities[letter] += 1
            total += self.probabilities[letter]
                
        if total > 0.0:        
            for letter, probability in self.probabilities.items():
                self.probabilities[letter] = probability / total   

    def receive_feedback(self, revealed_text: str, last_guess_correct:bool) -> None:
        """Handles feedback about the most recent guess"""
        self._filter_dictionary(self.guess_list[-1], revealed_text, last_guess_correct)

    def guess(self, revealed_text: str) -> str:
        """Returns a single letter guess based on the currently revealed letters"""
        if self.guess_count == 0:
            for word in self.dictionary:
                if len(word) == len(revealed_text):
                    self.subdictionary.append(word)
        self._set_probabilities_from_dictionary()
        probability_list = [(k, v) for k, v in self.probabilities.items()]
        random.shuffle(probability_list)
        probability_list = sorted(probability_list, key=lambda item: item[1], reverse=True)
        guess = probability_list[0][0]

        self.guess_list.append(guess)
        self.guess_count += 1
        return guess
        
    def reset(self) -> None:
        """Resets the machine so that it is ready for the next word"""
        self.subdictionary = []
        self.guess_count = 0
        self.guess_list = []
        for letter, probability in self.probabilities.items():
            self.probabilities[letter] = 0.0

