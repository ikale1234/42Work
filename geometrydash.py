import pygame
import random
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Geodash")
run = True
y = 400
yvel = 0
canjump = True
jump = False
grav = False

class obs:
    def __init__(self,x):
        self.x = x
        self.y = 450
        self.vel = -10
        self.move = False
    def draw(self,win):
        if self.move:
            pygame.draw.polygon(win, (0,0,0), [(self.x, self.y), (self.x+50, self.y), (self.x+25, self.y-50)])
tri = []

#obstacle places

tri.append(obs(800))
tri.append(obs(900))


for i in range(len(tri)):
    tri[i].move = True
while run:
    win.fill((200,100,100))

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_x] and canjump:
        jump = True
        canjump = False
    if jump:
        jump = False
        grav = True
        yvel = -30
    if grav:
        yvel+=4
        if yvel == 30:
            grav = False
            yvel = 0
            canjump = True
    for i in range(len(tri)):
        tri[i].x+=tri[i].vel

    y+=yvel
    #drawgame
    pygame.draw.line(win, (0,0,0), (0, 450), (800, 450), 2)
    pygame.draw.rect(win, (0,0,255), (150, y, 50, 50))
    for i in range(len(tri)):
        tri[i].draw(win)
    pygame.display.update()
pygame.quit()
