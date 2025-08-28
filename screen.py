import constants
import pygame

main_screen=pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("ExtraBite")
pygame.font.init()
font = pygame.font.SysFont('sansserifcollection' , 50)
title = font.render("ExtraBite", True, constants.TITLE_COLOR)


def menu_screen(sigh_loc,log_loc,place_loc,text_loc):
    main_screen.fill(constants.BACKGROUND_COLOR)
    pygame.draw.rect(main_screen,constants.BUTTON_COLOR,(sigh_loc,(constants.BUTTON_WIDTH,constants.BUTTON_HEIGHT)))
    pygame.draw.rect(main_screen, constants.BUTTON_COLOR, (log_loc,(constants.BUTTON_WIDTH,constants.BUTTON_HEIGHT)))
    pygame.draw.rect(main_screen, constants.BUTTON_COLOR, (place_loc,(constants.BUTTON_WIDTH1,constants.BUTTON_HEIGHT1)))
    main_screen.blit(title, text_loc)
    pygame.display.update()





