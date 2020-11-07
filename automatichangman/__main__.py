#!/usr/bin/env python3

# tic-tac-toe-py is a simple terminal tic tac toe game written in Python
#   Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

#   tic-tac-toe-py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   tic-tac-toe-py is distributed in the hope that it will be fun,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""This is the main module. It handles the overarching functionality of the program."""

from termcolor import colored, cprint
import time
from automatichangman.optimalmachine import OptimalMachine
from automatichangman.solution_manager import SolutionManager

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

GREY = 'grey'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
WHITE = 'white'

MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '2'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

ABOUT = f"""automatic_hangman_py {VERSION} - Fork me at <https://github.com/CorruptedArk/automatic_hangman_py>

automatic_hangman_py is a program designed to play hangman better than any human and allow a human to play as well
  Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

  automatic_hangman_py is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  automatic_hangman_py is distributed in the hope that it will be interesting and fun,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

quit_loop = False
    
DICTIONARY = pkg_resources.read_text(__package__, 'words_alpha.txt').split() 
machine = OptimalMachine(DICTIONARY)
solution_manager = SolutionManager(DICTIONARY)

def get_version() -> str:
    """Returns the formatted version string"""
    return VERSION

def body(wrong_guesses:int) -> str:
    """This function returns the correct ASCII art of the hangman body for a number of wrong guesses"""

    body0 = """ 
     -----   
     |   |
     |   
     |   
     |  
    --- 
    """

    body1 = """
     -----   
     |   |
     |   O
     |   
     |  
    --- 
    """

    body2 = """
     -----   
     |   |
     |   O
     |   |
     |  
    --- 
    """
    
    body3 = """
     -----   
     |   |
     |   O
     |  /|
     |  
    --- 
    """

    body4 = """
     -----   
     |   |
     |   O
     |  /|\\
     |  
    --- 
    """

    body5 = """ 
     -----   
     |   |
     |   O
     |  /|\\
     |  / 
    --- 
    """

    body6 = """
     -----   
     |   |
     |   O
     |  /|\\
     |  / \\
    --- 
    """

    switch = {
        0: colored(body0, GREEN),
        1: colored(body1, BLUE),
        2: colored(body2, CYAN),
        3: colored(body3, WHITE),
        4: colored(body4, YELLOW),
        5: colored(body5, RED),
        6: colored(body6, RED)
    }

    return switch.get(wrong_guesses, "error")

def wipe_screen() -> None:
    """Clears all text from the terminal"""
    print(chr(27) + "[H" + chr(27) + "[J", end="")

def let_machine_play() -> None:
    """Runs the hangman loop with the machine as the player"""
    wipe_screen()
    solution = input("Type a word for the machine to solve or leave it empty for a random word: ")
    if solution.isalpha():
        solution_manager.set_solution(solution.lower())
    else:
        solution_manager.generate_random_solution()
   
    game_over = False
    while not game_over:
        wipe_screen()
        #TODO - print out the state of the game
        # print(machine.probabilities)
        print(f"Solution: {solution_manager.solution}")
        print(body(solution_manager.get_wrong_guess_count()))
        print(solution_manager.reveal_text())
        print(f"Guesses: {solution_manager.guess_list}")
        print(f"Incorrect guesses: {solution_manager.get_wrong_guess_count()}")
        guess = machine.guess(solution_manager.reveal_text())
        is_correct = solution_manager.is_guess_correct(guess)
        machine.receive_feedback(solution_manager.reveal_text(), is_correct) 
        game_over = solution_manager.solution_found() or solution_manager.get_wrong_guess_count() > 5
        time.sleep(2)

    #TODO - print out the win/loss state
    wipe_screen()
    print(f"Solution: {solution_manager.solution}")
    print(body(solution_manager.get_wrong_guess_count()))
    print(solution_manager.reveal_text())
    print(f"Guesses: {solution_manager.guess_list}")
    print(f"Incorrect guesses: {solution_manager.get_wrong_guess_count()}")
    if solution_manager.solution_found():
        cprint("\nMachine wins!\n", GREEN)
    else:
        cprint("\nMachine loses!\n", RED)
    machine.reset()     
    
def let_player_play() -> None:
    """Runs the hangman loop with a human player"""
    wipe_screen()
    solution_manager.generate_random_solution()
    print("Alright, time to test your ability at hangman!")
    
    game_over = False
    while not game_over:
        #TODO - print out the state of the game 
        print(body(solution_manager.get_wrong_guess_count()))
        print(solution_manager.reveal_text())
        print(f"Guesses: {solution_manager.guess_list}")
        print(f"Incorrect guesses: {solution_manager.get_wrong_guess_count()}")
        guess = input("Enter your next guess: ")
        solution_manager.is_guess_correct(guess)
        game_over = solution_manager.solution_found() or solution_manager.get_wrong_guess_count() > 5
        wipe_screen()

    #TODO - print out the win/loss state
    if not solution_manager.solution_found():
        print(f"Solution: {solution_manager.solution}")
    print(body(solution_manager.get_wrong_guess_count()))
    print(solution_manager.reveal_text())
    print(f"Guesses: {solution_manager.guess_list}")
    print(f"Incorrect guesses: {solution_manager.get_wrong_guess_count()}")
    if solution_manager.solution_found():
        cprint("\nYou win!\n", GREEN)
    else:
        cprint("\nYou lose!\n", RED)

def print_about() -> None:
    """Prints out about and license information"""
    wipe_screen()
    print(ABOUT)

def quit_program() -> None:
    """Sets the quit_loop variable to True so that the main loop terminates"""
    global quit_loop
    quit_loop = True

def print_error() -> None:
    """Wipes the screen and prints out an error"""
    wipe_screen()
    print("Invalid choice, try again.")

def main() -> None:
    """The main function. It handles the main program loop."""
    wipe_screen()
    print("Welcome to automatic_hangman_py!") 
    global quit_loop
    while not quit_loop:

        try:
            option = int(input("""Choose one of the following options.
        
    1. Let the machine play
    2. Play hangman yourself
    3. Learn about this program
    4. Quit
            
Enter number: """))
        except ValueError:
            option = 0

        switch = {
            1: let_machine_play,
            2: let_player_play,
            3: print_about,
            4: quit_program
        }

        func = switch.get(option, print_error)
        func()

if __name__ == "__main__":
    main()
