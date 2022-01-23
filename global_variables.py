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

BACKGROUND_IMAGE = pygame.image.load(os.path.join(UI_FOLDER,'BackGround Uno Online.png'))
BACK_CARD_IMG = pygame.image.load(os.path.join(CARDS_FOLDER,'Back Card.png'))
RETRO_FONT = os.path.join(GAME_FOLDER,'Retro Gaming.ttf')
LEFT_ARROW = pygame.image.load(os.path.join(UI_FOLDER,'Left Arrow.png'))
RIGHT_ARROW = pygame.image.load(os.path.join(UI_FOLDER,'Right Arrow.png'))
UNO_BUTTON = pygame.image.load(os.path.join(UI_FOLDER,'Uno Button.png'))
SCORE_FRAME = pygame.image.load(os.path.join(UI_FOLDER,'Score Frame.png'))
DRAW_BUTTON =  pygame.image.load(os.path.join(UI_FOLDER,'botaodraw.png'))

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

#cards image initializing and handling, i had an easier way to do it but it was slow having to load every image every single loop iteration, so loading everything from the get go is way more efficient
#made a python script to generate all this code

_10r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'10r.png'))
_10y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'10y.png'))
_10g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'10g.png'))
_10b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'10b.png'))
_11r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'11r.png'))
_11y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'11y.png'))
_11g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'11g.png'))
_11b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'11b.png'))
_12r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'12r.png'))
_12y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'12y.png'))
_12g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'12g.png'))
_12b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'12b.png'))
_00r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'00r.png'))
_00y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'00y.png'))
_00g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'00g.png'))
_00b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'00b.png'))
_01r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'01r.png'))
_01y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'01y.png'))
_01g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'01g.png'))
_01b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'01b.png'))
_02r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'02r.png'))
_02y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'02y.png'))
_02g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'02g.png'))
_02b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'02b.png'))
_03r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'03r.png'))
_03y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'03y.png'))
_03g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'03g.png'))
_03b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'03b.png'))
_04r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'04r.png'))
_04y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'04y.png'))
_04g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'04g.png'))
_04b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'04b.png'))
_05r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'05r.png'))
_05y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'05y.png'))
_05g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'05g.png'))
_05b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'05b.png'))
_06r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'06r.png'))
_06y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'06y.png'))
_06g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'06g.png'))
_06b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'06b.png'))
_07r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'07r.png'))
_07y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'07y.png'))
_07g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'07g.png'))
_07b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'07b.png'))
_08r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'08r.png'))
_08y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'08y.png'))
_08g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'08g.png'))
_08b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'08b.png'))
_09r_image = pygame.image.load(os.path.join(CARDS_FOLDER,'09r.png'))
_09y_image = pygame.image.load(os.path.join(CARDS_FOLDER,'09y.png'))
_09g_image = pygame.image.load(os.path.join(CARDS_FOLDER,'09g.png'))
_09b_image = pygame.image.load(os.path.join(CARDS_FOLDER,'09b.png'))
_13d_image = pygame.image.load(os.path.join(CARDS_FOLDER,'13d.png'))
_14d_image = pygame.image.load(os.path.join(CARDS_FOLDER,'14d.png'))

def card_image_handler(id):
    if id == '10r':
        return _10r_image
    elif id == '10y':
        return _10y_image
    elif id == '10g':
        return _10g_image
    elif id == '10b':
        return _10b_image
    elif id == '11r':
        return _11r_image
    elif id == '11y':
        return _11y_image
    elif id == '11g':
        return _11g_image
    elif id == '11b':
        return _11b_image
    elif id == '12r':
        return _12r_image
    elif id == '12y':
        return _12y_image
    elif id == '12g':
        return _12g_image
    elif id == '12b':
        return _12b_image
    elif id == '00r':
        return _00r_image
    elif id == '00y':
        return _00y_image
    elif id == '00g':
        return _00g_image
    elif id == '00b':
        return _00b_image
    elif id == '01r':
        return _01r_image
    elif id == '01y':
        return _01y_image
    elif id == '01g':
        return _01g_image
    elif id == '01b':
        return _01b_image
    elif id == '02r':
        return _02r_image
    elif id == '02y':
        return _02y_image
    elif id == '02g':
        return _02g_image
    elif id == '02b':
        return _02b_image
    elif id == '03r':
        return _03r_image
    elif id == '03y':
        return _03y_image
    elif id == '03g':
        return _03g_image
    elif id == '03b':
        return _03b_image
    elif id == '04r':
        return _04r_image
    elif id == '04y':
        return _04y_image
    elif id == '04g':
        return _04g_image
    elif id == '04b':
        return _04b_image
    elif id == '05r':
        return _05r_image
    elif id == '05y':
        return _05y_image
    elif id == '05g':
        return _05g_image
    elif id == '05b':
        return _05b_image
    elif id == '06r':
        return _06r_image
    elif id == '06y':
        return _06y_image
    elif id == '06g':
        return _06g_image
    elif id == '06b':
        return _06b_image
    elif id == '07r':
        return _07r_image
    elif id == '07y':
        return _07y_image
    elif id == '07g':
        return _07g_image
    elif id == '07b':
        return _07b_image
    elif id == '08r':
        return _08r_image
    elif id == '08y':
        return _08y_image
    elif id == '08g':
        return _08g_image
    elif id == '08b':
        return _08b_image
    elif id == '09r':
        return _09r_image
    elif id == '09y':
        return _09y_image
    elif id == '09g':
        return _09g_image
    elif id == '09b':
        return _09b_image
    elif id == '13d':
        return _13d_image
    elif id == '14d':
        return _14d_image
