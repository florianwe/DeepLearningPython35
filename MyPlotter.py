from numpy import asarray
from matplotlib import pyplot
import numpy as np
from matplotlib.pyplot import plot, draw, show


class MyPloter(object):
    def __init__(self, framesize, max_rows, max_columns):
        self.__data_array = np.zeros((framesize * max_rows, framesize * max_columns))
        self.__framesize = framesize
        self.__max_rows = max_rows
        self.__max_columns = max_columns
        pyplot.ion()
        

    def add(self, pic, row, column):
        if row >= self.__max_rows or column >= self.__max_columns:
            return
        self.__data_array[row*self.__framesize:(row+1)*self.__framesize, column *self.__framesize:(column+1)*self.__framesize] = pic

    def show(self):
        pyplot.imshow(self.__data_array , cmap='gray', vmin=0, vmax=255)
        pyplot.show()
        pyplot.pause(0.001)