import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random as rd

pg.init()
VINDU_BREDDE = 600
VINDU_HOYDE  = 600
vindu=pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])

font = pg.font.SysFont("Arial", 24)

class Objekt:
    def __init__(self,typeObjekt,xpos,ypos,farge,vindu):
        self.typeObjekt=typeObjekt
        self.xpos=xpos
        self.ypos=ypos
        self.farge=farge
        self.vindu=vindu
        self.lengde=20
        self.bredde=20

    def tegn(self):
        pg.draw.rect(self.vindu,self.farge,(self.xpos,self.ypos,self.lengde,self.bredde))

class Spiller(Objekt):
    def __init__(self,typeObjekt,xpos,ypos,farge,vindu):
        super().__init__(typeObjekt,xpos,ypos,farge,vindu)
        self.fart=0.1
        self.xFart=0.1
        self.yFart=0
        self.poeng=0

    def flytt(self,taster):
        self.xpos+=self.xFart# slik at den ebeveger seg hele tiden
        self.ypos+=self.yFart
        """Metode for å flytte spilleren utifra tastene, farten øker med antall poeng trollet har"""
        if taster[K_UP]:
            self.xFart=0
            self.yFart=-(self.poeng+1)*self.fart
        if taster[K_DOWN]:
            self.xFart=0
            self.yFart=(self.poeng+1)*self.fart
        if taster[K_LEFT]:
            self.xFart=-(self.poeng+1)*self.fart
            self.yFart=0
        if taster[K_RIGHT]:
            self.xFart=(self.poeng+1)*self.fart
            self.yFart=0
        #stopper spillet om spilleren går utenfor skjermen
        if (self.xpos+self.lengde/2)>VINDU_BREDDE or (self.xpos-self.lengde/2)<0:
            pg.quit()
        if self.ypos>VINDU_HOYDE or self.ypos<0:
            pg.quit()


spillObjekter=[]

troll=Spiller("Troll",300,300,(0,255,0),vindu)
spillObjekter.append(troll)
antallObjekter=len(spillObjekter)

#lager matbitene og passer på at de aldri ligger oppå hverandre
while antallObjekter<=3:
    mat=Objekt("Mat",rd.randint(0,580),rd.randint(0,580),(255,255,0),vindu)
    spillObjekter.append(mat)

    for i in spillObjekter:#passer på at mat ikke generes oppå gammel mat eller troll
        for j in spillObjekter:
            if j!=i:
                usynligJ=pg.draw.rect(vindu,(255,255,255),(j.xpos,j.ypos,j.lengde,j.bredde))
                usynligI=pg.draw.rect(vindu,(255,255,255),(i.xpos,i.ypos,i.lengde,i.bredde))
                if usynligJ.colliderect(usynligI):#sjekker om de kolliderer
                    if j.typeObjekt=="Mat":
                        spillObjekter.remove(j)
                    elif i.typeObjekt=="Mat":
                        spillObjekter.remove(i)
    antallObjekter=len(spillObjekter)
hinderListe=[]
hinderListe.append(troll)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen lyseblå
    vindu.fill((0,0,0))
    #flytter trollet og skirver poengsum
    troll.flytt(trykkede_taster)
    poengsum = font.render(str(troll.poeng), True, (255, 255, 255))
    vindu.blit(poengsum, (50, 20))

    for i in spillObjekter:
        i.tegn()

        for j in spillObjekter:#sjekker for kollisjon mellom mat og troll
            if j!=i:
                usynligJ=pg.Rect(j.xpos,j.ypos,j.lengde,j.bredde)
                usynligI=pg.Rect(i.xpos,i.ypos,i.lengde,i.bredde)
                if usynligJ.colliderect(usynligI):
                    if j.typeObjekt=="Mat" and i.typeObjekt=="Troll":
                        troll.poeng+=1#legger til poeng om den spiser
                        hinder=Objekt("Hinder",j.xpos,j.ypos,(155,155,155),vindu)#lager et hinder der maten blir spist
                        hinderListe.append(hinder)
                        spillObjekter.remove(j)
                        antallObjekter=len(spillObjekter)

        while antallObjekter<=3:#legger til en ny matbit etter en blir spist
            mat=Objekt("Mat",rd.randint(0,580),rd.randint(0,580),(255,255,0),vindu)
            spillObjekter.append(mat)

            for k in spillObjekter:#passer på at det nye objektet ikke kolliderer med et eksisterende
                for l in spillObjekter:
                    if l!=k:
                        usynligJ=pg.draw.rect(vindu,(255,255,255),(l.xpos,l.ypos,l.lengde,l.bredde))
                        usynligI=pg.draw.rect(vindu,(255,255,255),(k.xpos,k.ypos,k.lengde,k.bredde))
                        if usynligJ.colliderect(usynligI):
                            if l.typeObjekt=="Mat":
                                spillObjekter.remove(l)
                            elif k.typeObjekt=="Mat":
                                spillObjekter.remove(k)
                        antallObjekter=len(spillObjekter)

    for i in hinderListe:#løkke for å sjekke om troll og hinder kolliderer
        if i.typeObjekt!="Troll":#Slik at trollet ikke tegnes 2 ganger
            i.tegn()
        #her prøvde jeg å lage noe som gjorde at spillet gikk over da tollet og hinderet kolliderte, men jeg fikk ikke til at det skulle ta litt tid før hinderet blir 'dødelig'
        '''for j in hinderListe:#sjekker om kollisjon mellom hinder og troll.
            if j!=i:
                usynligJ=pg.Rect(j.xpos,j.ypos,j.lengde,j.bredde)
                usynligI=pg.Rect(i.xpos,i.ypos,i.lengde,i.bredde)
                if usynligJ.colliderect(usynligI):
                    pg.quit()'''




    pg.display.flip()
# Avslutter pygame
pg.quit()
