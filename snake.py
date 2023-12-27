import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random as rd

pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE  = 600
vindu=pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])

font = pg.font.SysFont("Arial", 24)

class Spillobjekt:
    def __init__(self, xPos, yPos, farge):
        self.vindu = vindu
        self.xPos = xPos
        self.yPos = yPos
        self.farge = farge
    
    def tegnObjekt(self):
        pg.draw.rect(self.vindu,self.farge,(self.xPos,self.yPos,20,20))

class Slange(Spillobjekt):
    def __init__(self, xPos, yPos, farge):
        super().__init__(xPos,yPos,farge)
        self.fart = 0.05
        self.xFart = 0
        self.yFart = 0
    
    def flytt(self,taster):
        if taster[K_UP]:
            self.yFart = -self.fart
            self.xFart = 0
        elif taster[K_DOWN]:
            self.yFart = self.fart
            self.xFart = 0
        elif taster[K_RIGHT]:
            self.xFart = self.fart
            self.yFart = 0
        elif taster[K_LEFT]:
            self.xFart = -self.fart
            self.yFart = 0
        self.xPos += self.xFart
        self.yPos += self.yFart 
        self.tegnObjekt()

slange = Slange(300,300, (255,255,0))

fortsett = True
while fortsett:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    trykkedeTaster = pg.key.get_pressed()

    vindu.fill((0,0,0))

    slange.flytt(trykkedeTaster)

    tittel = font.render("Snake", True, (255, 255, 255))
    vindu.blit(tittel, (20,20))
    pg.display.flip()
