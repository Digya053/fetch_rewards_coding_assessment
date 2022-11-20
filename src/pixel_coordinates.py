import numpy as np
from argparse import ArgumentParser

import ast # this library converts list of strings to list of numeric values

class PixelCoordinates:

    def __init__(self, corner_points, n_rows, n_cols, n_decimal=2):
        self.corner_points = corner_points
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_decimal = n_decimal
        self.res = [[0 for i in range(self.n_cols)]for j in range(self.n_rows)]

        if self.n_rows == 0 and self.n_cols == 0:
            return self.res
        if len(self.corner_points) == 0:
            return

        self.diffrow = (self.corner_points[1][0] - self.corner_points[0][0])/(self.n_cols - 1)
        self.diffcol = (self.corner_points[2][1] - self.corner_points[0][1])/(self.n_rows - 1) 

    def set_corner_values(self):
        self.res[self.n_rows-1][0] = self.corner_points[0]
        self.res[self.n_rows-1][self.n_cols-1] = self.corner_points[1]
        self.res[0][0] = self.corner_points[2]
        self.res[0][self.n_cols-1] = self.corner_points[3]
          
    def calc_horizontal_boundary_coords(self):
        for i in range(self.n_cols-1):
            self.res[0][i+1] = [self.res[0][i][0] + self.diffrow, self.res[0][i][1]]	
            self.res[self.n_rows-1][i+1] = [self.res[self.n_rows-1][i][0] + self.diffrow, self.res[self.n_rows-1][i][1]]
        
    def calc_vertical_boundary_coords(self):
        for i in range(self.n_rows-1):
            self.res[i+1][0] = [self.res[i][0][0], self.res[i][0][1] - self.diffcol]
            self.res[i+1][self.n_cols-1] = [self.res[i][self.n_cols-1][0], self.res[i][self.n_cols-1][1] - self.diffcol]
    
    def calc_inside_coords(self):
        for row in range(1, self.n_rows):
            for col in range(1, self.n_cols):
                self.res[row][col] = [self.res[row][col-1][0] + self.diffrow, self.res[row][col-1][1]] 

    def get_result(self):
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

    pc = PixelCoordinates(ast.literal_eval(args.corner_pts), args.n_rows, args.n_cols, args.n_decimal)
    return pc.get_result()


if __name__=="__main__":
    print(main())







