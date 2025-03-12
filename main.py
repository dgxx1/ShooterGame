import pygame

print('setup start')
pygame.init()
screen = pygame.display.set_mode(size=(800, 600))
print('setup finish')

print('loop starting')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop break event1')
            pygame.quit()
            quit()
