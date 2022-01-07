import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame import mixer
import pygame.font
import os
import random
import sys

pygame.init()


WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uno")

FPS = 144

GAME_FOLDER = os.path.dirname(__file__)
TEXTURE_FOLDER = os.path.join(GAME_FOLDER,'Textures')
UI_FOLDER = os.path.join(TEXTURE_FOLDER,'UI')
CARDS_FOLDER = os.path.join(TEXTURE_FOLDER,'Cards')

#music on loop

mixer.music.load(os.path.join(UI_FOLDER,'BackMusic.mp3'))
mixer.music.play(-1)

def card_image_handler(id):
    file_name = id[:-1] + '.png'
    return os.path.join(CARDS_FOLDER,file_name)

def is_playable_logic(played_card, card_on_top,color):
    if played_card.color == color or played_card.type == card_on_top.type or played_card.type in ['13','14']:
        return True
    else:
        return False

def show_color_chooser(mos_pos):
    transparent_surface = pygame.Surface((WIDTH,HEIGHT))
    transparent_surface.set_alpha(128)
    transparent_surface.fill((0,0,0))
    SCREEN.blit(transparent_surface,(0,0))
    font = pygame.font.SysFont('Comic Sans', 70)
    font_color = (0,0,0)
    text_rect = pygame.Rect(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2)
    text_rect = text_rect.move(WIDTH/7,HEIGHT/25)
    text = font.render("Choose a color", True, font_color)
    center_red = (WIDTH / 3.2, HEIGHT / 1.8)
    center_blue = (WIDTH / 2.3, HEIGHT / 1.8)
    center_green = (WIDTH / 1.8, HEIGHT / 1.8)
    center_yellow = (WIDTH / 1.5, HEIGHT / 1.8)
    radius = HEIGHT / 12
    pygame.draw.circle(SCREEN,(255,0,0),center_red,radius)
    pygame.draw.circle(SCREEN,(0,0,255),center_blue,radius)
    pygame.draw.circle(SCREEN,(0,255,0),center_green,radius)
    pygame.draw.circle(SCREEN,(255,255,0),center_yellow,radius)
    SCREEN.blit(text,text_rect)

    if (abs(mos_pos[0] - center_red[0]) ** 2 + abs(mos_pos[1] - center_red[1]) ** 2) ** 0.5 <= radius:
        return 'r'
    elif (abs(mos_pos[0] - center_blue[0]) ** 2 + abs(mos_pos[1] - center_blue[1]) ** 2) ** 0.5 <= radius:
        return 'b'
    elif (abs(mos_pos[0] - center_green[0]) ** 2 + abs(mos_pos[1] - center_green[1]) ** 2) ** 0.5 <= radius:
        return 'g'
    elif (abs(mos_pos[0] - center_yellow[0]) ** 2 + abs(mos_pos[1] - center_yellow[1]) ** 2) ** 0.5 <= radius:
        return 'y'
    else:
        return 'd'
    
class Card():
    def __init__(self,identifier):

        self.identifier = identifier
        self.color = self.identifier[2]
        self.type = self.identifier[0:2]
        self.instance = self.identifier[3]

        self.image = pygame.image.load(card_image_handler(self.identifier))
        self.image = pygame.transform.scale(self.image,(WIDTH / 17.5,HEIGHT/4.7))
        self.rect = self.image.get_rect()

    def is_clicked(self,deck_in_game,mous_pos,color):
        if self.rect.collidepoint(mous_pos) and is_playable_logic(self,deck_in_game[-1],color):
            return self
        else:
            return None

    def update_positions(self,deck_player, deck_cpu,deck_in_game):
        if self in deck_player:
            self.rect = self.image.get_rect()
            order = deck_player.index(self)
            self.rect.center = (WIDTH/4 + WIDTH / 15 * order,HEIGHT * 0.8)
        elif self in deck_cpu:
            self.rect = self.image.get_rect()
            order = deck_cpu.index(self)
            self.rect.center = (WIDTH/4 + WIDTH / 15 * order,HEIGHT / 7)
        elif self in deck_in_game and self == deck_in_game[-1]:
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH/2, HEIGHT/2)

    def draw(self):
         SCREEN.blit(self.image,self.rect)

