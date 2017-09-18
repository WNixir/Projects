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
TOAHModel:  Model a game of Towers of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Towers of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


class TOAHModel:
    """Model a game of Towers Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.  Note that
    large, aged, cheeses at the bottom of each pile serve as stools, and
    these may not be moved!

    fill_first_stool - put an existing model in the standard starting config
    move - move cheese from one stool to another
    add - add a cheese to a stool
    cheese_location - index of the stool that the given cheese is on
    number_of_cheeses - number of cheeses in this game
    number_of_moves - number of moves so far
    number_of_stools - number of stools in this game
    get_move_seq - MoveSequence object that records the moves used so far
    """

    def __init__(self, number_of_stools):
        '''(TOAHModel, int) -> NoneType

        Initialize a model for TOAH with a number of stools
        '''
        # Representation Invariant
        # self._number_of_moves keeps count of the number of times
        # a piece of cheese is moved from a stool to the next
        #
        # self._number_of_stools is the number of stools used
        # for TOAHModel indexed from 0 to n where the 0th stool
        # is the first stool
        #
        # self._move_seq keeps track of all the indivdual moves that has
        # been performed using the current TOAHModel, indexed from 0 to n
        # where the 0th move is the first move

        self._number_of_moves = 0
        self._number_of_stools = number_of_stools
        self._move_seq = MoveSequence([])

        # use a list to store the stools
        self._stools = []
        # for each stool use a list to store the Cheeses
        for i in range(number_of_stools):
            self._stools.append([])

    def fill_first_stool(self: 'TOAHModel', number_of_cheeses: int):
        """
        Put number_of_cheeses cheeses on the first (i.e. 0-th) stool, in order
        of size, with a cheese of size == number_of_cheeses on bottom and
        a cheese of size == 1 on top.
        """
        # create a list to store all cheeses
        self._cheeses = []
        for i in range(1, number_of_cheeses+1):
            self._cheeses.append(Cheese(i))
        # reverse the list to order the cheese from largest to smallest
        self._cheeses.reverse()
        # add the stack of cheese to the 0th stool
        self._stools[0] = self._cheeses

    def top_cheese(self, stool):
        '''(TOAHModel, int) -> Cheese

        Return the top cheese from a stool at given index

        RAISES: IllegalMoveError if the wanted stool is not at valid index
        '''
        # raise error if the wanted stool is at an invalid index
        if (stool < 0) or (stool > self.number_of_stools()-1):
            raise IllegalMoveError
        # else return the top cheese
        else:
            return self._stools[stool][-1]

    def move(self, src_stool, dest_stool):
        '''(TOAHModel, int, int) -> NoneType

        Moves the top cheese from the source stool to destination stool

        RAISES: IllegalMoveError if src_stool is not at valid index
        RAISES: IllegalMoveError if dest_stool is not at valid index

        '''
        # check there is at least 1 cheese at the src_stool
        # and check the src_stool and dest_stool are at valid indexes
        if (len(self._stools[src_stool]) < 1) or (src_stool < 0) or (
            dest_stool < 0) or (src_stool > self.number_of_stools()-1) or (
                 dest_stool > self.number_of_stools()-1):
            raise IllegalMoveError

        else:
            # get the cheese from the top of src_stool
            new_cheese = self.top_cheese(src_stool)
            # check the size of the cheese is smaller than
            # the cheese at the top of dest_stool
            if (len(self._stools[dest_stool]) != 0) and (
                  new_cheese.size >= self.top_cheese(dest_stool).size):
                raise IllegalMoveError
            # else add the cheese to the dest_stool
            else:
                self.add(dest_stool, new_cheese)
                # remove the cheese from the src_stool
                self._stools[src_stool].pop()
                # update the number of moves
                self._number_of_moves += 1
                # update the list of move sequence
                self._move_seq.add_move(src_stool, dest_stool)

    def add(self, dest_stool, new_cheese):
        '''(TOAHModel, int, Cheese) -> NoneType

        Add a new piece of cheese to the destination stool

        RAISES: IllegalMoveError when the dest stool is not at valid index
        RAISES: IllegalMoveError if the new_cheese is of bigger size than
                what's on top of the dest_stool
        '''
        # raise error if dest_stool is not at a valid index or if
        # new cheese is larger than the size of the top cheese in dest_stool
        if (dest_stool > self.number_of_stools()-1) or (
              dest_stool < 0) or ((len(self._stools[dest_stool]) != 0) and (
                  self.top_cheese(dest_stool).size <= new_cheese.size)):
            raise IllegalMoveError

        # elif dest stool is empty or all the cheeses on dest stool
        # are larger than the new_cheese
        elif (len(self._stools[dest_stool]) == 0) or (
             self.top_cheese(dest_stool).size > new_cheese.size):
            # add the new_cheese to the stool
            self._stools[dest_stool].append(new_cheese)

    def cheese_location(self, cheese):
        '''(TOAHModel, Cheese) -> int

        Get the stool index location of the cheese we are looking for
        '''
        # loop over each stools
        for stool in self._stools:
            # if cheese is found return the index of the stool
            if cheese in stool:
                return self._stools.index(stool)

    def number_of_cheeses(self):
        '''(TOAHModel) -> int

        Return the number of cheeses used in the current config
        '''
        total = 0
        # loop over each stool
        for stool in self._stools:
            # total the number of cheeses from each stool
            total += len(stool)
        return total

    def number_of_moves(self):
        '''(TOAHModel) -> int'''
        return self._number_of_moves

    def number_of_stools(self):
        '''(TOAHModel) -> int'''
        return self._number_of_stools

    def get_move_seq(self: 'TOAHModel') -> 'MoveSequence':
        return self._move_seq

    def _cheese_at(self: 'TOAHModel', stool_index,
                   stool_height: int) -> 'Cheese':
        """
        If there are at least stool_height+1 cheeses
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        # if stool height is at least equal to
        # the number of cheeses on the stool
        if (stool_height+1 <= len(self._stools[stool_index])):
            # return the cheese at the stool height
            result = self._stools[stool_index][stool_height]
        # else return None
        else:
            result = None
        return result

    def __eq__(self: 'TOAHModel', other: 'TOAHModel') -> bool:
        """
        We're saying two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0,1)
        >>> m1.move(0,2)
        >>> m1.move(1,2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0,3)
        >>> m2.move(0,2)
        >>> m2.move(3,2)
        >>> m1 == m2
        True
        """
        # check both are TOAHModels and their stools have the same config
        return (isinstance(other, TOAHModel)) and (
                    self._stools == other._stools)

    def __str__(self: 'TOAHModel') -> str:
        """
        Depicts only the current state of the stools and cheese.
        """
        stool_str = "=" * (2 * (self.number_of_cheeses()) + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.number_of_stools()

        def cheese_str(size: int):
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = cheese_str(int(c.size))
                else:
                    s = cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


class Cheese:
    def __init__(self: 'Cheese', size: int):
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __repr__(self: 'Cheese') -> str:
        """
        Representation of this Cheese
        """
        return "Cheese(" + str(self.size) + ")"

    def __eq__(self: 'Cheese', other: 'Cheese') -> bool:
        """Is self equivalent to other? We say they are if they're the same
        size."""
        return isinstance(other, Cheese) and self.size == other.size


class IllegalMoveError(Exception):
    pass


class MoveSequence(object):
    def __init__(self: 'MoveSequence', moves: list):
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self: 'MoveSequence', i: int):
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self: 'MoveSequence', src_stool: int, dest_stool: int):
        self._moves.append((src_stool, dest_stool))

    def length(self: 'MoveSequence') -> int:
        return len(self._moves)

    def generate_TOAHModel(self: 'MoveSequence', number_of_stools: int,
                           number_of_cheeses: int) -> 'TOAHModel':
        """
        An alternate constructor for a TOAHModel. Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in move_seq.
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

    def __repr__(self: 'MoveSequence') -> str:
        return "MoveSequence(" + repr(self._moves) + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
