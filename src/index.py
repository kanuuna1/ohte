import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode([400, 600])
    pygame.display.set_caption("Mastermind")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()    
    pygame.quit()

if __name__ == "__main__":
    main()