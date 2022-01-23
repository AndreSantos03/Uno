import json
import pygame
import global_variables
from pygame.constants import MOUSEBUTTONDOWN

#set up all the buttons

main_uno_font = pygame.font.Font(global_variables.RETRO_FONT, int(global_variables.WIDTH/9.6), bold=True)
buttons_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/38.4))
font_color = (255,255,255)
uno_img = main_uno_font.render('UNO', True,font_color)
uno_rect = uno_img.get_rect(center=(int(global_variables.WIDTH/2), int(global_variables.HEIGHT / 2.5)))
play_img = buttons_font.render('PLAY',True,font_color)
play_rect = play_img.get_rect(center=(int(global_variables.WIDTH/2), int(global_variables.HEIGHT / 1.45)))
settings_img = buttons_font.render('SETTINGS',True,font_color)
settings_rect = settings_img.get_rect(center=(int(global_variables.WIDTH/2), int(global_variables.HEIGHT / 1.45 + global_variables.HEIGHT / 10)))
quit_img = buttons_font.render('QUIT',True,font_color)
quit_rect = quit_img.get_rect(center=(int(global_variables.WIDTH/2), int(global_variables.HEIGHT / 1.45 + global_variables.HEIGHT / 10 * 2)))
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
right_arrow_rect_3 = right_arrow.get_rect(center=(int(global_variables.WIDTH / 3 + global_variables.WIDTH / 6),int(global_variables.HEIGHT / 4 + global_variables.HEIGHT / 14 * 3)))

#close sign
x_font = pygame.font.Font(global_variables.RETRO_FONT,int(global_variables.WIDTH/38.4))
close_img = x_font.render('X',True,(255,255,255))
close_rect = close_img.get_rect(center=(int(global_variables.WIDTH/7),int(global_variables.HEIGHT/6.4)))

#to chane the fps
fps_changes = [30,45,60,90,120,144]

def loading_image(screen):

    loading_font = pygame.font.Font(global_variables.RETRO_FONT, 100, bold=True)
    background_surface = pygame.Surface((global_variables.WIDTH,global_variables.HEIGHT))
    background_surface.set_alpha(128)
    background_surface.fill((0,0,0))
    loading_image = loading_font.render('Loading...',True,(255,255,255))
    loading_rect = loading_image.get_rect(center=(int(global_variables.WIDTH/2),int(global_variables.HEIGHT/2)))
    screen.blit(background_surface,(0,0))
    screen.blit(loading_image,loading_rect)
    
    pygame.display.flip()

