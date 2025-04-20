import pygame, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption("test")
width, height = 800, 600  
screen = pygame.display.set_mode((width, height))




def drawBadge(pos, type=0, badgetext="",pressed=False, hover=False, mult=1):
    

    if pressed:
        DARKPART,LIGHTPART = (108,127,108), (216,245,208)
    elif type == 0:
        if hover:
            DARKPART, LIGHTPART = (171,171,171), (230,230,230)
        elif not hover:
            DARKPART, LIGHTPART = (70,70,70), (180,180,180)
    elif type == 1:
        if hover:
            DARKPART, LIGHTPART = (217,188,108), (245,237,206)
        else:
            DARKPART, LIGHTPART = (219,161,0), (245,228,156)
    else:
        DARKPART, LIGHTPART = (255,0,255), (0,0,0)

    pygame.draw.rect(screen, DARKPART, (pos[0], pos[1], 120*mult, 60*mult))
    pygame.draw.rect(screen, LIGHTPART, (pos[0]+(5*mult), pos[1]+(5*mult), 110*mult, 50*mult))
    font = pygame.font.SysFont("Arial", 10)  # Create font object
    text_surface = font.render(str(badgetext), True, (255, 0, 0))
    text_rect = text_surface.get_rect() 

   
    text_rect.center = (pos[0] + 60 * mult, pos[1] + 30 * mult) 

    
    screen.blit(text_surface, text_rect)



global_x = 0
global_y = 0
mouse_was_pressed = False
dragging = False
points=0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                
                start_x, start_y = pygame.mouse.get_pos()
                dragging = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                
                dragging = False

    




        
    rect = pygame.Rect(10+global_x, 10+global_y, 120, 60) 

    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    
    if rect.collidepoint(mouse_x,mouse_y):
        if mouse_pressed:
            drawBadge((10+global_x,10+global_y),0,points,True, True)
        else:
            drawBadge((10+global_x,10+global_y),1,points,False, True)
        if mouse_pressed and not mouse_was_pressed:
            points += 1
            mouse_was_pressed = True
        elif not mouse_pressed:
            
            mouse_was_pressed = False
    
    else:
        drawBadge((10+global_x,10+global_y), 1, points)
    
    if dragging and not rect.collidepoint(mouse_x,mouse_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        delta_x = mouse_x - start_x
        delta_y = mouse_y - start_y
        
        
        if abs(delta_x) >= 15: #update if big enough (15)
            global_x += delta_x
            start_x = mouse_x  
        
        if abs(delta_y) >= 15:
            global_y += delta_y
            start_y = mouse_y 

    pygame.display.flip()
    screen.fill((0,0,0))
    #clock.tick(30)
pygame.quit()
sys.quit()