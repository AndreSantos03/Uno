import os
import pygame
import json

pygame.init()

GAME_FOLDER = os.path.dirname(__file__)
TEXTURE_FOLDER = os.path.join(GAME_FOLDER,'Textures')
SOUND_FOLDER = os.path.join(GAME_FOLDER,'Sounds')
UI_FOLDER = os.path.join(TEXTURE_FOLDER,'UI')
CARDS_FOLDER = os.path.join(TEXTURE_FOLDER,'Cards')
SETTINGS = os.path.join(GAME_FOLDER,'settings.json')

BACKGROUND_MUSIC = os.path.join(SOUND_FOLDER,'BackMusic.mp3')

BACKGROUND_IMAGE = os.path.join(UI_FOLDER,'BackGround Uno Online.png')
RETRO_FONT = os.path.join(GAME_FOLDER,'Retro Gaming.ttf')
LEFT_ARROW = os.path.join(UI_FOLDER,'Left Arrow.png')
RIGHT_ARROW = os.path.join(UI_FOLDER,'Right Arrow.png')
CLOSE_SIGN = os.path.join(UI_FOLDER,'X Sign.png')
UNO_BUTTON = os.path.join(UI_FOLDER,'Uno Button.png')

PAUSE_TIMER = 1

info_screen = pygame.display.Info()
HEIGHT = info_screen.current_h
WIDTH = round(HEIGHT * 16 / 9) #to force a 16:9, i have an ultrawide and it was bugging me

PLAYED_CARD_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Card placed.mp3'))
MENU_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Menu Sound.mp3'))
GREEN_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Green.mp3'))
RED_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Red.mp3'))
BLUE_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Blue.mp3'))
YELLOW_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Yellow.mp3'))
DRAWN_CARD_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Drawn Card.mp3'))
REVERSE_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Reverse.mp3'))
DRAW_CARDS_ANNOUNCER_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Draw Cards.mp3'))
UNO_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Uno.mp3'))
SKIP_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Skip.mp3'))
DRAW_2_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Draw 2.mp3'))
DRAW_4_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Draw 4.mp3'))
WOW_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'Wow.mp3'))
RAINMAKER_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'RainMaker.mp3'))
NO_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER,'No.mp3'))

with open(SETTINGS,'r') as read_json:
    JSON_DATA = json.load(read_json)
    FPS = JSON_DATA['fps']
    MUSIC_VOLUME = JSON_DATA['music_volume']
    EFFECTS_VOLUME = JSON_DATA['effects_volume']
