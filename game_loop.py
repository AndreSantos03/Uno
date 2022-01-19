from turtle import width
import pygame
from pygame.constants import MOUSEBUTTONDOWN
import pygame.font
import os
import random
import global_variables

#functions

def card_image_handler(id):
    file_name = id[:-1] + '.png'
    return os.path.join(global_variables.CARDS_FOLDER,file_name)

def is_playable_logic(played_card, card_on_top,color):
    if played_card.color == color or played_card.type == card_on_top.type or played_card.type in ['13','14']:
        return True
    else:
        return False

def show_color_chooser(mos_pos,screen):
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


def pop_up_animation(screen,animation):
    animation_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/9.6))
    choosing_color_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/16))
    if animation == 'draw 2':
        animation_text = animation_font.render("Draw 2!",True,(255,255,255))
    elif animation == 'reverse':
        animation_text = animation_font.render("Reverse!",True,(255,255,255))
    elif animation == 'skip':
        animation_text = animation_font.render("Skip!",True,(255,255,255))
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
    elif animation == 'color chooser cpu':
        animation_text = choosing_color_font.render('CPU is choosing a color...',True,(255,255,255))
    elif animation == 'draw 4':
        animation_text = choosing_color_font.render('CPU is choosing a color...',True,(255,255,255))
    animation_rect = animation_text.get_rect(center = (global_variables.WIDTH/2,global_variables.HEIGHT/2))
    screen.blit(animation_text,animation_rect)

