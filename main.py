import pygame

import os

screen_length = 465

screen_height = 350

dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field) 
from home import homescreen
#From the home.py module import homescreen function
from curt import curt
  

clock = pygame.time.Clock()
#This helps the program keep track of time

running = True

FPS = 60

in_home = True

while running:

  clock.tick(FPS)
  #We want FPS=60
  
  for event in pygame.event.get():

    if in_home:
    #Want some way to keep track of what page you are in -> dont want to be in the menu anymore if don't need it
      #page = homescreen(screen_length,screen_height, dim_field, screen, event)

      #if page == "curt":
        curt(screen_length,screen_height, dim_field, screen, event)
        #in_home = False
      #elif page == "gary":
        #gary(screen_length,screen_height, dim_field, screen, event)
        #in_home = False
      #elif page == "niema":
        #niema(screen_length,screen_height, dim_field, screen, event)
        #in_home = False
      

    if event.type == pygame.KEYDOWN: 

     if event.key == pygame.K_q:

      running = False
      
  keys = pygame.key.get_pressed()

  pygame.display.update()