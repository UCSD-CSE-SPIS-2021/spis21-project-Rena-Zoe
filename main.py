import pygame

import os

screen_length = 465

screen_height = 350

dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field)

num_points = 0

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

#Jonny
jonny_x = 150
jonny_y = 145
jonny_rect = pygame.Rect(jonny_x, jonny_y, 23, 23)
jonny = pygame.image.load(os.path.join("curt", "jonny.png")).convert()
jonny.set_colorkey((0, 0, 0))
jonny = pygame.transform.scale(jonny, (25, 25))

#Josh
josh_x = 45
josh_y = 200
josh_rect = pygame.Rect(josh_x, josh_y, 23, 23)
josh = pygame.image.load(os.path.join("curt", "josh.png")).convert_alpha()
josh.set_colorkey((255, 255, 255))
josh = pygame.transform.scale(josh, (23, 23))

#Michael
michael_x = 285
michael_y = 145
michael_rect = pygame.Rect(michael_x, michael_y, 23, 23)
michael = pygame.image.load(os.path.join("curt", "michael.png")).convert()
michael.set_colorkey((0, 0, 0))
michael = pygame.transform.scale(michael, (23, 23))

#Gary player
gplayer_x = 15
gplayer_y = 40
gplayer_rect = pygame.Rect(gplayer_x, gplayer_y, 23, 23)
gplayer = pygame.image.load(os.path.join("gary", "gary.png")).convert()
gplayer.set_colorkey((0, 255, 0))
gplayer = pygame.transform.scale(gplayer, (23, 23))
#Diego
diego_x = 15
diego_y = 305
diego_rect = pygame.Rect(diego_x, diego_y, 23, 23)
diego = pygame.image.load(os.path.join("gary", "diego.png")).convert()
diego.set_colorkey((255, 255, 255))
diego = pygame.transform.scale(diego, (23, 23))
#Alarm clock
aclock_x = 425
aclock_y = 40
aclock_rect = pygame.Rect(aclock_x, aclock_y, 23, 23)
aclock = pygame.image.load(os.path.join("gary", "alarm_clock.png")).convert()
aclock.set_colorkey((0, 0, 0))
aclock = pygame.transform.scale(aclock, (23, 23))
#Akshat
akshat_x = 425
akshat_y = 305
akshat_rect = pygame.Rect(akshat_x, akshat_y, 23, 23)
akshat = pygame.image.load(os.path.join("gary", "akshat.png")).convert()
akshat.set_colorkey((0, 0, 0))
akshat = pygame.transform.scale(akshat, (23, 23))

#Niema
nplayer_x = 215
nplayer_y = 210
nplayer_rect = pygame.Rect(nplayer_x, nplayer_y, 23, 23)
nplayer = pygame.image.load(os.path.join("niema", "honda.png")).convert()
nplayer.set_colorkey((255, 255, 255))
nplayer = pygame.transform.scale(nplayer, (35, 35))
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
#Star sprites
starsprite = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
starsprite = pygame.transform.scale(starsprite, (15, 15))
#Hat sprites
hatsprite = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
hatsprite = pygame.transform.scale(hatsprite, (20, 20))
#Wine glasses
corksprite = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
corksprite = pygame.transform.scale(corksprite, (15, 20))
#Wine bottles
winesprite = pygame.image.load(os.path.join("gary", "wine1.png")).convert_alpha()
winesprite = pygame.transform.scale(winesprite, (10, 30))
#Lord of the Rings rings
ringsprite = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
ringsprite = pygame.transform.scale(ringsprite, (15, 15))
#Boba Drinks
bobasprite = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
bobasprite = pygame.transform.scale(bobasprite, (25, 25))


#Classes - Blueprint of an object
  #Object is code representation of a real life thing
#Classes == Factories
  #Class(dog) -> can make lots of dogs on a whim
    #Just call for the dog richard = dog

from home import homescreen
#From the home.py module import homescreen function
from curt import curt

from curt import c_walls

from curt import c10points

star_list = c10points(screen_length,screen_height, dim_field, screen, player_rect)

from curt import c50points

hat_list = c50points(screen_length,screen_height, dim_field, screen, player_rect)

from gary import gary

from gary import g_walls

from gary import g10points

from gary import g50points

from niema import niema

from niema import n_walls

from niema import n10points

from niema import n50points

from lose_page import lose_page

