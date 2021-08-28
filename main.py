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
#Jonny
jonny_x = 150
jonny_y = 145
jonny_rect = pygame.Rect(jonny_x, jonny_y, 23, 23)
jonny = pygame.image.load(os.path.join("curt", "jonny.png")).convert()
jonny.set_colorkey((0, 0, 0))
jonny = pygame.transform.scale(jonny, (25, 25))
screen.blit(jonny, jonny_rect)
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

#Gary player
gplayer_x = 20
gplayer_y = 45
gplayer_rect = pygame.Rect(gplayer_x, gplayer_y, 23, 23)
gplayer = pygame.image.load(os.path.join("gary", "gary.png")).convert()
gplayer.set_colorkey((0, 255, 0))
gplayer = pygame.transform.scale(gplayer, (23, 23))
screen.blit(gplayer, gplayer_rect)
#Diego
diego_x = 20
diego_y = 310
diego_rect = pygame.Rect(diego_x, diego_y, 23, 23)
diego = pygame.image.load(os.path.join("gary", "diego.png")).convert()
diego.set_colorkey((255, 255, 255))
diego = pygame.transform.scale(diego, (23, 23))
screen.blit(diego, diego_rect)
#Alarm clock
aclock_x = 420
aclock_y = 40
aclock_rect = pygame.Rect(aclock_x, aclock_y, 23, 23)
aclock = pygame.image.load(os.path.join("gary", "alarm_clock.png")).convert()
aclock.set_colorkey((0, 0, 0))
aclock = pygame.transform.scale(aclock, (23, 23))
screen.blit(aclock, aclock_rect)
#Akshat
akshat_x = 420
akshat_y = 310
akshat_rect = pygame.Rect(akshat_x, akshat_y, 23, 23)
akshat = pygame.image.load(os.path.join("gary", "akshat.png")).convert()
akshat.set_colorkey((0, 0, 0))
akshat = pygame.transform.scale(akshat, (23, 23))
screen.blit(akshat, akshat_rect)

#Niema
nplayer_x = 215
nplayer_y = 210
nplayer_rect = pygame.Rect(nplayer_x, nplayer_y, 23, 23)
nplayer = pygame.image.load(os.path.join("niema", "honda.png")).convert()
nplayer.set_colorkey((255, 255, 255))
nplayer = pygame.transform.scale(nplayer, (35, 35))
screen.blit(nplayer, nplayer_rect)
#Younus
younus_x =  70
younus_y = 200
younus_rect = pygame.Rect(younus_x, younus_y, 23, 23)
younus = pygame.image.load(os.path.join("niema", "younus.png")).convert()
younus.set_colorkey((0, 0, 0))
younus = pygame.transform.scale(younus, (23, 23))
#Belt
belt_x = 340
belt_y = 200
belt_rect = pygame.Rect(belt_x, belt_y, 23, 23)
belt = pygame.image.load(os.path.join("niema", "belt.png")).convert()
belt.set_colorkey((0, 0, 0))
belt = pygame.transform.scale(belt, (26, 26))
screen.blit(belt, belt_rect)

#Classes - Blueprint of an object
  #Object is code representation of a real life thing
#Classes == Factories
  #Class(dog) -> can make lots of dogs on a whim
    #Just call for the dog richard = dog

from home import homescreen
#From the home.py module import homescreen function
from curt import curt

from curt import c_walls

from gary import gary

from gary import g_walls

from niema import niema

from niema import n_walls

#from niema import niema

#from niema import n_walls

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

  # if state == "home":
  # #   #Want some way to keep track of what page you are in -> dont want to be in the menu anymore if don't need it

  #   page = homescreen(screen_length,screen_height, dim_field, screen, player_rect)
  #   state = page
  # elif state == "curt":
  #   curt(screen_length,screen_height, dim_field, screen, player_rect)
  #   curt_walls = c_walls(screen_length,screen_height, dim_field, screen, player_rect)
  # #   #Draw the player here to continuously draw it as its moving over the frames
  #   screen.blit(player, player_rect)
  #   screen.blit(hannah, hannah_rect)
  #   screen.blit(jonny, jonny_rect)
  #   screen.blit(josh, josh_rect)
  #   screen.blit(michael, michael_rect)
  # elif page == "gary":
  #   gary(screen_length,screen_height, dim_field, screen, player_rect)
  #   g_walls(screen_length,screen_height, dim_field, screen, gplayer_rect)
  #   screen.blit(gplayer, gplayer_rect)
  #   screen.blit(diego, diego_rect)
  #   screen.blit(aclock, aclock_rect)
  #   screen.blit(akshat, akshat_rect)
  # elif page == "niema":
  niema(screen_length,screen_height, dim_field, screen, nplayer_rect)
  n_walls(screen_length,screen_height, dim_field, screen, player_rect)
  screen.blit(nplayer, nplayer_rect)
  screen.blit(younus, younus_rect)
  screen.blit(belt, belt_rect)


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
  
  #if player_rect.collidelist(curt_walls) != -1:
    #direction = "stop"
      

  # if direction == "left":
  #   player_rect.move_ip(-2, 0)
  #   if player_rect.collidelist(curt_walls) != -1:
  #     player_rect.move_ip(2,0)
  #   #print("Left!")
  # elif direction == "right":
  #   player_rect.move_ip(2, 0)
  #   if player_rect.collidelist(curt_walls) != -1:
  #     player_rect.move_ip(-2,0)
  # elif direction == "up":
  #   player_rect.move_ip(0, -2)
  #   if player_rect.collidelist(curt_walls) != -1:
  #     player_rect.move_ip(0, 2)
  # elif direction == "down":
  #   player_rect.move_ip(0, 2)
  #   if player_rect.collidelist(curt_walls) != -1:
  #     player_rect.move_ip(0, -2)
  # else:
  #   pass #Skips over it, doesn't do anything
  
  # #Curt collisions 
    
  pygame.display.update()