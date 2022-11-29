#import pygame
from mastermind import Mastermind

class UI:
    def __init__(self):
        self.mastermind = Mastermind()


    def start(self):
        print("Tervetuloa!")
        self.mastermind.play()



    # def screen(self):
    #     pygame.init()

    #     screen = pygame.display.set_mode(
    #         [400, 600])  # pylint: disable=unused-variable
    #     pygame.display.set_caption("Mastermind")

    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False

    #     pygame.display.flip()
    #     self.draw_grid(screen)
    #     pygame.quit()

    # def draw_grid(self, screen):
    #     white = (194, 188, 187)
    #     for i in range(4):
    #         for j in range(8):
    #             rect = pygame.Rect(i * 50 + 5, (j+1) * 50, 45, 45)
    #             pygame.draw.rect(screen, white, rect, 3)

