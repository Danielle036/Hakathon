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

    return dict_values
from constants import PLACE_BUTTON2
from constants import SIZE_SCREEN
from constants import PLACE_BUTTON1
loc_dict = matrix_to_screen(matrix,SIZE_SCREEN)
from constants import BUTTON_LOG
from constants import BUTTON_SIGN
def buttons(mouse_loc):
     if mouse_loc == PLACE_BUTTON1 or PLACE_BUTTON2:
         x=PLACE_BUTTON1
         return x
     elif mouse_loc == BUTTON_LOG:
         x = BUTTON_LOG
         return x
     elif mouse_loc == BUTTON_SIGN:
         x = BUTTON_SIGN
         return x
     else:
         return False

def buttons_in_screen(X,dict1):
    if not X==False:
            for i in dict1.keys:
                if not i == X:
                   continue
                else:
                   return dict1[i]
    else:
       return None

