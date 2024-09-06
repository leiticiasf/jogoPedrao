#Setup de Entrada - Import Bibliotecas-----------------------------------------#
import pygame, sys

from pygame import mixer
#Setup de Entrada - Definições ----------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('jogo do pedrao :)')
screen = pygame.display.set_mode((800, 600),0,32)

mixer.music.load('musiga.mp3') 
mixer.music.set_volume(0.5)
mixer.music.play(-1)

font = pygame.font.SysFont(None, 30)
font1 = pygame.font.SysFont(None, 45)

#Definição de Escrita de Texto-------------------------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#Definição de ações do Menu Inicial--------------------------------------------#
def main_menu():
    while True:

        tela = pygame.image.load('fundo.png')
        screen.blit(tela,(0,0))
        draw_text('Menu Principal', font1, (101,70,54), screen, 290, 40)


        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)
        button_4 = pygame.Rect(300, 500, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                volume()
        if button_4.collidepoint((mx, my)):
            if click:
                exite()
        pygame.draw.rect(screen, (251,201,13), button_1)
        pygame.draw.rect(screen, (251,201,13), button_2)
        pygame.draw.rect(screen, (251,201,13), button_3)
        pygame.draw.rect(screen, (201,49,43), button_4)
        draw_text('Jogar', font, (101,70,54), screen, 372, 215)
        draw_text('Opções', font, (101,70,54), screen, 363, 315)
        draw_text('Volume', font, (101,70,54), screen, 368, 415)
        draw_text('Sair', font, (244,240,232), screen, 385, 515)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
        
#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def game():
    import main

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Olá', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def volume():
    running = True
    
    while running:
        screen.fill((0,0,0))
        volume = 0.5  # Volume inicial
        draw_text('Opções', font, (255, 255, 255), screen, 20, 20)
        draw_text('Volume: {int(volume * 100)}%', font, (255, 255, 255), screen, 20, 60)
        
        for event in pygame.event.get():
        
        # Aumenta o volume
            if event.type == KEYDOWN:
                    if event.key == K_UP:
                        volume = min(1.0, volume + 0.1)  # Aumenta o volume em 10%
                        pygame.mixer.music.set_volume(volume)
        
        # Diminui o volume
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    volume = max(0.0, volume - 0.1)  # Diminui o volume em 10%
                    pygame.mixer.music.set_volume(volume)

  
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

def exite():
    pygame.quit()
    sys.exit()

           
main_menu()