def beggining_menu():
    SCREEN = pygame.display.set_mode((global_variables.WIDTH , global_variables.HEIGHT))

    pygame.display.set_caption("Uno")

    background_image = global_variables.BACKGROUND_IMAGE
    background_image = pygame.transform.scale(background_image,(global_variables.WIDTH ,global_variables.HEIGHT))
    background_image_rect = background_image.get_rect()

    #update values from json
    m_volume_value_img = options_font.render("{}".format(int(global_variables.MUSIC_VOLUME * 100)),True,(255,255,255))
    effects_volume_value_img = options_font.render("{}".format(int(global_variables.EFFECTS_VOLUME * 100)),True,(255,255,255))
    fps_value_image = options_font.render("{}".format(global_variables.FPS),True,(255,255,255))

    mouse_position = (111111,11111111) #meaningless value
    run = True
    menu_up = False

    clock = pygame.time.Clock()


    while run:

        #FPS clock

        clock.tick(global_variables.FPS)

        #background
        SCREEN.blit(background_image,background_image_rect)

        #event listeners
        left_mouse_pressed = False
        event_list = pygame.event.get()
        for event in event_list:
            if event.type ==  pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_up = not menu_up
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                left_mouse_pressed = True

        
        #updates

            #click handleer
            mouse_position = pygame.mouse.get_pos()
            if left_mouse_pressed:
                menu_sound = False
                global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                if quit_rect.collidepoint(mouse_position) and not menu_up:
                    global_variables.MENU_SOUND.play()
                    menu_sound = True
                    return False
                elif settings_rect.collidepoint(mouse_position) and not menu_up:
                    global_variables.MENU_SOUND.play()
                    menu_up = True
                    menu_sound = True
                elif play_rect.collidepoint(mouse_position) and not menu_up:
                    global_variables.MENU_SOUND.play()
                    loading_image(SCREEN)
                    menu_sound = True
                    return True
                if menu_up:
                    if left_arrow_rect_1.collidepoint(mouse_position) and global_variables.MUSIC_VOLUME > 0:
                        global_variables.MUSIC_VOLUME = round(global_variables.MUSIC_VOLUME - 0.1,1)
                        global_variables.JSON_DATA['music_volume'] = global_variables.MUSIC_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        pygame.mixer.music.set_volume(global_variables.MUSIC_VOLUME)
                        menu_sound = True
                    elif right_arrow_rect_1.collidepoint(mouse_position) and global_variables.MUSIC_VOLUME < 1:
                        global_variables.MUSIC_VOLUME = round(global_variables.MUSIC_VOLUME + 0.1,1)
                        global_variables.JSON_DATA['music_volume'] = global_variables.MUSIC_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        pygame.mixer.music.set_volume(global_variables.MUSIC_VOLUME)
                        menu_sound = True
                    elif left_arrow_rect_2.collidepoint(mouse_position) and global_variables.EFFECTS_VOLUME > 0:
                        global_variables.EFFECTS_VOLUME = round(global_variables.EFFECTS_VOLUME - 0.1,1)
                        global_variables.JSON_DATA['effects_volume'] = global_variables.EFFECTS_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        menu_sound = True
                    elif right_arrow_rect_2.collidepoint(mouse_position) and global_variables.EFFECTS_VOLUME < 1:
                        global_variables.EFFECTS_VOLUME = round(global_variables.EFFECTS_VOLUME + 0.1,1)
                        global_variables.JSON_DATA['effects_volume'] = global_variables.EFFECTS_VOLUME
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        menu_sound = True
                    elif left_arrow_rect_3.collidepoint(mouse_position) and global_variables.FPS > 30:
                        index_fps = fps_changes.index(global_variables.FPS)
                        global_variables.FPS = fps_changes[index_fps - 1]
                        global_variables.JSON_DATA['fps'] = global_variables.FPS
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        menu_sound = True
                    elif right_arrow_rect_3.collidepoint(mouse_position) and global_variables.FPS < 144:
                        index_fps = fps_changes.index(global_variables.FPS)
                        global_variables.FPS = fps_changes[index_fps + 1]
                        global_variables.JSON_DATA['fps'] = global_variables.FPS
                        with open(global_variables.SETTINGS,'w') as dump_json:
                            json.dump(global_variables.JSON_DATA,dump_json)
                        menu_sound = True
                    elif close_rect.collidepoint(mouse_position):
                        menu_up = False
                        menu_sound = True
                else:
                    global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    if quit_rect.collidepoint(mouse_position) and not menu_up:
                        menu_sound = True
                        global_variables.MENU_SOUND.play()
                        return 0
                    elif settings_rect.collidepoint(mouse_position) and not menu_up:
                        global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        menu_up = True
                        menu_sound = True
                    elif play_rect.collidepoint(mouse_position) and not menu_up:
                        global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                        global_variables.MENU_SOUND.play()
                        loading_image(SCREEN)
                        return 1

                #update values
                m_volume_value_img = options_font.render("{}".format(int(global_variables.MUSIC_VOLUME * 100)),True,(255,255,255))
                effects_volume_value_img = options_font.render("{}".format(int(global_variables.EFFECTS_VOLUME * 100)),True,(255,255,255))
                fps_value_image = options_font.render("{}".format(global_variables.FPS),True,(255,255,255))
                               
                if menu_sound: 
                    global_variables.MENU_SOUND.set_volume(global_variables.EFFECTS_VOLUME)
                    global_variables.MENU_SOUND.play()
        #draw all the visual part

        #Buttons

        SCREEN.blit(uno_img,uno_rect)
        SCREEN.blit(play_img,play_rect)
        SCREEN.blit(settings_img,settings_rect)
        SCREEN.blit(quit_img,quit_rect)
        
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
            
        pygame.display.flip()
