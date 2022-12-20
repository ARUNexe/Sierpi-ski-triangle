import pygame
import random
import time
import math

pygame.init()

screen = pygame.display.set_mode((500, 500))

def midpt(mp_x,mp_y,*xy):
    x = xy[0][0][0]
    y = xy[0][0][1]
    x_mid_pt = (mp_x+x)/2
    y_mid_pt = (mp_y+y)/2
    return (x_mid_pt,y_mid_pt)

pt1 = (250,100)
pt2 = (100,400)
pt3 = (400,400)
screen.fill((255, 255, 255))
pts = [(250,100),(100,400),(400,400)]

start_lst = random.sample(pts,2)
print(start_lst)

mid_pt_x = (start_lst[0][0]+start_lst[1][0])/2
mid_pt_y = (start_lst[0][1]+start_lst[1][1])/2

runner = True
while runner:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            runner = False

    pygame.draw.circle(screen, (0, 0, 0), pt1, 1)
    pygame.draw.circle(screen, (0, 0, 0), pt2, 1)
    pygame.draw.circle(screen, (0, 0, 0), pt3, 1)

    pygame.draw.circle(screen, (0, 0, 0), (mid_pt_x, mid_pt_y), 1)

    out_pt = random.sample(pts,1)

    new_md = midpt(mid_pt_x,mid_pt_y,out_pt)

    pygame.draw.circle(screen, (0, 0, 0), (new_md[0],new_md[1]), 1)
    #time.sleep(0.0005)
    print(new_md[0],new_md[1])
    mid_pt_x = new_md[0]
    mid_pt_y = new_md[1]

    pygame.display.update()
