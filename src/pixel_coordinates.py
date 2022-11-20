import numpy as np
from argparse import ArgumentParser

class PixelCoordinates:
    """
    This class uses a dynamic programmic approach to calculate the pixel coordinate values of an image. Firstly,
    the distance between row and column endpoints are calculated (self.diffrow and self.diffcol).
    Then, the pixel coordinate values at the border (both horizontal and vertical) is calculated as in function
    calc_horizontal_boundary_coords() and calc_vertical_boundary_coords(). Thereafter, the coordinate values of equally 
    spaced non-boundary pixels are calculated.
    """

    def __init__(self, corner_points, n_rows, n_cols, n_decimal=2):
        """Assign the input values

        Parameters
        ----------
        corner_points: list
            The corner points of a 2D array
        n_rows: int
            The number of rows of a 2D array
        n_cols: int
            The number of columns of a 2D array
        n_decimal: int
            Additional input to round the array numbers with decimal to required places.
        """
        self.corner_points = corner_points
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_decimal = n_decimal
        self.incorrect_input = False
        self.error_msg = ""
        self.res = [[0 for i in range(self.n_cols)]for j in range(self.n_rows)]

        # If there is only one row, the space between extreme coordinates of column will be zero
        self.diffrow = (self.corner_points[1][0] - self.corner_points[0][0])/(self.n_cols - 1) if self.n_cols > 1 else 0
        # If there is only one column, the space between extreme coordinates of row will be zero
        self.diffcol = (self.corner_points[2][1] - self.corner_points[0][1])/(self.n_rows - 1) if self.n_rows > 1 else 0

    def handle_edge_cases_and_error(self):
        # Return empty values if corner points or dimension values are not present
        if self.n_rows == 0 and self.n_cols == 0:
            self.incorrect_input = True
            self.msg = self.res
            return
        if len(self.corner_points) == 0:
            self.incorrect_input = True
            self.msg = []
            return
        if not self.n_rows or not self.n_cols:
            self.incorrect_input = True
            self.error_msg = "The dimension cannot have only number of rows or only number of columns"
            return 
        if self.corner_points[0] == self.corner_points[1] == self.corner_points[2] == self.corner_points[3]:
            self.incorrect_input = True
            self.error_msg = "The corner point should have different values"
            return
        if (self.corner_points[0][1] != self.corner_points[1][1] or self.corner_points[0][0] != self.corner_points[2][0]
        or self.corner_points[2][1] != self.corner_points[3][1] or self.corner_points[1][0] != self.corner_points[3][0]):
            self.incorrect_input = True
            self.error_msg = "The rectangle should be parallel to x and y axes to obtain correct result"
            return 
        if (self.corner_points[3][1] < self.corner_points[2][1] or self.corner_points[1][1] < self.corner_points[0][1] 
        or self.corner_points[0][0] > self.corner_points[2][0] or self.corner_points[1][0] > self.corner_points[3][0]):
            self.incorrect_input = True
            self.error_msg = "Please pass proper corner point values to obtain correct result"
            return

    def set_corner_values(self):
        """Set the corner values""" 
        self.res[self.n_rows-1][0] = self.corner_points[0]
        self.res[self.n_rows-1][self.n_cols-1] = self.corner_points[1]
        self.res[0][0] = self.corner_points[2]
        self.res[0][self.n_cols-1] = self.corner_points[3]
          
    def calc_horizontal_boundary_coords(self):
        """Set the coordinate values of boundary rows"""
        for i in range(self.n_cols-1):
            self.res[0][i+1] = [self.res[0][i][0] + self.diffrow, self.res[0][i][1]]	
            self.res[self.n_rows-1][i+1] = [self.res[self.n_rows-1][i][0] + self.diffrow, self.res[self.n_rows-1][i][1]]
        
    def calc_vertical_boundary_coords(self):
        """Set the coordinate values of boundary columns"""
        for i in range(self.n_rows-1):
            self.res[i+1][0] = [self.res[i][0][0], self.res[i][0][1] - self.diffcol]
            self.res[i+1][self.n_cols-1] = [self.res[i][self.n_cols-1][0], self.res[i][self.n_cols-1][1] - self.diffcol]
    
    def calc_inside_coords(self):
        """Set the coordinate values of inside pixels using the boundary values"""
        for row in range(1, self.n_rows):
            for col in range(1, self.n_cols):
                self.res[row][col] = [self.res[row][col-1][0] + self.diffrow, self.res[row][col-1][1]] 

    def get_result(self):
        self.handle_edge_cases_and_error()
        if self.incorrect_input:
            return self.error_msg
        self.set_corner_values()
        self.calc_horizontal_boundary_coords()
        self.calc_vertical_boundary_coords()
        self.calc_inside_coords()

        return str(np.round(self.res, decimals = int(self.n_decimal)).tolist())

def main():
    parser = ArgumentParser()
    parser.add_argument("--corner_pts", type=str)
    parser.add_argument("--n_rows", type=int)
    parser.add_argument("--n_cols", type=int)
    parser.add_argument("--n_decimal", default=2, type=int)
    args = parser.parse_args()

    pc = PixelCoordinates(eval(args.corner_pts), args.n_rows, args.n_cols, args.n_decimal)
    return pc.get_result()

if __name__=="__main__":
    print(main())
