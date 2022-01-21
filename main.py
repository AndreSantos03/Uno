import pygame
import sys
import global_variables
from game_loop import main_game_loop
from initial_menu import beggining_menu

pygame.init()

#music

pygame.mixer.music.load(global_variables.BACKGROUND_MUSIC)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(global_variables.MUSIC_VOLUME)

start_game = beggining_menu() 

while start_game:
    start_game = main_game_loop()
        
pygame.quit()
sys.exit(0)