import pygame
import time
import random

pygame.init()

crashsound=pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("speed.mp3")
#ssound=pygame.mixer.Sound("scr.wav")

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)

bright_red=(200,0,0)
red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue=(0,0,225)

car_width = 53


pause=False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Barrier Racing')
clock = pygame.time.Clock()
road=pygame.image.load('1.jpg')
carImg = pygame.image.load('red.png')
carr = pygame.image.load('redr.png')
carl = pygame.image.load('redl.png')
treeimg=pygame.image.load('tree.png')
treeimg2=pygame.image.load('tree2.png')
bg= pygame.image.load('bg.png')
bg1= pygame.image.load('bg.jpg')

roadimg=pygame.image.load('r.png')

truckimg=pygame.image.load('truck.png')
carImg2=pygame.image.load('red32.png')
pygame.display.set_icon(carImg2)

def things_dodged(count) :
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things( thingx, thingy):
    gameDisplay.blit(truckimg,(thingx,thingy))

def tree(treey):
    gameDisplay.blit(treeimg,(1,treey))
def tree2(treey):
    gameDisplay.blit(treeimg2,(705,treey))

def car(x,y,l,r):
    if r==1:
        gameDisplay.blit(carr,(x,y))
    elif l==1:
        gameDisplay.blit(carl,(x,y))
    else:
        gameDisplay.blit(carImg,(x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def quitgame():
    pygame.quit()
    quit()
    

def crash():
    
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crashsound)
        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("You Crashed :(", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()


            button("Again",150,450,100,50,bright_green,green,game_loop)
            button("Quit",550,450,100,50,red,bright_red,quitgame)
            
            pygame.display.update()
            clock.tick(60)

def button(msg,x,y,w,h,ic,ac,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        #print(click)

        if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
            if click[0] == 1 and action!=None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        smallText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects(msg, smallText)
        TextRect.center = ((x+(w/2)),(y+(h/2)))
        gameDisplay.blit(TextSurf, TextRect)

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False

def paused():
    pygame.mixer.music.pause()    
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)



        button("Continue",150,450,100,50,bright_green,green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(60)


def gameintro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Barrier Racing", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


        button("GO!",150,450,100,50,bright_green,green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

        
def game_loop():
    global pause
    chk=False
    pygame.mixer.music.play(-1)
    
    x=(display_width * 0.45)
    y=(display_height*0.79)
    l=0
    r=0
    x_change = 0

    thing_startx = random.randrange(100, display_width-201)
    thing_starty = -1500
    tree_y=-900
    tree_y2=-1000

    
    tree_speed=8
    thing_speed = random.randrange(10,12)
    thing_width = 100
    thing_height = 240
    dodged=0
    
    gameExit=False
    #gameDisplay.blit(road,(0,0))

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -12
                 #   pygame.mixer.Sound.play(ssound)
                    l=1
                if event.key == pygame.K_RIGHT:
                    x_change = 12
                    r=1
                  #  pygame.mixer.Sound.play(ssound)
                if event.key == pygame.K_p:
                    pause=True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change=0
                    l=0
                    r=0

        x+=x_change

        
        gameDisplay.fill((105,105,105))
        gameDisplay.blit(bg,(-1,0))
        gameDisplay.blit(bg,(700,0))
        #gameDisplay.blit(roadimg,(100,0))
        #pygame.draw.rect(gameDisplay,(0,164,0),(0,0,98,600))
        pygame.draw.line(gameDisplay,black,(94,0),(94,600),15)
        pygame.draw.line(gameDisplay,black,(706,0),(706,600),15)        

        tree(tree_y)
        tree_y+=tree_speed
        tree2(tree_y2)
        tree_y2+=tree_speed
        
        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        car(x,y,l,r)
        things_dodged(dodged)


        
        if x>display_width-98 - car_width or x < 98:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(100,700-thing_width)
            dodged+=1
            thing_speed+=0.4

        if tree_y>display_height:
            tree_y=-1600
            tree(tree_y)
            tree_speed+=0.7

        if tree_y2>display_height:
            tree_y2=-1700
            tree2(tree_y2)
            
        
        if y+2<thing_starty+thing_height:
            #print("Y Crossover")

            if x>thing_startx and x< thing_startx+thing_width or x+car_width > thing_startx and x+ car_width < thing_startx+thing_width:
                #print("X Crossover")
                crash()


        pygame.display.update()
        clock.tick(70)
gameintro()
game_loop()
pygame.quit()
quit()
