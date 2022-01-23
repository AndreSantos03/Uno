from ast import Return
import json
from pickle import TRUE

from matplotlib import animation
from initial_menu import loading_image
import pygame
from pygame.constants import MOUSEBUTTONDOWN
import pygame.font
import os
import random
import global_variables


#settings handling

transparent_surface = pygame.Surface((global_variables.WIDTH,global_variables.HEIGHT))
transparent_surface.set_alpha(128)
transparent_surface.fill((0,0,0))
set_menu_rect = pygame.Rect(0,0,int(global_variables.WIDTH/1.35),int(global_variables.HEIGHT/1.35))
set_menu_rect.center = (int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2))

options_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/80))

#resolution
resolution_options_img = options_font.render("Resolution:",True,(255,255,255))
resolution_options_rect = resolution_options_img.get_rect(center=(int(global_variables.WIDTH / 3),int(global_variables.HEIGHT / 4)))
resolution_img = options_font.render("{}x{}".format(int(global_variables.WIDTH),int(global_variables.HEIGHT)),True,(255,255,255))
resolution_rect = resolution_img.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 7.25), int(global_variables.HEIGHT / 4)))

#volume
music_volume_img = options_font.render("Music Volume:",True,(255,255,255))
music_volume_rect = resolution_options_img.get_rect(center=(int(global_variables.WIDTH / 3),int(global_variables.HEIGHT / 4  + global_variables.HEIGHT / 14)))
percentage_sign_image = options_font.render("%",True,(255,255,255))
percentage_sign_rect_1 = resolution_options_img.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 3.75),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14)))
m_volume_value_img = options_font.render("{}".format(global_variables.MUSIC_VOLUME * 100),True,(255,255,255))
m_volume_value_rect = m_volume_value_img.get_rect(center = (int(global_variables.WIDTH / 3 + global_variables.WIDTH / 4.8),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14)))
left_arrow = global_variables.LEFT_ARROW
left_arrow = pygame.transform.scale(left_arrow,(int(global_variables.WIDTH/20),int(global_variables.HEIGHT/30)))
left_arrow_rect_1 = left_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 9),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14)))
right_arrow = global_variables.RIGHT_ARROW
right_arrow = pygame.transform.scale(right_arrow,(int(global_variables.WIDTH/20),int(global_variables.HEIGHT/30)))
right_arrow_rect_1 = right_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 6),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14)))
effects_volume_img = options_font.render("Effects Volume:",True,(255,255,255))
effects_volume_rect = resolution_options_img.get_rect(center=(int(global_variables.WIDTH / 3),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 2)))
percentage_sign_rect_2 = resolution_options_img.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 3.75),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 2)))
effects_volume_value_img = options_font.render("{}".format(int(global_variables.EFFECTS_VOLUME * 100)),True,(255,255,255))
effects_volume_value_rect = m_volume_value_img.get_rect(center = (int(global_variables.WIDTH / 3 + global_variables.WIDTH / 4.8),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 2)))
left_arrow_rect_2 = left_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 9),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 2)))
right_arrow_rect_2 = right_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 6),int(global_variables.HEIGHT / 4 + + global_variables.HEIGHT / 14 * 2)))
fps_image = options_font.render("FPS:",True,(255,255,255))
fps_rect = resolution_options_img.get_rect(center=(int(global_variables.WIDTH / 3),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 3)))
fps_value_image = options_font.render("{}".format(global_variables.FPS),True,(255,255,255))
fps_value_rect = fps_value_image.get_rect(center = (int(global_variables.WIDTH / 3 + global_variables.WIDTH / 4.8),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 3)))
left_arrow_rect_3 = left_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 9),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 3)))
right_arrow_rect_3 = right_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 6),int(global_variables.HEIGHT / 4 + + global_variables.HEIGHT / 14 * 3)))

#close sign
x_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/38.4))
close_img = x_font.render('X',True,(255,255,255))
close_rect = close_img.get_rect(center=(int(global_variables.WIDTH/7),int(global_variables.HEIGHT/6.4)))

#quit and retry
button_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/48))
retry_img = button_font.render('Restart',True,(255,255,255))
retry_rect_menu = retry_img.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 7.25),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 4.5)))
quit_img = button_font.render('Quit',True,(255,255,255))
quit_rect_menu = quit_img.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 7.25),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 6)))

