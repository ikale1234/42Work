import pygame
import random
bgdim = 800
array = 16
space = bgdim/array
win = pygame.display.set_mode((bgdim,bgdim))
pygame.display.set_caption("Snake")
run = True
spots = []
end = False
score = 0
for i in range(16):
    spots.append(i*50+1)

class part:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 49
        self.h = 49
        self.vel = 50
        self.up = False
        self.down = False
        self.right = False
        self.left = False
    def draw(self,win):
        pygame.draw.rect(win, (0,255,0), (self.x, self.y, self.w, self.h))
        global end
        if self.right:
            if self.x < 750:
                self.x+= self.vel
            else:
                end = True
        if self.down:
            if self.y < 750:
                self.y+= self.vel
            else:
                end = True
        if self.up:
            if self.y > 50:
                self.y-= self.vel
            else:
                end = True        
        if self.left:
            if self.x > 50:
                self.x-= self.vel
            else:
                end = True
def drawsnake():
    for i in range(len(snake)):
        snake[i].draw(win)
    pygame.display.update()

fx = random.choice(spots)
fy = random.choice(spots)

snake = []
snake.append(part(51,51))
while run:
    win.fill((255,255,255))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and snake[0].right == False:
        snake[0].left = True
        snake[0].right = False
        snake[0].down = False
        snake[0].up = False
    if key[pygame.K_UP] and snake[0].down == False:
        snake[0].left = False
        snake[0].right = False
        snake[0].down = False
        snake[0].up = True
    if key[pygame.K_RIGHT] and snake[0].left == False:
        snake[0].left = False
        snake[0].right = True
        snake[0].down = False
        snake[0].up = False
    if key[pygame.K_DOWN] and snake[0].up == False:
        snake[0].left = False
        snake[0].right = False
        snake[0].down = True
        snake[0].up = False

    #food
    pygame.draw.rect(win, (255,0,0), (fx, fy, 50, 50))
    if snake[0].x == fx and snake[0].y == fy:
        if snake[len(snake)-1].left:
            snake.append(part(snake[len(snake)-1].x+50, snake[len(snake)-1].y))

        if snake[len(snake)-1].up:
            snake.append(part(snake[len(snake)-1].x, snake[len(snake)-1].y+50))

        if snake[len(snake)-1].right:
            snake.append(part(snake[len(snake)-1].x-50, snake[len(snake)-1].y))

        if snake[len(snake)-1].down:
            snake.append(part(snake[len(snake)-1].x, snake[len(snake)-1].y-50))

        fx = random.choice(spots)
        fy = random.choice(spots)
        score+= 1
        print(score)

    #follow next in line
    for k in range(len(snake)-1):
        if snake[k].x+50 == snake[k+1].x:
            snake[k+1].right = False
            snake[k+1].left = True
            snake[k+1].up = False
            snake[k+1].down = False
        if snake[k].y+50 == snake[k+1].y:
            snake[k+1].right = False
            snake[k+1].left = False
            snake[k+1].up = True
            snake[k+1].down = False
        if snake[k].x-50 == snake[k+1].x:
            snake[k+1].right = True
            snake[k+1].left = False
            snake[k+1].up = False
            snake[k+1].down = False
        if snake[k].y-50 == snake[k+1].y:
            snake[k+1].right = False
            snake[k+1].left = False
            snake[k+1].up = False
            snake[k+1].down = True

    
    #ram into self
    for f in range(len(snake)-1):
        if snake[0].x == snake[f+1].x:
            if snake[0].y == snake[f+1].y:
                end = True
    
    #stop movement at end of game
    if end:
        for l in range(len(snake)):
            snake[l].right = False
            snake[l].left = False
            snake[l].up = False
            snake[l].down = False

    
    
    #grid
    for i in range(array):
        pygame.draw.line(win, (0,0,0), (0,space*i), (bgdim, space*i))
        pygame.draw.line(win, (0,0,0), (space*i,0), (space*i, bgdim))
    
    

    pygame.display.update()
    drawsnake()
pygame.quit()