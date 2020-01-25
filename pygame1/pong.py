import pygame
import random
pygame.init()
x1 = 0
x2 = 780
y1 = 300
y2 = 300
l = 20
h = 100
xc = 400
yc = 300
xvel = 10
yvel = 0
s1 = 0
s2 = 0


end = False

out = False
count = 0

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("PONG")
hit = False
run = True
endtext = "c"
while run:
    win.fill((0,0,0))

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if hit == True and xc > 200 and xc < 600:
        hit = False
    if end == False:
        xc += xvel
        yc += yvel
    if yc <=10:
        yvel=-yvel
    if yc >=590:
        yvel=-yvel


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y1>= 10:
        y1-=15
    if keys[pygame.K_s] and y1<= 590-h:
        y1+=15
    if keys[pygame.K_UP] and y2>= 10:
        y2-=15
    if keys[pygame.K_DOWN] and y2<= 590-h:
        y2+=15
    if xc >=770 and xc <= 803:
        if yc >y2-10 and yc< y2+h+10 and hit == False:
            hit = True
            centdis1 = yc-(y2+h/2)
            xvel = -xvel
            yvel += 0.1*centdis1
            if xvel <0:
                if xvel >-23:
                    xvel-=1
                elif xvel >-28:
                    xvel-=0.5
            if xvel >0:
                if xvel <23:
                    xvel+=1
                elif xvel < 28:
                    xvel+=0.5


    if xc <=30 and xc >= -3:
        if yc >y1 and yc< y1+h and hit == False:
            hit = True
            centdis2 = yc-(y1+h/2)
            xvel = -xvel
            yvel += 0.1*centdis2
            if xvel <0:
                if xvel >-23:
                    xvel-=1
                elif xvel >-28:
                    xvel-=0.5
            if xvel >0:
                if xvel <23:
                    xvel+=1
                elif xvel < 28:
                    xvel+=0.5
    if xc <= -100:
        xc = 400
        yc = 300
        xvel = 0.1
        yvel = 0
        out = True
        s2 +=1
    if xc >= 900:
        xc = 400
        yc = 300
        xvel = -0.1
        yvel = 0
        out = True
        s1 +=1
    if out == True:
        count +=1
        if count >50:
            count = 0
            out = False
            xvel *=100

    dscore = str(s1)+" - "+str(s2)
    if s1 == 7:
        end = True
        endtext = "Left Player Wins."
    if s2 == 7:
        end = True
        endtext = "Right Player Wins."

    font = pygame.font.SysFont("Times New Roman", 30)
    score = font.render(dscore,True, (255,255,255))
    win.blit(score, (400-score.get_rect().width/2,100))

    font2 = pygame.font.SysFont("Times New Roman", 80)
    ltext = font2.render(endtext,True, (255,255,255))
    if end == True:
        win.blit(ltext, (400-ltext.get_rect().width/2,270))


    if end == False:
        pygame.draw.circle(win,(0,255,0), (int(xc),int(yc)), 10, 10)
    pygame.draw.rect(win,(255,255,255), (x1,y1,l,h))
    pygame.draw.rect(win,(255,255,255), (x2,y2,l,h))
    pygame.display.update()


pygame.quit()