#Uno button
uno_button_img = global_variables.UNO_BUTTON
uno_button_img = pygame.transform.scale(uno_button_img,(int(global_variables.HEIGHT/4),int(global_variables.HEIGHT/4)))
uno_button_rect = uno_button_img.get_rect(center=(int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2)))


#to chane the fps
fps_changes = [30,45,60,90,120,144]

#end game menu
end_game_rect = pygame.Rect(0,0,int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2))
end_game_rect.center = (int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2))
result_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/19.2))
win_img = result_font.render("You Win!",True,(255,255,255))
win_rect = win_img.get_rect(center=(int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2.5)))
lost_img = result_font.render("You Loose!",True,(255,255,255))
lost_rect = win_img.get_rect(center=(int(global_variables.WIDTH/2 - global_variables.WIDTH/15),int(global_variables.HEIGHT/2.5)))
retry_rect_end = retry_img.get_rect(center=(int(global_variables.WIDTH/2),int(global_variables.HEIGHT/1.8)))
retry_rect_end.move_ip(int(-global_variables.WIDTH/12),0)
quit_rect_end = quit_img.get_rect(center=(int(global_variables.WIDTH/2),int(global_variables.HEIGHT/1.8)))
quit_rect_end.move_ip(int(global_variables.WIDTH/12),0)

def is_playable_logic(played_card, card_on_top,color):
    if played_card.color == color or played_card.type == card_on_top.type or played_card.type in ['13','14']:
        return True
    else:
        return False

def show_color_chooser(mos_pos,screen,not_playable): #not playable is related to the uno timer, so we dont click 2 objects at one time
    transparent_surface = pygame.Surface((global_variables.WIDTH,global_variables.HEIGHT))
    transparent_surface.set_alpha(128)
    transparent_surface.fill((0,0,0))
    screen.blit(transparent_surface,(0,0))
    font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/27.5))
    text_rect = pygame.Rect(int(global_variables.WIDTH/4),int(global_variables.HEIGHT/4),int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2))
    text_rect = text_rect.move(global_variables.WIDTH/7,global_variables.HEIGHT/25)
    text = font.render("Choose a color", True, (255,255,255))
    center_red = (int(global_variables.WIDTH / 3.2), int(global_variables.HEIGHT / 1.8))
    center_blue = (int(global_variables.WIDTH / 2.3), int(global_variables.HEIGHT / 1.8))
    center_green = (int(global_variables.WIDTH / 1.8), int(global_variables.HEIGHT / 1.8))
    center_yellow = (int(global_variables.WIDTH / 1.5), int(global_variables.HEIGHT / 1.8))
    radius = int(global_variables.HEIGHT / 12)
    pygame.draw.circle(screen,(255,0,0),center_red,radius)
    pygame.draw.circle(screen,(0,0,255),center_blue,radius)
    pygame.draw.circle(screen,(0,255,0),center_green,radius)
    pygame.draw.circle(screen,(255,255,0),center_yellow,radius)
    screen.blit(text,text_rect)
    if not not_playable:
        if (abs(mos_pos[0] - center_red[0]) ** 2 + abs(mos_pos[1] - center_red[1]) ** 2) ** 0.5 <= radius:
            return global_variables.PAUSE_TIMER,'cpu','r'
        elif (abs(mos_pos[0] - center_blue[0]) ** 2 + abs(mos_pos[1] - center_blue[1]) ** 2) ** 0.5 <= radius:
            return global_variables.PAUSE_TIMER,'cpu','b'
        elif (abs(mos_pos[0] - center_green[0]) ** 2 + abs(mos_pos[1] - center_green[1]) ** 2) ** 0.5 <= radius:
            return global_variables.PAUSE_TIMER,'cpu','g'
        elif (abs(mos_pos[0] - center_yellow[0]) ** 2 + abs(mos_pos[1] - center_yellow[1]) ** 2) ** 0.5 <= radius:
            return global_variables.PAUSE_TIMER,'cpu','y'
        else:
            return 0,'player','d'


