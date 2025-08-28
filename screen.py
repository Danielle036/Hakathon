import constants
import pygame

main_screen=pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("ExtraBite")


def menu_screen():
    main_screen.fill(constants.BACK_GROUND_COLOR)
