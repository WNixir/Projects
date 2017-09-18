import unittest


class TestMatrix(unittest.TestCase):
    '''
    A class for testing all the basic operations on a linear algebra matrix
    '''

    def test_num_rows_one_row(self):
        '''
        testing the case where the matrix only has 1 row
        '''
        test_matrix = Matrix(1, 3)
        test_matrix.set_row([1, 2, 3])
        self.assertTrue(test_matrix.num_rows(1))

    def test_num_rows_zero_row(self):
        '''
        testing the case where the matrix is empty
        '''
        test_matrix = Matrix(3, 4)
        self.assertTrue(test_matrix.num_rows(0))

    def test_num_rows_five_rows(self):
        '''
        matrix with multiple rows
        '''
        test_matrix = Matrix(5, 2)
        self.assertTrue(test_matrix.num_rows(5))

    def test_num_columns_one_column(self):
        '''
        testing the case where the matrix has one column
        '''
        test_matrix = Matrix(3, 1)
        self.assertTrue(test_matrix.num_columns(1))

    def test_num_columns_zero_column(self):
        '''
        testing the case where the matrix is empty
        '''
        test_matrix = Matrix()
        self.assertTrue(num_columns(0, []))

    def test_find_element_simple(self):
        '''
        testing the case where the element exists in one location
        '''
        test_matrix = Matrix([1, 2, 3])
        self.assertTrue(test_matrix.find_element((1, 3), 3))

    def test_find_element_multiple(self):
        '''
        testing the case where the same element exists in many locations
        '''
        test_matrix = Matrix([[1, 2, 3], [2, 4, 5]])
        self.assertTrue(test_matrix.find_element(((1, 2), (2, 1)), 2))

    def test_find_element_dne(self):
        '''
        testing the case where the element does not exist
        '''
        test_matrix = Matrix([1, 2, 3])
        test_matrix.find_element(50, 2)
        self.assertRaises(MatrixIndexError)

    def test_get_element_simple_case(self):
        '''
        testing the case where the element exists
        '''
        test_matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        ret_element = test_matrix.get_element(2, 2)
        self.assertEqual(ret_element, 5)

    def test_get_element_dne(self):
        '''
        testing the case where the given index is out of bounds
        '''
        test_matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        ret_element = test_matrix.get_element(6, 7)
        self.assertRaises(MatrixIndexEror)

    def test_get_row_simple_case(self):
        '''
        testing the case where the row exists
        '''
        test_matrix = Matrix([[1, 2, 3], [2, 4, 5]])
        ret_row = test_matrix.get_row(2)
        self.assertEqual(ret_row, [2, 4, 5])

    def test_get_row_dne(self):
        '''
        testing the case where the given row num is out of bounds
        '''
        test_matrix = Matrix([[1, 2, 3], [2, 4, 5]])
        ret_row = test_matrix.get_row(12)
        self.assertRaises(MatrixDimensionError)

    def test_get_column_simple_case(self):
        '''
        testing the case where the wanted column exists
        '''
        test_matrix = Matrix([[1, 2, 3], [2, 4, 5]])
        ret_column = test_matrix.get_column(3)
        self.assertEqual(ret_column, [3, 5])

    def test_get_column_dne(self):
        '''
        testing the case where the given column number is out of bounds
        '''
        test_matrix = Matrix([[1, 2, 3], [2, 4, 5]])
        ret_column = test_matrix.get_column(5)
        self.assertRaises(MatrixDimensionError)

    def test_set_element_empty_matrix(self):
        '''
        testing the case when the matrix is empty
        '''
        test_matrix = Matrix(None)
        test_matrix.set_element(1, 1, 2)
        expected_matrix = [2]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_element_one_element_matrix(self):
        '''
        testing the case when there is 1 element in the matrix
        '''
        test_matrix = Matrix([5])
        test_matrix.set_element(1, 1, 1)
        expected_matrix = [1]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_element_3_x_3_matrix(self):
        '''
        testing the case for a 3x3 matrix
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.set_element(2, 3, 12)
        expected_matrix = [[1, 2, 3], [4, 5, 12], [7, 8, 9]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_element_wrong_index(self):
        '''
        testing the case when trying to insert the element at invalid index
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.set_element(21, 13, 12)
        self.assertRaises(MatrixIndexError)

    def test_set_row_one_row(self):
        '''
        testing the case for a matrix with one row
        '''
        test_matrix = Matrix([1, 3, 5])
        test_matrix.set_row(1, [2, 4, 6])
        expected_matrix = [2, 4, 6]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_row_3_x_3_matrix(self):
        '''
        testing for a 3x3 matrix
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.set_row(2, [22, 44, 66])
        expected_matrix = [[1, 2, 3], [22, 44, 66], [7, 8, 9]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_row_invalid_row(self):
        '''
        testing the case when trying to set the elements at invalid row
        '''
        test_matrix = Matrix([1, 3, 5])
        test_matrix.set_row(55, [2, 4, 6])
        self.assertRaises(MatrixDimensionError)

    def test_set_row_too_many_elements(self):
        '''
        testing the case when tryint to insert a longer row of elements
        '''
        test_matrix = Matrix([1, 3, 5])
        test_matrix.set_row(1, [2, 4, 6, 8, 10, 11])
        self.assertRaises(MatrixDimensionError)

    def test_set_column_one_column(self):
        '''
        testing the case for a matrix with one column
        '''
        test_matrix = Matrix([1])
        test_matrix.set_column(1, [4])
        expected_matrix = [4]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_column_3_x_3_matrix(self):
        '''
        testing for a 3x3 matrix
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.set_column(2, [22, 44, 66])
        expected_matrix = [[1, 22, 3], [4, 44, 6], [7, 66, 9]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_column_invalid_column(self):
        '''
        testing the case when trying to set the elements at invalid column
        '''
        test_matrix = Matrix([1, 3, 5])
        test_matrix.set_column(55, [2])
        self.assertRaises(MatrixDimensionError)

    def test_set_column_too_many_elements(self):
        '''
        testing the case when tryint to insert too many elements
        '''
        test_matrix = Matrix([1, 3, 5])
        test_matrix.set_column(1, [2, 4, 6, 8, 10, 11])
        self.assertRaises(MatrixDimensionError)

    def test_swap_rows_one_row(self):
        '''
        tesing the case when there is only one row, no swaping is needed
        '''
        test_matrix = Matrix([1, 3, 5])
        test_matrix.swap_rows(1, 1)
        expected_matrix([1, 3, 5])
        self.assertEqual(test_matrix, expected_matrix)

    def test_swap_rows_3_x_3_matrix(self):
        '''
        testing for 3x3 matrix
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.swap_rows(1, 3)
        expected_matrix = [[4, 5, 6], [1, 2, 3], [7, 8, 9]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_swap_rows_invalid_num(self):
        '''
        testing the case when trying to swap a rows with invalid row num
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.swap_rows(11, 3)
        self.assertRaises(MatrixDimensionError)

    def test_swap_columns_one_column(self):
        '''
        tesing the case when there is only one column, no swaping is needed
        '''
        test_matrix = Matrix([[1], [2], [3]])
        test_matrix.swap_columns(1, 1)
        expected_matrix([[1], [2], [3]])
        self.assertEqual(test_matrix, expected_matrix)

    def test_swap_columns_3_x_3_matrix(self):
        '''
        testing for 3x3 matrix
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.swap_columns(1, 3)
        expected_matrix = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_swap_column_invalid_num(self):
        '''
        testing the case when trying to swap a rows with invalid col num
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.swap_columns(11, 3)
        self.assertRaises(MatrixDimensionError)

    def test_transpose_null_matrix(self):
        '''
        testing for the case where there is nothing in matrix
        '''
        test_matrix = Matrix(None)
        test_matrix.transpose()
        expected_matrix = [None]
        self.assertEqual(test_matrix, expected_matrix)

    def test_transpose_one_element(self):
        '''
        testing the case where the matrix has 1 element
        '''
        test_matrix = Matrix([3])
        test_matrix.transpose()
        expected_matrix = [3]
        self.assertEqual(test_matrix, expected_matrix)

    def test_transpose_one_row(self):
        '''
        testing the case where the matrix has 1 row
        '''
        test_matrix = Matrix([1, 2, 3])
        test_matrix.transpose()
        expected_matrix = [[1], [2], [3]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_transpose_3_x_3_matrix(self):
        '''
        testing for 3x3 matrix
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_matrix.transpose()
        expected_matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_matrix_addition_integers(self):
        '''
        testing the case where two matrices contain only int elements
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_1 = Matrix(3, 3, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])
        test_matrix.matrix_addition(matrix_1)
        expected_matrix = [[11, 13, 15], [17, 19, 21], [23, 25, 27]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_matrix_addition_strings(self):
        '''
        testing the case where 2 tring matrice are added together
        '''
        test_matrix = Matrix(['a', 'b', 'c'])
        matrix_1 = Matrix(['hello', 'hhh', '123'])
        test_matrix.matrix_addition(matrix_1)
        expected_matrix = ['ahello', 'bhhh', 'c123']
        self.assertEqual(test_matrix, expected_matrix)

    def test_matrix_addition_int_str(self):
        '''
        testing the case when trying to add an int with a str
        '''
        test_matrix = Matrix(['a', 'b', 'c'])
        matrix_1 = Matrix(['hello', 'hhh', 123])
        test_matrix.matrix_addition(matrix_1)
        self.assertRaises(InvalidOperationError)

    def test_matrix_addition_incompatible_matrices(self):
        '''
        testing the case when trying to add 2 matrices of different dimensions
        '''
        test_matrix = Matrix(['a', 'b', 'c'])
        matrix_1 = Matrix(['hello', 'hhh', 'a', 'e', '78'])
        test_matrix.matrix_addition(matrix_1)
        self.assertRaises(MatrixAdditionError)

    def test_matrix_subtraction_integers(self):
        '''
        testing the case where two matrices contain only int elements
        '''
        test_matrix = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_1 = Matrix(3, 3, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])
        test_matrix.matrix_subtraction(matrix_1)
        expected_matrix = [[-9, -9, -9], [-9, -9, -9], [-9, -9, -9]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_matrix_subtraction_strings(self):
        '''
        testing the case when trying to subtract str from each other
        '''
        test_matrix = Matrix(['a', 'b', 'c'])
        matrix_1 = Matrix(['hello', 'hhh', '123'])
        test_matrix.matrix_subtraction(matrix_1)
        self.assertRaises(InvalidOperationError)

    def test_matrix_subtraction_int_str(self):
        '''
        testing the case when trying to add an int with a str
        '''
        test_matrix = Matrix(['a', 'b', 'c'])
        matrix_1 = Matrix(['hello', 'hhh', 123])
        test_matrix.matrix_subtraction(matrix_1)
        self.assertRaises(InvalidOperationError)

    def test_matrix_subtraction_incompatible_matrices(self):
        '''
        testing the case when trying to add 2 matrices of different dimensions
        '''
        test_matrix = Matrix([1, 2, 3])
        matrix_1 = Matrix([1, 2, 3, 4, 5, 6, 8])
        test_matrix.matrix_subtraction(matrix_1)
        self.assertRaises(MatrixAdditionError)

    def test_matrix_multiplication_null_matrix(self):
        '''
        testing the case when multiply a matrix with the 0 matrix
        '''
        test_matrix = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        matrix_1 = Matrix[[0], [0]]
        test_matrix.matrix_multiplication(matrix_1)
        expected_matrix = [[0], [0], [0]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_matrix_multiplication_integer(self):
        '''
        testing the case when both matrices contain intergers
        '''
        test_matrix = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        matrix_1 = Matrix(2, 2, [[7, 8], [9, 0]])
        test_matrix.matrix_multiplication(matrix_1)
        expected_matrix = [[25, 8], [57, 24], [89, 40]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_matrix_multiplication_str(self):
        '''
        testing the case when str elements are in the matrix
        '''
        test_matrix = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        matrix_1 = Matrix(2, 2, [[7, 8], ['howareyou', 'hello']])
        test_matrix.matrix_multiplication(matrix_1)
        self.assertRaises(InvalidOperationError)

    def test_matrix_multiplication_incompatible(self):
        '''
        testing the case when trying to multiply 2 matrices with incompatible
        dimensions together
        '''
        test_matrix = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        matrix_1 = Matrix(3, 2, [[7, 8], [9, 0], [1, 3]])
        test_matrix.matrix_multiplication(matrix_1)
        self.assertRaises(MatrixMultiplicationError)

    def test_scalar_multiplication_zero(self):
        '''
        testing for when multiply all elements by 0
        '''
        test_matrix = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        test_matrix.scalar_multiplication(0)
        expected_matrix = [[0, 0], [0, 0], [0, 0]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_scalar_multiplication_interger(self):
        '''
        testing the case when the matrix has all intergers
        '''
        test_matrix = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        test_matrix.scalar_multiplication(2)
        expected_matrix = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_scalar_multiplication_int_str(self):
        '''
        testing the case when there are str elements in the matrix
        '''
        test_matrix = Matrix([['aa', 'hello', 2]])
        test_matrix.scalar_multiplication(2)
        expected_matrix = [['aaaa', 'hellohello', 4]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_scalar_multiplication_float_str(self):
        '''
        testing the case when a non-int type is attempted to multiply with str
        '''
        test_matrix = Matrix([['aa', 'hello', 2]])
        test_matrix.scalar_multiplication(3.14)
        self.assertRaises(InvalidOperationError)


class TestSquareMatrix(TestMatrix):

    def test_determinant_2_x_2(self):
        '''
        testing the case for computing the determinant of a 2x2 matrix
        '''
        test_matrix = SquareMatrix(2, [[1, 2], [3, 4]])
        det = test_matrix.detrminant()
        self.assertEqual(det, -2)

    def test_determinant_3_x_3(self):
        '''
        testing the case when computing the det for a 3x3 matrix
        '''
        test_matrix = SquareMatrix(3, [[1, 2, 1], [3, 4, 3], [5, 6, 9]])
        det = test_matrix.detrminant()
        self.assertRaises(MatrixDimensionError)

    def test_get_diagonal(self):
        test_matrix = SquareMatrix(3, [[1, 2, 1], [3, 4, 3], [5, 6, 9]])
        diagonal = test_matrix.get_diagonal()
        self.assertEqual(diagonal, [1, 4, 9])

    def test_set_diagonal(self):
        test_matrix = SquareMatrix(3, [[1, 2, 1], [3, 4, 3], [5, 6, 9]])
        diagonal = test_matrix.set_diagonal([11, 12, 13])
        expected_matrix = [[11, 2, 1], [3, 12, 3], [5, 6, 13]]
        self.assertEqual(test_matrix, expected_matrix)


class TestIdentityMatrix(TestSquareMatrix):

    def test_create_3_x_3_id_matrix(self):
        '''
        testing the creation of a 3x3 identity matrix
        '''
        test_matrix = IdentityMatrix(3)
        expected_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(test_matrix, expected_matrix)


class TestSymmetricMatrix(TestSquareMatrix):

    def test_set_element_i_row_j_column(self):
        '''
        testing the case where only the element on ith row, jth column
        is updated
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_element(3, 1, 99)
        expected_matrix = [[1, 7, 99], [7, 4, -5], [99, -5, 6]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_element_diagonal(self):
        '''
        testing the case when the element changed is on the diagonal
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_element(2, 2, 99)
        expected_matrix = [[1, 7, 3], [7, 99, -5], [3, -5, 6]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_element_dne(self):
        '''
        testing the case when trying to set an element out of bound
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_element(10, 2, 99)
        self.assertRaises(MatrixIndexError)

    def test_set_row_i_row(self):
        '''
        testing the case when trying to set the ith row with new elements
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_row(2, [99, 98, 97])
        expected_matrix = [[1, 99, 3], [99, 98, 97], [3, 97, 6]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_row_dne(self):
        '''
        testing the case when trying to set a row outside of bound
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_row(999, [99, 98, 97])
        self.assertRaises(MatrixDimentionError)

    def test_set_column_j_column(self):
        '''
        testing the case when trying to set the jth col with new elements
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_column(2, [99, 98, 97])
        expected_matrix = [[1, 99, 3], [99, 98, 97], [3, 97, 6]]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_column_dne(self):
        '''
        testing the case when trying to set a column outside of bound
        '''
        test_matrix = SymmetricMatrix(3, [[1, 7, 3], [7, 4, -5], [3, -5, 6]])
        test_matrix.set_column(999, [99, 98, 97])
        self.assertRaises(MatrixDimentionError)


class TestOneDimensionalMatrix(TestMatrix):

    def test_get_element_simple(self):
        '''
        testing the case when the element is in the matrix
        '''
        test_matrix = OneDimensionalMatrix([1, 2, 3, 4])
        ret_element = test_matrix.get_element(3)
        self.assertEqual(ret_element, 3)

    def test_get_element_dne(self):
        '''
        testing the case when attempting to get element from invalid index
        '''
        test_matrix = OneDimensionalMatrix([1, 2, 3, 4])
        ret_element = test_matrix.get_element(99)
        self.assertRaises(MatrixIndexError)

    def test_set_element_simple(self):
        '''
        testing the case when trying to set a element at valid position
        '''
        test_matrix = OneDimensionalMatrix([1, 2, 3, 4])
        test_matrix.set_element(2, 3000)
        expected_matrix = [1, 3000, 3, 4]
        self.assertEqual(test_matrix, expected_matrix)

    def test_set_element_dne(self):
        '''
        testing the case when trying to set the element at invalid position
        '''
        test_matrix = OneDimensionalMatrix([1, 2, 3, 4])
        test_matrix.set_element(99, 3000)
        self.assertRaises(MatrixIndexError)


if __name__ == '__main__':
    unittest.main(exit=False)
