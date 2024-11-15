import pygame,sys
import time,random

diff=25   #range 10-120
xx=720
yy=480
pygame.init()

pygame.display.set_caption("Monty's Hungry Python")
window=pygame.display.set_mode((xx,yy))

fps_controller=pygame.time.Clock()

snakepos=[100,50]
snakebody=[[100,50],[100-10,50],[100-(2*10),50]]

foodpos=[random.randrange(1,(xx//10))*10,random.randrange(1,(yy//10))*10]
foodspawn=True

direction='RIGHT'
changeto=direction

score=0

def gameover():
    font=pygame.font.SysFont('times new roman',90)
    gosurface=font.render('GAME OVER',True,pygame.Color(255,0,0))
    gorect=gosurface.get_rect()
    gorect.midtop=(xx/2,yy/4)
    window.fill(pygame.Color(0,0,0))
    window.blit(gosurface,gorect)
    show_score(0,pygame.Color(255,0,0),'times',20)
    pygame.display.flip()
    time.sleep(3)
    sys.exit()

def show_score(choice,color,font,size):
    sfont=pygame.font.SysFont(font,size)
    ssurface=sfont.render('Score:' +str(score),True,color)
    srect=ssurface.get_rect()
    if choice==1:
        srect.midtop=(xx/10,15)
    else:
        srect.midtop=(xx/2,yy/1.25)
    window.blit(ssurface,srect)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP or event.key==ord('w'):
                changeto='UP'
            if event.key==pygame.K_DOWN or event.key==ord('s'):
                changeto='DOWN'
            if event.key==pygame.K_LEFT or event.key==ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeto='RIGHT'

            #ESC KEY....IS ESCAPE
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changeto=='UP' and direction!='DOWN':
        direction='UP'
    if changeto=='DOWN' and direction!='UP':
        direction='DOWN'
    if changeto=='LEFT' and direction!='RIGHT':
        direction='LEFT'
    if changeto=='RIGHT' and direction!='LEFT':
        direction='RIGHT'

    if direction=='UP': #movement of snake
        snakepos[1]-=10
    if direction=='DOWN':
        snakepos[1]+=10
    if direction=='LEFT':
        snakepos[0]-=10
    if direction=='RIGHT':
        snakepos[0]+=10

    snakebody.insert(0,list(snakepos))     #snake growth
    if snakepos[0]==foodpos[0] and snakepos[1]==foodpos[1]:
        score+=1
        foodspawn=False
    else:
        snakebody.pop()


    #FOOD DISPLAY
    if not foodspawn:
        foodpos=[random.randrange(1,(xx//10))*10,random.randrange(1,(yy//10))*10]
    foodspawn=True


    #display colors
    window.fill(pygame.Color(0,0,0))
    for pos in snakebody:
        pygame.draw.rect(window,pygame.Color(0,255,0),pygame.Rect(pos[0],pos[1],10,10))


    #food
    pygame.draw.rect(window,pygame.Color(255,255,255),pygame.Rect(foodpos[0],foodpos[1],10,10))
    show_score(1,pygame.Color(255,255,255),'consolas',20)
    pygame.display.update()
    fps_controller.tick(diff)
    
    


  #Game over conditions
    #Border out
    if snakepos[0]<0 or snakepos[0]>xx-10:
        gameover()
    if snakepos[1]<0 or snakepos[1]>yy-10:
        gameover()
    #body hit
    for block in snakebody[1:]:
        if snakepos[0]==block[0] and snakepos[1]==block[1]:
            gameover()

show_score(1,pygame.Color(255,255,255),'consolas',20)
pygame.display.update()
fps_controller.tick(diff)
    
    
