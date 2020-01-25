import pygame
import random
pygame.init()
polex = 600
polex2 = 1050
poley = 0
len1 = 300
width = 100
len2 = 300
len3 = random.randrange(100, 500)
len4 = 600-len3

x = 100
y = 400
cirlen = 30
yvel = 0
s= 0
c = 1
onep= False

win = pygame.display.set_mode((600,800))
pygame.display.set_caption("Flappy Bird")
run = True
jump = False
end = False
while run:
    win.fill((0,0,0))

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if end == False:
        if keys[pygame.K_SPACE]:
            yvel = -46
            jump = True
    if yvel == 0:
        jump = False

    if jump == True:
        yvel+=2

    if polex < -100:
        polex = 800
        len1 = random.randrange(100,500)
        len2 = 600-len1
    if polex2 < -100:
        polex2 = 800
        len3 = random.randrange(100,500)
        len4 = 600-len3

    if polex <= 100 and polex+100 >= 100:
        if y-len1<30 or (len1+200)-y<30:
            end = True
    if polex2 <= 100 and polex2+100 >= 100:
        if y-len3<30 or (len3+200)-y<30:
            end = True
    if polex > 100 and polex <=130:
        if y-len1<30-(30+(130-polex)) or (len1+200)-y<30-(30-(130-polex)):
            end = True
    if polex+100>=70 and polex+100<100:
        if y-len1<30-(100-polex) or (len1+200)-y<30-(100-polex):
            end = True
    if polex2 > 100 and polex2 <=130:
        if y-len3<30-(30+(130-polex2)) or (len3+200)-y<30-(30-(130-polex2)):
            end = True
    if polex2+100>=70 and polex2+100<100:
        if y-len3<30-(100-polex2) or (len3+200)-y<30-(100-polex2):
            end = True


    if polex+100< 100 and c==1:
        onep = True
        c=0
    if polex2+100<100 and c==0:
        onep= True
        c= 1
    if onep==True:
        s+=1
        onep=False


    if end == False:
        polex -=10
        polex2 -=10



    if y>745:
        y = 745


    y+=yvel
    y+=25
    pygame.draw.rect(win, (255, 0, 0), (polex, poley, width, len1))
    pygame.draw.rect(win, (255, 0, 0), (polex, poley+len1+200, width, len2))
    pygame.draw.rect(win, (255, 0, 0), (polex2, poley, width, len3))
    pygame.draw.rect(win, (255, 0, 0), (polex2, poley+len3+200, width, len4))

    pygame.draw.circle(win, (0,255,0), (x,y), cirlen)

    dscore= "Score: "+ str(s)
    font = pygame.font.SysFont("Times New Roman", 30)
    score = font.render(dscore,True, (255,255,255))
    win.blit(score, (300-score.get_rect().width/2,100))

    pygame.display.update()


pygame.quit()