class Card():
    def __init__(self,identifier):

        self.identifier = identifier
        self.color = self.identifier[2]
        self.type = self.identifier[0:2]
        self.instance = self.identifier[3]

        self.image = pygame.image.load(card_image_handler(self.identifier))
        self.image = pygame.transform.scale(self.image,(int(global_variables.WIDTH / 17.5),int(global_variables.HEIGHT/4.7)))
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
        self.image = pygame.image.load(os.path.join(global_variables.UI_FOLDER,'Score Frame.png'))
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
    button_image = pygame.image.load(os.path.join(global_variables.UI_FOLDER,'botaodraw.png'))
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

    test_rec_score_upper = UI(int(global_variables.WIDTH/8),int(global_variables.HEIGHT/15),False)
    test_rec_score_lower = UI(int(global_variables.WIDTH/8),int(global_variables.HEIGHT  * 0.8),True)
    ui_group = [test_rec_score_upper,test_rec_score_lower]

    SCREEN = pygame.display.set_mode((global_variables.WIDTH,global_variables.HEIGHT))
    pygame.display.set_caption("Uno")

    clock = pygame.time.Clock()
    hold_on_timer = 0
    animation_timer = 0
    last_tick_frame = 0
    run = True
    while run:

        # fps running
        clock.tick(global_variables.FPS)
        
        #update ticks
        tick = pygame.time.get_ticks()
        delta_time = (tick - last_tick_frame) / 1000
        last_tick_frame = tick
        hold_on_timer -= delta_time
        animation_timer -= delta_time

        #background image

        back_image = pygame.image.load(os.path.join(global_variables.UI_FOLDER,'BackGround Uno Online.png'))
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

        #check for win

        #check if deck needs to be replaced

        if len(deck_shuffle) <= 4:
            for n in range(len(deck_in_game) -1):
                deck_shuffle.append(deck_in_game.pop(0))
            random.shuffle(deck_shuffle)

        #resets the played card
        played_card = None

        #checks if there's a possible play, and then processes an eventual click
        if game_color != 'd':
            if check_for_possible_moves(play_turn,deck_player,deck_cpu,deck_in_game,game_color):
                if play_turn == 'player' and hold_on_timer < 0: #player logic
                    if left_mouse_pressed:
                        for card_player in deck_player:
                            if card_player.is_clicked(deck_in_game,mouse_position,game_color):
                                played_card = card_player

                #CPU Logic            
                elif play_turn == 'cpu' and game_color != 'd' and hold_on_timer < 0:
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
                    played_card = highest_card
        
            else:
                if not draw_cards_sound_played and animation_timer < 0:
                    global_variables.DRAW_CARDS_ANNOUNCER_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.DRAW_CARDS_ANNOUNCER_SOUND.play()
                    latest_animation = "draw cards"
                    animation_timer = global_variables.PAUSE_TIMER
                    draw_cards_sound_played = True
                #player can draw through the function
                draw_card_animation(play_turn,deck_player,mouse_position,left_mouse_pressed,deck_shuffle,SCREEN)
                #cpu drawing cards
                if play_turn == 'cpu' and hold_on_timer < 0:
                    deck_cpu.append(draw_cards(1,deck_shuffle))
                    hold_on_timer = global_variables.PAUSE_TIMER
                    global_variables.DRAWN_CARD_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.DRAWN_CARD_SOUND.play()

        #Card is played logic
        if not played_card == None:
            draw_cards_sound_played = False
            if played_card.type in ['00','01','02','03','04','05','06','07','08','09']:
                if play_turn == 'player':
                    deck_player.remove(played_card)
                    deck_in_game.append(played_card)
                    play_turn = 'cpu'
                else:
                    deck_cpu.remove(played_card)
                    deck_in_game.append(played_card)
                    play_turn = 'player'
                game_color = played_card.color
                hold_on_timer = global_variables.PAUSE_TIMER
            elif played_card.type == '12':
                if play_turn == 'player':
                    deck_player.remove(played_card)
                    deck_in_game.append(played_card)
                    deck_cpu.extend(draw_cards(2,deck_shuffle))
                    play_turn = 'cpu'
                else:
                    deck_cpu.remove(played_card)
                    deck_in_game.append(played_card)
                    deck_player.extend(draw_cards(2,deck_shuffle))
                    play_turn = 'player'
                game_color = played_card.color
                latest_animation = 'draw 2'
                global_variables.DRAW_2_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                global_variables.DRAW_2_SOUND.play()
                animation_timer = global_variables.PAUSE_TIMER
                hold_on_timer = global_variables.PAUSE_TIMER
            elif played_card.type == '13':
                if play_turn == 'player':
                    deck_player.remove(played_card)
                    deck_in_game.append(played_card)
                else:
                    deck_cpu.remove(played_card)
                    deck_in_game.append(played_card)
                game_color = played_card.color
                global_variables.WOW_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                global_variables.WOW_SOUND.play() 
                hold_on_timer = global_variables.PAUSE_TIMER                   
            elif played_card.type == '14':
                if play_turn == 'player':
                    deck_player.remove(played_card)
                    deck_in_game.append(played_card)
                    deck_cpu.extend(draw_cards(4,deck_shuffle))
                else:
                    deck_cpu.remove(played_card)
                    deck_in_game.append(played_card)
                    deck_in_game.extend(draw_cards(4,deck_shuffle))
                game_color = played_card.color
                latest_animation = 'draw 4'
                animation_timer = global_variables.PAUSE_TIMER * 2
                global_variables.DRAW_4_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                global_variables.DRAW_4_SOUND.play()
                hold_on_timer = global_variables.PAUSE_TIMER  * 2
            else: #for the stop and turn signals, which both work the same
                if play_turn == 'player':
                    deck_player.remove(played_card)
                    deck_in_game.append(played_card)
                else:
                    deck_cpu.remove(played_card)
                    deck_in_game.append(played_card)
                game_color = played_card.color
                #differentiate both animations
                if played_card.type == "10":
                    latest_animation = 'skip'
                    global_variables.SKIP_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.SKIP_SOUND.play()
                else:
                    latest_animation = 'reverse'
                    global_variables.REVERSE_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.REVERSE_SOUND.play()
                hold_on_timer = global_variables.PAUSE_TIMER
                animation_timer = global_variables.PAUSE_TIMER
        
            global_variables.PLAYED_CARD_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
            global_variables.PLAYED_CARD_SOUND.play()

        #deal with color chooser

        #system to draw cards (but not all draws are here)

        visible_cards = []
        visible_cards.extend(deck_player)
        visible_cards.extend(deck_cpu)
        visible_cards.append(deck_in_game[-1])

        [card.update_positions(deck_player, deck_cpu,deck_in_game) for card in visible_cards]    
        [ui.update(len(deck_player), len(deck_cpu)) for ui in ui_group]

        #draw

        [ui.draw(SCREEN) for ui in ui_group]
        [cards.draw(SCREEN) for cards in visible_cards]

        #black cards handling

        if game_color == 'd':
            if play_turn == 'player':
                hold_on_timer,play_turn, game_color = show_color_chooser(mouse_position,SCREEN)
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
                latest_animation = 'color chooser cpu'
                animation_timer = global_variables.PAUSE_TIMER
                if hold_on_timer <= 0:
                    num_of_blue_cards = ['b',0]
                    num_of_red_cards = ['r',0]    
                    num_of_yellow_cards = ['y',0]    
                    num_of_green_cards = ['g',0]
                    for card_cpu_2 in deck_cpu:
                        num_of_blue_cards[1] += 1 * (card_cpu_2.color == 'b')     
                        num_of_red_cards[1] += 1 * (card_cpu_2.color == 'r')  
                        num_of_yellow_cards[1] += 1 * (card_cpu_2.color == 'y')  
                        num_of_green_cards[1] += 1 * (card_cpu_2.color == 'g')
                    maximum = max([num_of_blue_cards,num_of_green_cards,num_of_red_cards,num_of_yellow_cards])
                    for variable in [num_of_yellow_cards,num_of_blue_cards,num_of_green_cards,num_of_blue_cards]:
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


        #middle screen animation

        if animation_timer >= 0:
            #draw 4 has some special effects
            if latest_animation == 'draw 4' and play_turn == 'cpu':
                print(animation_timer)
                if animation_timer >= global_variables.PAUSE_TIMER / 2:
                    pop_up_animation(SCREEN,'draw 4')
                else:
                    pop_up_animation(SCREEN,'color chooser cpu')
            else:
                pop_up_animation(SCREEN,latest_animation)

        pygame.display.flip()