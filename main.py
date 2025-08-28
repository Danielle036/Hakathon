import pygame

import constants
import screen
import matrix
from matrix import loc_dict
from screen import main_screen


def main():
    pygame.init()
    main_screen.fill(constants.BACKGROUND_COLOR)
    pygame.display.flip()
    sigh_loc = loc_dict[constants.BUTTON_SIGN][0]
    log_loc = loc_dict[constants.BUTTON_LOG][0]
    place_loc = loc_dict[constants.PLACE_BUTTON2][0]
    text_loc = loc_dict[constants.TITLE1][0]
    screen.menu_screen(sigh_loc,log_loc,place_loc,text_loc)
    pygame.init()
    running=True
    while running:
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # matrix.buttoms(pos)





            pygame.display.update()
    pygame.quit()



if __name__=="__main__":
    main()