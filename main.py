import pygame

import os

screen_length = 465

screen_height = 350

dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field)

#Draw all the players out here in future
player_x = 45
player_y = 200
player_width = 30
player_height = 30
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
player = pygame.image.load(os.path.join("curt", "camel.png")).convert()
player.set_colorkey((0, 0, 0))
player = pygame.transform.scale(player, (player_width, player_height))

#Classes - Blueprint of an object
  #Object is code representation of a real life thing
#Classes == Factories
  #Class(dog) -> can make lots of dogs on a whim
    #Just call for the dog richard = dog

from home import homescreen
#From the home.py module import homescreen function
from curt import curt

clock = pygame.time.Clock()
#This helps the program keep track of time

running = True

FPS = 60

in_home = True

state = "home"

loaded = False

direction = "stop"

#in_game = True

while running:

  clock.tick(FPS)
  #We want FPS=60

  if state == "home":
    #Want some way to keep track of what page you are in -> dont want to be in the menu anymore if don't need it

    page = homescreen(screen_length,screen_height, dim_field, screen, player_rect)
    state = page

  elif state == "curt":
    curt(screen_length,screen_height, dim_field, screen, player_rect)
    #Draw the player here to continuously draw it as its moving over the frames
    screen.blit(player, player_rect)
  #elif page == "gary":
    #gary(screen_length,screen_height, dim_field, screen, player_rect)
    #screen.blit(player, player_rect)
  #elif page == "niema":
    #niema(screen_length,screen_height, dim_field, screen, player_rect)
    #screen.blit(player, player_rect)

    #Note: when you make the other players name them player_g or player_n because curt is player
    
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN: 

      if event.key == pygame.K_q:

        running = False

      if event.key == pygame.K_LEFT:
        direction = "left"
      if event.key == pygame.K_RIGHT:
        direction = "right"
      if event.key == pygame.K_UP:
        direction = "up"
      if event.key == pygame.K_DOWN:
        direction = "down"

  #State (Variable) = Curt:
    #Stuff happens and shows up

  if direction == "left":
    player_rect.move_ip(-5, 0)
    #print("Left!")
  elif direction == "right":
    player_rect.move_ip(5, 0)
  elif direction == "up":
    player_rect.move_ip(0, -5)
  elif direction == "down":
    player_rect.move_ip(0, 5)
  else:
    pass #Skips over it, doesn't do anything

  pygame.display.update()