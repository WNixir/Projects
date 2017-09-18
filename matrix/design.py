class MatrixError(Exception):
    '''
    Parent class for Matrix errors
    '''


class MatrixIndexError(MatrixError):
    '''
    Raised when trying to access an element outside of the dimension of Matrix
    '''


class MatrixDimensionError(MatrixError):
    '''
    Raised when trying to perform Matrix operations on Matrix of incompatible
    dimensions
    '''


class MatrixArithmeticError(MatrixError):
    '''
    Class for matrix arithmetic errors
    '''


class InvalidOperationError(MatrixArithmeticError):
    '''
    Raised when trying to perform invalid operations involving strings
    '''


class MatrixAdditionError(MatrixArithmeticError):
    '''
    Raised when trying to add matrices with incompatible dimensions
    '''


class MatrixSubtractionError(MatrixArithmeticError):
    '''
    Raised when trying to subtract matrices with incompatible dimensions
    '''


class MatrixMultiplicationError(MatrixArithmeticError):
    '''
    Raised when trying to multiply matrices with incompatible dimensions
    '''


class MatrixAssymmetryError(MatrixError):
    '''
    Raised when trying to create a symmetric Matrix from impossible elements
    '''


class Matrix:
    '''
    The Matrix class is an implementation of a Linear Algebra Matrix, where
    basic Matrix arithmatic operations are defined. For Matrix containing str
    elements, the basic python str operations (string addition, integer
    multiplication) are defined.
    '''

    def __init__(self, m=1, n=1, elements=0):
        '''(Matrix, int, int) -> NoneType
        Creates a new row(m) x column(n) Matrix with all elements set to 0
        if no dimensions are given, defaults to a 1 x 1 zero Matrix
        '''

    def __str__(self):
        '''(Matrix) -> str
        Return a string representation for all the elements in the Matrix
        '''

    def num_rows(self):
        '''(Matrix) -> int
        Return the total number of rows

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.num_rows()
        3
        '''

    def num_columns(self):
        '''(Matrix) -> int
        Return the total number of columns

        >>> matrix = Matrix(2, 4, [[1, 2, 3, 4], [4, 5, 6, 7]])
        >>> matrix.num_columns()
        4
        '''

    def find_element(self, element):
        '''(Matrix) -> tuple
        Return the index location(s) of target element from the Matrix in
        a tuple, where the first num denotes the row and the second num
        denotes the column the element can be found at.

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.find_element(8)
        (3, 2)
        >>> matrix = Matrix([[1, 2, 3], [2, 4, 5]])
        >>> matrix.find_element(2)
        [(1, 2), (2, 1)]
        '''

    def get_element(self, i, j):
        '''(Matrix, int, int) -> Object
        Return the element from the ith row, jth column

        RAISES: MatrixIndexError if i or j is outside of the dimension

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.get_element(2, 3)
        6
        >>> matrix.get_element(3, 1)
        7
        '''

    def get_row(self, i):
        '''(Matrix, int) -> list
        Return all the elements from the ith row of a Matrix

        RAISES: MatrixDimensionError if i is an invalid row number

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.get_row(1)
        [1, 2, 3]
        >>> matrix.get_row(3)
        [7, 8, 9]
        '''

    def get_column(self, j):
        '''(Matrix, int) -> list
        Return the elements from the jth column of a Matrix

        RAISES: MatrixDimensionError if j is an invalid column number

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.get_column(2)
        [2, 5, 8]
        '''

    def set_element(self, i, j, element):
        '''(Matrix, int, int, object) -> NoneType
        Set the element at ith row, jth column to new object

        REQ: element must be an int or str

        RAISES: MatrixIndexError if i or j is outside of the dimension

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.set_element(3, 1, 5000)
        >>> matrix.elements()
        [[1, 2, 3], [4, 5, 6], [5000, 8, 9]]
        '''

    def set_row(self, i, new_elements):
        '''(Matrix, int, list) -> NoneType
        Set the list of new elements as the ith row

        REQ: list must only contain int or str

        RAISES: MatrixDimensionError if i is an invalid row number
        RAISES: MatrixDimensionError when trying to add more elements than
                the dimension of Matrix

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.set_row(2, [10, 11, 12])
        >>> matrix.elements()
        [[1, 2, 3], [10, 11, 12], [7, 8, 9]]
        '''

    def set_column(self, j, new_elements):
        '''(Matrix, int, list) -> NoneType
        Set the list of new elements as the jth column

        REQ: list must only contain int or str

        RAISES: MatrixDimensionError if j is an invalid column number
        RAISES: MatrixDimensionError if the new column is longer than
                the dimension of matrix

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.set_column(1, [13, 14, 15])
        >>> matrix.elements()
        [[13, 2, 3], [14, 5, 6], [15, 8, 9]]
        '''

    def swap_rows(self, i_ori, i_dest):
        '''(Matrix, int, int) -> NoneType
        Swap the position of the original row with the position
        of the destination row

        RAISES: MatrixDimensionError if i is invalid

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.swap_rows(1, 2)
        >>> matrix.elements()
        [[4, 5, 6], [1, 2, 3], [7, 8, 9]]
        '''

    def swap_columns(self, j_ori, j_dest):
        '''(Matrix, int, int) -> NoneType
        Swap the position of the original column with the position
        of the destination column

        RAISES: MatrixDimensionError if j is invalid

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.swap_columns(3, 2)
        >>> matrix.elements()
        [[1, 3, 2], [4, 6, 5], [7, 9, 8]]
        '''

    def transpose(self):
        '''(Matrix) -> Matrix
        Return the transpose of the Matrix

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.transpose()
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        '''

    def matrix_addition(self, matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new Matrix after performing Matrix Addition on 2 compatible
        matrices

        RAISES: MatrixAdditionError when trying to add 2 matrices of
                incompatible dimensions
        RAISES: InvalidOperationError if trying to add an int element
                to a str elements

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix_1 = Matrix(3, 3, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])
        >>> matrix.matrix_addition(matrix_1)
        [[11, 13, 15], [17, 19, 21], [23, 25, 27]]
        '''

    def matrix_subtraction(self, matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new Matrix after performing Matrix Subtraction on 2
        compatible matrices

        RAISES: MatrixSubtractionError when trying to subtract 2 matrices of
                incompatible dimensions
        RAISES: InvalidOperationError if trying to subtract an int element
                from a str element

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix_1 = Matrix(3, 3, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])
        >>> matrix.matrix_subtraction(matrix_1)
        [[-9, -9, -9], [-9, -9, -9], [-9, -9, -9]]
        '''

    def matrix_multiplication(self, matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new Matrix after performing matric multiplication on 2
        compatible matrices

        RAISES: MatrixMultiplicationError if the 2 matrices have incompatible
                dimensions
        RAISES: InvalidOperationError when 2 str are attemped to be multiplied
                together

        >>> matrix1 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        >>> matrix2 = Matrix(2, 2, [[7, 8], [9, 0]])
        >>> matrix1.matrix_multiplication(matrix2)
        [[25, 8], [57, 24], [89, 40]]
        '''

    def scalar_multiplication(self, num):
        '''(Matrix, int) -> Matrix
        Return a new Matrix after multiplying each element by the scalar

        RAISES: InvalidOperationError when trying to multiply a str element
                with a non-integer element

        >>> matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.scalar_multiplication(2)
        [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        >>> matrix = Matrix([['aa', 'hello', 2]])
        >>> matrix.scallar_multiplication(2)
        [['aaaa', 'hellohello', 4]]
        '''


class SquareMatrix(Matrix):
    '''
    A class for a NxN square Matrix, Square Matrix is a child class of Matrix
    '''

    def __init__(self, n=1, elements=0):
        '''
        Creates a new NxN Square Matrix
        '''

    def determinant(self):
        '''(Matrix) -> float
        Return the determinant of a 2x2 Matrix

        RAISES: MatrixDimensionError when trying to compute the determinant
                of a non 2x2 Matrix

        >>> matrix = SquareMatrix(2, [[1, 2], [3, 4]])
        >>> matrix.determinant()
        -2
        '''

    def get_diagonal(self):
        '''(Matrix) -> list
        Return all elements along the diagonal of a square Matrix

        >>> matrix = SquareMatrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.get_diagonal()
        [1, 5, 9]
        '''

    def set_diagonal(self, new_elements):
        '''(Matrix, list) -> NoneType
        Set the list of new elements as the diagonal of a square Matrix

        REQ: list must contain only int or str

        RAISES: MatrixDimensionError if the length of new_elements is longer
                than the length of diagonal

        >>> matrix = SquareMatrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> matrix.set_diagonal([20, 30, 40])
        >>> matrix.elements()
        [[20, 2, 3], [4, 30, 6], [7, 8, 40]]
        '''


class SymmetricMatrix(SquareMatrix):
    '''
    A class for creating a Symmetric Matrix, where the Matrix is equal to
    its own transpose. The Symmetric Matrix is a child class of Square Matrix
    '''

    def __init__(self, n=1, elements=0):
        '''
        Create a symmetric Matrix, where all the input elements are checked
        to ensure the Matrix maintains symmetry

        RAISES: MatrixAsymmetryError when the input elements cannot be made
                into a symmetric Matrix
        '''

    def set_element(self, i, j, element):
        '''(Matrix, int, int, object) -> NoneType
        Set the new element at the ith row, jth column position
        Set the same element at the jth row, ith column position

        REQ: element must be an int or str

        RAISES: MatrixIndexError if i or j are out of bounds
        '''

    def set_row(self, i, new_elements):
        '''(Matrix, int, list) -> NoneType
        Set the new elements as the ith row
        Set the same elements along the ith column

        REQ: elements must contain int or str

        RAISES: MatrixDimensionError if i is invalid
        '''

    def set_column(self, j, new_elements):
        '''(Matrix, int, list) -> NoneType
        Set the new elements as the jth column
        Set the same elements along the jth row

        REQ: elements must contain int or str

        RAISES: MatrixDimensionError if j is invalid
        '''


class IdentityMatrix(SymmetricMatrix):
    '''
    A class for creating an Identity Matrix, where every element along
    the diagonal is set to 1 and the rest of elements are 0's
    '''


class OneDimensionalMatrix(Matrix):
    '''
    A class for a 1xN Matrix
    '''

    def get_element(self, j):
        '''(Matrix, int) -> Object
        Return the Object at the jth column position from 1xN Matrix

        RAISES: MatrixIndexError when trying to get element outside the bounds

        >>> matrix = OneDimensionalMatrix([1, 2, 3, 4])
        >>> matrix.get_element(3)
        3
        '''

    def set_element(self, j, element):
        '''(Matrix, int, object) -> NoneType
        Set the object at the jth column position in 1xN Matrix

        RAISES: MatrixIndexError when trying to set the element out of bounds

        REQ: element must be an int or a str

        >>> matrix = OneDimensionalMatrix([1, 2, 3, 4])
        >>> matrix.set_element(2, 3000)
        >>> matrix.elements()
        [1, 3000, 3, 4]
        '''
