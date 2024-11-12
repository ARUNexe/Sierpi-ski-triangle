
import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1100, 1000))
screen.fill((255, 255, 255))


def calculate_midpoint(node,vertice):
    x = vertice[0][0]
    y = vertice[0][1]
    x_mid_pt = (node[0]+x)/2
    y_mid_pt = (node[1]+y)/2
    return (x_mid_pt,y_mid_pt)

pt1 = (550,100)
pt2 = (100,900)
pt3 = (1000,900)
vertices = [pt1,pt2,pt3]

node = pt1

while True:
    for i in vertices:
        pygame.draw.circle(screen, (0, 0, 0), i, 4)

    random_vertices = random.sample(vertices,1)
    midpoint = calculate_midpoint(node,random_vertices)

    node = midpoint

    pygame.draw.circle(screen, (0, 0, 0), node, 1)

    pygame.display.update()
