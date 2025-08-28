from constants import PIXEL_PER_BLOCK
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
import pygame

def create_matrix():
    matrix = []
    for i in range(SCREEN_HEIGHT//PIXEL_PER_BLOCK):
        list1 = []
        for j in range(SCREEN_WIDTH//PIXEL_PER_BLOCK):
            matrix.append(list1)
    return matrix

matrix = create_matrix()
def matrix_to_screen(matrix1,screen):
    dict_values = {}
    for i in range(SCREEN_HEIGHT):
        for j in range(SCREEN_WIDTH):
            list1 = []
            y = i
            x = j
            for v in range(PIXEL_PER_BLOCK):
                    list1.append((x,y))
                    x += 1
            dict_values[(i//10,j//10)] = list1

    return print(dict_values)

from constants import SIZE_SCREEN

loc_dict = matrix_to_screen(matrix,SIZE_SCREEN
from constants import BUTTON_LOG
from constants import BUTTON_SIGN
def buttons(dict1,mouse_loc):
  if mouse_loc ==