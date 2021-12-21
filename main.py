import pygame
import pygame.font
import os
import random

pygame.init()


WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uno")

FPS = 30

GAME_FOLDER = os.path.dirname(__file__)
TEXTURE_FOLDER = os.path.join(GAME_FOLDER,'Textures')
UI_FOLDER = os.path.join(TEXTURE_FOLDER,'UI')
CARDS_FOLDER = os.path.join(TEXTURE_FOLDER,'Cards')

def card_image_handler(id):
    file_name = id[:-1] + '.png'
    return os.path.join(CARDS_FOLDER,file_name)
    




class Card():
    def __init__(self,identifier):

        self.identifier = identifier
        self.color = self.identifier[2]
        self.type = self.identifier[0:2]
        self.instance = self.identifier[3]

        self.image = pygame.image.load(card_image_handler(self.identifier))
        self.image = pygame.transform.scale(self.image,(100,200))
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self,deck_player, deck_cpu):
        if self in deck_player:
            self.rect = self.rect.move_ip(WIDTH/6 + 50,HEIGHT/15)
            print("moving")
    
    def draw(self):
        SCREEN.blit(self.image,self.rect)
        pygame.display.flip()

class UI():
    def __init__(self,position_x,position_y):

        self.image = pygame.image.load(os.path.join(UI_FOLDER,'Score Frame.png'))
        self.size = WIDTH / 15
        self.image = pygame.transform.scale(self.image, (self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position_x,position_y)
        self.font = pygame.font.SysFont('Comic Sans', 45)
        self.font_color = (0,0,0)
        self.font_background = (255,255,255)
        self.text = self.font.render("10", True, self.font_color, self.font_background)
        self.text_rect = self.rect
        self.text_rect = self.text_rect.move(40,30)



    # def update(self ):
    
    def draw(self):
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
global deck_shuffle
deck_shuffle = ALL_CARDS.copy()

def draw_cards(num_to_draw):
    drawn_cards_list = []
    for n in range(num_to_draw):
        drawn_index = random.randrange(len(deck_shuffle))
        drawn_cards_list.append(deck_shuffle[drawn_index])
        del deck_shuffle[drawn_index]
    return drawn_cards_list

global deck_player
global deck_cpu
global deck_in_game
deck_player = draw_cards(7)
deck_cpu = draw_cards(7)
deck_in_game = []

card_not_gotten = True
while card_not_gotten:
    check_index = random.randrange(len(deck_shuffle))
    if deck_shuffle[check_index].identifier[0:2] in ['01','02','03','04','05','06','07','08','09']:
        deck_in_game.append(deck_shuffle[check_index])
        del deck_shuffle[check_index]
        card_not_gotten = False

test_rec_score_upper = UI(WIDTH/6,HEIGHT/15)
test_rec_score_lower = UI(WIDTH/6,HEIGHT  * 0.8)
ui_group = [test_rec_score_upper,test_rec_score_lower]

def main():
    mouse_position = (11111111111111,11111111111111111111) #meaningless value
    clock = pygame.time.Clock()
    run = True
    while run:
        # fps running

        clock.tick(FPS)

        #event listeners

        event_list = pygame.event.get()
        for event in event_list:
            if event.type ==  pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    run = False

        #updates     

        [cards.draw() for cards in ALL_CARDS]

        #draw
        
        SCREEN.fill((255,255,255))

        [ui.draw() for ui in ui_group]
        [cards.draw() for cards in ALL_CARDS]

        pygame.display.flip()

main()

pygame.quit()

if __name__ == "__main__":
    main()