class UI():
    def __init__(self,position_x,position_y, player):
        self.player = player #to differenciate player from cpu
        self.number = 7 #starting number of cards
        self.image = pygame.image.load(os.path.join(UI_FOLDER,'Score Frame.png'))
        self.size = WIDTH / 16
        self.image = pygame.transform.scale(self.image, (self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position_x,position_y)
        self.font = pygame.font.SysFont('Comic Sans', int(WIDTH/38))
        self.font_color = (255,255,255)
        self.text_rect = self.rect
        self.text_rect = self.text_rect.move(WIDTH/48,HEIGHT/43)



    def update(self, num_player, num_cpu):
        if self.player:
            self.number = num_player
        else:
            self.number = num_cpu
    
    def draw(self):
        self.text = self.font.render(str(self.number), True, self.font_color)
        SCREEN.blit(self.image,self.rect)
        SCREEN.blit(self.text,self.text_rect)

def deck_creation():
    # 10 = stop, 11 = reverse, 12 = +2 , 13 = +4, 14 = color change, the rest are equal to the numbers with a zero before
    return_deck = []
    for number_code in ['10','11','12','00']:
        for color in ['red','yellow','green','blue']:
            id = str(number_code) + color[0] + "1"
            return_deck.append(Card(id))

    for number_code in ['01','02','03','04','05','06','07','08','09']:
        for color in ['red','yellow','green','blue']:
            count = 1
            while count < 3:
                id = str(number_code) + color[0] + str(count)
                return_deck.append(Card(id))
                count += 1
    for number_code in ['13','14']:
        for n in range(1,5):
            id = str(number_code) + "d" + str(n)            #d for dark
            return_deck.append(Card(id))
    
    return return_deck

ALL_CARDS = deck_creation()
deck_shuffle = ALL_CARDS.copy()

def draw_cards(num_to_draw):
    drawn_cards_list = []
    for n in range(num_to_draw):
        drawn_index = random.randrange(len(deck_shuffle))
        drawn_cards_list.append(deck_shuffle[drawn_index])
        del deck_shuffle[drawn_index]
    return drawn_cards_list

deck_player = draw_cards(7)
deck_cpu = draw_cards(7)
deck_in_game = []

card_not_gotten = True
while card_not_gotten:
    check_index = random.randrange(len(deck_shuffle))
    if deck_shuffle[check_index].identifier[0:2] in ['00,''01','02','03','04','05','06','07','08','09']:
        deck_in_game.append(deck_shuffle[check_index])
        del deck_shuffle[check_index]
        card_not_gotten = False

test_rec_score_upper = UI(WIDTH/8,HEIGHT/15,False)
test_rec_score_lower = UI(WIDTH/8,HEIGHT  * 0.8,True)
ui_group = [test_rec_score_upper,test_rec_score_lower]

def check_for_possible_moves(turn,player_deck,cpu_deck,game_deck,color):
    if turn == 'player':
        for card in player_deck:
            if is_playable_logic(card,game_deck[-1],color):
                return True
        return False
    else:
        for card in cpu_deck:
            if is_playable_logic(card,game_deck[-1],color):
                return True
        return False

def draw_card_animation(turn,deck_player_r,deck_cpu_r,mouse_p,left_pressed):
    button_image = pygame.image.load(os.path.join(UI_FOLDER,'botaodraw.png'))
    button_image = pygame.transform.scale(button_image,(WIDTH/16,WIDTH/16))
    button_rect = button_image.get_rect()
    if turn == 'player':
        button_rect = button_rect.move(WIDTH/40,HEIGHT * 0.8)
    else:
        button_rect = button_rect.move(WIDTH/40,HEIGHT/30)
    SCREEN.blit(button_image,button_rect)
    if left_pressed:
        if button_rect.collidepoint(mouse_p):
            if turn == 'player':
                deck_player_r.extend(draw_cards(1))
            else:
                deck_cpu_r.extend(draw_cards(1))

game_color = deck_in_game[0].color
play_turn = 'player'
mouse_position = (11111111111111,11111111111111111111) #meaningless value
clock = pygame.time.Clock()
run = True
while run:
    # fps running
    clock.tick(FPS)
    
    #background image

    back_image = pygame.image.load(os.path.join(UI_FOLDER,'BackGround Uno Online.png'))
    back_rect = pygame.Rect(0,0,WIDTH,HEIGHT)
    SCREEN.blit(back_image,back_rect)

    #event listener

    left_mouse_pressed = False
    event_list = pygame.event.get()
    for event in event_list:
        if event.type ==  pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                run = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            left_mouse_pressed = True
            mouse_position = pygame.mouse.get_pos()

    #updates and played_card_logic

    #checks if there's a possible play, and then processes an eventual click
    if check_for_possible_moves(play_turn,deck_player,deck_cpu,deck_in_game,game_color):    
        if left_mouse_pressed:
            if play_turn == 'player': #player logic
                for card_in_deck in deck_player:
                    played_card = card_in_deck.is_clicked(deck_in_game,mouse_position,game_color)
                    if played_card == None:
                        pass
                    else:
                        if played_card.type in ['00','01','02','03','04','05','06','07','08','09']:
                            deck_player.remove(played_card)
                            deck_in_game.append(played_card)
                            play_turn = 'cpu'
                            game_color = played_card.color
                        elif played_card.type == '12':
                            deck_player.remove(played_card)
                            deck_in_game.append(played_card)
                            deck_cpu.extend(draw_cards(2))
                            play_turn = 'cpu'
                            game_color = played_card.color
                        elif played_card.type == '13':
                            deck_player.remove(played_card)
                            deck_in_game.append(played_card)
                            game_color = played_card.color
                        elif played_card.type == '14':
                            deck_player.remove(played_card)
                            deck_in_game.append(played_card)
                            deck_cpu.extend(draw_cards(4))
                            game_color = played_card.color
                        else: #for the stop and turn signals, which both work the same
                            deck_player.remove(played_card)
                            deck_in_game.append(played_card)
                            game_color = played_card.color
            else: #cpu logic
                for card_in_deck in deck_cpu:
                    played_card = card_in_deck.is_clicked(deck_in_game,mouse_position,game_color)
                    if played_card == None:
                        pass
                    else:
                        if played_card.type in ['00','01','02','03','04','05','06','07','08','09']:
                            deck_cpu.remove(played_card)
                            deck_in_game.append(played_card)
                            play_turn = 'player'
                            game_color = played_card.color
                        elif played_card.type == '12':
                            deck_cpu.remove(played_card)
                            deck_in_game.append(played_card)
                            deck_player.extend(draw_cards(2))
                            play_turn = 'player'
                            game_color = played_card.color
                        elif played_card.type == '13':
                            deck_cpu.remove(played_card)
                            deck_in_game.append(played_card)
                            game_color = played_card.color
                        elif played_card.type == '14':
                            deck_cpu.remove(played_card)
                            deck_in_game.append(played_card)
                            deck_player.extend(draw_cards(4))
                            game_color = played_card.color
                        else: #for the stop and turn signals, which both work the same
                            deck_cpu.remove(played_card)
                            deck_in_game.append(played_card)
                            game_color = played_card.color   
    #system to draw cards (but not all draws are here)
    else:
        draw_card_animation(play_turn,deck_player,deck_cpu,mouse_position,left_mouse_pressed)

    visible_cards = []
    visible_cards.extend(deck_player)
    visible_cards.extend(deck_cpu)
    visible_cards.append(deck_in_game[-1])

    [card.update_positions(deck_player, deck_cpu,deck_in_game) for card in visible_cards]    
    [ui.update(len(deck_player), len(deck_cpu)) for ui in ui_group]

    #draw

    [ui.draw() for ui in ui_group]
    [cards.draw() for cards in visible_cards]
    if game_color == 'd':
        game_color = show_color_chooser(mouse_position)
        if game_color != "d":
            if play_turn == 'player':
                play_turn = 'cpu'
            else:
                play_turn = 'player'
    pygame.display.flip()
        
pygame.quit()
sys.exit(0)