# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap,
# Dustin Wehr, Brian Harrington, Rixin Wang
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Summer 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
ConsoleController: User interface for manually solving Anne Hoy's problems
from the console.

move: Apply one move to the given model, and print any error message
to the console.
"""

from TOAHModel import TOAHModel, Cheese, IllegalMoveError
import tkinter as TI
import time


def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console.

    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want
             to move
    dest - the stool number that you want to move the top cheese
            on stool origin onto.
    '''
    # use the move method from TOAHModel
    model.move(origin, dest)


class ConsoleController:

    def __init__(self: 'ConsoleController',
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool,
                            not counting the bottom cheese acting as stool
        number_of_stools - number of stools, to be shown as large cheeses
        """
        # Representation Invariant
        # ConsoleController is an interactive TOAHModel
        # created using a player defined number of cheeses
        # and player defined number of stools
        #
        # all the cheeses will be placed at the 0th stool at the start
        # at the end all the cheeses will be moved to the nth stool
        # by the player, where self._tour will be equivalent to self._end_tour

        # create the tour with the number of stools
        self._tour = TOAHModel(number_of_stools)
        # and fill the first stool with the number of cheeses
        self._tour.fill_first_stool(number_of_cheeses)
        # create the wanted tour with the number of stools
        self._end_tour = TOAHModel(number_of_stools)
        # make a copy of the cheeses from the 0th stool of self._tour
        s_copy = self._tour._stools[0].copy()
        # move it to the last stool of end_tour
        self._end_tour._stools[-1] = s_copy

    def play_loop(self: 'ConsoleController'):
        '''
        Console-based game.
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provded to print a representation of the current state of the game.
        '''
        player_input = ''
        # check the game's current state and the desired state
        # stop when both are equivalent or the player choose to exit the game
        while (not self._tour.__eq__(self._end_tour)) and (
             player_input != "E"):
            print(self._tour)
            print('Number of moves: ' + str(self._tour.number_of_moves()))

            # ask the player for input
            player_input = input("Enter your command: ")
            # if player entered 'E', exit the game
            if player_input == 'E':
                print('Goodbye!')
            else:
                # move the cheeses accodring to player input
                try:
                    origin = int(player_input[0])
                    dest = int(player_input[-1])
                    move(self._tour, origin, dest)
                except:
                    print('Illegal Move! Try again.')

        # exit when all cheeses are moved from 1st to last stool
        if self._tour.__eq__(self._end_tour):
            print(self._tour)
            print('Tour Completed. Congratulations!')
            print('Total number of moves: ' + str(
                               self._tour.number_of_moves()))


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    print('''
    Welcome to the Tour of Anne Hoy, a more fun version of the classic
    puzzle: Tower of Hanoi! Here instead of moving plates from tower to
    tower, you'll be asked to move pieces of cheeses from stool to stool!
    YAY!! The objective of the game is to move all the cheeses from the
    1st stool (indexed at 0) to the last stool. I know you must be
    DYING to start playing! But before you jump right in, here's some rules
    to keep in mind:

    To win:
    1. You must move all the cheeses from the first stool to the last stool
    2. Only one cheese can be moved at any given time
    3. Only the top cheese can be moved at any given time
    4. Larger cheese can NOT be placed on top of a smaller cheese

    To play:
    1. Initiate the game by entering the number of cheeses you would like
       to play with. Be sensible! The number can be any positive integer
       greater than 1. But if you really want to spend an eternity on moving
       infinite cheeses from one stool to the next, I ain't gonna stop you.
    2. Enter the number of stools you are going to use, please use at least
       2 stools, otherwise the game would be boring!! In fact, I recommend
       at least 3 stools if you intend to move more than 1 piece of cheese.

    Controls:
    1. Move a piece of cheese from one stool to another by entering 2 integers
    where the first integer is the stool you are moving from (indexed at
    0), and the 2nd integer is the stool you are moving the cheese to.
    2. To exit the game at any time, simply enter "E" (must be capitalized)

    For example:
        To move a piece of cheese from the 1st stool to the 2nd stool
        in the following Tour
              -
             ===  ===

        I just need to enter: 01
                   -
             ===  ===
        At this point all the cheeses have been moved to the last stool,
        and the game ends.
    ''')
    number_of_cheeses = ''
    # ask the player to input the number of cheeses to play with
    # and check that the entry is a positive integer no less than 1
    while (not isinstance(number_of_cheeses, int)) or (number_of_cheeses < 1):
        number_of_cheeses = input("To start, enter the number of cheeses\
 for this Tour: ")
        try:
            number_of_cheeses = int(number_of_cheeses)
            # check the number of cheeses is at least 1
            if number_of_cheeses < 1:
                print('Please play with at least 1 Cheese')
        except:
            print('Please enter a positive integer')

    number_of_stools = ''
    # ask the player to input the number of stools to play with
    # check the entry is a positive integer no less than 2
    while (not isinstance(number_of_stools, int)) or (number_of_stools < 2):
        number_of_stools = input('Enter the number of stools for this Tour: ')
        try:
            number_of_stools = int(number_of_stools)
            # check the number of stools is at least 2
            if number_of_stools < 2:
                print('Please play with at least 2 Stools')
        except:
            print('Please enter a positive integer')

    # if the players has enterd more than 1 Cheese and less than 3 stools
    # game is unsolvable
    if (number_of_cheeses > 1) and (number_of_stools < 3):
        print("Sorry, I don't think this game is solvable...")
    else:
        # start the game with player's inputs
        tour = ConsoleController(number_of_cheeses, number_of_stools)
        tour.play_loop()
