import pygame
from setting import *
import random
from data_use import *

class Player:
    def __init__(self, coords) -> None:
        self.coords = coords
        self.size = 40
        self.rect = pygame.rect.Rect(coords,(self.size, self.size))
        self.record = getinfo(PLAYERNAME)
    def draw(self, window):
        pygame.draw.ellipse(window, PLAYERCOLOR, self.rect)
    def update(self):
        ncord = pygame.mouse.get_pos()
        self.rect.center = ncord
class Enemy:
    def __init__(self, size, spawn, color) -> None:
        self.size = size
        self.color = color
        if spawn == 0:
            coords = (-NOSCREEN, random.randint(0, SCREENY))
            self.speedx = random.randint(1, 10)
            self.speedy = random.randint(-10, 10)
        if spawn == 1:
            coords = (SCREENX + NOSCREEN, random.randint(0, SCREENY))
            self.speedx = -random.randint(1, 10)
            self.speedy = random.randint(-10, 10)
        if spawn == 2:
            coords = (random.randint(0, SCREENX), -NOSCREEN)
            self.speedy = random.randint(1, 10)
            self.speedx = random.randint(-10, 10)
        if spawn == 3:
            coords = (random.randint(0, SCREENX), SCREENY + NOSCREEN)
            self.speedy = -random.randint(1, 10)
            self.speedx = random.randint(-10, 10)
        self.coords = coords
        self.rect = pygame.rect.Rect(coords, (self.size, self.size))
    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.rect)
    def update(self):
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        self.collidewall()
    def collidewall(self):
        if self.rect.centerx >= SCREENX + 100 or self.rect.centerx <= -100 or self.rect.centery >= SCREENY + 100 or self.rect.centery <= -100:
            return True
        else:
            return False

class Food:
    def __init__(self, spawn) -> None:
        self.rect = pygame.rect.Rect(spawn, (7,7))
    
    def draw(self, window):
        pygame.draw.rect(window, (108, 0, 1), self.rect)

class Button:
    def __init__(self, pict, spawn, font, text) -> None:
        self.pict = pict
        self.rect = self.pict.get_rect()
        self.font = font
        self.text = text
        self.cout = self.font.render(self.text)
        self.rect.center = spawn
        self.cout[1].center = spawn
    def draw(self, face):
        face.blit(self.pict, self.rect)
        face.blit(self.cout[0], self.cout[1])