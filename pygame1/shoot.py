import pygame
import random
pygame.init()
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("kill those mofos")
run = True
py = 700
px = 400
rx = 400
ry = -100
end = False
shoot = False
shdone = True
m1x = random.randrange(50,750)
m1y = -100
m2x = random.randrange(50,750)
m2y = -300
m3x = random.randrange(50,750)
m3y = -500
s = 0
col = 0
while run:
    win.fill((col,0,0))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys= pygame.key.get_pressed()
    if end == False:
        if keys[pygame.K_LEFT]:
            px-=15
        if keys[pygame.K_RIGHT]:
            px+=15
        if keys[pygame.K_SPACE] and shdone == True:
            shoot= True
    if shoot == True:
        rx= px-5
        ry= py-10
        shdone = False
        shoot = False
    if shdone == False:
        ry-=30
        if ry<-40:
            shdone = True
    if end == False:
        m1y +=7
        if ry<=m1y and ry>m1y-40:
            if abs((rx+5)-m1x)<20:
                m1y =-100
                m1x = random.randrange(50,750)
                s+=1
        m2y +=7
        if ry<=m2y and ry>m2y-40:
            if abs((rx+5)-m2x)<20:
                m2y =-100
                m2x = random.randrange(50,750)
                s+=1
        m3y +=7
        if ry<=m3y and ry>m3y-40:
            if abs((rx+5)-m3x)<20:
                m3y =-100
                m3x = random.randrange(50,750)
                s+=1
    if m1y >800 or m2y> 800 or m3y > 800:
        end = True
        col =255




    pygame.draw.circle(win, (255,0,0), (m1x,m1y), 15, 0)
    pygame.draw.circle(win, (255,0,0), (m2x,m2y), 15, 0)
    pygame.draw.circle(win, (255,0,0), (m3x,m3y), 15, 0)

    dscore = "Score: "+str(s)
    if end == True:
        dscore = "You ended up killing "+str(s)+" before you failed."
    font = pygame.font.SysFont("Times New Roman", 30)
    score = font.render(dscore,True, (255,255,255))
    win.blit(score, (400-score.get_rect().width/2,100))

    pygame.draw.rect(win, (100,100,255), (rx,ry,10,40))
    pygame.draw.polygon(win, (0,255,0), [(px,py), (px-30,py+30), (px+30,py+30)], 0)
    pygame.display.update()


pygame.quit()
