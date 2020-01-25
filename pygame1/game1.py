import pygame
import random
pygame.init()


win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tic Tac Toe")
run = True
count = 2
symbol = "X"
dcon = True

box1x = False
box1o= False
box2x= False
box2o= False
box3x= False
box3o= False
box4x= False
box4o= False
box5x= False
box5o= False
box6x= False
box6o= False
box7x= False
box7o= False
box8x= False
box8o= False
box9x= False
box9o= False
end = False
draw = False

switch = False


e = False
what = "c"
while run:
    win.fill((0,0,0))

    pygame.time.delay(10)
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print (x)
            if end ==False:
                if box1x == False and box1o == False and end == False:
                    if x > 200 and x < 200+400/3-7:
                        if y > 200 and y < 200+400/3-7:
                            if symbol == "X":
                                box1x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box1o = True
                                symbol = "X"
                                print (symbol)

                if box2x == False and box2o == False and end == False:
                    if x > 200+400/3+7 and x < 200+800/3-7:
                        if y > 200 and y < 200+400/3-7:
                            if symbol == "X":
                                box2x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box2o = True
                                symbol = "X"
                                print (symbol)

                if box3x == False and box3o == False and end == False:
                    if x > 200+800/3+7 and x < 600:
                        if y > 200 and y < 200+400/3-7:
                            if symbol == "X":
                                box3x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box3o = True
                                symbol = "X"
                                print (symbol)

                if box4x == False and box4o == False and end == False:
                    if x > 210 and x < 200+400/3-7:
                        if y > 200+400/3+7 and y < 200+800/3-7:
                            if symbol == "X":
                                box4x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box4o = True
                                symbol = "X"
                                print (symbol)

                if box5x == False and box5o == False and end == False:
                    if x > 200+400/3+7 and x < 200+800/3-7:
                        if y > 200+400/3+7 and y < 200+800/3-7:
                            if symbol == "X":
                                box5x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box5o = True
                                symbol = "X"
                                print (symbol)

                if box6x == False and box6o == False and end == False:
                    if x > 200+800/3+7 and x < 600:
                        if y > 200+400/3+7 and y < 200+800/3-7:
                            if symbol == "X":
                                box6x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box6o = True
                                symbol = "X"
                                print (symbol)

                if box7x == False and box7o == False and end == False:
                    if x > 200 and x < 200+400/3-7:
                        if y > 200+800/3+7 and y < 600:
                            if symbol == "X":
                                box7x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box7o = True
                                symbol = "X"
                                print (symbol)

                if box8x == False and box8o == False and end == False:
                    if x > 200+400/3+7 and x < 200+800/3-7:
                        if y > 200+800/3+7 and y < 600:
                            if symbol == "X":
                                box8x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box8o = True
                                symbol = "X"
                                print (symbol)

                if box9x == False and box9o == False and end == False:
                    if x > 200+800/3+7 and x < 600:
                        if y > 200+800/3+7 and y < 600:
                            if symbol == "X":
                                box9x = True
                                symbol = "O"
                                print (symbol)
                            elif symbol == "O":
                                box9o = True
                                symbol = "X"
                                print (symbol)




    if box1x == True:
        pygame.draw.line(win, (0,0,255), (210,210), (200+400/3-17,200+400/3-17), 5)
        pygame.draw.line(win, (0,0,255), (210,200+400/3-17), (200+400/3-17,210), 5)
    if box1o == True:
        pygame.draw.circle(win, (0,255,0), (263,263), 60, 3)
    if box2x == True:
        pygame.draw.line(win, (0,0,255), (200+400/3+17,210), (200+800/3-17,200+400/3-17), 5)
        pygame.draw.line(win, (0,0,255), (200+400/3+17,200+400/3-17), (200+800/3-17,210), 5)
    if box2o == True:
        pygame.draw.circle(win, (0,255,0), (400,263), 60, 3)
    if box3x == True:
        pygame.draw.line(win, (0,0,255), (200+800/3+17,210), (590,200+400/3-17), 5)
        pygame.draw.line(win, (0,0,255), (200+800/3+17,200+400/3-17), (590,210), 5)
    if box3o == True:
        pygame.draw.circle(win, (0,255,0), (533,263), 60, 3)
    if box4x == True:
        pygame.draw.line(win, (0,0,255), (210,200+400/3+17), (200+400/3-17,200+800/3-17), 5)
        pygame.draw.line(win, (0,0,255), (210,200+800/3-17), (200+400/3-17,200+400/3+17), 5)
    if box4o == True:
        pygame.draw.circle(win, (0,255,0), (263,400), 60, 3)
    if box5x == True:
        pygame.draw.line(win, (0,0,255), (200+400/3+17,200+400/3+17), (200+800/3-17,200+800/3-17), 5)
        pygame.draw.line(win, (0,0,255), (200+800/3-17,200+400/3+17), (200+400/3+17,200+800/3-17), 5)
    if box5o == True:
        pygame.draw.circle(win, (0,255,0), (400,400), 60, 3)
    if box6x == True:
        pygame.draw.line(win, (0,0,255), (200+800/3+17,200+400/3+17), (590,200+800/3-17), 5)
        pygame.draw.line(win, (0,0,255), (590,200+400/3+17), (200+800/3+17,200+800/3-17), 5)
    if box6o == True:
        pygame.draw.circle(win, (0,255,0), (533,400), 60, 3)
    if box7x == True:
        pygame.draw.line(win, (0,0,255), (210,200+800/3+17), (200+400/3-17,590), 5)
        pygame.draw.line(win, (0,0,255), (210,590), (200+400/3-17,200+800/3+17), 5)
    if box7o == True:
        pygame.draw.circle(win, (0,255,0), (263,533), 60, 3)
    if box8x == True:
        pygame.draw.line(win, (0,0,255), (200+400/3+17,200+800/3+17), (200+800/3-17,590), 5)
        pygame.draw.line(win, (0,0,255), (200+400/3+17,590), (200+800/3-17,200+800/3+17), 5)
    if box8o == True:
        pygame.draw.circle(win, (0,255,0), (400,533), 60, 3)
    if box9x == True:
        pygame.draw.line(win, (0,0,255), (200+800/3+17,200+800/3+17), (590,590), 5)
        pygame.draw.line(win, (0,0,255), (200+800/3+17,590), (590,200+800/3+17), 5)
    if box9o == True:
        pygame.draw.circle(win, (0,255,0), (533,533), 60, 3)


    def wincomb(b1,b2,b3):
        global end
        if b1 == True and b2 == True and b3 == True:
            end = True


    wincomb(box1x,box2x,box3x)
    wincomb(box4x,box5x,box6x)
    wincomb(box7x,box8x,box9x)
    wincomb(box1x,box4x,box7x)
    wincomb(box2x,box5x,box8x)
    wincomb(box3x,box6x,box9x)
    wincomb(box1x,box5x,box9x)
    wincomb(box7x,box5x,box3x)

    wincomb(box1o,box2o,box3o)
    wincomb(box4o,box5o,box6o)
    wincomb(box7o,box8o,box9o)
    wincomb(box1o,box4o,box7o)
    wincomb(box2o,box5o,box8o)
    wincomb(box3o,box6o,box9o)
    wincomb(box1o,box5o,box9o)
    wincomb(box7o,box5o,box3o)
    if (box1x == True or box1o == True) and (box2x == True or box2o == True) and (box3x == True or box3o == True) and (box4x == True or box4o == True) and (box5x == True or box5o == True) and (box6x == True or box6o == True)\
    and (box7x == True or box7o == True) and (box8x == True or box8o == True) and (box9x == True or box9o == True):
        draw = True
    pygame.draw.rect(win,(255,0,0),(200,200+800/3-7,400,14))
    pygame.draw.rect(win,(255,0,0),(200,200+400/3-7,400,14))
    pygame.draw.rect(win,(255,0,0),(200+400/3-7,200,14,400))
    pygame.draw.rect(win,(255,0,0),(200+800/3-7,200,14,400))

    if draw == True or end == True:
        if symbol == "X":
            what = "O"
        if symbol == "O":
            what = "X"
        if end != True:
            what = "Nobody"
        who = what+" wins."
    else:
        who = "It is "+symbol+"\'s turn."


    font = pygame.font.SysFont("Times New Roman", 30)
    turn = font.render(who,True, (255,255,255))
    win.blit(turn, (400-turn.get_rect().width/2,100))

    pygame.display.update()

pygame.quit()
