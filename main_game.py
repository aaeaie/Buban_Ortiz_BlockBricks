#BUBAN, SARAH BERNADINE
#ORTIZ, MARLO
#BSCS 1-1

import pygame, sys
from button_class import Button
from game_class import Game
from colors_class import Colors
from sfx import Sfx
import time

pygame.init()

main_theme = pygame.mixer.Sound("Sounds/main.ogg")
main_theme.play(-1)
main_theme.set_volume(0.45)
filepath = 'medium_highscore.txt'

fx = Sfx()
delay = 0.80
mode = 200
ranks = {'Rookie':0,
         'Master':500,
         'Legend': 1500,
         'Maestro': 3000,
         'Virtuoso': 5000,
         'Supreme': 8000}

game_screen = pygame.display.set_mode((1280, 720))

menu_bg = pygame.image.load("assets/menu_bg.jpg")
play_bg = pygame.image.load("assets/play_bg.jpg")


def font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        game_screen.blit(menu_bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font(100).render("BLOCKBRICKS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=font(75), base_color="#d7fcd4", hovering_color="Green")
        
        MODE_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="MODE", font=font(75), base_color="#d7fcd4", hovering_color="Green")
     
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=font(75), base_color="#d7fcd4", hovering_color="red")

        game_screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, MODE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(game_screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_time = time.time()
                main_theme.stop()
                fx.bye()
                while time.time() - start_time < delay:
                    pygame.event.pump()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_theme.stop()
                    fx.click()
                    play()
                if MODE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fx.click()
                    game_mode()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_time = time.time()
                    main_theme.stop()
                    fx.bye()
                    while time.time() - start_time < delay:
                        pygame.event.pump()
                        
                    pygame.quit()
                    sys.exit()


        pygame.display.update()


def play():
    global mode
    highscore = 0
    player_rank = ''
    while True:
        
        with open(filepath, 'r', encoding='utf8') as file:
            score = file.read()
            if len(score) != 0:
                highscore = int(score)
            else:
                highscore = 0


        game_screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Buban_Ortiz BlockBricks")
        

        BACK = Button(image=pygame.image.load("assets/back rect.png"), pos=(230, 570), 
                            text_input="BACK", font=font(40), base_color="#d7fcd4", hovering_color="Green")
        RESET = Button(image=pygame.image.load("assets/reset rect.png"), pos=(235, 470), 
                            text_input="RESET", font=font(40), base_color="#d7fcd4", hovering_color="Green")


        title_font = font(50)
        hs_font = font(40)
        score_surf = title_font.render("SCORE", True, Colors.white)
        next_surf = title_font.render("NEXT", True, Colors.white)
        game_over_surf = title_font.render("GAME OVER", True, Colors.red, "gray")
        highest_score_surf = hs_font.render("HIGHSCORE", True, Colors.white)

        score_box = pygame.Rect(890, 150, 300, 150) 
        next_box = pygame.Rect(958, 415, 170, 180) 
        hs_box = pygame.Rect(88, 150, 300, 150) 

        speed = pygame.time.Clock()

        game = Game()

        GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(GAME_UPDATE, mode)

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    start_time = time.time()
                    game.stop_bgm()
                    fx.bye()
                    while time.time() - start_time < delay:
                        pygame.event.pump()
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT and game.game_over == False:
                        game.move_left()
                    if e.key == pygame.K_RIGHT and game.game_over == False:
                        game.move_right()
                    if e.key == pygame.K_DOWN and game.game_over == False:
                        game.move_down()
                        game.score_upd(0, 1)
                    if e.key == pygame.K_UP and game.game_over == False:
                        game.rotate()
                if e.type == GAME_UPDATE and game.game_over == False:
                    game.move_down()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.checkForInput(PLAY_MOUSE_POS):
                        fx.click()
                        game.stop_bgm()
                        main_theme.play(-1)
                        main_menu()
                    if RESET.checkForInput(PLAY_MOUSE_POS):
                        game.game_over = False
                        fx.click()
                        game.new_game()

            
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            game_screen.blit(play_bg, (0, 0))
            BACK.changeColor(PLAY_MOUSE_POS)
            BACK.update(game_screen)
            RESET.changeColor(PLAY_MOUSE_POS)
            RESET.update(game_screen)

            if int(highscore) > game.score:
                highscore_value= title_font.render(str(highscore), True, Colors.white)
            else:
                highscore_value= title_font.render(str(game.score), True, Colors.white)
            
            score_value_surface = title_font.render(str(game.score), True, Colors.white)

            for rank, rank_value in ranks.items():
                if game.score >= rank_value:
                    player_rank = rank
                    if player_rank == 'Rookie':
                        x = 90
                    elif player_rank == 'Master':
                        x = 90
                    elif player_rank == 'Legend':
                        x = 86
                    elif player_rank == 'Maestro':
                        x = 64
                    elif player_rank == 'Virtuoso':
                        x = 45
                    else:
                        x = 68
                
            rank_value = title_font.render(player_rank, True, Colors.white)
            game_screen.blit(rank_value, (x, 345, 50, 50))
            
            game_screen.blit(score_surf, (915, 73, 50, 50)) 
            game_screen.blit(next_surf, (950, 335, 50, 50))
            game_screen.blit(highest_score_surf, (60, 80, 50,50))


            pygame.draw.rect(game_screen, Colors.light_blue, score_box, 0, 10)
            game_screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_box.centerx, centery = score_box.centery))
            pygame.draw.rect(game_screen, Colors.light_blue, next_box, 0, 10)
            game.draw(game_screen)
            pygame.draw.rect(game_screen, Colors.light_blue, hs_box, 0, 10)
            game_screen.blit(highscore_value, highscore_value.get_rect(centerx = hs_box.centerx, centery = hs_box.centery))

            if game.game_over == True:
                with open(filepath, 'r+', encoding='utf8') as file:
                    score = file.read()
                    if score:
                        int_score = int(score)
                        if game.score > int_score:
                            file.seek(0)
                            file.write(str(game.score))
                            highscore = str(game.score)
                            
                    else:
                        file.write(str(game.score))
                        highscore = str(game.score)

                game_screen.blit(game_over_surf, (410, 640, 50, 50)) 
            pygame.display.update()
            speed.tick(60)
    
