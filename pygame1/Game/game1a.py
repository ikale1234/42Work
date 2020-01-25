import pygame
import random
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("jump")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

shoot = False


class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y  =y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.jcount = 10
        self.left  = False
        self.right = False
        self.wcount = 0
        self.alive = True
    def draw(self,win):
        if self.alive:
            if self.wcount + 1 >= 27:
                self.wcount = 0
            if self.left:
                win.blit(walkLeft[self.wcount//3], (self.x,self.y))
                self.wcount += 1
            elif self.right:
                win.blit(walkRight[self.wcount//3], (self.x,self.y))
                self.wcount += 1
            else:
                win.blit(char, (self.x,self.y))

class bullet():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel = 30
        self.shoot = False
    def draw(self,win):
        if self.shoot == True:
            pygame.draw.rect(win, (0,0,255), (self.x, self.y, 20, 10))
        if self.x <-1000 or self.x >2000:
            self.shoot = False

run = True
def drawgame():
    win.blit(bg, (0,0))
    for i in range(len(bs)):
        bs[i].draw(win)
    for i in range(len(ds)):
        ds[i].draw(win)
    guy.draw(win)
    dude.draw(win)
    if l1 != 0:
        pygame.draw.rect(win, (255,0,0), (guy.x, guy.y, l1, 5))
    if l2 != 0:
        pygame.draw.rect(win, (255,0,255), (dude.x, dude.y, l2, 5))

    pygame.display.update()
guy = player(300, 410, 64, 64)
dude = player(100, 410, 64, 64)
bs = []
ds = []
bnum = -1
dnum = -1
bwait= 40
dwait= 40
bcount = 69
dcount = 69
p1score = 0
p2score = 0
p1win = False
p2win = False
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    l1 = 70 - 7*p1score
    l2 = 70 - 7*p2score
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and guy.x > guy.vel:
        guy.x-=guy.vel
        guy.left = True
        guy.right = False
    elif key[pygame.K_RIGHT] and guy.x< 500-guy.width-guy.vel:
        guy.x+=guy.vel
        guy.left = False
        guy.right = True
    else:
        guy.left= False
        guy.right= False
        guy.wcount = 0


    if guy.jump == False:
        if key[pygame.K_UP]:
            guy.jump = True
            guy.left= False
            guy.right= False
            guy.wcount = 0

    else:
        if guy.jcount >= -10:
            neg = 1
            if guy.jcount < 0:
                neg = -1
            guy.y-=(guy.jcount**2)*0.5*neg
            guy.jcount -=1
        else:
            guy.jump = False
            guy.jcount =10













    if key[pygame.K_a] and dude.x > dude.vel:
        dude.x-=dude.vel
        dude.left = True
        dude.right = False
    elif key[pygame.K_d] and dude.x< 500-dude.width-guy.vel:
        dude.x+=dude.vel
        dude.left = False
        dude.right = True
    else:
        dude.left= False
        dude.right= False
        dude.wcount = 0


    if dude.jump == False:
        if key[pygame.K_w]:
            dude.jump = True
            dude.left= False
            dude.right= False
            dude.wcount = 0

    else:
        if dude.jcount >= -10:
            neg = 1
            if dude.jcount < 0:
                neg = -1
            dude.y-=(dude.jcount**2)*0.5*neg
            dude.jcount -=1
        else:
            dude.jump = False
            dude.jcount =10



    if l1 == 0:
        guy.alive = False
        p2win = True
    if l2 == 0:
        dude.alive = False
        p1win = True



    dwait+=1
    if key[pygame.K_e] and dwait>10:
        dwait = 0
        ds.append(bullet())
        dnum+=1
        ds[dnum].x= dude.x
        ds[dnum].y= dude.y+20
        ds[dnum].shoot = True
        dcount = 0
    if dcount == 0:
        if ds[dnum].shoot == True:
            dcount = 1
            if dude.right:
                mul = 1
            elif dude.left:
                mul = -1
            else:
                mul = random.choice([1,-1])
            ds[dnum].vel = ds[dnum].vel*mul
    for k in range(len(ds)):
        if ds[k].shoot:
            ds[k].x+=ds[k].vel
            if guy.alive:
                if ds[k].x > guy.x-5 and ds[k].x < guy.x+50:
                    if ds[k].y > guy.y and ds[k].y < guy.y+65:
                        p1score +=1
                        ds[k].shoot = False









    bwait+=1
    if key[pygame.K_RSHIFT] and bwait>10:
        bwait = 0
        bs.append(bullet())
        bnum+=1
        bs[bnum].x= guy.x
        bs[bnum].y= guy.y+20
        bs[bnum].shoot = True
        bcount = 0
    if bcount == 0:
        if bs[bnum].shoot == True:
            bcount = 1
            if guy.right:
                mul = 1
            elif guy.left:
                mul = -1
            else:
                mul = random.choice([1,-1])
            bs[bnum].vel = bs[bnum].vel*mul
    for k in range(len(bs)):
        if bs[k].shoot:
            bs[k].x+=bs[k].vel
            if dude.alive:
                if bs[k].x > dude.x-5 and bs[k].x < dude.x+50:
                    if bs[k].y > dude.y and bs[k].y < dude.y+65:
                        p2score +=1
                        bs[k].shoot = False

    if p2win:
        sent = "Pink wins!"
    if p1win:
        sent = "Red wins!"
    if p1win or p2win:
        font = pygame.font.SysFont("Arial", 30)
        thing = font.render(sent,True, (255,255,255))
        win.blit(thing, (400-thing.get_rect().width/2,100))


    drawgame()
pygame.quit()
