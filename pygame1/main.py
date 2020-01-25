import pygame
import random
pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("easy ass game")

x = 50
y =60
w=40
h=60
vel=10
rx = random.randrange(100,700)
ry = random.randrange(100,700)
scor = 0
jump =False
jcount = 10
run = True
up = False
down =  False
right = False
left = False
end = False
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    dscore = "Score: "+str(scor)
    if scor>=20:
        dscore = "You Won!"
        end = True


    cx=x+w/2
    cy=y+h/2
    zx = rx+5
    zy = ry+5
    disx= cx-zx
    disy= cy-zy
    if disx <= (w/2)+5 and disx >= (-w/2)-5:
        if disy <=(h/2)+5 and disy >=(-h/2)-5:
            rx = random.randrange(100,700)
            ry = random.randrange(100,700)
            scor +=1
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left = True
        up = False
        down =  False
        right = False
    if keys[pygame.K_RIGHT]:
        left = False
        up = False
        down =  False
        right = True

    if keys[pygame.K_UP]:
        left = False
        up = True
        down =  False
        right = False
    if keys[pygame.K_DOWN]:
        left = False
        up = False
        down =  True
        right = False
    if left == True:
        x-=vel
    if up == True:
        y-=vel
    if down == True:
        y+=vel
    if right == True:
        x+=vel

    win.fill((0,0,0))
    if x >=760:
        x=760
    if x<=0:
        x=0
    if y>=740:
        y=740
    if y<=0:
        y=0
    font = pygame.font.SysFont("Times New Roman", 30)
    score = font.render(dscore,True, (255,255,255))
    win.blit(score, (400-score.get_rect().width/2,100))
    if end == False:
        pygame.draw.rect(win,(255,0,0),(x,y,w,h))
        pygame.draw.rect(win,(0,255,0),(rx,ry,10,10))
    pygame.display.update()


pygame.quit()