def game_mode():
    global mode
    global filepath

    gamemode_screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Select Difficulty")

    EASY = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(650, 200), 
                            text_input="EASY", font=font(50), base_color="#d7fcd4", hovering_color="yellow")
    MEDIUM = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(650, 350), 
                            text_input="MEDIUM", font=font(50), base_color="#d7fcd4", hovering_color="orange")
    HARD = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(650, 500), 
                            text_input="HARD", font=font(50), base_color="#d7fcd4", hovering_color="red")
    
    while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    start_time = time.time()
                    main_theme.stop()
                    fx.bye()
                    while time.time() - start_time < delay:
                        pygame.event.pump()
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                        if EASY.checkForInput(PLAY_MOUSE_POS):
                            mode = 400
                            filepath = 'easy_highscore.txt'
                            fx.set_mode()
                            main_menu()
                            
                        if MEDIUM.checkForInput(PLAY_MOUSE_POS):
                            mode = 200
                            filepath = 'medium_highscore.txt'
                            fx.set_mode()
                            main_menu()
                            
                        if HARD.checkForInput(PLAY_MOUSE_POS):
                            mode = 100
                            filepath = 'hard_highscore.txt'
                            fx.set_mode()
                            main_menu()
            
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            gamemode_screen.blit(menu_bg, (0, 0))
            EASY.changeColor(PLAY_MOUSE_POS)
            EASY.update(gamemode_screen)
            MEDIUM.changeColor(PLAY_MOUSE_POS)
            MEDIUM.update(gamemode_screen)
            HARD.changeColor(PLAY_MOUSE_POS)
            HARD.update(gamemode_screen)
           
        
            pygame.display.update()
            
main_menu()