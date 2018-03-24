# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap,
# Dustin Wehr, Brian Harrington, Rixin Wang
# Distributed under the terms of the GNU General Public License.
#
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
from ConsoleController import ConsoleController
from GUIController import GUIController
from TOAHModel import TOAHModel

import time
NUM_CHEESES = 3


def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5,
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to use ConsoleController to animate the
       tour
       delay_btw_moves - time delay between moves in seconds IF
                         console_animate == True
                         no effect if console_animate == False
    """
    # get the number of cheeses
    num_cheeses = model.number_of_cheeses()
    # move cheeses from stool[0] to stool[3] using Frame-Stewart Algorithm
    frame_stewart(model, num_cheeses, 0, 3, 1, 2)

    # if animation is enabled
    if console_animate is True:
        # initiate the ConsoleController with num_cheeses and 4 stools
        console = ConsoleController(num_cheeses, 4)
        # display the Tour's current state
        print(console._tour)

        # get number of moves
        num_movs = model.number_of_moves()
        # get the move sequence from model
        mov_seq = model.get_move_seq()
        # create a loop that:
        for i in range(0, num_movs):
            # move cheese according to the move sequence
            (src_stool, dest_stool) = mov_seq.get_move(i)
            console._tour.move(src_stool, dest_stool)
            # display the state of Tour at each step
            print(console._tour)
            time.sleep(delay_btw_moves)


def get_k(n):
    '''(int) -> int

    Helper function for STEP 1 of the Frame-Stewart Algorithm that
    picks the initial k number of cheeses to be moved using all four stools
    '''
    # current formula used: k = N - (sqrt(2N + 1) + 1)
    return int(n - ((2*n + 1)**(1/2.0)) + 1)


def hanoi(model, num_cheeses, orig_stool, dest_stool, spare_stool):
    '''(TOAHModel, int, int, int, int) -> NoneType

    Helper function for STEP 2 of the Frame-Stewart Algorithm
    that moves number of cheese from the origin stool to the destination
    stool using the classic ToH Algorithm
    '''
    # base case: move 1 cheese from the orig_stool to dest_stool
    if num_cheeses == 1:
        model.move(orig_stool, dest_stool)

    else:
        # RD: move n-1 cheeses from orig_stool to the spare_stool
        # using the dest_stool as spare
        hanoi(model, num_cheeses-1, orig_stool, spare_stool, dest_stool)
        # move the largest cheese from orig_stool to dest_stool
        model.move(orig_stool, dest_stool)
        # lastly move n-1 cheeses from the spare_stool to dest_stool
        # using the orig_stool as the spare
        hanoi(model, num_cheeses-1, spare_stool, dest_stool, orig_stool)


def frame_stewart(model, num_cheeses, orig_stool, dest_stool, spare_stool_1,
                  spare_stool_2):
    '''(TOAHModel, int, int, int, int, int) -> NoneType

    The Frame-Stewart Algorithm for solving a variation of ToH puzzle using
    four stools

    STEP 1: move the first k=n-i cheeses to intermediate using 4 stools
    STEP 2: move the rest of the cheeses to destination using 3 stools
    STEP 3: move k cheeses from intermediate to destination using 4 stools
    '''
    # base case: use ToH algorithm if num_cheeses is less than or equal to 2
    if num_cheeses <= 2:
        hanoi(model, num_cheeses, orig_stool, dest_stool, spare_stool_1)

    else:
        # solve for k=n-i cheeses to move
        k = get_k(num_cheeses)
        # STEP 1: move k cheeses from orig_stool to spare_stool_1
        #         using all 4 stools
        frame_stewart(model, k, orig_stool, spare_stool_1, spare_stool_2,
                      dest_stool)

        # find the number of cheeses to move using 3 stools
        num_for_hanoi = num_cheeses - k
        # STEP 2: move these use the ToH algorithm
        hanoi(model, num_for_hanoi, orig_stool, dest_stool, spare_stool_2)

        # STEP 3: use 4 stools again to move k cheeses
        #         from spare_stool_1 to dest_stool
        frame_stewart(model, k, spare_stool_1, dest_stool, orig_stool,
                      spare_stool_2)


if __name__ == '__main__':
    # DO NOT MODIFY THE CODE BELOW.

    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=5)

    tour_of_four_stools(four_stools,
                        console_animate=True,
                        delay_btw_moves=0.05)

    print(four_stools.number_of_moves())
