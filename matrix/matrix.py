class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''


class MatrixDimensionError(Exception):
    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''


class MatrixInvalidOperationError(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, row, column, contents, right=None, down=None):
        '''(MatrixNode, int, int, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        # Representation Invariant
        # contents is the data stored in the Matrix
        # if self._contents is None
        # the Node is the head node of a Matrix:
        #    column is the total columns the Matrix has
        #    row is the total num of rows the Matrix has
        #    self._contents is None
        #
        # if right is None:
        #    there are no more columns to the right of current Node
        #
        # if down is None:
        #    there are no more rows below the current Node
        #
        # elif (contents is not None, the Node represents an entry in
        #        the Matrix) and (right or down are not None):
        #     row is an int representing the Node's row position in Matrix
        #     column is an int representing the Node's col position in the
        #          Matrix
        #    self._right is a Node from the next column
        #    self._right is a node from the next row

        self._contents = contents
        self._row = row
        self._column = column
        self._right = right
        self._down = down

    def __repr__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_row_num(self):
        '''(MatrixNode) -> int
        Return the row number value stored in this node
        '''
        return self._row

    def get_column_num(self):
        '''(MatrixNode) -> int
        Return the column number value stored in this node
        '''
        return self._column

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node


class Matrix():
    '''A class to represent a mathematical matrix
    Note: Uses 0-indexing, so an m x n matrix will have
    indices (0,0) through (m-1, n-1)'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        # Representation Invariant
        # m is the dimension of the rows
        # n is the dimension of columns
        # default is the default_values at every index of a newly made Matrix
        # self._total_rows is the row index, starting from 0
        # self._total_columms is the col index, starting from 0
        # a mXn matrix have indices (0, 0) to (m-1, n-1)
        # the head of the Matrix stores the index of the Matrix
        self._head = MatrixNode(m, n, None)
        self._default = default
        self._total_rows = m-1
        self._total_columns = n-1

    def _traverse(self, i, j):
        '''(Matrix, int, int) -> tuple
        A helper function that returns the memory addresses of a Node at index
        (i, j),  and the addresses to  Nodes immediately to the left and
        above the Node
        '''
        curr = self._head
        ret_node = None
        left_pointer = self._head.get_down()
        up_pointer = self._head.get_right()

        row_count = 0
        col_count = 0
        # if the node is in zeroeth row
        if (i == 0) and (curr.get_down()):
            curr = curr.get_down()
        # if the node is in zeroeth column
        if (j == 0) and (curr.get_right()):
            curr = curr.get_right()
        # loop down to the correct row
        while (row_count < i) and (curr.get_down()):
            curr = curr.get_down()
            row_count = curr.get_row_num()
        # loop right to the correct column
        while (col_count < j) and (curr.get_right()):
            curr = curr.get_right()
            col_count = curr.get_column_num()

        # return the address of the node if it matches the row and col num
        if (curr.get_row_num() == i) and (curr.get_column_num() == j):
            ret_node = curr

        # move the left_node pointer to the left of curr
        if left_pointer is not None:
            while (left_pointer.get_row_num() < i) and (
                   left_pointer.get_down()):
                left_pointer = left_pointer.get_down()
            while (left_pointer.get_right() is not ret_node) and (
                   left_pointer.get_right()) and (
                       left_pointer.get_right().get_column_num() < j):
                left_pointer = left_pointer.get_right()

        # move the up_node to above the node we want
        if up_pointer is not None:
            while (up_pointer.get_column_num() < j) and (
                   up_pointer.get_right()):
                up_pointer = up_pointer.get_right()
            while (up_pointer.get_down() is not ret_node) and (
                   up_pointer.get_down()) and (
                       up_pointer.get_down().get_row_num() < i):
                up_pointer = up_pointer.get_down()
        return ret_node, left_pointer, up_pointer

    def _find_node(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        A helper function that returns the a Node address in the Matrix
        '''
        return self._traverse(i, j)[0]

    def _left_node(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        A helper function that returns the Node immediately to the left of
        target Node
        '''
        left_node = None
        pointer = self._traverse(i, j)[1]

        # check the left_node is in the correct row
        if pointer and (pointer.get_row_num() == i):
            left_node = pointer
        return left_node

    def _up_node(self, i, j):
        '''(Matrix, int, int) -> MatrixNode
        A helper function that returns the Node immediately to above the target
        Node
        '''
        up_node = None
        pointer = self._traverse(i, j)[2]

        # check the up_node in in the correct column
        if pointer and (pointer.get_column_num() == j):
            up_node = pointer
        return up_node

    def _insert_row_head(self, row_head):
        '''(Matrix, MatrixNode) -> NoneType
        Insert a newly created ith row_head node into a sorted linked list
        keeping track of all rows in a Matrix
        '''
        # if the Matrix is currently empty, link the new Node to the head
        if self._head.get_down() is None:
            self._head.set_down(row_head)

        # if the new row index is less than the existing first down_node
        # linkd the new node between the head and the 1st row head
        elif (self._head.get_down().get_row_num()) > (
              row_head.get_row_num()):
            row_head.set_down(self._head.get_down())
            self._head.set_down(row_head)

        # loop over the rows and find the previous node
        else:
            curr = self._head
            while (curr.get_down() is not None) and (
                   curr.get_down().get_row_num() < row_head.get_row_num()):
                curr = curr.get_down()
            row_head.set_down(curr.get_down())
            curr.set_down(row_head)

    def _insert_column_head(self, col_head):
        '''(Matrix, MatrixNode) -> NoneType
        Insert a newly created jth col_head node into a sorted linked list
        keeping trackt of all columns in a Matrix
        '''
        # if the Matrix is empty, link the matrix head to the col_head
        if self._head.get_right() is None:
            self._head.set_right(col_head)

        # if the new col index is less than the first right_node
        # inser the new col_head between the head the first col_node
        elif (self._head.get_right().get_column_num()) > (
              col_head.get_column_num()):
            col_head.set_right(self._head.get_right())
            self._head.set_right(col_head)

        # else loop right to the correct column position
        else:
            curr = self._head
            while (curr.get_right() is not None) and (
                   curr.get_right().get_column_num() <
                   col_head.get_column_num()):
                curr = curr.get_right()
            col_head.set_right(curr.get_right())
            curr.set_right(col_head)

    def _delete(self, i, j):
        '''(Matrix, int, int) -> NoneType
        a helper function that deletes a node at the (i, j) index from Matrix
        '''
        del_node = self._find_node(i, j)
        # if the Node exists
        # set the up_node's down to old node's down
        # set the left_node's right to the old node's right
        if del_node:
            up_node = self._up_node(i, j)
            left_node = self._left_node(i, j)
            up_node.set_down(del_node.get_down())
            left_node.set_right(del_node.get_right())

    def _go_to_row(self, row_num):
        '''(Matrix, int) -> MatrixNode
        a helper function that finds the head of an existing row in the Matrix
        '''
        row_head = None
        curr = self._head
        counter = 0
        # if the row we want is the zeroeth row
        # the row head is down from the head_node
        if (row_num == 0) and (curr.get_down().get_row_num() == 0):
            row_head = curr.get_down()
        else:
            # find the wanted row in the Matrix
            while counter < row_num and curr.get_down():
                curr = curr.get_down()
                counter = curr.get_row_num()

                # if curr's row num is the same as the wanted
                # return curr
                if curr.get_row_num() == row_num:
                    row_head = curr
        return row_head

    def _go_to_col(self, col_num):
        '''(Matrix, int) -> MatrixNode
        a helper function that finds the head of an existing col in the Matrix
        '''
        col_head = None
        curr = self._head
        counter = 0

        # if the column we need is the 0th col
        # the col_head is right from the head_node
        if (col_num == 0) and (curr.get_right().get_column_num == 0):
            col_head = curr.get_right()
        else:
            # find the wanted column in the Matrix
            while (counter < col_num) and curr.get_right():
                curr = curr.get_right()
                counter = curr.get_column_num()

                # if curr's col num matches the wanted col
                # return curr
                if curr.get_column_num() == col_num:
                    col_head = curr
        return col_head

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m

        REQ: i and j must both be integers
        '''
        # raise MatrixIndexError if i or j is outside the Matrix
        if (i > self._total_rows) or (j > self._total_columns):
            raise MatrixIndexError

        ret_val = self._default
        # if there is an exsiting Node in current Matrix
        # return its contents
        # else the default value is returned
        if self._find_node(i, j):
            ret_val = self._find_node(i, j).get_contents()
        return ret_val

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m

        REQ: i and j must be integers
        REQ: new_val must be a float

        RAISES: MatrixIndexError when trying to set a new value outside
                of the dimension of the Matrix
        RAISES: MatrixInvalidOperationError is the new_val is a float or int
        '''
        # raise MatrixIndexError if i or j is outside the Matrix
        if (i > self._total_rows) or (j > self._total_columns):
            raise MatrixIndexError

        # raise MatrixInvalidOperationError if new_val is not a float and int
        if (not isinstance(new_val, float)) and (
             not isinstance(new_val, int)):
            raise MatrixInvalidOperationError

        # if m[i, j] is an existing Node in the current Matrix
        # set the Node's content to new_val
        if self._find_node(i, j):
            self._find_node(i, j).set_contents(new_val)

        curr = self._head
        new_node = MatrixNode(i, j, new_val)
        row_head = MatrixNode(i, None, 'row_node: ' + str(i))
        col_head = MatrixNode(None, j, 'col_node: ' + str(j))

        # if the Matrix is empty
        # insert the first node
        if (curr.get_down() is None) and (curr.get_right() is None):
            # create the new head nodes for row and column
            self._insert_row_head(row_head)
            self._insert_column_head(col_head)
            # link the head nodes to the new node
            curr.get_down().set_right(new_node)
            curr.get_right().set_down(new_node)

        else:
            up_node = self._up_node(i, j)
            left_node = self._left_node(i, j)
            existing_row = self._go_to_row(i)
            existing_col = self._go_to_col(j)

            # create a new node if there is no node at the index
            if (not existing_row) and (not existing_col):
                self._insert_column_head(col_head)
                col_head.set_down(new_node)
                self._insert_row_head(row_head)
                row_head.set_right(new_node)

            # insert the new_node into an existing row and column
            elif existing_row and existing_col:
                new_node.set_down(up_node.get_down())
                new_node.set_right(left_node.get_right())
                up_node.set_down(new_node)
                left_node.set_right(new_node)

            # insert a new value into an existing column
            elif up_node and (not existing_row):
                new_node.set_down(up_node.get_down())
                self._insert_row_head(row_head)
                row_head.set_right(new_node)
                up_node.set_down(new_node)

                # insert a new value into an existing row
            elif left_node and (not existing_col):
                self._insert_column_head(col_head)
                col_head.set_down(new_node)
                new_node.set_right(left_node.get_right())
                left_node.set_right(new_node)

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix as an OneDimensionalMatrix

        REQ: row_num must be an integer

        RAISES: MatrixDimensionError when trying to get a row outside
                the matrix
        '''
        # raise MatrixDimensionError if row_num is ouside the Matrix
        if (row_num > self._total_rows):
            raise MatrixDimensionError

        # create a new Matrix
        n = self._total_columns + 1
        default = self._default
        row_matrix = OneDimensionalMatrix(n, default)

        # move a pointer to the wanted row
        curr = self._go_to_row(row_num)
        # if the row exists
        if curr:
            # loop along the row of this Matrix
            # and add any value to the OneDimensionalMatrix
            while curr.get_right():
                col = curr.get_right().get_column_num()
                item = curr.get_right().get_contents()
                row_matrix.set_item(col, item)
                curr = curr.get_right()
        return row_matrix

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row

        REQ: row_num must be an integer
        REQ: new_row must be of type OneDimensionalMatrix

        RAISES: MatrixDimensionError if trying to set a new row
                outside the matrix
        RAISES: MatrixInvalidOperationError if the user tries to pass in
                a none OnedimensionalMatrix as the new row
        '''
        # raise MatrixDimensionError if row_num is ouside the Matrix
        if (row_num > self._total_rows):
            raise MatrixDimensionError

        # raise MatrixInvalidOperationError is the object passed is not
        # an OneDimensionalMatrix
        if not isinstance(new_row, OneDimensionalMatrix):
            raise MatrixInvalidOperationError

        # check to see if the new_row to be inserted is to
        # replace an existing row
        pointer = self._go_to_row(row_num)
        while pointer and pointer.get_right():
                del_node = pointer.get_right()
                row_num = del_node.get_row_num()
                col_num = del_node.get_column_num()
                self._delete(row_num, col_num)

        # move along the OneDimensonalMatrix and add each new value
        # to the original Matrix
        curr = new_row._head.get_down()
        while curr.get_right():
            col_num = curr.get_right().get_column_num()
            new_value = curr.get_right().get_contents()
            self.set_val(row_num, col_num, new_value)
            curr = curr.get_right()

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix

        REQ: col_num must be an integer

        RAISES: MatrixDimensionError when user attempts to get an column
                outside of the matrix
        '''
        # raise MatrixDimensionError if col_num is ouside the Matrix
        if (col_num > self._total_columns):
            raise MatrixDimensionError

        # create a new Matrix
        n = self._total_rows + 1
        default = self._default
        col_matrix = OneDimensionalMatrix(n, default)

        # move a pointer to the wanted row
        curr = self._go_to_col(col_num)
        # if the row exists
        if curr:
            # loop along the row of this Matrix
            # and add any value to the OneDimensionalMatrix
            while curr.get_down():
                col = curr.get_down().get_row_num()
                item = curr.get_down().get_contents()
                col_matrix.set_item(col, item)
                curr = curr.get_down()
        return col_matrix

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix
        to those of new_row

        REQ: col_num must be an integer
        REQ: new_col must be of type OneDimensionalMatrix

        RAISES: MatrixDimensionError when trying to set the new column
                outside of the valid dimension
        RAISES: MatrixInvalidOperationError when attempting to set a
                None OneDimensionalMatrix object as the new column
        '''
        # raise MatrixDimensionError if col_num is ouside the Matrix
        if (col_num > self._total_rows):
            raise MatrixDimensionError

        # raise MatrixInvalidOperationError is the object passed is not
        # an OneDimensionalMatrix
        if not isinstance(new_col, OneDimensionalMatrix):
            raise MatrixInvalidOperationError

        # check to see if the new_col to be inserted is to
        # replace an existing row
        pointer = self._go_to_col(col_num)
        while pointer and pointer.get_down():
                del_node = pointer.get_down()
                row_num = del_node.get_row_num()
                col_num = del_node.get_column_num()
                self._delete(row_num, col_num)

        # move along the OneDimensonalMatrix and add each new value
        # to the original Matrix
        curr = new_col._head.get_down()
        while curr.get_right():
            row_num = curr.get_right().get_column_num()
            new_value = curr.get_right().get_contents()
            self.set_val(row_num, col_num, new_value)
            curr = curr.get_right()

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix

        REQ: i and j must be integers

        RAISES: MatrixDimensionError if i or j is outside of the Matrix
        '''
        # raise MatrixDimensionError if row_num is ouside the Matrix
        if (i > self._total_rows) or (j > self._total_rows):
            raise MatrixDimensionError

        # store the ith and jth row in temp OneDimensionalMatrix
        # then reinsert the new rows
        temp_i = self.get_row(j)
        temp_j = self.get_row(i)
        self.set_row(i, temp_i)
        self.set_row(j, temp_j)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix

        REQ: i and j must be integers

        RAISES: MatrixDimensionError if i or j is outsie the matrix
        '''
        # raise MatrixDimensionError if col_num is ouside the Matrix
        if (i > self._total_columns) or (j > self._total_columns):
            raise MatrixDimensionError

        # store ith col and jth col in temp OneDimensionalMatrix
        # reset the new columns
        temp_i = self.get_col(j)
        temp_j = self.get_col(i)
        self.set_col(i, temp_i)
        self.set_col(j, temp_j)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value

        REQ: add_value must be of type float

        RAISES: MatrixInvalidOperationError if trying the add_value is
                not of type float or int
        '''
        # raise MatrixInvalidOperationError if add_val is not a float and int
        if (not isinstance(add_value, float)) and (
             not isinstance(add_value, int)):
            raise MatrixInvalidOperationError

        # first increase all default value by add_value
        self._default += add_value

        # if the Matrix is none empty
        if self._head.get_down():
            # loop down along the row heads
            row_head = self._head.get_down()
            while row_head:
                # loop along each node in the row
                # and change the contents to new value
                pointer = row_head
                while pointer.get_right():
                    row_node = pointer.get_right()
                    old_val = row_node.get_contents()
                    new_val = old_val + add_value
                    row_node.set_contents(new_val)
                    pointer = pointer.get_right()
                row_head = row_head.get_down()

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # add the negative to the Matrix
        neg = (-sub_value)
        self.add_scalar(neg)

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value

        REQ: mult_value must be a float

        RAISES: MatrixInvalidOperationError is mult_value is not float or int
        '''
        # raise MatrixInvalidOperationError if mult_val is not a float and int
        if (not isinstance(mult_value, float)) and (
             not isinstance(mult_value, int)):
            raise MatrixInvalidOperationError

        # first increase all default value by add_value
        self._default *= mult_value

        # if the Matrix is none empty
        if self._head.get_down():
            # loop down along the row heads
            row_head = self._head.get_down()
            while row_head:
                # loop along each node in the row
                # and change the contents to new value
                pointer = row_head
                while pointer.get_right():
                    row_node = pointer.get_right()
                    old_val = row_node.get_contents()
                    new_val = old_val * mult_value
                    row_node.set_contents(new_val)
                    pointer = pointer.get_right()
                row_head = row_head.get_down()

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix

        REQ: adder_matrix must be another Matrix with compatible dimensions

        RAISES: MatrixDimensionError if tryint to add 2 matrices of
                incompatible dimensions
        RAISES: MatrixInvalidOperationError if the adder_matrix
                is not a Matrix
        '''
        # first check the two Matrix are of the right dimensions
        if (self._total_columns != adder_matrix._total_columns) or (
             self._total_rows != adder_matrix._total_rows):
            raise MatrixDimensionError

        # raise MatrixInvalidOperationError if the
        # object passed is not a Matrix
        if not isinstance(adder_matrix, Matrix):
            raise MatrixInvalidOperationError

        default = self._default + adder_matrix._default
        row = self._total_rows + 1
        column = self._total_columns + 1
        new_matrix = Matrix(row, column, default)

        for i in range(row):
            # get each row from self and adder_matrix
            row_1 = self.get_row(i)
            row_2 = adder_matrix.get_row(i)

            # if the row is non-existing in the second matrix
            # insert the row from 1st matrix into new matrix
            if (row_1._head.get_down() is not None) and (
                 row_2._head.get_down() is None):
                row_1.add_scalar(adder_matrix._default)
                new_matrix.set_row(i, row_1)

            # if the row is non-existing in the first matrix
            # insert the row from 2nd matrix into new matrix
            elif (row_1._head.get_down() is None) and (
                  row_2._head.get_down() is not None):
                row_2.add_scalar(self._default)
                new_matrix.set_row(i, row_2)

            # if the row_index exists in both matrices
            elif (row_1._head.get_down() is not None) and (
                  row_2._head.get_down() is not None):
                pointer_1 = row_1._head.get_down()
                pointer_2 = row_2._head.get_down()

                # loop over each node and add the contents
                while pointer_1.get_right() and pointer_2.get_right():
                    # get the value from matrix 1's nodes
                    # and add to matrix 2's default
                    val_1 = pointer_1.get_right().get_contents()
                    sum_1 = val_1 + adder_matrix._default
                    col_1 = pointer_1.get_right().get_column_num()

                    # get the value from matrix 2's node
                    # and add matrix 1's default to each value
                    val_2 = pointer_2.get_right().get_contents()
                    sum_2 = val_2 + self._default
                    col_2 = pointer_2.get_right().get_column_num()

                    # compare the col_nums
                    if col_1 != col_2:
                        new_matrix.set_val(i, col_1, sum_1)
                        new_matrix.set_val(i, col_2, sum_2)
                    elif col_1 == col_2:
                        new_sum = val_1 + val_2
                        new_matrix.set_val(i, col_1, new_sum)
                    # lastly move the pointers to next node
                    pointer_1 = pointer_1.get_right()
                    pointer_2 = pointer_2.get_right()

                    # find the longer row and add it's values to new_matrix
                    while pointer_1.get_right():
                        val_1 = pointer_1.get_right().get_contents()
                        sum_1 = val_1 + adder_matrix._default
                        col_1 = pointer_1.get_right().get_column_num()
                        new_matrix.set_val(i, col_1, sum_1)
                        pointer_1 = pointer_1.get_right()
                    while pointer_2.get_right():
                        val_2 = pointer_2.get_right().get_contents()
                        sum_2 = val_2 + self._default
                        col_2 = pointer_2.get_right().get_column_num()
                        new_matrix.set_val(i, col_2, sum_2)
                        pointer_2 = pointer_2.get_right()
        return new_matrix

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix

        REQ: mult_matrix must be another matrix with compatible dimensions

        RAISES: MatrixDimensionError if trying to multiply 2 matrices where
                the num of columns of the first matrix is not equal to the num
                of rows of the second matrix
        RAISES: MatrixInvalidOperationError if the mult_matrix is not a matrix
        '''
        # first check the two Matrix are of the right dimensions
        if (self._total_columns) != (mult_matrix._total_rows):
            raise MatrixDimensionError

        # raise MatrixInvalidOperationError if the
        # object passed is not a Matrix
        if not isinstance(mult_matrix, Matrix):
            raise MatrixInvalidOperationError

        row = self._total_rows + 1
        column = mult_matrix._total_columns + 1
        default = row*(self._default * mult_matrix._default)
        new_matrix = Matrix(row, column, default)

        # loop along the rows of the first matrix
        # loop along the columns of the mult_matrix
        i = 0
        j = 0
        self_pointer = self._head.get_down()
        mult_pointer = mult_matrix._head.get_right()

        for i in range(row):
            # get each row from self and adder_matrix
            self_pointer = self._head.get_down()
            mult_pointer = mult_matrix._head.get_right()

            # if the column is non-existing in the second matrix
            # get the elements from the frist row of self
            if (self_pointer is not None) and (mult_pointer is None):
                # get the row_num
                row_num = self_pointer.get_row_num()
                self_row = self.get_row(row_num)
                # multiply all the elements in the row and sum them up
                index = 0
                mult_sum = 0
                while index < row:
                    content = self_row.get_item(index)
                    # multiply the content by the defaul of mult matrix
                    # and add it to the sum
                    mult_content = content * mult_matrix._default
                    mult_sum += mult_content
                    index += 1
                # set the sum at ith rown ith column index
                new_matrix.set_val(row_num, row_num, mult_sum)
                i += row_num

            # if there are no rows in the self matrix
            # and there are columns in mult matrix
            elif (self_pointer is None) and (mult_pointer is not None):
                # get the col_num from mult_matrix
                col_num = mult_pointer.get_column_num()
                mult_column = mult_matrix.get_col(col_num)
                # multiply all the elements in the column and sum them up
                index = 0
                mult_sum = 0
                while index < row:
                    content = mult_column.get_item(index)
                    mult_content = content * self._default
                    mult_sum += mult_content
                    index += 1
                # set the new val in the new matrix
                new_matrix.set_val(col_num, col_num, mult_sum)
                i += col_num

            # if cols and rows are found in both matrix
            elif (self_pointer is not None) and (mult_pointer is not None):
                # loop over all the rows
                # loop over all the columns
                count_1 = 0
                mult_sum = 0
                while count_1 < row:
                    self_row = self_pointer.get_row_num()
                    mult_column = mult_pointer.get_column_num()
                    # if the 2 are equal
                    if self_row == mult_column:
                        # get the values along self's row
                        self_val = self.get_val(sel_row, count_1)
                        # get the values along mult_matrix's column
                        mult_val = mult_matrix.get_val(mult_column, count_1)
                        # take the sum and add to the new matrix
                        mult_sum += (self_val * mult_val)
                        new_matrix.set_val(self_row, mult_column, mult_sum)
                    count_1 += 1
                i += 1
        return new_matrix


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''

    def __init__(self, column, default=0):
        '''(Matrix, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(0, column, None)
        self._default = default
        self._total_rows = 0
        self._total_columns = column-1

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix

        REQ: i must be an integer
        '''
        return self.get_val(0, i)

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val

        REQ: i must be an integer
        REQ: new_val must be a float
        '''
        self.set_val(0, i, new_val)


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def __init__(self, column, default=0):
        '''(Matrix, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        self._head = MatrixNode(column, column, None)
        self._default = default
        self._total_rows = column-1
        self._total_columns = column-1

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        # the square matrix is its own Transpose
        return self

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        columns = self._total_columns + 1
        default = self._default
        diagonal_matrix = OneDimensionalMatrix(columns, default)

        # loop down the diagonal, get each value from the matrix
        # set the values as entries in the diagonal matrix
        counter = 0
        while counter < columns:
            for j in range(columns):
                new_node = self._find_node(counter, j)
                if new_node is not None:
                    value = new_node.get_contents()
                    diagonal_matrix.set_item(counter, value)
            counter += 1
        return diagonal_matrix

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal

        REQ: new_diagonal must be an OneDimensionalMatrix

        RAISES: MatrixDimensionError if the number of elements in the
                new_diagonal is different from numbers of elements along
                the matris' diagonal
        RAISES: MatrixInvalidOperationError if the new_diagonal is not
                a OneDimensionalMatrix
        '''
        # in a Diagonal Matrix, the length of each side is equal to
        # the length of the diagonal
        if self._total_columns != new_diagonal._total_columns:
            raise MatrixDimensionError

        # check the type of the diagonal to be added
        # is an OneDimensionalMatrix
        if not isinstance(new_diagonal, OneDimensionalMatrix):
            raise MatrixInvalidOperationError

        # check to see the new_diagonal's default value is the same as
        # self's default value
        # if not, add the new default values along the diagonal
        if new_diagonal._default != self._default:
            index = self._total_columns + 1
            i = 0
            while i < index:
                for j in range(index):
                    if i == j:
                        self.set_val(i, i, new_diagonal._default)
                i += 1

        # loop over the diagonal matrix if there is a node
        # add its value to the Matrix
        pointer = new_diagonal._head.get_down()
        while pointer.get_right() is not None:
            new_val = pointer.get_right().get_contents()
            new_index = pointer.get_right().get_column_num()
            self.set_val(new_index, new_index, new_val)
            pointer = pointer.get_right()


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''

    def set_val(self, row, col, new_val):
        '''(SymmetricMatrix, int, int, float) -> NoneType
        set each new value at both the index (i, j) and index (j, i)

        REQ: row must be an int
        REQ: col must be an int
        REQ: new_val must be a float
        '''
        # set the new value at the m[row, col] position
        SquareMatrix.set_val(self, row, col, new_val)
        # set the new value at the m[col, row] position
        SquareMatrix.set_val(self, col, row, new_val)


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''

    def set_val(self, row, col, new_val):
        '''(DiagonalMatrix, int, int, float) -> NoneType
        set each new value along the diagonal

        REQ: row must be an int
        REQ: col must be an int
        REQ: new_val must be a float

        RAISES: MatrixInvalidOperationError if number of rows and
                the number of columns are different
        '''
        # check the row num is equal to the col num
        if row != col:
            raise MatrixInvalidOperationError

        # else set the new_val at the wanted index
        else:
            SquareMatrix.set_val(self, row, col, new_val)


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''

    def __init__(self, dimension, default=1):
        '''(MatrixNode, int, int) -> NoneType
         Simplifies the creation of an Identity Matrix,
         where every element along the diagonal is set to 1 and the
         rest of elements are 0's
        '''
        self._head = MatrixNode(dimension, dimension, None)
        self._default = default
        self._total_rows = dimension-1
        self._total_columns = dimension-1

    def get_val(self, row, col):
        '''(IdentityMatrix, int, int) -> NoneType
        the matrix returns 1 if looking for a value along the diagonal

        REQ: row must be an int
        REQ: col must be an int
        '''
        # if the given indices are not equal
        # return 0
        if row != col:
            ret_val = 0
        # else return 1
        else:
            ret_val = self._default
        return ret_val