from win_page import win_page

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

  #When we have the ability to lose and win we need to tie in these functions:
  #lose_page(screen_length,screen_height, dim_field, screen, player_rect)
  #win_page(screen_length,screen_height, dim_field, screen, player_rect)

  if state == "home":
    #Want some way to keep track of what page you are in -> dont want to be in the menu anymore if don't need it

    page = homescreen(screen_length,screen_height, dim_field, screen, player_rect)

    state = page

  elif state == "curt":
    #Calling Curt's screen
    curt(screen_length,screen_height, dim_field, screen, player_rect, num_points)
    #Calling Curt's walls
    curt_walls = c_walls(screen_length,screen_height, dim_field, screen, player_rect)

    #Curt's sprites
    bye_star = player_rect.collidelist(star_list)
    if bye_star != -1:
      star_list.remove(star_list[bye_star])
      num_points += 10
    for star in star_list:
      screen.blit(starsprite, star)
    bye_hat = player_rect.collidelist(hat_list)
    if bye_hat != -1:
      hat_list.remove(hat_list[bye_hat])
      num_points += 50
    for hat in hat_list:
      screen.blit(hatsprite, hat)
      
    screen.blit(player, player_rect)
    screen.blit(hannah, hannah_rect)
    screen.blit(jonny, jonny_rect)
    screen.blit(josh, josh_rect)
    screen.blit(michael, michael_rect)
      #Draw the player here to continuously draw it as its moving over the frames
    #Curt's player's movement
    if direction == "left":
      player_rect.move_ip(-3, 0)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(3,0)
    elif direction == "right":
      player_rect.move_ip(3, 0)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(-3,0)
    elif direction == "up":
      player_rect.move_ip(0, -3)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(0, 3)
    elif direction == "down":
      player_rect.move_ip(0, 3)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(0, -3)
    else:
      pass

  elif page == "gary":
    #Gary's screen is called
    gary(screen_length,screen_height, dim_field, screen, player_rect)
    
    #Walls get set up
    gary_walls = g_walls(screen_length,screen_height, dim_field, screen, gplayer_rect)

    #Gary's points
    gary_10_points = g10points(screen_length,screen_height, dim_field, screen, player_rect)
    gary_50_points = g50points(screen_length,screen_height, dim_field, screen, player_rect)

    #Blitting all of Gary's sprites
    screen.blit(gplayer, gplayer_rect)
    screen.blit(diego, diego_rect)
    screen.blit(aclock, aclock_rect)
    screen.blit(akshat, akshat_rect)

    #Gary's movement
    if direction == "left":
      gplayer_rect.move_ip(-3, 0)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(3,0)
    elif direction == "right":
      gplayer_rect.move_ip(3, 0)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(-3,0)
    elif direction == "up":
      gplayer_rect.move_ip(0, -3)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(0, 3)
    elif direction == "down":
      gplayer_rect.move_ip(0, 3)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(0, -3)
    else:
      pass


  elif page == "niema":
    #Calling Niema's screen
    niema(screen_length,screen_height, dim_field, screen, nplayer_rect)
    
    #Calling Niema's walls
    niema_walls = n_walls(screen_length,screen_height, dim_field, screen, player_rect)

    #Niema's points
    niema_10_points = n10points(screen_length,screen_height, dim_field, screen, player_rect)
    niema_50_points = n50points(screen_length,screen_height, dim_field, screen, player_rect)
    
    #Niema's sprites
    screen.blit(nplayer, nplayer_rect)
    screen.blit(younus, younus_rect)
    screen.blit(belt, belt_rect)
    
    #Niema's movement
    if direction == "left":
      nplayer_rect.move_ip(-4, 0)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(4,0)
    elif direction == "right":
      nplayer_rect.move_ip(4, 0)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(-4,0)
    elif direction == "up":
      nplayer_rect.move_ip(0, -4)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(0, 4)
    elif direction == "down":
      nplayer_rect.move_ip(0, 4)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(0, -4)
    else:
      pass
    
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN: 

      if event.key == pygame.K_q:

        running = False

      #Directions, help know what left, right, up and down is, used earlier in loop
      if event.key == pygame.K_LEFT:
        direction = "left"
      if event.key == pygame.K_RIGHT:
        direction = "right"
      if event.key == pygame.K_UP:
        direction = "up"
      if event.key == pygame.K_DOWN:
        direction = "down"

  pygame.display.update()