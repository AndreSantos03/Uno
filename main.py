from glob import glob
import pygame
import sys
import global_variables
import game_loop
import initial_menu

pygame.init()

#music

pygame.mixer.music.load(global_variables.BACKGROUND_MUSIC)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(global_variables.MUSIC_VOLUME)

if initial_menu.beggining_menu():
    game_loop.main_game_loop()
        
pygame.quit()
sys.exit(0)