import pygame

import os

screen_length = 465

screen_height = 350

dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field)

#Draw all the players out here in future
player_x = 218
player_y = 40
player_width = 23
player_height = 23
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
player = pygame.image.load(os.path.join("curt", "camel.png")).convert()
player.set_colorkey((0, 0, 0))
player = pygame.transform.scale(player, (player_width, player_height))
#Hannah
hannah_x = 385
hannah_y = 200
hannah_rect = pygame.Rect(hannah_x, hannah_y, 23, 23)
hannah = pygame.image.load(os.path.join("curt", "hannah.png")).convert()
hannah.set_colorkey((0, 0, 0))
hannah = pygame.transform.scale(hannah, (23, 23))
screen.blit(hannah, hannah_rect)
#Johnny
johnny_x = 150
johnny_y = 145
johnny_rect = pygame.Rect(johnny_x, johnny_y, 23, 23)
johnny = pygame.image.load(os.path.join("curt", "johnny.png")).convert()
johnny.set_colorkey((0, 0, 0))
johnny = pygame.transform.scale(johnny, (25, 25))
screen.blit(johnny, johnny_rect)
#Josh
josh_x = 45
josh_y = 200
josh_rect = pygame.Rect(josh_x, josh_y, 23, 23)
josh = pygame.image.load(os.path.join("curt", "josh.png")).convert_alpha()
josh.set_colorkey((255, 255, 255))
josh = pygame.transform.scale(josh, (23, 23))
screen.blit(josh, josh_rect)
#Michael
michael_x = 285
michael_y = 150
michael_rect = pygame.Rect(michael_x, michael_y, 23, 23)
michael = pygame.image.load(os.path.join("curt", "michael.png")).convert()
michael.set_colorkey((0, 0, 0))
michael = pygame.transform.scale(michael, (23, 23))
screen.blit(michael, michael_rect)

#Classes - Blueprint of an object
  #Object is code representation of a real life thing
#Classes == Factories
  #Class(dog) -> can make lots of dogs on a whim
    #Just call for the dog richard = dog

from home import homescreen
#From the home.py module import homescreen function
from curt import curt

from curt import walls

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

  #if state == "home":
    #Want some way to keep track of what page you are in -> dont want to be in the menu anymore if don't need it

    #page = homescreen(screen_length,screen_height, dim_field, screen, player_rect)
    #state = page
  #elif state == "curt":
  curt(screen_length,screen_height, dim_field, screen, player_rect)
    #Draw the player here to continuously draw it as its moving over the frames
  screen.blit(player, player_rect)
  screen.blit(hannah, hannah_rect)
  screen.blit(johnny, johnny_rect)
  screen.blit(josh, josh_rect)
  screen.blit(michael, michael_rect)
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

  curt_walls = walls(screen_length,screen_height, dim_field, screen, player_rect)
  
  #if player_rect.collidelist(curt_walls) != -1:
    #direction = "stop"
      

  if direction == "left":
    player_rect.move_ip(-5, 0)
    if player_rect.collidelist(curt_walls) != -1:
      player_rect.move_ip(5,0)
    #print("Left!")
  elif direction == "right":
    player_rect.move_ip(5, 0)
    if player_rect.collidelist(curt_walls) != -1:
      player_rect.move_ip(-5,0)
  elif direction == "up":
    player_rect.move_ip(0, -5)
    if player_rect.collidelist(curt_walls) != -1:
      player_rect.move_ip(0, 5)
  elif direction == "down":
    player_rect.move_ip(0, 5)
    if player_rect.collidelist(curt_walls) != -1:
      player_rect.move_ip(0, -5)
  else:
    pass #Skips over it, doesn't do anything
  
  #Curt collisions 
    
  pygame.display.update()