def pop_up_animation(screen,animation,sound):
    animation_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/9.6))
    choosing_color_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/16))
    if animation == 'draw 2':
        animation_text = animation_font.render("Draw 2!",True,(255,255,255))
        if not sound:
            global_variables.DRAW_2_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
            global_variables.DRAW_2_SOUND.play()
    elif animation == 'reverse':
        animation_text = animation_font.render("Reverse!",True,(255,255,255))
        if not sound:
            global_variables.REVERSE_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
            global_variables.REVERSE_SOUND.play()
    elif animation == 'skip':
        animation_text = animation_font.render("Skip!",True,(255,255,255))
        if not sound:
            global_variables.SKIP_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
            global_variables.SKIP_SOUND.play()
    elif animation == 'yellow':
        animation_text = animation_font.render("Yellow!",True,(255,255,255))
    elif animation == 'red':
        animation_text = animation_font.render("Red!",True,(255,255,255))
    elif animation == 'blue':
        animation_text = animation_font.render("Blue!",True,(255,255,255))
    elif animation == 'green':
        animation_text = animation_font.render("Green!",True,(255,255,255))
    elif animation == 'draw cards':
        animation_text = animation_font.render("Draw Cards!",True,(255,255,255))
    elif animation == 'uno cpu':
        animation_text = animation_font.render("UNO!",True,(255,255,255))
    elif animation == 'color chooser cpu':
        animation_text = choosing_color_font.render("CPU is choosing a color...",True,(255,255,255))
    elif animation == 'draw 4':
        animation_text = choosing_color_font.render("Draw 4!",True,(255,255,255))
        if not sound:
            global_variables.DRAW_4_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
            global_variables.DRAW_4_SOUND.play()
    
    animation_rect = animation_text.get_rect(center = (global_variables.WIDTH/2,global_variables.HEIGHT/2))
    screen.blit(animation_text,animation_rect)

class Card():
    def __init__(self,identifier):

        self.identifier = identifier
        self.color = self.identifier[2]
        self.type = self.identifier[0:2]
        self.instance = self.identifier[3]

    def is_clicked(self,deck_in_game,mous_pos,color):
        if self.rect.collidepoint(mous_pos) and is_playable_logic(self,deck_in_game[-1],color):
            return self
        else:
            return None

    def update_image(self,black_card):
        if black_card:
            self.image = global_variables.BACK_CARD_IMG
        else:
            self.image = global_variables.card_image_handler(self.identifier[:-1])
        self.image = pygame.transform.scale(self.image,(int(global_variables.WIDTH / 17.5),int(global_variables.HEIGHT/4.7)))
        self.rect = self.image.get_rect()

    def update_positions(self,deck_player, deck_cpu,deck_in_game):
        if self in deck_player:
            self.rect = self.image.get_rect()
            order = deck_player.index(self)
            deck_length = len(deck_player)
            self.rect.center = (int(global_variables.WIDTH/4) + (int(global_variables.WIDTH / 1.5) / deck_length * order),int(global_variables.HEIGHT * 0.8))
        elif self in deck_cpu:
            self.rect = self.image.get_rect()
            order = deck_cpu.index(self)
            deck_length = len(deck_cpu)
            self.rect.center = (int(global_variables.WIDTH/4) + int((global_variables.WIDTH / 1.5) /deck_length * order),int(global_variables.HEIGHT / 7))
        elif self in deck_in_game and self == deck_in_game[-1]:
            self.rect = self.image.get_rect()
            self.rect.center = (int(global_variables.WIDTH/2), int(global_variables.HEIGHT/2))

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class UI():
    def __init__(self,position_x,position_y, player):
        self.player = player #to differenciate player from cpu
        self.number = 7 #starting number of cards
        self.image = global_variables.SCORE_FRAME
        self.size = int(global_variables.WIDTH / 16)
        self.image = pygame.transform.scale(self.image, (self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position_x,position_y)
        self.font = font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/50))
        self.font_color = (255,255,255)
        self.text_rect = self.rect
        self.text_rect = self.text_rect.move(int(global_variables.WIDTH/48),int(global_variables.HEIGHT/43))



    def update(self, num_player, num_cpu):
        if self.player:
            self.number = num_player
        else:
            self.number = num_cpu
    
    def draw(self,screen):
        self.text = self.font.render(str(self.number), True, self.font_color)
        screen.blit(self.image,self.rect)
        screen.blit(self.text,self.text_rect)

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

