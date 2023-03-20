import pygame
import pygame_gui
import sys
import os
import play

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Atomix')

manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
is_running = True

background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
background.fill(pygame.Color('#000000'))

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 200), (100, 50)), text='Play', manager=manager)
settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 275), (100, 50)), text='Settings', manager=manager)

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_button:
                play.run()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == settings_button:
                print('Hello World!')

    manager.update(time_delta)

    screen.blit(background, (0,0))
    manager.draw_ui(screen)


    pygame.display.update()