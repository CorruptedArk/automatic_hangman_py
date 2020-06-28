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

"""This module contains the SolutionManager class"""

import random as rand
from typing import List

class SolutionManager:
    """This class handles the solution and gamestate during hangman"""
    def __init__(self, dictionary: List[str], solution: str = ""):
        """Constructor takes dictionary as a list of words and optionally a solution as a string"""
        self.dictionary = dictionary
        self.solution = solution
        self.guess_list = []
        self.revealed_text = "_" * len(solution) 
        self.wrong_guess_count = 0

    def generate_random_solution(self) -> None:
        """
        Picks a random solution from the dictionary
        Also preps the manager for a new game
        """
        self.solution = rand.choice(self.dictionary)
        self.revealed_text = "_" * len(self.solution) 
        self.guess_list = []
        self.wrong_guess_count = 0

    def set_solution(self, solution: str) -> None:
        """
        Sets the solution directly from input
        Also preps the manager for a new game
        """
        self.solution = solution
        self.revealed_text = "_" * len(solution) 
        self.guess_list = []
        self.wrong_guess_count = 0

    def is_guess_correct(self, guess: str) -> bool:
        """
        Returns true if the guess is correct
        Also progresses the state of the game
        """
        is_correct = guess in self.solution
        is_repeat = guess in self.guess_list
        if not is_repeat:
            self.guess_list.append(guess)
        new_revealed = ""
        if(is_correct and not is_repeat):  
            for i in range(len(self.solution)):
                if self.solution[i] == guess:
                    new_revealed += guess
                else:
                    new_revealed += self.revealed_text[i]
            self.revealed_text = new_revealed
        else:
            self.wrong_guess_count += 1

        return is_correct and not is_repeat

    def reveal_text(self) -> str:
        """Returns the currently revealed text"""
        return self.revealed_text 

    def solution_found(self) -> bool:
        """Returns True if all letters in the solution are found"""
        return "_" not in self.revealed_text

    def get_wrong_guess_count(self) -> int:
        """Returns the current number of incorrect guesses"""
        return self.wrong_guess_count