def draw_cards(num_to_draw,shuffled):
    drawn_cards_list = []
    for n in range(num_to_draw):
        drawn_index = random.randrange(len(shuffled))
        drawn_cards_list.append(shuffled[drawn_index])
        del shuffled[drawn_index]
    if len(drawn_cards_list) == 1:
        return drawn_cards_list[0]
    return drawn_cards_list

test_rec_score_upper = UI(int(global_variables.WIDTH/8),int(global_variables.HEIGHT/15),False)
test_rec_score_lower = UI(int(global_variables.WIDTH/8),int(global_variables.HEIGHT  * 0.8),True)
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

def draw_card_animation(turn,deck_player_r,mouse_p,left_pressed,shuffle,screen):
    button_image = global_variables.DRAW_BUTTON
    button_image = pygame.transform.scale(button_image,(int(global_variables.WIDTH/16),int(global_variables.WIDTH/16)))
    button_rect = button_image.get_rect()
    if turn == 'player':
        button_rect = button_rect.move(int(global_variables.WIDTH/40),int(global_variables.HEIGHT * 0.8))
    else:
        button_rect = button_rect.move(int(global_variables.WIDTH/40),int(global_variables.HEIGHT/30))
    screen.blit(button_image,button_rect)
    if left_pressed and button_rect.collidepoint(mouse_p) and turn == 'player':
        deck_player_r.append(draw_cards(1,shuffle))
        global_variables.DRAWN_CARD_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
        global_variables.DRAWN_CARD_SOUND.play()

