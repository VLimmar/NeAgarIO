import pygame
from setting import *
from sprite import *
from data_use import *
import random
import pygame.freetype
pygame.init()

def gamemenu():
    window.fill(MENCOLOR)
    startbutton.draw(window)
    exitbutton.draw(window)
    text = pygame.freetype.Font("new_zelek.ttf", 32)
    toplist = top(3)
    ytop = 180
    for temp in toplist:
            text.render_to(window, (100, ytop), F"{temp[1]} - {temp[0]}")
            ytop += 30

def enemystart():
    spawn = random.randint(0, 3)
    a = player.rect.width
    enemy = Enemy(random.randint(a - 10, a + 15), spawn, (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150)))
    if len(enemylist) <= ENEMYCOUNT:
        enemylist.append(enemy)

def fastfood():
    spawn = (random.randint(0, SCREENX), random.randint(0, SCREENY))
    food = Food(spawn)
    if len(foodlist) <= FOODCOUNT:
        foodlist.append(food)
def eat():
    for temp in enemylist:
        if player.rect.colliderect(temp.rect):
            if player.rect.width >= temp.size:
                enemylist.remove(temp)
                player.rect.width += 2
                player.rect.height += 2
            else:
                return 1
            if player.record < player.rect.width:
                setsave(PLAYERNAME, player.rect.width)
                player.record = player.rect.width

def restart():
    gamemode = 1
    player.rect.center = (SCREENX / 2, SCREENY / 2)
    player.rect.width = player.size
    player.rect.height = player.size
    foodlist.clear()
    enemylist.clear()
    return gamemode

def enemydraw(window):
    for temp in enemylist:
        temp.draw(window)
        temp.update()

def enemres():
    for temp in enemylist:
        if temp.collidewall() is True:
            enemylist.remove(temp)

def nofood():
    for temp in foodlist:
        if player.rect.colliderect(temp.rect):
            foodlist.remove(temp)
            player.rect.width += 1
            player.rect.height += 1


def foodraw(window):
    for temp in foodlist:
        temp.draw(window)


buttonpng = pygame.image.load("buttonGreen.png")
window = pygame.display.set_mode((SCREENX, SCREENY))
clock = pygame.time.Clock() 
whil = 0
player = Player((SCREENX / 2, SCREENY / 2))
enemylist = []
foodlist = []
font = pygame.freetype.Font("new_zelek.ttf", 24)
startbutton = Button(buttonpng, (SCREENX / 2, SCREENY / 2), font, "START")
exitbutton = Button(buttonpng, (SCREENX / 2, SCREENY / 2 + 90), font, "EXIT GAME")
gamemode = 1
while whil != 1:
    do = pygame.event.get()
    for temp in do:
        if temp.type == pygame.QUIT:
            whil = 1
        if temp.type == pygame.KEYDOWN:
            if temp.key == pygame.K_x:
                gamemode = restart()
        if temp.type == pygame.MOUSEBUTTONDOWN:
            if startbutton.rect.collidepoint(temp.pos) is True:
                plus = pygame.time.get_ticks() // 1000
                gamemode = 0
            if exitbutton.rect.collidepoint(temp.pos) is True:
                whil = 1


   
    window.fill((240, 240, 240))
    if gamemode == 0:
        player.draw(window)
        player.update()
        enemystart()
        enemres()
        enemydraw(window)
        fastfood()
        foodraw(window)
        nofood()
        if eat() == 1:
            gamemode = 1
    if gamemode == 1:
        gamemenu()
    # print(enemylist)
    pygame.display.update()
    clock.tick(FPS)

