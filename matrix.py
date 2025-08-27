from constants import PIXEL_PER_BLOCK
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
def create_matrix():
    matrix = []
    for i in range(SCREEN_HEIGHT)//PIXEL_PER_BLOCK:
        list1 = []
        for j in range(SCREEN_WIDTH)//PIXEL_PER_BLOCK:
            matrix.append(list1)
    return matrix

matrix = create_matrix()
def screen_to_matrix(matrix1):
    dict_values = {}
    for i in range(len(matrix1)):
        for j in range(matrix1[i]):