def main_game_loop():
    
    play_turn = 'player'

    ALL_CARDS = deck_creation()
    deck_shuffle = ALL_CARDS.copy()
    
    first_card_drawn = False
    while not first_card_drawn:
        drawn_card = draw_cards(1,deck_shuffle)
        if drawn_card.type in ['00,''01','02','03','04','05','06','07','08','09']:
            deck_in_game = [drawn_card]
            first_card_drawn = True

    game_color = deck_in_game[0].color

    legal_player_deck = False

    while not legal_player_deck:
        temp_deck = draw_cards(7,deck_shuffle)
        for temp_card in temp_deck:
            if is_playable_logic(temp_card,deck_in_game[0],game_color):
                legal_player_deck = True
                deck_player = temp_deck
                break

    deck_cpu = draw_cards(7,deck_shuffle)

    mouse_position = (11111111111111,11111111111111111111) #meaningless value

    latest_animation = None
    draw_cards_sound_played = False
    sound_played = False
    winning_sound_played = False

    test_rec_score_upper = UI(int(global_variables.WIDTH/8),int(global_variables.HEIGHT/15),False)
    test_rec_score_lower = UI(int(global_variables.WIDTH/8),int(global_variables.HEIGHT  * 0.8),True)
    ui_group = [test_rec_score_upper,test_rec_score_lower]

    settings_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/80))
    settings_img =  settings_font.render("Settings",True,(255,255,255))
    settings_rect = settings_img.get_rect()
    settings_rect = settings_rect.move(global_variables.WIDTH/192,global_variables.HEIGHT/216)

    #update values from json
    m_volume_value_img = options_font.render("{}".format(int(global_variables.MUSIC_VOLUME * 100)),True,(255,255,255))
    effects_volume_value_img = options_font.render("{}".format(int(global_variables.EFFECTS_VOLUME * 100)),True,(255,255,255))
    fps_value_image = options_font.render("{}".format(global_variables.FPS),True,(255,255,255))

    SCREEN = pygame.display.set_mode((global_variables.WIDTH,global_variables.HEIGHT))
    pygame.display.set_caption("Uno")

    clock = pygame.time.Clock()
    hold_on_timer = 0
    animation_timer = 0
    last_tick_frame = 0
    uno_timer = 0
    game_end = False
    run = True
    menu_up = False
    uno_time = False

    while run:

        # fps running
        clock.tick(global_variables.FPS)
        
        #update ticks
        if not menu_up:
            tick = pygame.time.get_ticks()
            delta_time = (tick - last_tick_frame) / 1000
            last_tick_frame = tick
            hold_on_timer -= delta_time
            uno_timer -= delta_time
            if not uno_time:
                animation_timer -= delta_time

        #background image

        back_image = global_variables.BACKGROUND_IMAGE
        back_rect = pygame.Rect(0,0,global_variables.WIDTH,global_variables.HEIGHT)
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

        #reset latest played card
        played_card = None

        #check for win
        if len(deck_player) == 0:
            game_end = True
            play_turn = 'player'
            if not winning_sound_played:
                global_variables.RAINMAKER_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                global_variables.RAINMAKER_SOUND.play()
                winning_sound_played = True
        elif len(deck_cpu) == 0:
            game_end = True
            play_turn = 'cpu'
            if not winning_sound_played:
                global_variables.NO_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                global_variables.NO_SOUND.play()
                winning_sound_played = True

        if not game_end:
            #check if deck needs to be replaced
            if len(deck_shuffle) <= 4:
                for n in range(len(deck_in_game) -1):
                    deck_shuffle.append(deck_in_game.pop(0))
                random.shuffle(deck_shuffle)

            if menu_up:
                #Menu click handling
                if left_mouse_pressed:
                    menu_up = False
                    if left_arrow_rect_1.collidepoint(mouse_position) and global_variables.MUSIC_VOLUME > 0:
                        menu_up = True
                        global_variables.MUSIC_VOLUME = round(global_variables.MUSIC_VOLUME - 0.1,1)
                        global_variables.JSON_DATA['music_volume'] = global_variables.MUSIC_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        pygame.mixer.music.set_volume(global_variables.MUSIC_VOLUME)
                    elif right_arrow_rect_1.collidepoint(mouse_position) and global_variables.MUSIC_VOLUME < 1:
                        menu_up = True
                        global_variables.MUSIC_VOLUME = round(global_variables.MUSIC_VOLUME + 0.1,1)
                        global_variables.JSON_DATA['music_volume'] = global_variables.MUSIC_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        pygame.mixer.music.set_volume(global_variables.MUSIC_VOLUME)
                    elif left_arrow_rect_2.collidepoint(mouse_position) and global_variables.EFFECTS_VOLUME > 0:
                        menu_up = True
                        global_variables.EFFECTS_VOLUME = round(global_variables.EFFECTS_VOLUME - 0.1,1)
                        global_variables.JSON_DATA['effects_volume'] = global_variables.EFFECTS_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                    elif right_arrow_rect_2.collidepoint(mouse_position) and global_variables.EFFECTS_VOLUME < 1:
                        menu_up = True
                        global_variables.EFFECTS_VOLUME = round(global_variables.EFFECTS_VOLUME + 0.1,1)
                        global_variables.JSON_DATA['effects_volume'] = global_variables.EFFECTS_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                    elif left_arrow_rect_3.collidepoint(mouse_position) and global_variables.FPS > 30:
                        menu_up = True
                        index_fps = fps_changes.index(global_variables.FPS)
                        global_variables.FPS = fps_changes[index_fps - 1]
                        global_variables.JSON_DATA['fps'] = global_variables.FPS
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                    elif right_arrow_rect_3.collidepoint(mouse_position) and global_variables.FPS < 144:
                        menu_up = True
                        index_fps = fps_changes.index(global_variables.FPS)
                        global_variables.FPS = fps_changes[index_fps + 1]
                        global_variables.JSON_DATA['fps'] = global_variables.FPS
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                    elif close_rect.collidepoint(mouse_position):
                        menu_up = True
                        menu_up = False
                    elif quit_rect_menu.collidepoint(mouse_position):                        
                        global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        global_variables.MENU_SOUND.play()
                        return False
                    elif retry_rect_menu.collidepoint(mouse_position):
                        global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        global_variables.MENU_SOUND.play()
                        loading_image(SCREEN)
                        return True

                    #update values
                    m_volume_value_img = options_font.render("{}".format(int(global_variables.MUSIC_VOLUME * 100)),True,(255,255,255))
                    effects_volume_value_img = options_font.render("{}".format(int(global_variables.EFFECTS_VOLUME * 100)),True,(255,255,255))
                    fps_value_image = options_font.render("{}".format(global_variables.FPS),True,(255,255,255))

                    if menu_up:
                        global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        global_variables.MENU_SOUND.play()
            else:
                #checks if there's a possible play, and then processes an eventual click
                if game_color != 'd':
                    if check_for_possible_moves(play_turn,deck_player,deck_cpu,deck_in_game,game_color):
                        must_draw_cards = False
                        if play_turn == 'player': #player logic
                            if left_mouse_pressed:
                                sound_played = False
                                for card_player in deck_player:
                                    if card_player.is_clicked(deck_in_game,mouse_position,game_color):
                                        played_card = card_player

                        #CPU Logic  , choose which card to play          
                        elif play_turn == 'cpu' and game_color != 'd' and hold_on_timer < 0 and animation_timer < 0 and not menu_up and not uno_time:
                            sound_played = False
                            highest_card = None
                            highest_rating = 0
                            for card_cpu in deck_cpu:
                                card_rating = 0 #1 for black cards, 2 for different colors same numbers, 3 for numbers of same colors, 4 for special cards of same color
                                if card_cpu.color == game_color and card_cpu.type in ['10','11','12']:
                                    card_rating = 4
                                elif card_cpu.color == game_color and card_cpu.type in ['00','01','02','03','04','05','06','07','08','09']:
                                    card_rating = 3
                                elif card_cpu.type == deck_in_game[-1].type:
                                    card_rating = 2
                                elif card_cpu.color == 'd':
                                    card_rating = 1
                                if card_rating > highest_rating:
                                    highest_card = card_cpu
                                    highest_rating = card_rating
                            hold_on_timer = global_variables.PAUSE_TIMER
                            played_card = highest_card
                    else:
                        if not uno_time and animation_timer < 0:
                            must_draw_cards = True
                            if not draw_cards_sound_played and not len(deck_player) == 1:
                                latest_animation = "draw cards"
                                animation_timer = global_variables.PAUSE_TIMER
                                hold_on_timer = global_variables.PAUSE_TIMER
                                draw_cards_sound_played = True
                                global_variables.DRAW_CARDS_ANNOUNCER_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                                global_variables.DRAW_CARDS_ANNOUNCER_SOUND.play()

                            #cpu drawing cards
                            if play_turn == 'cpu' and hold_on_timer < 0:
                                deck_cpu.append(draw_cards(1,deck_shuffle))
                                hold_on_timer = global_variables.PAUSE_TIMER / 2

                #Card is played logic
                if played_card != None:
                    #in case there's player uno
                    if len(deck_player) == 2 and play_turn == 'player' and not uno_time: 
                        uno_time = True
                        uno_timer = 2
                        play_turn_saved = 'player'
                    #in case there's a cpu uno
                    elif len(deck_cpu) == 2 and play_turn == 'cpu' and not uno_time:
                        play_turn_saved = 'cpu'
                        uno_time = True
                        uno_timer = 1
                        animation_timer = global_variables.PAUSE_TIMER * 2 #times 2 to leave time for another animations
                        global_variables.UNO_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        global_variables.UNO_SOUND.play()

                    #reset variable                
                    draw_cards_sound_played = False
                    
                    #deal with turns
                    if play_turn == 'player':
                        deck_player.remove(played_card)
                        deck_in_game.append(played_card)
                    else:
                        deck_cpu.remove(played_card)
                        deck_in_game.append(played_card)

                    #deal with cards played
                    if played_card.type in ['00','01','02','03','04','05','06','07','08','09']:
                        if play_turn == 'player':
                            play_turn = 'cpu'
                        else:
                            play_turn = 'player'
                        game_color = played_card.color
                        animation_timer = -1
                        hold_on_timer = global_variables.PAUSE_TIMER
                    elif played_card.type == '12':
                        if play_turn == 'player':
                            deck_cpu.extend(draw_cards(2,deck_shuffle))
                            play_turn = 'cpu'
                        else:
                            deck_player.extend(draw_cards(2,deck_shuffle))
                            play_turn = 'player'
                        game_color = played_card.color
                        latest_animation = 'draw 2'
                        hold_on_timer = global_variables.PAUSE_TIMER
                        animation_timer = global_variables.PAUSE_TIMER
                    elif played_card.type == '13':
                        game_color = played_card.color
                        if play_turn == 'cpu':
                            latest_animation = 'color chooser cpu'
                            animation_timer = global_variables.PAUSE_TIMER
                        global_variables.WOW_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        global_variables.WOW_SOUND.play()
                        hold_on_timer = global_variables.PAUSE_TIMER
                    elif played_card.type == '14':
                        if play_turn == 'player':
                            deck_cpu.extend(draw_cards(4,deck_shuffle))
                            global_variables.DRAW_4_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                            global_variables.DRAW_4_SOUND.play()
                        else:
                            deck_player.extend(draw_cards(4,deck_shuffle))
                            latest_animation = 'draw 4'
                            animation_timer = global_variables.PAUSE_TIMER * 2
                            hold_on_timer = global_variables.PAUSE_TIMER * 2
                        game_color = played_card.color
                    else: #for the stop and turn signals, which both work the same
                        game_color = played_card.color
                        #differentiate both animations
                        if played_card.type == '10':
                            latest_animation = 'skip'
                        else:
                            latest_animation = 'reverse'
                        animation_timer = global_variables.PAUSE_TIMER
                        hold_on_timer = global_variables.PAUSE_TIMER
                    global_variables.PLAYED_CARD_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.PLAYED_CARD_SOUND.play()



        
        #system to draw cards (but not all draws are here)

        visible_cards = []
        visible_cards.extend(deck_player)
        visible_cards.extend(deck_cpu)
        visible_cards.append(deck_in_game[-1])

        [card.update_image(False) for card in deck_player]
        deck_in_game[-1].update_image(False)
        [card.update_image(True) for card in deck_cpu]           
        [card.update_positions(deck_player, deck_cpu,deck_in_game) for card in visible_cards]    
        [ui.update(len(deck_player), len(deck_cpu)) for ui in ui_group]

        #draw

        [ui.draw(SCREEN) for ui in ui_group]
        [cards.draw(SCREEN) for cards in visible_cards]

        #black cards handling

        if game_color == 'd' and not menu_up:
            if play_turn == 'player':
                hold_on_timer,play_turn, game_color = show_color_chooser(mouse_position,SCREEN,uno_time)
                if game_color == 'y': 
                    latest_animation = 'yellow'
                    global_variables.YELLOW_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.YELLOW_SOUND.play()
                    animation_timer = global_variables.PAUSE_TIMER
                elif game_color == 'r':
                    latest_animation = 'red'
                    global_variables.RED_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.RED_SOUND.play()
                    animation_timer = global_variables.PAUSE_TIMER
                elif game_color == 'g':
                    latest_animation = 'green'
                    global_variables.GREEN_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.GREEN_SOUND.play()
                    animation_timer = global_variables.PAUSE_TIMER
                if game_color == 'b':
                    latest_animation = 'blue'
                    global_variables.BLUE_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.BLUE_SOUND.play()
                    animation_timer = global_variables.PAUSE_TIMER
            else:        
                if hold_on_timer < 0:
                    #choosing the best color to pick cpu
                    num_of_blue_cards = ['b',0]
                    num_of_red_cards = ['r',0]    
                    num_of_yellow_cards = ['y',0]    
                    num_of_green_cards = ['g',0]
                    for card_cpu_2 in deck_cpu:
                        num_of_blue_cards[1] += 1 * (card_cpu_2.color == 'b')     
                        num_of_red_cards[1] += 1 * (card_cpu_2.color == 'r')  
                        num_of_yellow_cards[1] += 1 * (card_cpu_2.color == 'y')  
                        num_of_green_cards[1] += 1 * (card_cpu_2.color == 'g')
                    maximum = max([num_of_blue_cards,num_of_green_cards,num_of_red_cards,num_of_yellow_cards],key = lambda x: x[1])
                    for variable in [num_of_yellow_cards,num_of_red_cards,num_of_green_cards,num_of_blue_cards]:
                        if maximum == variable:
                            game_color = variable[0]
                            play_turn = 'player'
                            if game_color == 'y':
                                latest_animation = 'yellow'
                                global_variables.YELLOW_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                                global_variables.YELLOW_SOUND.play()
                            elif game_color == 'r':
                                latest_animation = 'red'
                                global_variables.RED_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                                global_variables.RED_SOUND.play()
                            elif game_color == 'g':
                                latest_animation = 'green'
                                global_variables.GREEN_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                                global_variables.GREEN_SOUND.play()
                            if game_color == 'b':
                                latest_animation = 'blue'
                                global_variables.BLUE_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                                global_variables.BLUE_SOUND.play()
                            animation_timer = global_variables.PAUSE_TIMER
                            break


        if must_draw_cards:
            draw_card_animation(play_turn,deck_player,mouse_position,left_mouse_pressed,deck_shuffle,SCREEN)

        #uno animtions
        if uno_time: 
            if play_turn_saved == 'player': #New variable because we change the values of play_turn between the uno_time change and this part
                SCREEN.blit(transparent_surface,(0,0))
                SCREEN.blit(uno_button_img,uno_button_rect)
                hold_on_timer
                if left_mouse_pressed and uno_button_rect.collidepoint(mouse_position):
                    global_variables.UNO_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.UNO_SOUND.play()
                    hold_on_timer = global_variables.PAUSE_TIMER
                    uno_time = False
                elif uno_timer < 0:
                    deck_player.extend(draw_cards(2,deck_shuffle))
                    uno_time = False
                    animation_timer = global_variables.PAUSE_TIMER
                    latest_animation = 'draw 2'
                    uno_timer = global_variables.PAUSE_TIMER
            else:
                pop_up_animation(SCREEN,"uno cpu",False)
                if uno_timer < 0:
                    uno_time = False

        #draw animations
        elif animation_timer >= 0 and not game_end:
            #draw 4 has some special effects
            if latest_animation == 'draw 4' and play_turn == 'cpu':
                if animation_timer >= global_variables.PAUSE_TIMER:
                    pop_up_animation(SCREEN,'draw 4',sound_played)
                else:
                    pop_up_animation(SCREEN,'color chooser cpu',sound_played)
            else:
                pop_up_animation(SCREEN,latest_animation,sound_played)
            sound_played = True
        
        #menu animations
        if menu_up:
            SCREEN.blit(transparent_surface,(0,0))
            pygame.draw.rect(SCREEN,(255,163,1),set_menu_rect)
            SCREEN.blit(resolution_options_img,resolution_options_rect)
            SCREEN.blit(resolution_img,resolution_rect)
            SCREEN.blit(music_volume_img,music_volume_rect)
            SCREEN.blit(percentage_sign_image,percentage_sign_rect_1)
            SCREEN.blit(m_volume_value_img,m_volume_value_rect)
            SCREEN.blit(effects_volume_value_img,effects_volume_value_rect)
            SCREEN.blit(effects_volume_img,effects_volume_rect)
            SCREEN.blit(fps_image,fps_rect)
            SCREEN.blit(fps_value_image,fps_value_rect)
            SCREEN.blit(percentage_sign_image,percentage_sign_rect_2)
            SCREEN.blit(left_arrow,left_arrow_rect_1)
            SCREEN.blit(right_arrow,right_arrow_rect_1)
            SCREEN.blit(left_arrow,left_arrow_rect_2)
            SCREEN.blit(right_arrow,right_arrow_rect_2)
            SCREEN.blit(left_arrow,left_arrow_rect_3)
            SCREEN.blit(right_arrow,right_arrow_rect_3)
            SCREEN.blit(close_img,close_rect)
            SCREEN.blit(quit_img,quit_rect_menu)
            SCREEN.blit(retry_img,retry_rect_menu)

        elif game_end:
            if left_mouse_pressed:
                if quit_rect_end.collidepoint(mouse_position):
                    return False
                if retry_rect_end.collidepoint(mouse_position):
                    loading_image(SCREEN)
                    return True
            SCREEN.blit(transparent_surface,(0,0))
            pygame.draw.rect(SCREEN,(255,163,1),end_game_rect)
            if play_turn == 'player':
                SCREEN.blit(win_img,win_rect)
            else:
                SCREEN.blit(lost_img,lost_rect)
            SCREEN.blit(retry_img,retry_rect_end)
            SCREEN.blit(quit_img,quit_rect_end)

        else:
            SCREEN.blit(settings_img,settings_rect)
            if left_mouse_pressed and settings_rect.collidepoint(mouse_position):
                global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                global_variables.MENU_SOUND.play()
                menu_up = True

        pygame.display.flip()