import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random as rd

pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE  = 600
vindu=pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])

font = pg.font.SysFont("Arial", 24)

class Spillobjekt:
    def __init__(self, xPos, yPos, farge, hoyde, bredde):
        self.vindu = vindu
        self.xPos = xPos
        self.yPos = yPos
        self.farge = farge
        self.hoyde = hoyde
        self.bredde = bredde
    
    def tegnObjekt(self):
        pg.draw.rect(self.vindu,self.farge,(self.xPos,self.yPos,self.bredde,self.hoyde))
    
    def getRect(self):
        return pg.Rect(self.xPos,self.yPos,self.bredde,self.hoyde)

class Slange(Spillobjekt):
    def __init__(self, xPos, yPos, farge, hoyde, bredde):
        super().__init__(xPos,yPos,farge, hoyde, bredde)
        self.fart = 0.05
        self.xFart = 0
        self.yFart = 0
        self.length = 1
        self.hoyde = hoyde
        self.bredde = bredde
    
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

class Mat(Spillobjekt):
    def __init__(self, xPos, yPos, farge, hoyde, bredde):
        super().__init__(xPos, yPos, farge, hoyde, bredde)
        self.xPos = xPos
        self.yPos = yPos
        self.hoyde = hoyde
        self.bredde = bredde

slange = Slange(300,300, (255,255,0),20,20)
mat = Mat(rd.randint(0,580),rd.randint(0,580),(255,0,0),20,20)

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    trykkedeTaster = pg.key.get_pressed()

    vindu.fill((0,0,0))

    slange.flytt(trykkedeTaster)
    mat.tegnObjekt()

    tittel = font.render("Snake: "+ str(slange.length-1), True, (255, 255, 255))
    vindu.blit(tittel, (20,20))
    pg.display.flip()
