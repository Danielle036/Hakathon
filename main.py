import pygame
import screen


def main():
    pygame.init()
    running=True
    while running:
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:





            pygame.display.update()
    pygame.quit()



if __name__=="__main__":
    main()