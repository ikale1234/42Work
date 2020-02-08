import pygame
import random
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Geodash")
run = True

yvel = 0
b1 = 150
b2 = 200
canjump = True
jump = False
grav = False
gry = 400
y = gry-50
boxx = 150
alive = True
isnl = False
end = False
class obs:
    def __init__(self,x):
        self.x = x
        self.y = gry
        self.vel = -10
        self.move = False
    def draw(self,win):
        global alive
        if self.move:
            self.y = gry
            pygame.draw.polygon(win, (0,0,0), [(self.x, self.y), (self.x+50, self.y), (self.x+25, self.y-50)])
            if self.x <b2 and self.x+25 >=b2:
                dis = b2 - self.x
            elif self.x+50 >b1 and self.x+25 <b1:
                dis = (self.x+50) - b1
            else:
                dis = -500
            if y+50 > gry-2*dis:
                alive = False


tri = []

#obstacle places

for j in range(10):
    tri.append(obs(850+300*j))
    tri.append(obs(800+300*j))

#while loop
for i in range(len(tri)):
    tri[i].move = True
while run:
    win.fill((200,100,100))

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if alive:
        if key[pygame.K_x] and canjump:
            jump = True
            canjump = False
    
    if jump:
        jump = False
        grav = True
        yvel = -40
    if grav:
        yvel+=4
        if yvel == 40:
            grav = False
            yvel = 0
            canjump = True
    
    dcount = 0
    for i in range(len(tri)):
        tri[i].x+=tri[i].vel
        if alive != True:
            tri[i].vel = 0
        if tri[i].x < -200:
            dcount +=1
        if dcount == len(tri):
            end = True
    

    y+=yvel
    #drawgame
    pygame.draw.line(win, (0,0,0), (0, gry), (800, gry), 2)
    if alive:
        pygame.draw.rect(win, (0,0,255), (boxx, y, 50, 50))
    for i in range(len(tri)):
        tri[i].draw(win)
    pygame.display.update()
    if end:
        boxx +=10
pygame.quit()
